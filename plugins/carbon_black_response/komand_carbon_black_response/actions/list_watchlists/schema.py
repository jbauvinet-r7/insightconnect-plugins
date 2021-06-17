# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "List all watchlists"


class Input:
    pass

class Output:
    WATCHLISTS = "watchlists"
    

class ListWatchlistsInput(komand.Input):
    schema = json.loads("""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ListWatchlistsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "watchlists": {
      "type": "array",
      "title": "Watchlists",
      "description": "The list of watchlists",
      "items": {
        "$ref": "#/definitions/watchlist"
      },
      "order": 1
    }
  },
  "definitions": {
    "watchlist": {
      "type": "object",
      "title": "watchlist",
      "properties": {
        "alliance_id": {
          "type": "integer",
          "title": "Alliance ID",
          "order": 8
        },
        "date_added": {
          "type": "string",
          "title": "Date Added",
          "displayType": "date",
          "format": "date-time",
          "order": 10
        },
        "enabled": {
          "type": "boolean",
          "title": "Enabled",
          "order": 4
        },
        "from_alliance": {
          "type": "boolean",
          "title": "From Alliance",
          "order": 14
        },
        "group_id": {
          "type": "integer",
          "title": "Group ID",
          "order": 11
        },
        "index_type": {
          "type": "string",
          "title": "Index Type",
          "description": "Index to search for this watchlist",
          "enum": [
            "events",
            "modules"
          ],
          "order": 6
        },
        "last_hit": {
          "type": "string",
          "title": "Last Hit",
          "displayType": "date",
          "format": "date-time",
          "order": 13
        },
        "last_hit_count": {
          "type": "integer",
          "title": "Last Hit Count",
          "order": 1
        },
        "list_query": {
          "type": "string",
          "title": "List Query",
          "description": "URL-encoded search query associated with this watchlist",
          "order": 3
        },
        "list_timestamp": {
          "type": "string",
          "title": "List Timestamp",
          "displayType": "date",
          "format": "date-time",
          "order": 5
        },
        "name": {
          "type": "string",
          "title": "Name",
          "order": 2
        },
        "readonly": {
          "type": "boolean",
          "title": "Readonly",
          "order": 7
        },
        "total_hits": {
          "type": "string",
          "title": "Total Hits",
          "order": 9
        },
        "total_tags": {
          "type": "string",
          "title": "Total Tags",
          "order": 12
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)