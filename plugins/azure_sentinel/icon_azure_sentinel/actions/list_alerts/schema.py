# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "This action is used to get all alerts for a given incident"


class Input:
    INCIDENTID = "incidentId"
    RESOURCEGROUPNAME = "resourceGroupName"
    SUBSCRIPTIONID = "subscriptionId"
    WORKSPACENAME = "workspaceName"
    

class Output:
    ALERTS = "alerts"
    

class ListAlertsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "incidentId": {
      "type": "string",
      "title": "Incident ID",
      "description": "Incident ID",
      "order": 1
    },
    "resourceGroupName": {
      "type": "string",
      "title": "Resource Group Name",
      "description": "The name of the resource group within the user's subscription",
      "order": 2
    },
    "subscriptionId": {
      "type": "string",
      "title": "Subscription ID",
      "description": "Azure subscription ID",
      "order": 3
    },
    "workspaceName": {
      "type": "string",
      "title": "Workspace Name",
      "description": "The name of the workspace",
      "order": 4
    }
  },
  "required": [
    "incidentId",
    "resourceGroupName",
    "subscriptionId",
    "workspaceName"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ListAlertsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "alerts": {
      "type": "array",
      "title": "Alerts",
      "description": "All the alerts assigned to the given incident",
      "items": {
        "$ref": "#/definitions/Alert"
      },
      "order": 1
    }
  },
  "definitions": {
    "Alert": {
      "type": "object",
      "title": "Alert",
      "properties": {
        "properties": {
          "$ref": "#/definitions/AlertProperties",
          "title": "Properties",
          "description": "Alert's properties",
          "order": 1
        }
      },
      "definitions": {
        "AlertProperties": {
          "type": "object",
          "title": "AlertProperties",
          "properties": {
            "additionalData": {
              "type": "object",
              "title": "Additional Data",
              "description": "Custom fields that should be part of the entity and will be presented to the user",
              "order": 1
            },
            "alertDisplayName": {
              "type": "string",
              "title": "Alert Display Name",
              "description": "The display name of the alert",
              "order": 2
            },
            "alertLink": {
              "type": "string",
              "title": "Alert Link",
              "description": "The URI link of the alert",
              "order": 3
            },
            "alertType": {
              "type": "string",
              "title": "Alert Type",
              "description": "The type name of the alert",
              "order": 4
            },
            "compromisedEntity": {
              "type": "string",
              "title": "Compromised Entity",
              "description": "Display name of the main entity being reported on",
              "order": 5
            },
            "confidenceLevel": {
              "type": "string",
              "title": "Confidence Level",
              "description": "The confidence level of this alert",
              "order": 6
            },
            "confidenceReasons": {
              "type": "array",
              "title": "Confidence Reasons",
              "description": "The confidence reasons",
              "items": {
                "$ref": "#/definitions/ConfidenceReasons"
              },
              "order": 7
            },
            "confidenceScore": {
              "type": "integer",
              "title": "Confidence Score",
              "description": "The confidence score of the alert",
              "order": 8
            },
            "confidenceScoreStatus": {
              "type": "string",
              "title": "Confidence Score Status",
              "description": "The confidence score calculation status, i.e. indicating if score calculation is pending for this alert, not applicable or final",
              "order": 9
            },
            "description": {
              "type": "string",
              "title": "Description",
              "description": "Alert description",
              "order": 10
            },
            "endTimeUtc": {
              "type": "string",
              "title": "End Time UTC",
              "displayType": "date",
              "description": "The impact end time of the alert",
              "format": "date-time",
              "order": 11
            },
            "friendlyName": {
              "type": "string",
              "title": "Friendly Display Name",
              "description": "The graph item display name which is a short humanly readable description of the graph item instance",
              "order": 12
            },
            "intent": {
              "type": "string",
              "title": "Intent",
              "description": "Holds the alert intent stage(s) mapping for this alert",
              "order": 13
            },
            "processingEndTime": {
              "type": "string",
              "title": "Processing End Time",
              "displayType": "date",
              "description": "The time the alert was made available for consumption",
              "format": "date-time",
              "order": 14
            },
            "productComponentName": {
              "type": "string",
              "title": "Product Component Name",
              "description": "The name of a component inside the product which generated the alert",
              "order": 15
            },
            "productName": {
              "type": "string",
              "title": "Product Name",
              "description": "The name of the product which published this alert",
              "order": 16
            },
            "productVersion": {
              "type": "string",
              "title": "Product Version",
              "description": "The version of the product generating the alert",
              "order": 17
            },
            "providerAlertId": {
              "type": "string",
              "title": "Provider Alert ID",
              "description": "The identifier of the alert inside the product which generated the alert",
              "order": 18
            },
            "remediationSteps": {
              "type": "array",
              "title": "Remediation Steps",
              "description": "Manual action items to take to remediate the alert",
              "items": {
                "type": "string"
              },
              "order": 19
            },
            "resourceIdentifiers": {
              "type": "array",
              "title": "Resource Identifiers",
              "description": "The list of resource identifiers of the alert",
              "items": {
                "type": "object"
              },
              "order": 20
            },
            "severity": {
              "type": "string",
              "title": "Severity",
              "description": "The severity of the alert",
              "order": 21
            },
            "startTimeUtc": {
              "type": "string",
              "title": "Start Time UTC",
              "displayType": "date",
              "description": "The impact start time of the alert (the time of the first event contributing to the alert)",
              "format": "date-time",
              "order": 22
            },
            "status": {
              "type": "string",
              "title": "Status",
              "description": "The lifecycle status of the alert",
              "order": 23
            },
            "systemAlertId": {
              "type": "string",
              "title": "System Alert ID",
              "description": "Holds the product identifier of the alert for the product",
              "order": 24
            },
            "systemData": {
              "$ref": "#/definitions/SystemData",
              "title": "System Data",
              "description": "Azure Resource Manager metadata containing createdBy and modifiedBy information",
              "order": 25
            },
            "tactics": {
              "type": "array",
              "title": "Tactics",
              "description": "The tactics of the alert",
              "items": {
                "type": "string"
              },
              "order": 26
            },
            "timeGenerated": {
              "type": "string",
              "title": "Title",
              "displayType": "date",
              "description": "The time the alert was generated",
              "format": "date-time",
              "order": 27
            },
            "type": {
              "type": "string",
              "title": "Title",
              "description": "Azure resource type",
              "order": 28
            },
            "vendorName": {
              "type": "string",
              "title": "Vendor Name",
              "description": "The name of the vendor that raised the alert",
              "order": 29
            }
          },
          "definitions": {
            "ConfidenceReasons": {
              "type": "object",
              "title": "ConfidenceReasons",
              "properties": {
                "reason": {
                  "type": "string",
                  "title": "Reason",
                  "description": "Reason's description",
                  "order": 1
                },
                "reasonType": {
                  "type": "string",
                  "title": "Reason Type",
                  "description": "The reason's type (category)",
                  "order": 2
                }
              }
            },
            "CreatedByType": {
              "type": "object",
              "title": "CreatedByType",
              "properties": {
                "Application": {
                  "type": "string",
                  "title": "Application",
                  "description": "Application",
                  "order": 1
                },
                "Key": {
                  "type": "string",
                  "title": "Key",
                  "description": "Description",
                  "order": 2
                },
                "ManagedIdentity": {
                  "type": "string",
                  "title": "Managed Indentity",
                  "description": "Managed identity",
                  "order": 3
                },
                "User": {
                  "type": "string",
                  "title": "User",
                  "description": "User",
                  "order": 4
                }
              }
            },
            "SystemData": {
              "type": "object",
              "title": "SystemData",
              "properties": {
                "createdAt": {
                  "type": "string",
                  "title": "Created At",
                  "displayType": "date",
                  "description": "The timestamp of resource creation (UTC)",
                  "format": "date-time",
                  "order": 1
                },
                "createdBy": {
                  "type": "string",
                  "title": "Created By",
                  "description": "The identity that created the resource",
                  "order": 2
                },
                "createdByType": {
                  "$ref": "#/definitions/CreatedByType",
                  "title": "Created By Type",
                  "description": "The type of identity that created the resource",
                  "order": 3
                },
                "lastModifiedAt": {
                  "type": "string",
                  "title": "Last Modified At",
                  "displayType": "date",
                  "description": "The timestamp of resource last modification (UTC)",
                  "format": "date-time",
                  "order": 4
                },
                "lastModifiedBy": {
                  "type": "string",
                  "title": "Last Modified By",
                  "description": "The identity that last modified the resource",
                  "order": 5
                },
                "lastModifiedByType": {
                  "$ref": "#/definitions/CreatedByType",
                  "title": "Last Modified By Type",
                  "description": "The type of identity that last modified the resource",
                  "order": 6
                }
              },
              "definitions": {
                "CreatedByType": {
                  "type": "object",
                  "title": "CreatedByType",
                  "properties": {
                    "Application": {
                      "type": "string",
                      "title": "Application",
                      "description": "Application",
                      "order": 1
                    },
                    "Key": {
                      "type": "string",
                      "title": "Key",
                      "description": "Description",
                      "order": 2
                    },
                    "ManagedIdentity": {
                      "type": "string",
                      "title": "Managed Indentity",
                      "description": "Managed identity",
                      "order": 3
                    },
                    "User": {
                      "type": "string",
                      "title": "User",
                      "description": "User",
                      "order": 4
                    }
                  }
                }
              }
            }
          }
        },
        "ConfidenceReasons": {
          "type": "object",
          "title": "ConfidenceReasons",
          "properties": {
            "reason": {
              "type": "string",
              "title": "Reason",
              "description": "Reason's description",
              "order": 1
            },
            "reasonType": {
              "type": "string",
              "title": "Reason Type",
              "description": "The reason's type (category)",
              "order": 2
            }
          }
        },
        "CreatedByType": {
          "type": "object",
          "title": "CreatedByType",
          "properties": {
            "Application": {
              "type": "string",
              "title": "Application",
              "description": "Application",
              "order": 1
            },
            "Key": {
              "type": "string",
              "title": "Key",
              "description": "Description",
              "order": 2
            },
            "ManagedIdentity": {
              "type": "string",
              "title": "Managed Indentity",
              "description": "Managed identity",
              "order": 3
            },
            "User": {
              "type": "string",
              "title": "User",
              "description": "User",
              "order": 4
            }
          }
        },
        "SystemData": {
          "type": "object",
          "title": "SystemData",
          "properties": {
            "createdAt": {
              "type": "string",
              "title": "Created At",
              "displayType": "date",
              "description": "The timestamp of resource creation (UTC)",
              "format": "date-time",
              "order": 1
            },
            "createdBy": {
              "type": "string",
              "title": "Created By",
              "description": "The identity that created the resource",
              "order": 2
            },
            "createdByType": {
              "$ref": "#/definitions/CreatedByType",
              "title": "Created By Type",
              "description": "The type of identity that created the resource",
              "order": 3
            },
            "lastModifiedAt": {
              "type": "string",
              "title": "Last Modified At",
              "displayType": "date",
              "description": "The timestamp of resource last modification (UTC)",
              "format": "date-time",
              "order": 4
            },
            "lastModifiedBy": {
              "type": "string",
              "title": "Last Modified By",
              "description": "The identity that last modified the resource",
              "order": 5
            },
            "lastModifiedByType": {
              "$ref": "#/definitions/CreatedByType",
              "title": "Last Modified By Type",
              "description": "The type of identity that last modified the resource",
              "order": 6
            }
          },
          "definitions": {
            "CreatedByType": {
              "type": "object",
              "title": "CreatedByType",
              "properties": {
                "Application": {
                  "type": "string",
                  "title": "Application",
                  "description": "Application",
                  "order": 1
                },
                "Key": {
                  "type": "string",
                  "title": "Key",
                  "description": "Description",
                  "order": 2
                },
                "ManagedIdentity": {
                  "type": "string",
                  "title": "Managed Indentity",
                  "description": "Managed identity",
                  "order": 3
                },
                "User": {
                  "type": "string",
                  "title": "User",
                  "description": "User",
                  "order": 4
                }
              }
            }
          }
        }
      }
    },
    "AlertProperties": {
      "type": "object",
      "title": "AlertProperties",
      "properties": {
        "additionalData": {
          "type": "object",
          "title": "Additional Data",
          "description": "Custom fields that should be part of the entity and will be presented to the user",
          "order": 1
        },
        "alertDisplayName": {
          "type": "string",
          "title": "Alert Display Name",
          "description": "The display name of the alert",
          "order": 2
        },
        "alertLink": {
          "type": "string",
          "title": "Alert Link",
          "description": "The URI link of the alert",
          "order": 3
        },
        "alertType": {
          "type": "string",
          "title": "Alert Type",
          "description": "The type name of the alert",
          "order": 4
        },
        "compromisedEntity": {
          "type": "string",
          "title": "Compromised Entity",
          "description": "Display name of the main entity being reported on",
          "order": 5
        },
        "confidenceLevel": {
          "type": "string",
          "title": "Confidence Level",
          "description": "The confidence level of this alert",
          "order": 6
        },
        "confidenceReasons": {
          "type": "array",
          "title": "Confidence Reasons",
          "description": "The confidence reasons",
          "items": {
            "$ref": "#/definitions/ConfidenceReasons"
          },
          "order": 7
        },
        "confidenceScore": {
          "type": "integer",
          "title": "Confidence Score",
          "description": "The confidence score of the alert",
          "order": 8
        },
        "confidenceScoreStatus": {
          "type": "string",
          "title": "Confidence Score Status",
          "description": "The confidence score calculation status, i.e. indicating if score calculation is pending for this alert, not applicable or final",
          "order": 9
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Alert description",
          "order": 10
        },
        "endTimeUtc": {
          "type": "string",
          "title": "End Time UTC",
          "displayType": "date",
          "description": "The impact end time of the alert",
          "format": "date-time",
          "order": 11
        },
        "friendlyName": {
          "type": "string",
          "title": "Friendly Display Name",
          "description": "The graph item display name which is a short humanly readable description of the graph item instance",
          "order": 12
        },
        "intent": {
          "type": "string",
          "title": "Intent",
          "description": "Holds the alert intent stage(s) mapping for this alert",
          "order": 13
        },
        "processingEndTime": {
          "type": "string",
          "title": "Processing End Time",
          "displayType": "date",
          "description": "The time the alert was made available for consumption",
          "format": "date-time",
          "order": 14
        },
        "productComponentName": {
          "type": "string",
          "title": "Product Component Name",
          "description": "The name of a component inside the product which generated the alert",
          "order": 15
        },
        "productName": {
          "type": "string",
          "title": "Product Name",
          "description": "The name of the product which published this alert",
          "order": 16
        },
        "productVersion": {
          "type": "string",
          "title": "Product Version",
          "description": "The version of the product generating the alert",
          "order": 17
        },
        "providerAlertId": {
          "type": "string",
          "title": "Provider Alert ID",
          "description": "The identifier of the alert inside the product which generated the alert",
          "order": 18
        },
        "remediationSteps": {
          "type": "array",
          "title": "Remediation Steps",
          "description": "Manual action items to take to remediate the alert",
          "items": {
            "type": "string"
          },
          "order": 19
        },
        "resourceIdentifiers": {
          "type": "array",
          "title": "Resource Identifiers",
          "description": "The list of resource identifiers of the alert",
          "items": {
            "type": "object"
          },
          "order": 20
        },
        "severity": {
          "type": "string",
          "title": "Severity",
          "description": "The severity of the alert",
          "order": 21
        },
        "startTimeUtc": {
          "type": "string",
          "title": "Start Time UTC",
          "displayType": "date",
          "description": "The impact start time of the alert (the time of the first event contributing to the alert)",
          "format": "date-time",
          "order": 22
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "The lifecycle status of the alert",
          "order": 23
        },
        "systemAlertId": {
          "type": "string",
          "title": "System Alert ID",
          "description": "Holds the product identifier of the alert for the product",
          "order": 24
        },
        "systemData": {
          "$ref": "#/definitions/SystemData",
          "title": "System Data",
          "description": "Azure Resource Manager metadata containing createdBy and modifiedBy information",
          "order": 25
        },
        "tactics": {
          "type": "array",
          "title": "Tactics",
          "description": "The tactics of the alert",
          "items": {
            "type": "string"
          },
          "order": 26
        },
        "timeGenerated": {
          "type": "string",
          "title": "Title",
          "displayType": "date",
          "description": "The time the alert was generated",
          "format": "date-time",
          "order": 27
        },
        "type": {
          "type": "string",
          "title": "Title",
          "description": "Azure resource type",
          "order": 28
        },
        "vendorName": {
          "type": "string",
          "title": "Vendor Name",
          "description": "The name of the vendor that raised the alert",
          "order": 29
        }
      },
      "definitions": {
        "ConfidenceReasons": {
          "type": "object",
          "title": "ConfidenceReasons",
          "properties": {
            "reason": {
              "type": "string",
              "title": "Reason",
              "description": "Reason's description",
              "order": 1
            },
            "reasonType": {
              "type": "string",
              "title": "Reason Type",
              "description": "The reason's type (category)",
              "order": 2
            }
          }
        },
        "CreatedByType": {
          "type": "object",
          "title": "CreatedByType",
          "properties": {
            "Application": {
              "type": "string",
              "title": "Application",
              "description": "Application",
              "order": 1
            },
            "Key": {
              "type": "string",
              "title": "Key",
              "description": "Description",
              "order": 2
            },
            "ManagedIdentity": {
              "type": "string",
              "title": "Managed Indentity",
              "description": "Managed identity",
              "order": 3
            },
            "User": {
              "type": "string",
              "title": "User",
              "description": "User",
              "order": 4
            }
          }
        },
        "SystemData": {
          "type": "object",
          "title": "SystemData",
          "properties": {
            "createdAt": {
              "type": "string",
              "title": "Created At",
              "displayType": "date",
              "description": "The timestamp of resource creation (UTC)",
              "format": "date-time",
              "order": 1
            },
            "createdBy": {
              "type": "string",
              "title": "Created By",
              "description": "The identity that created the resource",
              "order": 2
            },
            "createdByType": {
              "$ref": "#/definitions/CreatedByType",
              "title": "Created By Type",
              "description": "The type of identity that created the resource",
              "order": 3
            },
            "lastModifiedAt": {
              "type": "string",
              "title": "Last Modified At",
              "displayType": "date",
              "description": "The timestamp of resource last modification (UTC)",
              "format": "date-time",
              "order": 4
            },
            "lastModifiedBy": {
              "type": "string",
              "title": "Last Modified By",
              "description": "The identity that last modified the resource",
              "order": 5
            },
            "lastModifiedByType": {
              "$ref": "#/definitions/CreatedByType",
              "title": "Last Modified By Type",
              "description": "The type of identity that last modified the resource",
              "order": 6
            }
          },
          "definitions": {
            "CreatedByType": {
              "type": "object",
              "title": "CreatedByType",
              "properties": {
                "Application": {
                  "type": "string",
                  "title": "Application",
                  "description": "Application",
                  "order": 1
                },
                "Key": {
                  "type": "string",
                  "title": "Key",
                  "description": "Description",
                  "order": 2
                },
                "ManagedIdentity": {
                  "type": "string",
                  "title": "Managed Indentity",
                  "description": "Managed identity",
                  "order": 3
                },
                "User": {
                  "type": "string",
                  "title": "User",
                  "description": "User",
                  "order": 4
                }
              }
            }
          }
        }
      }
    },
    "ConfidenceReasons": {
      "type": "object",
      "title": "ConfidenceReasons",
      "properties": {
        "reason": {
          "type": "string",
          "title": "Reason",
          "description": "Reason's description",
          "order": 1
        },
        "reasonType": {
          "type": "string",
          "title": "Reason Type",
          "description": "The reason's type (category)",
          "order": 2
        }
      }
    },
    "CreatedByType": {
      "type": "object",
      "title": "CreatedByType",
      "properties": {
        "Application": {
          "type": "string",
          "title": "Application",
          "description": "Application",
          "order": 1
        },
        "Key": {
          "type": "string",
          "title": "Key",
          "description": "Description",
          "order": 2
        },
        "ManagedIdentity": {
          "type": "string",
          "title": "Managed Indentity",
          "description": "Managed identity",
          "order": 3
        },
        "User": {
          "type": "string",
          "title": "User",
          "description": "User",
          "order": 4
        }
      }
    },
    "SystemData": {
      "type": "object",
      "title": "SystemData",
      "properties": {
        "createdAt": {
          "type": "string",
          "title": "Created At",
          "displayType": "date",
          "description": "The timestamp of resource creation (UTC)",
          "format": "date-time",
          "order": 1
        },
        "createdBy": {
          "type": "string",
          "title": "Created By",
          "description": "The identity that created the resource",
          "order": 2
        },
        "createdByType": {
          "$ref": "#/definitions/CreatedByType",
          "title": "Created By Type",
          "description": "The type of identity that created the resource",
          "order": 3
        },
        "lastModifiedAt": {
          "type": "string",
          "title": "Last Modified At",
          "displayType": "date",
          "description": "The timestamp of resource last modification (UTC)",
          "format": "date-time",
          "order": 4
        },
        "lastModifiedBy": {
          "type": "string",
          "title": "Last Modified By",
          "description": "The identity that last modified the resource",
          "order": 5
        },
        "lastModifiedByType": {
          "$ref": "#/definitions/CreatedByType",
          "title": "Last Modified By Type",
          "description": "The type of identity that last modified the resource",
          "order": 6
        }
      },
      "definitions": {
        "CreatedByType": {
          "type": "object",
          "title": "CreatedByType",
          "properties": {
            "Application": {
              "type": "string",
              "title": "Application",
              "description": "Application",
              "order": 1
            },
            "Key": {
              "type": "string",
              "title": "Key",
              "description": "Description",
              "order": 2
            },
            "ManagedIdentity": {
              "type": "string",
              "title": "Managed Indentity",
              "description": "Managed identity",
              "order": 3
            },
            "User": {
              "type": "string",
              "title": "User",
              "description": "User",
              "order": 4
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
