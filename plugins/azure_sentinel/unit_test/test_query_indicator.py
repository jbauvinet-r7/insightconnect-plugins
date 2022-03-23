import logging
import sys
import os
from unittest import TestCase, mock

from icon_azure_sentinel.connection import Connection
from icon_azure_sentinel.actions.query_indicator import QueryIndicator
from icon_azure_sentinel.util.api import AzureSentinelClient

sys.path.append(os.path.abspath("../"))


class TestQueryIndicator(TestCase):
    def setUp(self) -> None:
        self.action = QueryIndicator()
        self.connection = Connection()
        self.connection.auth_token = "12345"
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action logger")
        self.params = {
            "resourceGroupName": "integrationLab",
            "subscriptionId": "abcde",
            "workspaceName": "sentinel",
            "keywords": "test",
        }
        self.action.connection.api_client = mock.create_autospec(AzureSentinelClient)

    def test_query_indicator(self):
        self.action.run(self.params)
        self.action.connection.api_client.query_indicator.assert_called_once_with(
            "integrationLab", "sentinel", "abcde", keywords=self.params["keywords"]
        )
