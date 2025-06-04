# Data Accounts

This API allows interaction with various Domo data operations, including retrieving, creating, and managing accounts.

## GET Account by ID

**Method**: `GET`  
**Endpoint**: `/api/data/v1/accounts/{account_id}`

**Example**:
```json
{
	"method": "GET",
	"url": "https://{domo_instance}.domo.com/api/data/v1/accounts/{account_id}",
	"headers": {
		"X-DOMO-Developer-Token": "",
		"Content-Type": "application/json"
	},
	"body": {}
}
```

**Parameters**:

| Property Name | Type    | Required | Description                              |
| ------------- | ------- | -------- | ---------------------------------------- |
| account_id    | String  | yes      | The unique identifier for the account.   |

**Response**:  
Description of the Response with an example of the data
```json
  HTTP/1.1 200 OK
  Content-Type: application/json;charset=UTF-8
  {
    "accountId": "{account_id}",
    "displayName": "Account Display Name",
    "status": "Active"
  }
```

## GET all accounts

**Method**: `GET`  
**Endpoint**: `/api/data/v1/accounts/`

**Example**:
```json
{
	"method": "GET",
	"url": "https://{domo_instance}.domo.com/api/data/v1/accounts/",
	"headers": {
		"X-DOMO-Developer-Token": "",
		"Content-Type": "application/json"
	},
	"body": {}
}
```

**Response**:  
Description of the Response with an example of the data
```json
  HTTP/1.1 200 OK
  Content-Type: application/json;charset=UTF-8
  [
    {
      "accountId": "{account_id}",
      "displayName": "Account 1"
    },
    {
      "accountId": "{account_id}",
      "displayName": "Account 2" 
    }
  ]
```

## Search Accounts by Name

**Method**: `POST`  
**Endpoint**: `/api/search/v1/query`

**Example**:
```json
{
	"method": "POST",
	"url": "https://{domo_instance}.domo.com/api/search/v1/query",
	"headers": {
		"X-DOMO-Developer-Token": "",
		"Content-Type": "application/json"
	},
	"body": {
		"count": 100,
		"offset": 0,
		"combineResults": false,
		"query": "*sdk*",
		"filters": [],
		"facetValuesToInclude": [
			"DATAPROVIDERNAME",
			"OWNED_BY_ID",
			"VALID",
			"USED",
			"LAST_MODIFIED_DATE"
		],
		"queryProfile": "GLOBAL",
		"entityList": [
			["account"]
		],
		"sort": {
			"fieldSorts": [
				{
					"field": "display_name_sort",
					"sortOrder": "ASC"
				}
			]
		}
	}
}
```

**Parameters**:

| Property Name        | Type           | Required | Description                                                                                               |
| -------------------- | -------------- | -------- | --------------------------------------------------------------------------------------------------------- |
| count                | Number         | no       | How many results to return, default is 10                                                                  |
| offset               | Number         | no       | The results offset, default is 0                                                                            |
| query                | String         | yes      | The search query string                                                                                   |
| filters              | Array of Filter| no       | Filters to apply to the search.                                                                            |
| facetValuesToInclude | Array of String| no       | Facet values to include in the search results.                                                            |
| queryProfile         | String         | no       | The query profile to use (e.g., `GLOBAL`)                                                                  |
| entityList           | Array of Array | yes      | The entity list to search within (e.g., `["account"]`)                                                     |
| sort                 | Object         | no       | Sort options, including the field and order.   |

**Response**:  
Description of the Response with an example of the data
```json
  HTTP/1.1 200 OK
  Content-Type: application/json;charset=UTF-8
  {
    "results": [
      {
        "accountId": "{account_id}",
        "displayName": "SDK Account",
        "status": "Active"
      }
    ]
  }
```

## Create Account

**Method**: `POST`  
**Endpoint**: `/api/data/v1/accounts`

**Example**:
```json
{
	"method": "POST",
	"url": "https://{domo_instance}.domo.com/api/data/v1/accounts",
	"headers": {
		"X-DOMO-Developer-Token": "",
		"Content-Type": "application/json"
	},
	"body": {
		"displayName": "New Account",
		"accountType": "Standard"
	}
}
```

**Parameters**:

| Property Name | Type   | Required | Description                          |
| ------------- | ------ | -------- | ------------------------------------ |
| displayName   | String | yes      | The name of the new account.         |
| accountType   | String | yes      | The type of account (e.g., "Standard"). |

**Response**:  
Description of the Response with an example of the data
```json
  HTTP/1.1 200 OK
  Content-Type: application/json;charset=UTF-8
  {
    "accountId": "{account_id}",
    "displayName": "New Account",
    "status": "Active"
  }
```
