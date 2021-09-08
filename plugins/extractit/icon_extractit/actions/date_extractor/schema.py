# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Extracts all dates from a string or file"


class Input:
    FILE = "file"
    STR = "str"
    

class Output:
    DATES = "dates"
    

class DateExtractorInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "file": {
      "type": "string",
      "title": "File",
      "displayType": "bytes",
      "description": "Input file as bytes",
      "format": "bytes",
      "order": 2
    },
    "str": {
      "type": "string",
      "title": "String",
      "description": "Input string",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DateExtractorOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "dates": {
      "type": "array",
      "title": "Dates",
      "description": "List of extracted dates",
      "items": {
        "type": "string",
        "displayType": "date",
        "format": "date-time"
      },
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
