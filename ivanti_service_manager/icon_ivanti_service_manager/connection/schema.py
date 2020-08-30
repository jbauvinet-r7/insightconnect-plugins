# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Input:
    CREDENTIALS = "credentials"
    SSL_VERIFY = "ssl_verify"
    URL = "url"
    

class ConnectionSchema(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "credentials": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "API Key",
      "description": "API key from account",
      "order": 1
    },
    "ssl_verify": {
      "type": "boolean",
      "title": "TLS / SSL Verify",
      "description": "Validate TLS / SSL certificate",
      "default": true,
      "order": 3
    },
    "url": {
      "type": "string",
      "title": "URL",
      "description": "API access URL",
      "order": 2
    }
  },
  "required": [
    "credentials",
    "url"
  ],
  "definitions": {
    "credential_secret_key": {
      "id": "credential_secret_key",
      "type": "object",
      "title": "Credential: Secret Key",
      "description": "A shared secret key",
      "properties": {
        "secretKey": {
          "type": "string",
          "title": "Secret Key",
          "displayType": "password",
          "description": "The shared secret key",
          "format": "password"
        }
      },
      "required": [
        "secretKey"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)