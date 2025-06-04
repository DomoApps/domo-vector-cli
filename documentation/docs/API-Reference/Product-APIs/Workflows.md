---
stoplight-id: kspv2orr3oi30
---

# Workflows Product API

This API reference is useful if you are trying to hit workflows from:

1. An external Domo Instance
2. An environment from outside of Domo
3. A script running in Domo's Jupyter Workspaces

If you are looking to hit a workflow from a Domo App, see the [App Framework API Reference for Workflows](../Domo-App-APIs/Workflows-API.md) and the [guide on how to hit a workflow from a Domo App](https://developer.domo.com/portal/81056f6209bfc-start-a-workflow-from-an-app).

If you are unfamiliar with how to authenticate against Product APIs, [please see this overview page](../Getting-Started/api-authentication.md).

For more background on Workflows, check out the [Knowledge Base for an overview](https://domo-support.domo.com/s/article/000005108?language=en_US).

### Start a Workflow

---

Starts a Workflow and returns details about the Workflow Instance.

**Method:** `POST`  
**Endpoint:** `https://{instance}.domo.com/api/workflow/v1/instances/message`

#### Request Body

| Property Name | Type   | Required | Description                                                                     |
| ------------- | ------ | -------- | ------------------------------------------------------------------------------- |
| messageName   | String | Required | Message passed to start the Workflow Instance, usually `"Start {workflow_name}` |
| version       | String | Required | The version identifier e.g. `0.0.1`                                             |
| modelId       | String | Required | The id of the Workflow                                                          |
| data          | Object | Required | The start parameters required to kick off the Workflow.                         |

> #### Input Parameters
>
> For the `data` object containing the start parameters required to run the workflow, be careful to structure this object so it is consistent with the input types that you've already defined in your workflow.
>
> The valid input type options are:
>
> - `boolean`
> - `date`
> - `dateTime`
> - `decimal`
> - `duration`
> - `number`
> - `object`
> - `person`
> - `dataset`
> - `group`
> - `text`
> - `time`
>
> You may pass in lists containing the above types and may also nest additional information in `object` type inputs.

A simple example of a workflow that takes two numerical inputs, might look like the following:

```json
{ "parameter1": 13, "parameter2": 7 }
```

#### Example

```json
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/workflow/v1/instances/message",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": {
    "messageName": "Start {{workflow_name}}",
    "version": "{{workflow_version}}",
    "modelId": "{{workflow_id}}",
    "data": {}
  }
}
```

#### HTTP Response

Returns the information about the instance of the Workflow that was just started. The `status` property can take the values `null`, `IN_PROGRESS`, `CANCELED`, or `COMPLETED`.

A status of `null` might be valid. It just means the workflow hasn’t reported back as started yet.

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8

{
    "id": "2052e10a-d142-4391-a731-2be1ab1c0188", // id of the newly created workflow instance
    "modelId": "a8afdc89-9491-4ee4-b7c3-b9e9b86c0138", // id of the workflow
    "modelName": "AddTwoNumbers", // name of the workflow
    "modelVersion": "1.1.0", // workflow version number
    "createdBy": "8811501", // user id of workflow creator
    "createdOn": "2023-11-15T15:28:57.479Z",
    "updatedBy": "8811501",
    "updatedOn": "2023-11-15T15:28:57.479Z",
    "status": "null"
}
```

### Canceling a Workflow

---

Cancels an in progress Workflow. If you are unfamiliar with how to authenticate against Product APIs, [please see this overview page](../Getting-Started/api-authentication.md).

**Method**: `POST`  
**Endpoint**: `/api/workflow/v1/instances/${instanceId}/cancel`  
**Path Parameters**:

- `id` - The ID of the Workflow instance to cancel
  - String
  - Required

**Example**

```json
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/workflow/v1/instances/${instanceId}/cancel",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  }
}
```

**Response**:

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
{
  "id": string,
  "modelId": string,
  "deploymentId": string,
  "modelName": string,
  "modelVersion": string,
  "bpmnProcessId": string,
  "bpmnProcessName": string,
  "createdBy": string,
  "createdOn": string,
  "updatedBy": string,
  "updatedOn": string,
  "status": string,
  "isTestRun": boolean
}
```

### Changing a Workflow's Permissions

---

Changes the permissions of a workflow.

**Method:** `POST`  
**Endpoint:** `https://{instance}.domo.com/api/workflow/v1/models/${modelId}/permissions`

#### Request Body

| Property Name | Type   | Required | Description                   |
| ------------- | ------ | -------- | ----------------------------- |
| modelId       | String | Required | The id of the workflow model. |

#### Example

```json
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/workflow/v1/models/${modelId}/permissions",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": {
    [
        {
            "id": "123456",
            "permissions": [
                "ADMIN",
                "SHARE",
                "DELETE",
                "WRITE",
                "READ",
                "EXPORT",
                "EXECUTE",
                "UPDATE_CONTENT"
            ],
            "name": "John Doe",
            "type": "USER"
        },
        {
            "id": "98765",
            "name": "John Smith",
            "type": "USER",
            "permissions": [
                "READ"
            ]
        }
    ]
  }
}
```

#### HTTP Response

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
```
