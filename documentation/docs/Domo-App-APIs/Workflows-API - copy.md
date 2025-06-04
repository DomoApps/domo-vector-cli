---
internal: true
---

### Get Workflow Instance

If you are checking on the status of an existing Workflow instance.

#### Code Example

```js
const getWorkflowInstance = async (workflowAlias, workflowInstanceId) => {
    const instance = await domo.get(`/domo/workflow/v1/models/${workflowAlias}/instance/${workflowInstanceId}`)
    return instance;
  }
```

#### Arguments

| Property Name      | Type   | Required | Description                                    |
| ------------------ | ------ | -------- | ---------------------------------------------- |
| workflowAlias      | String | Required | The name given to the Workflow in the manifest |
| workflowInstanceId | String | Required | The UUID of the Workflow instance              |

#### HTTP Request

```text
GET /domo/workflow/v1/models/{workflowAlias}/instance/{workflowInstanceId}
```

#### HTTP Response

Returns the information about the instance of the Workflow requested. The `status` property can take the values `null`, `IN_PROGRESS`, `CANCELED`,  or `COMPLETED`.

A status of `null` might be valid. It just means the workflow hasn’t reported back as started yet.

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8

{
    "id": "2052e10a-d142-4391-a731-2be1ab1c0188", // id of the workflow
    "modelId": "a8afdc89-9491-4ee4-b7c3-b9e9b86c0138", // id of the workflow instance
    "modelName": "AddTwoNumbers", // name of the workflow
    "modelVersion": "1.1.0", // workflow version number
    "createdBy": "8811501", // user id of workflow creator
    "createdOn": "2023-11-15T15:28:57.479Z",
    "updatedBy": "8811501",
    "updatedOn": "2023-11-15T15:28:57.479Z",
    "status": "COMPLETED"
}
```
