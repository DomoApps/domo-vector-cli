# Remote Domostats API

This API provides access to retrieve information about applications and jobs within the Domo environment. It includes methods to fetch a list of applications, view job details for specific applications, and update job configurations.

## Get Applications

**Method:** `GET`  
**Endpoint:** `/api/executor/v1/applications/`

### Example Request:

```json
{
  "method": "GET",
  "url": "https://{domo_instance}.domo.com/api/executor/v1/applications/",
  "headers": {
    "X-DOMO-Developer-Token": "",
  }
}
```

### Parameters:

| Property Name | Type   | Required | Description                             |
| ------------- | ------ | -------- | --------------------------------------- |
| session_token | String | Yes      | Authentication token to access the API. |

### Response:

```json
{
  "id": "94a4edfa-5926-4f0c-ad1e-a341f53f6113",
  "displayType": "DataFlow",
  "type": "DataFlow",
  "name": "DomoStats People with Activity Log",
  "owner": {
    "id": "",
    "name": "",
    "type": "USER",
    "group": false
  },
  "status": "SUCCESS",
  "created": 1624432428000,
  "lastTouched": 1651769881000,
  "rowCount": 833556,
  "columnCount": 18,
  "cardInfo": {
    "cardCount": 9,
    "cardViewCount": 0
  },
  "properties": {
    "formulas": {
      "formulas": {
        "calculation_534c74ab-37aa-48dc-8322-34bb5784a9f0": {
          "templateId": 1109,
          "name": "Content Creation Filter",
          "formula": "(CASE WHEN ((`Object_Type` = 'CARD') AND `Action` IN ('CREATED', 'UPDATED', 'ADDED', 'DUPLICATED', 'SHARED')) THEN 1 ELSE 0 END)"
        }
      }
    }
  }
}
```

## Get List of Jobs

**Method**: `GET`  
**Endpoint**: `/api/executor/v2/applications/{applicationId}/jobs`

### Example Request

```json
{
  "method": "GET",
  "url": "https://{domo_instance}.domo.com/api/executor/v2/applications/50e7230f-d2f2-42e2-a208-d94c8ae9f64c/jobs?offset=0",
  "headers": {
    "X-DOMO-Developer-Token": "",
  }
}
```

### **Parameters**

| Property Name | Type   | Required | Description                           |
| ------------- | ------ | -------- | ------------------------------------- |
| `offset`      | Number | no       | The results offset. The default is 0. |

### **Response**

```json
{
  "id": "94a4edfa-5926-4f0c-ad1e-a341f53f6113",
  "displayType": "DataFlow",
  "type": "DataFlow",
  "name": "DomoStats People with Activity Log",
  "owner": {
    "id": "",
    "name": "",
    "type": "USER",
    "group": false
  },
  "status": "SUCCESS",
  "created": 1624432428000,
  "lastTouched": 1651769881000,
  "lastUpdated": 1651769880787,
  "rowCount": 833556,
  "columnCount": 18,
  "cardInfo": {
    "cardCount": 9,
    "cardViewCount": 0
  },
  "properties": {
    "formulas": {
      "calculation_534c74ab-37aa-48dc-8322-34bb5784a9f0": {
        "templateId": 1109,
        "id": "calculation_534c74ab-37aa-48dc-8322-34bb5784a9f0",
        "name": "Content Creation Filter",
        "formula": "(CASE WHEN ((`Object_Type` = 'CARD') AND `Action` IN ('CREATED', 'UPDATED’, ‘ADDED’, ‘DUPLICATED’, ‘SHARED')) THEN 1 WHEN ((`Object_Type` = 'DRILL_VIEW') AND (`Action` = 'ADD_DRILL_VIEW')) THEN 1 ...",
        "status": "VALID",
        "persistedOnDataSource": true
      }
    }
  },
  "validConfiguration": true,
  "validAccount": true,
  "adc": true,
  "cloudId": "domo",
  "permissions": "READ_WRITE_DELETE_SHARE_ADMIN",
  "tags": "[\"domoStats\",\"domostats\",\"c_people\"]"
}
```

## Update the Job

**Method**: `PUT`  
**Endpoint**: `/api/executor/v1/applications/{Application_Id}/jobs/{Job_Id}`

### Example:

```json
{
  "method": "PUT",
  "url": "https://{domo_instance}.domo.com/api/executor/v1/applications/{Application_Id}/jobs/{Job_Id}",
  "body": {
    "jobId": "526906bb-e7e0-4f70-9ca0-3bb4fdf99c82",
    "jobName": "domo-labs-dev2.dev.domo.com",
    "executionTimeout": 720,
    "executionPayload": {
      "remoteInstance": "domo-labs-dev.dev.domo.com",
      "subscriberJobId": "b8ff1dc6-4426-4256-8176-1cb9482e79c0",
      "policies": {
        "AccessTokens": "85f65936-e0c3-4e74-8398-13096df9bdb3",
        "DomainWhitelist": "cd473383-9589-4d44-a85a-ffd58c0b1d55",
        "IPWhitelist": "6f570767-ec10-4d9b-b0f2-abb0bf1bd8d2",
        "OIDC": "d26a1d1e-a6c0-4367-b929-70a6e01e5b46",
        "SAML": "081d8320-c6df-4d0b-8802-97875989236d",
        "DirectSignOn": "7b1f43e1-165d-4eed-b195-491a6bedcef0"
      },
      "metricsDatasetId": "2644b5d0-344b-4bc0-b379-d3854923a29c"
    },
    "executionResponse": {},
    "accounts": [479],
    "resources": {
      "requests": {
        "memory": "256M"
      },
      "limits": {
        "memory": "256M"
      }
    },
    "triggers": []
  }
}
```

### Response:

```json
{
  "status": "OK",
  "code": 200,
  "message": "Job updated successfully"
}
```
