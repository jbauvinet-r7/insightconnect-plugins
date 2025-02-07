import json
from typing import Any, Dict, List, Tuple, Optional, Union
import urllib.parse

import requests
from icon_azure_sentinel.util.tools import return_non_empty
from insightconnect_plugin_runtime.exceptions import PluginException

from .endpoints import Endpoint


class AzureClient:
    def __init__(self, logger: Any, tenant_id: str, client_id: str, client_secret: str):
        self.O365_AUTH_ENDPOINT = "https://login.microsoftonline.com/{}/oauth2/token"
        self.SCOPE = "https://management.azure.com"
        self._auth_token = ""  # nosec
        self.tenant_id = tenant_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.logger = logger

    @property
    def auth_token(self):
        tenant_id = self.tenant_id
        client_id = self.client_id
        client_secret = self.client_secret

        self.logger.info("Updating auth token...")

        data = {
            "grant_type": "client_credentials",
            "client_id": client_id,
            "resource": self.SCOPE,
            "client_secret": client_secret,
        }

        formatted_endpoint = self.O365_AUTH_ENDPOINT.format(tenant_id)
        self.logger.info("Getting token from: " + formatted_endpoint)

        request = requests.request("POST", formatted_endpoint, data=data)
        self.logger.info("Authentication request status: " + str(request.status_code))

        if request.status_code != 200:
            self.logger.error(request.text)
            raise PluginException(
                cause="Unable to authorize against Microsoft graph API.",
                assistance="The application may not be authorized to connect "
                "to the Microsoft Graph API. Please verify your connection information is correct and contact your "
                "Azure administrator.",
                data=request.text,
            )
        token = request.json().get("access_token")
        self._auth_token = token
        self.logger.info(f"Authentication Token: ****************{self._auth_token[-5:]}")
        return token


class AzureSentinelClient(AzureClient):
    def __init__(self, logger: Any, tenant_id: str, client_id: str, client_secret: str):
        super(AzureSentinelClient, self).__init__(logger, tenant_id, client_id, client_secret)  # noqa
        self.headers = {"Content-Type": "application/json", "Authorization": f"Bearer {self.auth_token}"}

    def _call_api(
        self, method: str, url: str, headers: dict, payload: Optional[dict] = None, params: Optional[dict] = None
    ) -> Tuple[int, Dict]:
        """_call_api. Send a http call to a given endpoint.

        :param method: Http method to be called.
        :type method: str
        :param url: Url to be called.
        :type url: str
        :param headers: Headers to be sent in the http call.
        :type headers: dict
        :param payload: Payload to be sent in the http call.
        :type payload: Optional[dict]
        :rtype: Union[Dict, int]
        """

        try:
            data = json.dumps(payload) if payload else None
            kwargs = {"headers": headers, "data": data}
            if params:
                payload_str = urllib.parse.urlencode(params, safe="$")
                kwargs["params"] = payload_str

            response = requests.request(method, url, **kwargs)
            response.raise_for_status()
            if response.headers.get("content-type") == "application/json; charset=utf-8":
                return response.status_code, response.json()
            return response.status_code, {}

        except json.decoder.JSONDecodeError as error:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=error)
        except requests.exceptions.HTTPError as error:
            if error.response.status_code == 400:
                raise PluginException(
                    cause="Combination of input arguments is incorrect", assistance=error.response.json().get("error")
                )
            if error.response.status_code == 401:
                raise PluginException(cause=error.response.json().get("error"))
            if error.response.status_code == 403:
                raise PluginException(preset=PluginException.Preset.UNAUTHORIZED)
            if error.response.status_code == 404:
                raise PluginException(preset=PluginException.Preset.NOT_FOUND)
            if error.response.status_code >= 500:
                raise PluginException(preset=PluginException.Preset.SERVER_ERROR)
        except requests.exceptions.Timeout:
            raise PluginException(preset=PluginException.Preset.TIMEOUT)

    def _list_all(self, method: str, uri: str, filters: Dict = {}, type_: str = "value") -> List[Any]:
        """_list_all. Get all the objects of a given type. It sends multiple requests
            in order to get everything.

        :param method: HTTP method used to call the api.
        :type method: str
        :param uri: URL to be called.
        :type uri: str
        :param filters: Filters to be used to fetch the data. Order, amount etc.
        :type filters: Dict
        :rtype: List[Any]
        """
        final_uri = uri
        filters = {f"${key}": filters[key] for key in filters}
        _, objects = self._call_api(method, final_uri, self.headers, params=filters)
        results = objects.get(type_, [])
        nextLink = objects.get("nextLink", None)
        while nextLink:
            _, return_object = self._call_api(method, nextLink, self.headers)
            results += return_object.get(type_, [])
            nextLink = return_object.get("nextLink", None)
        return results

    def get_incident(
        self,
        incident_id: str,
        resource_group_name: str,
        workspace_name: str,
        subscription_id: str,
        api_version: str = "2021-04-01",
    ) -> Union[Dict, int]:
        uri = Endpoint.GETINCIDENT
        final_uri = uri.format(
            subscription_id,
            resource_group_name,
            workspace_name,
            incident_id,
            api_version,
        )
        _, results = self._call_api("GET", final_uri, self.headers)
        return return_non_empty(results)

    def create_incident(
        self,
        incident_id: str,
        resource_group_name: str,
        workspace_name: str,
        subscription_id: str,
        api_version: str = "2021-04-01",
        **kwargs,
    ) -> Union[Dict, int]:
        uri = Endpoint.CREATEINCIDENT
        final_uri = uri.format(
            subscription_id,
            resource_group_name,
            workspace_name,
            incident_id,
            api_version,
        )
        kwargs = return_non_empty(kwargs)
        _, results = self._call_api("PUT", final_uri, self.headers, payload=kwargs)
        return results

    def list_incident(
        self,
        resource_group_name: str,
        workspace_name: str,
        filters: Dict,
        subscription_id: str,
        api_version: str = "2021-04-01",
    ) -> List:
        uri = Endpoint.LISTINCIDENTS
        final_uri = uri.format(subscription_id, resource_group_name, workspace_name, api_version)
        filters = return_non_empty(filters)
        results = self._list_all("GET", final_uri, filters)
        return [return_non_empty(incident) for incident in results]

    def delete_incident(
        self,
        incident_id: str,
        resource_group_name: str,
        workspace_name: str,
        subscription_id: str,
        api_version: str = "2021-04-01",
    ) -> Union[Dict, int]:
        uri = Endpoint.DELETEINCIDENT
        final_uri = uri.format(
            subscription_id,
            resource_group_name,
            workspace_name,
            incident_id,
            api_version,
        )
        status, _ = self._call_api("DELETE", final_uri, self.headers)
        return status

    def list_bookmarks(
        self,
        incident_id: str,
        resource_group_name: str,
        workspace_name: str,
        subscription_id: str,
        api_version: str = "2021-04-01",
    ) -> List:
        uri = Endpoint.LISTBOOKMARKS
        final_uri = uri.format(
            subscription_id,
            resource_group_name,
            workspace_name,
            incident_id,
            api_version,
        )
        results = self._list_all("POST", final_uri)
        return [return_non_empty(bookmark) for bookmark in results]

    def list_alerts(
        self,
        incident_id: str,
        resource_group_name: str,
        workspace_name: str,
        subscription_id: str,
        api_version: str = "2021-04-01",
    ) -> List:
        uri = Endpoint.LISTALERTS
        final_uri = uri.format(
            subscription_id,
            resource_group_name,
            workspace_name,
            incident_id,
            api_version,
        )
        results = self._list_all("POST", final_uri)
        return [return_non_empty(alert) for alert in results]

    def list_entities(
        self,
        incident_id: str,
        resource_group_name: str,
        workspace_name: str,
        subscription_id: str,
        api_version: str = "2021-04-01",
    ) -> List:
        uri = Endpoint.LISTENTITIES
        final_uri = uri.format(
            subscription_id,
            resource_group_name,
            workspace_name,
            incident_id,
            api_version,
        )
        results = self._list_all("POST", final_uri, type_="entities")
        return [return_non_empty(entity) for entity in results]
