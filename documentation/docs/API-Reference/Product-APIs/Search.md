# Search Product API

This API reference is useful if you are trying to use the search API to find entities.

## Query

**_Known Limits_**

- The maximum number of records that can be returned is 10,000.
- Rate limited. It is recommended to not exceed 120 requests per minute, but this can vary depending on instance

**Method:** `POST`  
**Endpoint:** `https://{instance}.domo.com/api/search/v1/query`

### Body Parameters

| Property Name        | Type                       | Required                   | Description                                                                                                                              |
| -------------------- | -------------------------- | -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| count                | Number                     | no. default is 10          | How many results to return                                                                                                               |
| offset               | Number                     | no. default is 0           | The results offset. The count and offset can only be used to return a total of 10,000 records                                            |
| query                | String                     | yes                        | The query term. Use \* for wildcard                                                                                                      |
| filters              | Array of [Filter](#filter) | no                         | Search results must match ALL filters.                                                                                                   |
| orFilters            | Array of [Filter](#filter) | no                         | Search results must match ANY filter.                                                                                                    |
| notFilters           | Array of [Filter](#filter) | no                         | Search results must NOT match any filter.                                                                                                |
| sort                 | [Sort](#sort)              | no. defaults to relevance  | How to sort the results. relevance sorting will show the most relevant content for a user first.                                         |
| facetValuesToInclude | Array of Strings           | no                         | Facets (or groupings) to include in the search results.                                                                                  |
| facetValueLimit      | Number                     | no. default is 0           | How many of the facet values to return                                                                                                   |
| facetValueOffset     | Number                     | no. default is 0           | The facet value offset                                                                                                                   |
| includePhonetic      | Boolean                    | no                         | Whether to use phonetic matching                                                                                                         |
| entityList           | Array of Arrays of Strings | yes                        | Which entities to perform the query on. Entities can be grouped together. i.e. `[["account"],["alert"],["app"],["data_app","app_card"]]` |
| fieldsToReturn       | Array of Strings           | no. defaults to all fields | Define which fields to return                                                                                                            |

> #### Some Valid Entities
>
> - account
> - alert
> - app
> - beast_mode
> - card
> - connector
> - data_app
> - dataset
> - dataflow
> - group
> - page
> - user
>
> Others may be available depending on your instance.

### Example Request:

```json
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/search/v1/query",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": {
    "count": 20,
    "offset": 0,
    "query": "<insert query>",
    "filters": [],
    "sort": {},
    "facetValuesToInclude": [],
    "facetValueLimit": 0,
    "facetValueOffset": 0,
    "includePhonetic": true,
    "entityList": [["dataflow"]]
  }
}
```

### Response

| Property Name    | Description                                         |
| ---------------- | --------------------------------------------------- |
| facetMap         | The facet groupings requested                       |
| totalResultCount | The total count of results that match the query     |
| sort             | The sort used in the query                          |
| queryUuid        | A unique generated id                               |
| searchObjects    | A list of all search results                        |
| searchResultsMap | Search results grouped as defined by the entityList |

```json
{
  "facetMap": {
    "OWNER_ID": {
      "fieldName": "owned_by_id",
      "searchFacetEnum": "OWNER_ID",
      "facetValues": []
    }
  },
  "totalResultCount": 1865,
  "sort": {
    "fieldSorts": null,
    "activity": null,
    "activitySortType": null,
    "metricAction": null,
    "isHotness": false,
    "isRelevance": true
  },
  "queryUuid": "d775bcda-f3f6-4c62-b0b1-d3c57a609637",
  "hideSearchObjects": false,
  "searchObjects": [],
  "searchResultsMap": {
    "dataflow": []
  }
}
```

## Filter

Filters are used to narrow down the search results. Use the property `filterType` to specify the type of filter.

Example

```json
{
  "filterType": "term",
  "field": "databaseId",
  "value": "abcd-xyz"
}
```

### Text filters

#### term

| Property Name | Type             | Required             | Description                                     |
| ------------- | ---------------- | -------------------- | ----------------------------------------------- |
| field         | String           | yes                  | The field to query                              |
| value         | String           | yes (or values)      | The term to match                               |
| values        | Array of Strings | yes (or value)       | The terms to match. Cannot be used with `value` |
| not           | Boolean          | no. default is false | Whether to invert the match                     |

#### wildcard

| Property Name | Type   | Required | Description                              |
| ------------- | ------ | -------- | ---------------------------------------- |
| field         | String | yes      | The field to query                       |
| query         | String | yes      | The query to match. Use `*` for wildcard |

#### queryString

| Property Name | Type   | Required | Description               |
| ------------- | ------ | -------- | ------------------------- |
| field         | String | yes      | The field to query        |
| queryString   | String | yes      | The query string to match |

### Date Filters

#### dateBucket

| Property Name | Type   | Required | Description                                                                             |
| ------------- | ------ | -------- | --------------------------------------------------------------------------------------- |
| field         | String | yes      | The field to query                                                                      |
| value         | String | yes      | The date bucket to use. Valid buckets are LAST_DAY, LAST_WEEK, LAST_MONTH, LAST_QUARTER |

#### dateRange

| Property Name | Type      | Required             | Description                 |
| ------------- | --------- | -------------------- | --------------------------- |
| field         | String    | yes                  | The field to query          |
| from          | Timestamp | no                   | The lower bound date        |
| to            | Timestamp | no                   | The upper bound date        |
| not           | Boolean   | no. default is false | Whether to invert the match |

### Numeric Filters

#### numeric

| Property Name | Type    | Required             | Description                        |
| ------------- | ------- | -------------------- | ---------------------------------- |
| field         | String  | yes                  | The field to query                 |
| longNumber    | Long    | yes (or floatNumber) | The long value to match            |
| floatNumber   | Float   | yes (or longNumber)  | The float value to match           |
| operator      | String  | yes                  | The operator: LT, LTE, EQ, GT, GTE |
| not           | Boolean | no. default is false | Whether to invert the match        |

#### range

| Property Name | Type   | Required | Description              |
| ------------- | ------ | -------- | ------------------------ |
| field         | String | yes      | The field to query       |
| from          | Number | no       | The lower bound to match |
| to            | Number | no       | The upper bound to match |

### Boolean Filters

#### boolean

| Property Name | Type    | Required | Description        |
| ------------- | ------- | -------- | ------------------ |
| field         | String  | yes      | The field to query |
| value         | Boolean | yes      | The value to match |

#### missing

| Property Name | Type    | Required             | Description                     |
| ------------- | ------- | -------------------- | ------------------------------- |
| field         | String  | yes                  | The field to match if it exists |
| not           | Boolean | no. default is false | Whether to invert the match     |

## Sort

Use the sort to order search results.
Example:

```json
{
  "fieldSorts": [
    {
      "field": "createDate",
      "sortOrder": "DESC"
    }
  ],
  "isRelevance": false
}
```

| Property Name | Type               | Required | Description                           |
| ------------- | ------------------ | -------- | ------------------------------------- |
| fieldSorts    | Array of FieldSort | no       | The fields to order by                |
| isRelevance   | Boolean            | no       | Whether to order by relevance to user |
