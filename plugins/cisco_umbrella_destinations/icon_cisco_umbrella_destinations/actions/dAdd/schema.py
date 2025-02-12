# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Add a destination to the destination list"


class Input:
    COMMENT = "comment"
    DESTINATION = "destination"
    DESTINATIONLISTID = "destinationListId"
    

class Output:
    SUCCESS = "success"
    

class DAddInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "comment": {
      "type": "string",
      "title": "Comment",
      "description": "Information about domain",
      "order": 3
    },
    "destination": {
      "type": "string",
      "title": "Destination Name",
      "description": "Title for the destination list",
      "order": 2
    },
    "destinationListId": {
      "type": "integer",
      "title": "Destination List ID",
      "description": "Unique ID for destination list",
      "order": 1
    }
  },
  "required": [
    "destination",
    "destinationListId"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DAddOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "$ref": "#/definitions/dlCollection",
      "title": "Success",
      "description": "Successful returned value",
      "order": 1
    }
  },
  "required": [
    "success"
  ],
  "definitions": {
    "dlCollection": {
      "type": "object",
      "title": "dlCollection",
      "properties": {
        "access": {
          "type": "string",
          "title": "Access",
          "description": "Can be allow or block",
          "order": 3
        },
        "createdAt": {
          "type": "string",
          "title": "Created At",
          "displayType": "date",
          "description": "Timestamp for creation of the destination list",
          "format": "date-time",
          "order": 7
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Unique ID of the destination list",
          "order": 1
        },
        "isGlobal": {
          "type": "boolean",
          "title": "Is Global",
          "description": "Boolean value indicating global state",
          "order": 4
        },
        "isMspDefault": {
          "type": "boolean",
          "title": "Is MSP Default",
          "description": "Whether or not MSP is default",
          "order": 9
        },
        "markedForDeletion": {
          "type": "boolean",
          "title": "Marked For Deletion",
          "description": "Whether or not destination list is marked for deletion",
          "order": 10
        },
        "meta": {
          "$ref": "#/definitions/meta",
          "title": "Metadata",
          "description": "Secondary information",
          "order": 11
        },
        "modifiedAt": {
          "type": "string",
          "title": "Modified At",
          "displayType": "date",
          "description": "Timestamp for modification of the destination list",
          "format": "date-time",
          "order": 8
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Title for the destination list",
          "order": 5
        },
        "organizationId": {
          "type": "integer",
          "title": "Organization ID",
          "description": "ID of organization",
          "order": 2
        },
        "thirdpartyCategoryId": {
          "type": "integer",
          "title": "Third Party Category ID",
          "description": "ID, if any, for third parties",
          "order": 6
        }
      },
      "definitions": {
        "meta": {
          "type": "object",
          "title": "meta",
          "properties": {
            "destinationCount": {
              "type": "integer",
              "title": "DestinationCount",
              "description": "Total number of destinations in a destination list",
              "order": 1
            },
            "domainCount": {
              "type": "integer",
              "title": "DomainCount",
              "description": "Total number of domains in a destination list",
              "order": 2
            },
            "ipv4Count": {
              "type": "integer",
              "title": "Ipv4Count",
              "description": "Total number of IPs in a destination list",
              "order": 4
            },
            "urlCount": {
              "type": "integer",
              "title": "UrlCount",
              "description": "Total number of URLs in a destination list",
              "order": 3
            }
          }
        }
      }
    },
    "meta": {
      "type": "object",
      "title": "meta",
      "properties": {
        "destinationCount": {
          "type": "integer",
          "title": "DestinationCount",
          "description": "Total number of destinations in a destination list",
          "order": 1
        },
        "domainCount": {
          "type": "integer",
          "title": "DomainCount",
          "description": "Total number of domains in a destination list",
          "order": 2
        },
        "ipv4Count": {
          "type": "integer",
          "title": "Ipv4Count",
          "description": "Total number of IPs in a destination list",
          "order": 4
        },
        "urlCount": {
          "type": "integer",
          "title": "UrlCount",
          "description": "Total number of URLs in a destination list",
          "order": 3
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
