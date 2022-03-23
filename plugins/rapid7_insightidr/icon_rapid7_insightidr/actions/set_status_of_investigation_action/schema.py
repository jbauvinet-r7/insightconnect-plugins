# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Set the status of the investigation with the given ID"


class Input:
    ID = "id"
    STATUS = "status"
    

class Output:
    INVESTIGATION = "investigation"
    

class SetStatusOfInvestigationActionInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "string",
      "title": "ID",
      "description": "The ID of the investigation to change the status of",
      "order": 1
    },
    "status": {
      "type": "string",
      "title": "Status",
      "description": "The new status for the investigation",
      "default": "CLOSED",
      "enum": [
        "OPEN",
        "CLOSED"
      ],
      "order": 2
    }
  },
  "required": [
    "id",
    "status"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SetStatusOfInvestigationActionOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "investigation": {
      "$ref": "#/definitions/investigation",
      "title": "Investigations",
      "description": "The investigation for which the status was set",
      "order": 1
    }
  },
  "required": [
    "investigation"
  ],
  "definitions": {
    "alerts": {
      "type": "object",
      "title": "alerts",
      "properties": {
        "first_event_time": {
          "type": "string",
          "title": "First Event Time",
          "description": "The time the first event involved in this alert occurred",
          "order": 1
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Alert type",
          "order": 2
        },
        "type_description": {
          "type": "string",
          "title": "Type Description",
          "description": "An optional description of this type of alert",
          "order": 3
        }
      }
    },
    "assignee": {
      "type": "object",
      "title": "assignee",
      "properties": {
        "email": {
          "type": "string",
          "title": "Email",
          "description": "The email of the assigned user",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "The name of the assigned user",
          "order": 2
        }
      }
    },
    "investigation": {
      "type": "object",
      "title": "investigation",
      "properties": {
        "alerts": {
          "type": "array",
          "title": "Alerts",
          "description": "The alerts involved in this investigation, if any",
          "items": {
            "$ref": "#/definitions/alerts"
          },
          "order": 2
        },
        "assignee": {
          "$ref": "#/definitions/assignee",
          "title": "Assignee",
          "description": "The user assigned to this investigation, if any",
          "order": 1
        },
        "created_time": {
          "type": "string",
          "title": "Created Time",
          "description": "The time the investigation was created as an ISO formatted timestamp",
          "order": 3
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "The ID of the investigation",
          "order": 4
        },
        "source": {
          "type": "string",
          "title": "Source",
          "description": "The source of this investigation",
          "order": 5
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "The status of the investigation",
          "order": 6
        },
        "title": {
          "type": "string",
          "title": "Title",
          "description": "Investigation title",
          "order": 7
        }
      },
      "definitions": {
        "alerts": {
          "type": "object",
          "title": "alerts",
          "properties": {
            "first_event_time": {
              "type": "string",
              "title": "First Event Time",
              "description": "The time the first event involved in this alert occurred",
              "order": 1
            },
            "type": {
              "type": "string",
              "title": "Type",
              "description": "Alert type",
              "order": 2
            },
            "type_description": {
              "type": "string",
              "title": "Type Description",
              "description": "An optional description of this type of alert",
              "order": 3
            }
          }
        },
        "assignee": {
          "type": "object",
          "title": "assignee",
          "properties": {
            "email": {
              "type": "string",
              "title": "Email",
              "description": "The email of the assigned user",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "The name of the assigned user",
              "order": 2
            }
          }
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)