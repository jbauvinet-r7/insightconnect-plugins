# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Extract URLs from a string or file"


class Input:
    FILE = "file"
    STR = "str"
    

class Output:
    URLS = "urls"
    

class UrlExtractorInput(insightconnect_plugin_runtime.Input):
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


class UrlExtractorOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "urls": {
      "type": "array",
      "title": "URLs",
      "description": "List of extracted URLs",
      "items": {
        "type": "string"
      },
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)