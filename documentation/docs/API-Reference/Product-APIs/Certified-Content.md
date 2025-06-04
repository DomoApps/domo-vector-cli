# Certified Content

## Get Certification Status

Get the certification status of your card or dataset. The entityType can either be `CARD` or `DATA_SOURCE` (Dataset).

#### Query Parameters

| Property Name | Type   | Required | Description                                                            |
| ------------- | ------ | -------- | ---------------------------------------------------------------------- |
| entityId      | String | Required | Id of the card or dataset you are requesting certification status for. |
| entityType    | String | Required | The entityType can either be `CARD` or `DATA_SOURCE` (Dataset).        |

#### HTTP Request

```text
GET https://{instance}.domo.com/api/tags/v3/{entityType}/{entityId}/system/CERTIFIED/state

HTTP/1.1
Accept: application/json
```

#### HTTP Response

Returns status of 200 if successful.

```json
HTTP/1.1 200 SUCCESS

{
    "tag": "CERTIFIED",
    "state": null,
    "metadata": null,
    "updated": null
}
```

## Certify Content

Certify a Card or a Dataset.

#### Query Parameters

| Property Name | Type   | Required | Description                                                            |
| ------------- | ------ | -------- | ---------------------------------------------------------------------- |
| entityId      | String | Required | Id of the card or dataset you are requesting certification status for. |
| entityType    | String | Required | The entityType can either be `CARD` or `DATA_SOURCE` (Dataset).        |

#### HTTP Request

```text
PUT https://{instance}.domo.com/api/tags/v3/{entityType}/{entityId}/system/CERTIFIED/state/ACTIVE

HTTP/1.1
Accept: application/json
```

#### HTTP Response

Returns status of 200 if successful.

```json
HTTP/1.1 200 SUCCESS
```

## Delete a Certification

Removes certification on a Card or Dataset.

#### Query Parameters

| Property Name | Type   | Required | Description                                                            |
| ------------- | ------ | -------- | ---------------------------------------------------------------------- |
| entityId      | String | Required | Id of the card or dataset you are requesting certification status for. |
| entityType    | String | Required | The entityType can either be `CARD` or `DATA_SOURCE` (Dataset).        |

#### HTTP Request

```text
DELETE https://{instance}.domo.com/api/tags/v3/{entityType}/{entityId}/system/CERTIFIED/state

HTTP/1.1
Accept: application/json
```

#### HTTP Response

Returns status of 204 if successful.

```json
HTTP/1.1 204 No Content
```
