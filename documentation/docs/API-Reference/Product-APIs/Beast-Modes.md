# Beast Modes

Beast Modes are run time calculations on Cards or Datasets.

## Get Statistics

Fetch instance-wide statistics on Beast Mode usage.

**Method:** `GET`  
**Endpoint:** `/api/query/v1/functions/statistics`

### Example

```json
{
  "method": "GET",
  "url": "https://{instance}.domo.com/api/query/v1/functions/statistics",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  }
}
```

### Response

```json
  HTTP/1.1 200 OK
  Content-Type: application/json;charset=UTF-8
  {
    "total": 525,
    "onDatasets": 406,
    "onCards": 119,
    "inVisualizations": 98,
    "locked": 0,
    "invalid": 0,
    "invalidLink": 68,
    "archived": 0
}
```

## Get All Beast Modes

Gets all Beast Mode objects in the instance.

**Method:** `POST`  
**Endpoint:** `/api/query/v1/functions/search`

### Body Parameters

| Parameter | Type             | Required | Description                                                                   |
| --------- | ---------------- | -------- | ----------------------------------------------------------------------------- |
| `name`    | String           | No       | To search for Beast Modes by name.                                            |
| `filters` | Array of objects | Yes      | Filter criteria for the request.                                              |
| `sort`    | Object           | Yes      | Object that takes the `field` to sort by and `ascending` as `true` or `false` |
| `limit`   | Integer          | Yes      | How many records to limit the request by. Must be between 1 and 5000.         |
| `offset`  | Integer          | No       | Which record to start the response with.                                      |

### Example

```json
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/query/v1/functions/search",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": {
    "name": "",
    "filters": [
      {
        "field": "notvariable"
      }
    ],
    "sort": {
      "field": "name",
      "ascending": true
    },
    "limit": 3,
    "offset": 0
  }
}
```

### Response

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
{
  "totalHits": 525,
  "results": [
    {
      "id": 427,
      "name": "% Behind Schedule Objects",
      "owner": 8811501,
      "lastModified": 1670963682352,
      "created": 1670963682352,
      "global": false,
      "locked": false,
      "legacyId": "calculation_ab07cd22-2558-4f8f-b692-f39f6869a01a",
      "status": "VALID",
      "links": [
        {
          "resource": {
            "type": "CARD",
            "id": "dr:1947052903:616023142"
          },
          "visible": true,
          "active": false,
          "valid": "VALID"
        },
        {
          "resource": {
            "type": "DATA_SOURCE",
            "id": "aa7d9422-9abe-4581-bbf3-4a8cb5d3fc25"
          },
          "visible": false,
          "active": false,
          "valid": "ILLEGAL_REFERENCE"
        }
      ],
      "archived": false,
      "activeLinks": {}
    }
  ],
  "hasMore": true,
  "degraded": false
}
```

## Get Beast Mode by Id

Gets a specified Beast Mode calculation.

**Method:** `GET`  
**Endpoint:** `api/query/v1/functions/template/<beastmodeId>`

### Path Parameters

| Property Name | Type   | Required | Description         |
| ------------- | ------ | -------- | ------------------- |
| beastmodeId   | Number | yes      | ID of the BeastMode |

### Example

```json
{
  "method": "GET",
  "url": "https://{instance}.domo.com/api/query/v1/functions/template/{beastmodeId}",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  }
}
```

### Response

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
{
  "id": 232,
  "name": "% Change - Orders",
  "owner": 27,
  "locked": false,
  "global": false,
  "expression": "(CASE  WHEN (sum((CASE  WHEN ((DateDiff(AddDate(Current_Date(),-1),`Date`) < (28 + (52 * 7))) AND (DateDiff(Current_Date(),`Date`) > (52 * 7))) THEN `Orders` END )) = 0) THEN 0 ELSE ((sum((CASE  WHEN ((DateDiff(AddDate(Current_Date(),-1),`Date`) < 28) AND (DateDiff(Current_Date(),`Date`) > 0)) THEN `Orders` END )) - sum((CASE  WHEN ((DateDiff(AddDate(Current_Date(),-1),`Date`) < (28 + (52 * 7))) AND (DateDiff(Current_Date(),`Date`) > (52 * 7))) THEN `Orders` END ))) / sum((CASE  WHEN ((DateDiff(AddDate(Current_Date(),-1),`Date`) < (28 + (52 * 7))) AND (DateDiff(Current_Date(),`Date`) > (52 * 7))) THEN `Orders` END ))) END )",
  "checkSum": "4041d1731163b41ae86552ebb46f8a2f1d5aecd5",
  "links": [
    {
      "resource": {
        "type": "DATA_SOURCE",
        "id": "32e6af61-c725-487a-8a4a-a46fbfed9fb1"
      },
      "visible": true,
      "active": false,
      "valid": "VALID"
    }
  ],
  "legacyId": "calculation_6ca6ab70-412a-4394-82d7-d6f648758907",
  "lastModified": 1654190830737,
  "created": 1654190830737,
  "aggregated": true,
  "analytic": false,
  "nonAggregatedColumns": [],
  "dataType": "DECIMAL",
  "status": "VALID",
  "cacheWindow": "day",
  "columnPositions": [
    {
      "columnName": "`Date`",
      "columnPosition": 67
    },
    {
      "columnName": "`Date`",
      "columnPosition": 123
    },
    {
      "columnName": "`Orders`",
      "columnPosition": 149
    }
    }
  ],
  "functions": [
    "DOMO_OP_MULTIPLY",
    "ADDDATE",
    "DOMO_OP_ADD",
    "SUM",
    "DOMO_OP_SUBTRACT",
    "DATEDIFF",
    "DOMO_OP_DIVIDE"
  ],
  "functionTemplateDependencies": [],
  "archived": false,
  "hidden": false,
  "variable": false
}
```

## Update a Beast Mode

Update the formula that consitutes the calculation in the Beast Mode.

**Method:** `PUT`  
**Endpoint:** `/api/query/v1/functions/template/<beastmodeId>?strict=false`

### Path Parameters

| Parameter     | Type    | Required | Description                        |
| ------------- | ------- | -------- | ---------------------------------- |
| `beastmodeId` | Integer | Yes      | The ID of the Beast Mode to update |

### Body Parameters

| Parameter    | Type   | Required | Description                |
| ------------ | ------ | -------- | -------------------------- |
| `expression` | String | Yes      | The text formula to update |

### Example

```json
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/query/v1/functions/template/{beastmodeId}?strict=false",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": {
    "expression": "(CASE  WHEN (sum((CASE  WHEN ((DateDiff(AddDate(Current_Date(),-1),`Date`) < (28 + (52 * 7))) AND (DateDiff(Current_Date(),`Date`) > (52 * 7))) THEN `Orders` END )) = 0) THEN 0 ELSE ((sum((CASE  WHEN ((DateDiff(AddDate(Current_Date(),-1),`Date`) < 28) AND (DateDiff(Current_Date(),`Date`) > 0)) THEN `Orders` END )) - sum((CASE  WHEN ((DateDiff(AddDate(Current_Date(),-1),`Date`) < (28 + (52 * 7))) AND (DateDiff(Current_Date(),`Date`) > (52 * 7))) THEN `Orders` END ))) / sum((CASE  WHEN ((DateDiff(AddDate(Current_Date(),-1),`Date`) < (28 + (52 * 7))) AND (DateDiff(Current_Date(),`Date`) > (52 * 7))) THEN `Orders` END ))) END )"
  }
}
```

### Response

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
{
  "id": 232,
  "name": "% Change - Orders",
  "owner": 27,
  "locked": true,
  "global": false,
  "expression": "(CASE  WHEN (sum((CASE  WHEN ((DateDiff(AddDate(Current_Date(),-1),`Date`) < (28 + (52 * 7))) AND (DateDiff(Current_Date(),`Date`) > (52 * 7))) THEN `Orders` END )) = 0) THEN 0 ELSE ((sum((CASE  WHEN ((DateDiff(AddDate(Current_Date(),-1),`Date`) < 28) AND (DateDiff(Current_Date(),`Date`) > 0)) THEN `Orders` END )) - sum((CASE  WHEN ((DateDiff(AddDate(Current_Date(),-1),`Date`) < (28 + (52 * 7))) AND (DateDiff(Current_Date(),`Date`) > (52 * 7))) THEN `Orders` END ))) / sum((CASE  WHEN ((DateDiff(AddDate(Current_Date(),-1),`Date`) < (28 + (52 * 7))) AND (DateDiff(Current_Date(),`Date`) > (52 * 7))) THEN `Orders` END ))) END )",
  "checkSum": "4041d1731163b41ae86552ebb46f8a2f1d5aecd5",
  "links": [
    {
      "resource": {
        "type": "DATA_SOURCE",
        "id": "32e6af61-c725-487a-8a4a-a46fbfed9fb1"
      },
      "visible": true,
      "active": false,
      "valid": "VALID"
    }
  ],
  "legacyId": "calculation_6ca6ab70-412a-4394-82d7-d6f648758907",
  "lastModified": 1734532686486,
  "created": 1654190830737,
  "aggregated": true,
  "analytic": false,
  "nonAggregatedColumns": [],
  "dataType": "DECIMAL",
  "status": "VALID",
  "cacheWindow": "day",
  "columnPositions": [
    {
      "columnName": "`Date`",
      "columnPosition": 67
    },
    {
      "columnName": "`Date`",
      "columnPosition": 123
    },
    {
      "columnName": "`Orders`",
      "columnPosition": 149
    }
  ],
  "functions": [
    "DOMO_OP_MULTIPLY",
    "ADDDATE",
    "DOMO_OP_ADD",
    "SUM",
    "DOMO_OP_SUBTRACT",
    "DATEDIFF",
    "DOMO_OP_DIVIDE"
  ],
  "functionTemplateDependencies": [],
  "archived": false,
  "hidden": false,
  "variable": false
}
```

## Lock Beast Mode

Locks a Beast Mode so it cannot be altered.

**Method:** `PUT`  
**Endpoint:** `/api/query/v1/functions/template/<beastmodeId>`

### Path Parameters

| Parameter     | Type    | Required | Description                      |
| ------------- | ------- | -------- | -------------------------------- |
| `beastmodeId` | Integer | Yes      | The ID of the Beast Mode to lock |

### Body Parameters

| Parameter | Type    | Required | Description                                      |
| --------- | ------- | -------- | ------------------------------------------------ |
| `locked`  | Boolean | Yes      | `true` to lock Beast Mode. `false` to unlock it. |

### Example

```json
{
  "method": "PUT",
  "url": "https://{instance}.domo.com/api/query/v1/functions/template/{beastmodeId}",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": {
    "locked": true
  }
}
```

### Response

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
{
  "id": 232,
  "name": "% Change - Orders",
  "owner": 27,
  "locked": true,
  "global": false,
  "expression": "(CASE  WHEN (sum((CASE  WHEN ((DateDiff(AddDate(Current_Date(),-1),`Date`) < (28 + (52 * 7))) AND (DateDiff(Current_Date(),`Date`) > (52 * 7))) THEN `Orders` END )) = 0) THEN 0 ELSE ((sum((CASE  WHEN ((DateDiff(AddDate(Current_Date(),-1),`Date`) < 28) AND (DateDiff(Current_Date(),`Date`) > 0)) THEN `Orders` END )) - sum((CASE  WHEN ((DateDiff(AddDate(Current_Date(),-1),`Date`) < (28 + (52 * 7))) AND (DateDiff(Current_Date(),`Date`) > (52 * 7))) THEN `Orders` END ))) / sum((CASE  WHEN ((DateDiff(AddDate(Current_Date(),-1),`Date`) < (28 + (52 * 7))) AND (DateDiff(Current_Date(),`Date`) > (52 * 7))) THEN `Orders` END ))) END )",
  "checkSum": "4041d1731163b41ae86552ebb46f8a2f1d5aecd5",
  "links": [
      {
          "resource": {
              "type": "DATA_SOURCE",
              "id": "32e6af61-c725-487a-8a4a-a46fbfed9fb1"
          },
          "visible": true,
          "active": false,
          "valid": "VALID"
      }
  ],
  "legacyId": "calculation_6ca6ab70-412a-4394-82d7-d6f648758907",
  "lastModified": 1734470226460,
  "created": 1654190830737,
  "aggregated": true,
  "analytic": false,
  "dataType": "DECIMAL",
  "status": "VALID",
  "cacheWindow": "day",
  "columnPositions": [
    {
      "columnName": "`Date`",
      "columnPosition": 67
    },
    {
      "columnName": "`Date`",
      "columnPosition": 123
    },
    {
      "columnName": "`Orders`",
      "columnPosition": 149
    }
  ],
  "functions": [
    "DOMO_OP_MULTIPLY",
    "ADDDATE",
    "DOMO_OP_ADD",
    "SUM",
    "DOMO_OP_SUBTRACT",
    "DATEDIFF",
    "DOMO_OP_DIVIDE"
  ],
  "archived": false,
  "hidden": false,
  "variable": false
}
```
