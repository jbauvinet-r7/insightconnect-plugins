# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Convert a Datetime to an Epoch"


class Input:
    DATETIME = "datetime"
    

class Output:
    EPOCH = "epoch"
    

class EpochFromDateInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "datetime": {
      "type": "string",
      "title": "Datetime",
      "displayType": "date",
      "description": "Date in RFC3339 format",
      "format": "date-time",
      "order": 1
    }
  },
  "required": [
    "datetime"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class EpochFromDateOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "epoch": {
      "type": "integer",
      "title": "Epoch",
      "description": "Epoch after conversion",
      "order": 1
    }
  },
  "required": [
    "epoch"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)