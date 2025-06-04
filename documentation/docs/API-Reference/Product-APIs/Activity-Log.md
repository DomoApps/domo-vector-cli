# Activity Log API

The Activity Log API allows users to retrieve audit logs and enumerate object types within their Domo instance. The following endpoints are available.


## Get Activity Log

**Method**: GET  
**Endpoint**: `/api/audit/v1/user-audits`

**Description**: Retrieves a list of user activity logs based on the provided query parameters.

**Query Parameters**:

| Property Name | Type   | Required          | Description                                                                                   |
| ------------- | ------ | ----------------- | --------------------------------------------------------------------------------------------- |
| `start`       | Number | yes               | The start timestamp for the query (in milliseconds).                                          |
| `end`         | Number | yes               | The end timestamp for the query (in milliseconds).                                            |
| `offset`      | Number | no. default is 0  | The results offset.                                                                           |
| `limit`       | Number | no. default is 300| The maximum number of results to return.                                                     |
| `objectType`  | String | no                | A comma-separated list of object types to filter by. Valid values: `ACCOUNT`, `DATAFLOW_TYPE`, `DATA_SOURCE`. |

**Example**:

```json
{
  "method": "GET",
  "url": "https://{domo_instance}.domo.com/api/audit/v1/user-audits?start=1646434158639&end=1654206558639&offset=0&limit=300&objectType=DATAFLOW_TYPE,ACCOUNT",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  }
}
```

**Response**:  
Returns an array of activity log entries.

```json
[
  {
    "userName": "Jae Wilson",
    "userId": "1893952720",
    "userType": "USER",
    "actionType": "VIEWED",
    "objectType": "ACTIVITY_LOG",
    "additionalComment": "Jae Wilson viewed the activity log.",
    "time": 1654205894927,
    "eventText": "Viewed activity log"
  },
  {
    "userName": "Bryan Van Kampen",
    "userId": "587894148",
    "userType": "USER",
    "actionType": "VIEWED",
    "objectType": "PAGE",
    "additionalComment": "Bryan Van Kampen viewed page 'How Should we manage this monster?'.",
    "time": 1654189333186,
    "eventText": "Viewed page"
  }
]
```


## Get (Enumerate) Activity Log Object Types

**Method**: GET  
**Endpoint**: `/api/audit/v1/user-audits/objectTypes`

**Description**: Retrieves a list of available object types that can be queried in the Activity Log API.

**Example**:

```json
{
  "method": "GET",
  "url": "https://{domo_instance}.domo.com/api/audit/v1/user-audits/objectTypes",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  }
}
```

**Response**:  
Returns an array of object types.

```json
[
  "ACCOUNT",
  "DATAFLOW_TYPE",
  "DATA_SOURCE"
]
```