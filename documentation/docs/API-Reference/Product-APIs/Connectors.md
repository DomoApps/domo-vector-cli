# Connectors

## Run a Connector

Running a connector requires knowing the `streamId` of the Dataset associated with the connector. This can be found using the `GET /api/data/v3/datasources/{datasetId}` and looking for the `streamId` property in the response.

#### Query Parameters

| Property Name | Type   | Required | Description                                                         |
| ------------- | ------ | -------- | ------------------------------------------------------------------- |
| streamId      | String | Required | The `streamId` of the Dataset associated with the connector to run. |

#### HTTP Request

```text
POST https://{instance}.domo.com/api/data/v1/streams/{streamId}/executions

HTTP/1.1
Accept: application/json

{
    "runType": "MANUAL"
}

```

#### Request Body

| Property Name | Type   | Required | Description                                                                    |
| ------------- | ------ | -------- | ------------------------------------------------------------------------------ |
| runType       | String | Required | The type of connector run. To run the connector immediately, choose `"MANUAL"` |

#### HTTP Response

Returns status of 201 if successful.

```json
HTTP/1.1 201 CREATED

{
    "streamId": 25775,
    "executionId": 2,
    "toe": "HAK43KQGQ7-GNKF0-SRC9Y",
    "startedAt": 1734458216.000000000,
    "endedAt": null,
    "updateMethod": "REPLACE",
    "index": true,
    "retryCount": 0,
    "retryExecution": null,
    "containerManagerId": "cm-90cb7970-86a2-43b3-a051-bdde4105b2d8",
    "uploadId": null,
    "indexRequestKey": null,
    "currentState": "ACTIVE",
    "runType": "MANUAL",
    "createdAt": null,
    "modifiedAt": null,
    "latestPhase": null,
    "currentPhase": null,
    "removed": false,
    "rowsInserted": 0,
    "bytesInserted": 0,
    "startedBy": "1129696109",
    "cancelledBy": null,
    "dataTag": null,
    "peakMemoryUsedBytes": null,
    "peakMemoryCommittedBytes": null,
    "exportable": false,
    "manualIndex": false,
    "errors": []
}


```
