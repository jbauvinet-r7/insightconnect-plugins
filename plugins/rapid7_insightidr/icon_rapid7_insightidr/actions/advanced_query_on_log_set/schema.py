# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Realtime query an InsightIDR log set. This will query entire log sets for results"


class Input:
    LOG_SET = "log_set"
    QUERY = "query"
    RELATIVE_TIME = "relative_time"
    TIME_FROM = "time_from"
    TIME_TO = "time_to"
    TIMEOUT = "timeout"
    

class Output:
    COUNT = "count"
    RESULTS = "results"
    

class AdvancedQueryOnLogSetInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "log_set": {
      "type": "string",
      "title": "Log Set",
      "description": "Log Set to search",
      "enum": [
        "Advanced Malware Alert",
        "Active Directory Admin Activity",
        "Asset Authentication",
        "Cloud Service Admin Activity",
        "Cloud Service Activity",
        "DNS Query",
        "Endpoint Activity",
        "EndPoint Agent",
        "Exploit Mitigation Alert",
        "File Access Activity",
        "File Modification Activity",
        "Firewall Activity",
        "Network Flow",
        "Host To IP Observations",
        "IDS Alert",
        "Ingress Authentication",
        "Raw Log",
        "SSO Authentication",
        "Unparsed Data",
        "Third Party Alert",
        "Virus Alert",
        "Web Proxy Activity"
      ],
      "order": 6
    },
    "query": {
      "type": "string",
      "title": "Query",
      "description": "LQL Query",
      "order": 1
    },
    "relative_time": {
      "type": "string",
      "title": "Relative Time",
      "description": "A relative time in the past to look for alerts",
      "default": "Last 5 Minutes",
      "enum": [
        "Last 5 Minutes",
        "Last 10 Minutes",
        "Last 20 Minutes",
        "Last 30 Minutes",
        "Last 45 Minutes",
        "Last 1 Hour",
        "Last 2 Hours",
        "Last 3 Hours",
        "Last 6 Hours",
        "Last 12 Hours",
        "Use Time From Value"
      ],
      "order": 2
    },
    "time_from": {
      "type": "string",
      "title": "Time From",
      "description": "Beginning date and time for the query. This will be ignored unless Relative Time input is set to 'Use Time From Value'. The format is flexible and will work with simple dates (e.g. 01-01-2020) to full ISO time (e.g. 01-01-2020T00:00:00)",
      "order": 3
    },
    "time_to": {
      "type": "string",
      "title": "Time To",
      "description": "Date and time for the end of the query. If left blank, the current time will be used. The format is flexible and will work with simple dates (e.g. 01-01-2020) to full ISO time (e.g. 01-01-2020T00:00:00)",
      "order": 4
    },
    "timeout": {
      "type": "integer",
      "title": "Timeout",
      "description": "Time in seconds to wait for the query to return. If exceeded the plugin will throw an error",
      "default": 60,
      "order": 5
    }
  },
  "required": [
    "log_set",
    "query",
    "relative_time",
    "timeout"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AdvancedQueryOnLogSetOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "count": {
      "type": "integer",
      "title": "Count",
      "description": "Number of log entries found",
      "order": 2
    },
    "results": {
      "type": "array",
      "title": "Query Results",
      "description": "Query Results",
      "items": {
        "$ref": "#/definitions/events"
      },
      "order": 1
    }
  },
  "required": [
    "count",
    "results"
  ],
  "definitions": {
    "eventData": {
      "type": "object",
      "title": "eventData",
      "properties": {
        "asSignatureCreationTime": {
          "type": "string",
          "title": "As Signature Creation Time",
          "description": "As signature creation time",
          "order": 6
        },
        "assignatureVersion": {
          "type": "string",
          "title": "As Signature Version",
          "description": "As signature version",
          "order": 4
        },
        "avSignatureCreationTime": {
          "type": "string",
          "title": "AV Signature Creation Time",
          "description": "AV signature creation time",
          "order": 20
        },
        "avsignatureVersion": {
          "type": "string",
          "title": "AV Signature Version",
          "description": "AV signature version",
          "order": 21
        },
        "bmState": {
          "type": "string",
          "title": "BMS State",
          "description": "BMS state",
          "order": 11
        },
        "data": {
          "type": "array",
          "title": "Data",
          "description": "Data",
          "items": {
            "type": "object"
          },
          "order": 18
        },
        "engineVersion": {
          "type": "string",
          "title": "Engine Version",
          "description": "Engine version",
          "order": 10
        },
        "ioavState": {
          "type": "string",
          "title": "IOAV State",
          "description": "IOAV state",
          "order": 5
        },
        "lastAsSignatureAge": {
          "type": "string",
          "title": "Last As Signature Age",
          "description": "Last as signature age",
          "order": 2
        },
        "lastAvSignatureAge": {
          "type": "string",
          "title": "Last AV Signature Age",
          "description": "Last AV signature age",
          "order": 22
        },
        "lastFullScanAge": {
          "type": "string",
          "title": "Last Full Scan Age",
          "description": "Last full scan age",
          "order": 25
        },
        "lastFullScanEndTime": {
          "type": "string",
          "title": "Last Full Scan End Time",
          "description": "Last full scan end time",
          "order": 13
        },
        "lastFullScanSource": {
          "type": "string",
          "title": "Last Full Scan Source",
          "description": "Last full scan source",
          "order": 7
        },
        "lastFullScanStartTime": {
          "type": "string",
          "title": "Last Full Scan Start Time",
          "description": "Last full scan start time",
          "order": 9
        },
        "lastQuickScanAge": {
          "type": "string",
          "title": "Last Quick Scan Age",
          "description": "Last quick scan age",
          "order": 17
        },
        "lastQuickScanEndTime": {
          "type": "string",
          "title": "Last Quick Scan End Time",
          "description": "Last quick scan end time",
          "order": 19
        },
        "lastQuickScanSource": {
          "type": "string",
          "title": "Last Quick Scan Source",
          "description": "Last quick scan source",
          "order": 12
        },
        "lastQuickScanStartTime": {
          "type": "string",
          "title": "Last Quick Scan Start Time",
          "description": "Last quick scan start time",
          "order": 24
        },
        "nriEngineVersion": {
          "type": "string",
          "title": "NRI Engine Version",
          "description": "NRI engine version",
          "order": 23
        },
        "nriSignatureVersion": {
          "type": "string",
          "title": "NRI Signature Version",
          "description": "NRI signature version",
          "order": 8
        },
        "oaState": {
          "type": "string",
          "title": "OA State",
          "description": "OA state",
          "order": 1
        },
        "platformVersion": {
          "type": "string",
          "title": "Platform Version",
          "description": "Platform version",
          "order": 16
        },
        "productName": {
          "type": "string",
          "title": "Product Name",
          "description": "Product name",
          "order": 14
        },
        "productStatus": {
          "type": "string",
          "title": "Product Status",
          "description": "Product status",
          "order": 3
        },
        "rtpState": {
          "type": "string",
          "title": "RTP State",
          "description": "RTP state",
          "order": 15
        }
      }
    },
    "events": {
      "type": "object",
      "title": "events",
      "properties": {
        "labels": {
          "type": "array",
          "title": "Labels",
          "description": "List of labels",
          "items": {
            "$ref": "#/definitions/label"
          },
          "order": 1
        },
        "links": {
          "type": "array",
          "title": "Links",
          "description": "Links",
          "items": {
            "$ref": "#/definitions/link"
          },
          "order": 6
        },
        "log_id": {
          "type": "string",
          "title": "Log ID",
          "description": "Log ID",
          "order": 4
        },
        "message": {
          "$ref": "#/definitions/message",
          "title": "Message",
          "description": "Message",
          "order": 5
        },
        "sequence_number": {
          "type": "integer",
          "title": "Sequence Number",
          "description": "Sequence number",
          "order": 3
        },
        "timestamp": {
          "type": "integer",
          "title": "Timestamp",
          "description": "Timestamp",
          "order": 2
        }
      },
      "definitions": {
        "eventData": {
          "type": "object",
          "title": "eventData",
          "properties": {
            "asSignatureCreationTime": {
              "type": "string",
              "title": "As Signature Creation Time",
              "description": "As signature creation time",
              "order": 6
            },
            "assignatureVersion": {
              "type": "string",
              "title": "As Signature Version",
              "description": "As signature version",
              "order": 4
            },
            "avSignatureCreationTime": {
              "type": "string",
              "title": "AV Signature Creation Time",
              "description": "AV signature creation time",
              "order": 20
            },
            "avsignatureVersion": {
              "type": "string",
              "title": "AV Signature Version",
              "description": "AV signature version",
              "order": 21
            },
            "bmState": {
              "type": "string",
              "title": "BMS State",
              "description": "BMS state",
              "order": 11
            },
            "data": {
              "type": "array",
              "title": "Data",
              "description": "Data",
              "items": {
                "type": "object"
              },
              "order": 18
            },
            "engineVersion": {
              "type": "string",
              "title": "Engine Version",
              "description": "Engine version",
              "order": 10
            },
            "ioavState": {
              "type": "string",
              "title": "IOAV State",
              "description": "IOAV state",
              "order": 5
            },
            "lastAsSignatureAge": {
              "type": "string",
              "title": "Last As Signature Age",
              "description": "Last as signature age",
              "order": 2
            },
            "lastAvSignatureAge": {
              "type": "string",
              "title": "Last AV Signature Age",
              "description": "Last AV signature age",
              "order": 22
            },
            "lastFullScanAge": {
              "type": "string",
              "title": "Last Full Scan Age",
              "description": "Last full scan age",
              "order": 25
            },
            "lastFullScanEndTime": {
              "type": "string",
              "title": "Last Full Scan End Time",
              "description": "Last full scan end time",
              "order": 13
            },
            "lastFullScanSource": {
              "type": "string",
              "title": "Last Full Scan Source",
              "description": "Last full scan source",
              "order": 7
            },
            "lastFullScanStartTime": {
              "type": "string",
              "title": "Last Full Scan Start Time",
              "description": "Last full scan start time",
              "order": 9
            },
            "lastQuickScanAge": {
              "type": "string",
              "title": "Last Quick Scan Age",
              "description": "Last quick scan age",
              "order": 17
            },
            "lastQuickScanEndTime": {
              "type": "string",
              "title": "Last Quick Scan End Time",
              "description": "Last quick scan end time",
              "order": 19
            },
            "lastQuickScanSource": {
              "type": "string",
              "title": "Last Quick Scan Source",
              "description": "Last quick scan source",
              "order": 12
            },
            "lastQuickScanStartTime": {
              "type": "string",
              "title": "Last Quick Scan Start Time",
              "description": "Last quick scan start time",
              "order": 24
            },
            "nriEngineVersion": {
              "type": "string",
              "title": "NRI Engine Version",
              "description": "NRI engine version",
              "order": 23
            },
            "nriSignatureVersion": {
              "type": "string",
              "title": "NRI Signature Version",
              "description": "NRI signature version",
              "order": 8
            },
            "oaState": {
              "type": "string",
              "title": "OA State",
              "description": "OA state",
              "order": 1
            },
            "platformVersion": {
              "type": "string",
              "title": "Platform Version",
              "description": "Platform version",
              "order": 16
            },
            "productName": {
              "type": "string",
              "title": "Product Name",
              "description": "Product name",
              "order": 14
            },
            "productStatus": {
              "type": "string",
              "title": "Product Status",
              "description": "Product status",
              "order": 3
            },
            "rtpState": {
              "type": "string",
              "title": "RTP State",
              "description": "RTP state",
              "order": 15
            }
          }
        },
        "label": {
          "type": "object",
          "title": "label",
          "properties": {
            "id": {
              "type": "string",
              "title": "ID",
              "description": "Label ID",
              "order": 1
            },
            "links": {
              "type": "array",
              "title": "Links",
              "description": "Label links",
              "items": {
                "$ref": "#/definitions/link"
              },
              "order": 2
            }
          },
          "definitions": {
            "link": {
              "type": "object",
              "title": "link",
              "properties": {
                "href": {
                  "type": "string",
                  "title": "HREF",
                  "description": "HREF",
                  "order": 2
                },
                "rel": {
                  "type": "string",
                  "title": "Relation",
                  "description": "Relation",
                  "order": 1
                }
              }
            }
          }
        },
        "link": {
          "type": "object",
          "title": "link",
          "properties": {
            "href": {
              "type": "string",
              "title": "HREF",
              "description": "HREF",
              "order": 2
            },
            "rel": {
              "type": "string",
              "title": "Relation",
              "description": "Relation",
              "order": 1
            }
          }
        },
        "message": {
          "type": "object",
          "title": "message",
          "properties": {
            "computerName": {
              "type": "string",
              "title": "Computer Name",
              "order": 3
            },
            "eventCode": {
              "type": "integer",
              "title": "Event Code",
              "order": 2
            },
            "eventData": {
              "$ref": "#/definitions/eventData",
              "title": "Event Data",
              "order": 6
            },
            "isDomainController": {
              "type": "boolean",
              "title": "Is Domain Controller",
              "order": 5
            },
            "sid": {
              "type": "string",
              "title": "SID",
              "order": 4
            },
            "sourceName": {
              "type": "string",
              "title": "Source Name",
              "order": 1
            },
            "timeWritten": {
              "type": "string",
              "title": "Time Written",
              "order": 7
            }
          },
          "definitions": {
            "eventData": {
              "type": "object",
              "title": "eventData",
              "properties": {
                "asSignatureCreationTime": {
                  "type": "string",
                  "title": "As Signature Creation Time",
                  "description": "As signature creation time",
                  "order": 6
                },
                "assignatureVersion": {
                  "type": "string",
                  "title": "As Signature Version",
                  "description": "As signature version",
                  "order": 4
                },
                "avSignatureCreationTime": {
                  "type": "string",
                  "title": "AV Signature Creation Time",
                  "description": "AV signature creation time",
                  "order": 20
                },
                "avsignatureVersion": {
                  "type": "string",
                  "title": "AV Signature Version",
                  "description": "AV signature version",
                  "order": 21
                },
                "bmState": {
                  "type": "string",
                  "title": "BMS State",
                  "description": "BMS state",
                  "order": 11
                },
                "data": {
                  "type": "array",
                  "title": "Data",
                  "description": "Data",
                  "items": {
                    "type": "object"
                  },
                  "order": 18
                },
                "engineVersion": {
                  "type": "string",
                  "title": "Engine Version",
                  "description": "Engine version",
                  "order": 10
                },
                "ioavState": {
                  "type": "string",
                  "title": "IOAV State",
                  "description": "IOAV state",
                  "order": 5
                },
                "lastAsSignatureAge": {
                  "type": "string",
                  "title": "Last As Signature Age",
                  "description": "Last as signature age",
                  "order": 2
                },
                "lastAvSignatureAge": {
                  "type": "string",
                  "title": "Last AV Signature Age",
                  "description": "Last AV signature age",
                  "order": 22
                },
                "lastFullScanAge": {
                  "type": "string",
                  "title": "Last Full Scan Age",
                  "description": "Last full scan age",
                  "order": 25
                },
                "lastFullScanEndTime": {
                  "type": "string",
                  "title": "Last Full Scan End Time",
                  "description": "Last full scan end time",
                  "order": 13
                },
                "lastFullScanSource": {
                  "type": "string",
                  "title": "Last Full Scan Source",
                  "description": "Last full scan source",
                  "order": 7
                },
                "lastFullScanStartTime": {
                  "type": "string",
                  "title": "Last Full Scan Start Time",
                  "description": "Last full scan start time",
                  "order": 9
                },
                "lastQuickScanAge": {
                  "type": "string",
                  "title": "Last Quick Scan Age",
                  "description": "Last quick scan age",
                  "order": 17
                },
                "lastQuickScanEndTime": {
                  "type": "string",
                  "title": "Last Quick Scan End Time",
                  "description": "Last quick scan end time",
                  "order": 19
                },
                "lastQuickScanSource": {
                  "type": "string",
                  "title": "Last Quick Scan Source",
                  "description": "Last quick scan source",
                  "order": 12
                },
                "lastQuickScanStartTime": {
                  "type": "string",
                  "title": "Last Quick Scan Start Time",
                  "description": "Last quick scan start time",
                  "order": 24
                },
                "nriEngineVersion": {
                  "type": "string",
                  "title": "NRI Engine Version",
                  "description": "NRI engine version",
                  "order": 23
                },
                "nriSignatureVersion": {
                  "type": "string",
                  "title": "NRI Signature Version",
                  "description": "NRI signature version",
                  "order": 8
                },
                "oaState": {
                  "type": "string",
                  "title": "OA State",
                  "description": "OA state",
                  "order": 1
                },
                "platformVersion": {
                  "type": "string",
                  "title": "Platform Version",
                  "description": "Platform version",
                  "order": 16
                },
                "productName": {
                  "type": "string",
                  "title": "Product Name",
                  "description": "Product name",
                  "order": 14
                },
                "productStatus": {
                  "type": "string",
                  "title": "Product Status",
                  "description": "Product status",
                  "order": 3
                },
                "rtpState": {
                  "type": "string",
                  "title": "RTP State",
                  "description": "RTP state",
                  "order": 15
                }
              }
            }
          }
        }
      }
    },
    "label": {
      "type": "object",
      "title": "label",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Label ID",
          "order": 1
        },
        "links": {
          "type": "array",
          "title": "Links",
          "description": "Label links",
          "items": {
            "$ref": "#/definitions/link"
          },
          "order": 2
        }
      },
      "definitions": {
        "link": {
          "type": "object",
          "title": "link",
          "properties": {
            "href": {
              "type": "string",
              "title": "HREF",
              "description": "HREF",
              "order": 2
            },
            "rel": {
              "type": "string",
              "title": "Relation",
              "description": "Relation",
              "order": 1
            }
          }
        }
      }
    },
    "link": {
      "type": "object",
      "title": "link",
      "properties": {
        "href": {
          "type": "string",
          "title": "HREF",
          "description": "HREF",
          "order": 2
        },
        "rel": {
          "type": "string",
          "title": "Relation",
          "description": "Relation",
          "order": 1
        }
      }
    },
    "message": {
      "type": "object",
      "title": "message",
      "properties": {
        "computerName": {
          "type": "string",
          "title": "Computer Name",
          "order": 3
        },
        "eventCode": {
          "type": "integer",
          "title": "Event Code",
          "order": 2
        },
        "eventData": {
          "$ref": "#/definitions/eventData",
          "title": "Event Data",
          "order": 6
        },
        "isDomainController": {
          "type": "boolean",
          "title": "Is Domain Controller",
          "order": 5
        },
        "sid": {
          "type": "string",
          "title": "SID",
          "order": 4
        },
        "sourceName": {
          "type": "string",
          "title": "Source Name",
          "order": 1
        },
        "timeWritten": {
          "type": "string",
          "title": "Time Written",
          "order": 7
        }
      },
      "definitions": {
        "eventData": {
          "type": "object",
          "title": "eventData",
          "properties": {
            "asSignatureCreationTime": {
              "type": "string",
              "title": "As Signature Creation Time",
              "description": "As signature creation time",
              "order": 6
            },
            "assignatureVersion": {
              "type": "string",
              "title": "As Signature Version",
              "description": "As signature version",
              "order": 4
            },
            "avSignatureCreationTime": {
              "type": "string",
              "title": "AV Signature Creation Time",
              "description": "AV signature creation time",
              "order": 20
            },
            "avsignatureVersion": {
              "type": "string",
              "title": "AV Signature Version",
              "description": "AV signature version",
              "order": 21
            },
            "bmState": {
              "type": "string",
              "title": "BMS State",
              "description": "BMS state",
              "order": 11
            },
            "data": {
              "type": "array",
              "title": "Data",
              "description": "Data",
              "items": {
                "type": "object"
              },
              "order": 18
            },
            "engineVersion": {
              "type": "string",
              "title": "Engine Version",
              "description": "Engine version",
              "order": 10
            },
            "ioavState": {
              "type": "string",
              "title": "IOAV State",
              "description": "IOAV state",
              "order": 5
            },
            "lastAsSignatureAge": {
              "type": "string",
              "title": "Last As Signature Age",
              "description": "Last as signature age",
              "order": 2
            },
            "lastAvSignatureAge": {
              "type": "string",
              "title": "Last AV Signature Age",
              "description": "Last AV signature age",
              "order": 22
            },
            "lastFullScanAge": {
              "type": "string",
              "title": "Last Full Scan Age",
              "description": "Last full scan age",
              "order": 25
            },
            "lastFullScanEndTime": {
              "type": "string",
              "title": "Last Full Scan End Time",
              "description": "Last full scan end time",
              "order": 13
            },
            "lastFullScanSource": {
              "type": "string",
              "title": "Last Full Scan Source",
              "description": "Last full scan source",
              "order": 7
            },
            "lastFullScanStartTime": {
              "type": "string",
              "title": "Last Full Scan Start Time",
              "description": "Last full scan start time",
              "order": 9
            },
            "lastQuickScanAge": {
              "type": "string",
              "title": "Last Quick Scan Age",
              "description": "Last quick scan age",
              "order": 17
            },
            "lastQuickScanEndTime": {
              "type": "string",
              "title": "Last Quick Scan End Time",
              "description": "Last quick scan end time",
              "order": 19
            },
            "lastQuickScanSource": {
              "type": "string",
              "title": "Last Quick Scan Source",
              "description": "Last quick scan source",
              "order": 12
            },
            "lastQuickScanStartTime": {
              "type": "string",
              "title": "Last Quick Scan Start Time",
              "description": "Last quick scan start time",
              "order": 24
            },
            "nriEngineVersion": {
              "type": "string",
              "title": "NRI Engine Version",
              "description": "NRI engine version",
              "order": 23
            },
            "nriSignatureVersion": {
              "type": "string",
              "title": "NRI Signature Version",
              "description": "NRI signature version",
              "order": 8
            },
            "oaState": {
              "type": "string",
              "title": "OA State",
              "description": "OA state",
              "order": 1
            },
            "platformVersion": {
              "type": "string",
              "title": "Platform Version",
              "description": "Platform version",
              "order": 16
            },
            "productName": {
              "type": "string",
              "title": "Product Name",
              "description": "Product name",
              "order": 14
            },
            "productStatus": {
              "type": "string",
              "title": "Product Status",
              "description": "Product status",
              "order": 3
            },
            "rtpState": {
              "type": "string",
              "title": "RTP State",
              "description": "RTP state",
              "order": 15
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