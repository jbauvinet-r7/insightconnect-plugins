# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Delete an Adversary in the ThreatConnect platform"


class Input:
    ID = "id"
    OWNER = "owner"
    

class Output:
    STATUS = "status"
    

class DeleteAdversaryInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "integer",
      "title": "ID",
      "description": "Adversary To Delete",
      "order": 2
    },
    "owner": {
      "type": "string",
      "title": "Owner",
      "description": "Owner/Organization",
      "order": 1
    }
  },
  "required": [
    "id",
    "owner"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DeleteAdversaryOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "status": {
      "type": "boolean",
      "title": "Status",
      "description": "Status",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)