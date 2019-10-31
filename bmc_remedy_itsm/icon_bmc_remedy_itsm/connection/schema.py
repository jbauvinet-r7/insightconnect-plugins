# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    CREDENTIALS = "credentials"
    PORT = "port"
    SSL_VERIFY = "ssl_verify"
    URL = "url"
    

class ConnectionSchema(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "credentials": {
      "$ref": "#/definitions/credential_username_password",
      "title": "Credentials",
      "description": "Username and password",
      "order": 1
    },
    "port": {
      "type": "string",
      "title": "Port",
      "description": "The port the REST API is listening on. This may be different than the port for the web interface",
      "order": 3
    },
    "ssl_verify": {
      "type": "boolean",
      "title": "SSL Verify",
      "description": "Boolean property used to decide whether to verify a TSL or SSL certificate",
      "order": 4
    },
    "url": {
      "type": "string",
      "title": "URL",
      "description": "The URL for the BCM Remedy ITSM server. e.g. http://remd-itsm1902.xxx.xxx.rapid7.com",
      "order": 2
    }
  },
  "required": [
    "credentials",
    "port",
    "ssl_verify",
    "url"
  ],
  "definitions": {
    "credential_username_password": {
      "id": "credential_username_password",
      "type": "object",
      "title": "Credential: Username and Password",
      "description": "A username and password combination",
      "properties": {
        "password": {
          "type": "string",
          "title": "Password",
          "displayType": "password",
          "description": "The password",
          "format": "password"
        },
        "username": {
          "type": "string",
          "title": "Username",
          "description": "The username to log in with"
        }
      },
      "required": [
        "username",
        "password"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)