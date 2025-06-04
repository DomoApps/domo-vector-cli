---
stoplight-id: 1ay1akbc787jg
---

# Workflows API

Domo Workflows allows you to graphically model a business process into an executable workflow using Business Process Management (BPM) notations and flows. Orchestration capabilities offer robust solutions for integrating internal and external systems, configuring decision logic, and automating activities in a workflow.


For more background on Workflows, check out the [Knowledge Base for an overview](https://domo-support.domo.com/s/article/000005108?language=en_US). 

If you haven't leveraged Workflows from within Apps before, checkout [the guide on hitting a Workflow from an App](../Apps/App-Framework/Guides/hitting-a-workflow.md), which details how to configure your `manifest.json` file and wire up Workflows to your app.


### Start a Workflow
---
Starts a Workflow and returns details about the Workflow Instance.


#### Code Example

```js
const startWorkflow = async (workflowAlias, body) => {
    const instance = await domo.post(`/domo/workflow/v1/models/${workflowAlias}/start`, body)
    return instance;
  }
  ```

#### Arguments
| Property Name| Type | Required | Description |
| --- | --- | --- | --- |
|workflowAlias	|String	|Required	|The name given to the Workflow in the manifest|

#### HTTP Request
```text
POST /domo/workflow/v1/models/{workflowAlias}/start
```

#### Request Body

The request body accepts an object containing the start parameters required to run the workflow. These parameters are also defined in the `manifest.json` file and properties in the object should correspond to the `aliasName` of the parameter.

```json
{"parameter1": parameter1, "parameter2": parameter2}
```

#### HTTP Response

Returns the information about the instance of the Workflow that was just started. The `status` property can take the values `null`, `IN_PROGRESS`, `CANCELED`,  or `COMPLETED`. 

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
    "status": "null"
}
```

### Get Metrics for a Workflow
---
Returns key metric information about a Workflow.


#### Code Example

```js
const getWorkflowMetrics = async (workflowAliasedName) => {
    const metrics = await domo.get(`/domo/workflow/v1/models/${workflowAliasedName}/overall`);
    return metrics;
  }
  ```

#### Arguments (query parameters)
| Property Name| Type | Required | Description |
| --- | --- | --- | --- |
|limit	|Long	|Optional	|limit of instance metrics returns|
|offset	|Long	|Optional	|offset for pagination|
|after	|Long	|Optional	|after a certain time|
|until	|Long	|Optional	|before a certain time|
|status	|String	|Optional	|Only show instances that have the provided status(es) `IN_PROGRESS`, `CANCELED`, `COMPLETED`|

#### HTTP Request
```text
GET /domo/workflow/v1/models/{workflowAliasedName}/overall
```



#### HTTP Response

Returns the information about the instance of the Workflow that was just started. The `status` property can take the values `null`, `IN_PROGRESS`, `CANCELED`,  or `COMPLETED`. 

A status of `null` might be valid. It just means the workflow hasn’t reported back as started yet.


```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8

{
    "modelId": "a8afdc89-9491-4ee4-b7c3-b9e9b86c0138",
    "version": "1.1.0",
    "completedWorkflows": 0,
    "inProgressWorkflows": 4,
    "failedWorkflows": 1,
    "canceledWorkflows": 0,
    "averageCycleTime": 0,
    "instanceMetric": [
        {
            "instanceId": "2052e10a-d142-4391-a731-2be1ab1c0188",
            "modelId": "a8afdc89-9491-4ee4-b7c3-b9e9b86c0138",
            "version": "1.1.0",
            "creatorId": "8811501",
            "workflowStartTime": "2023-11-15T15:28:57.522Z",
            "workflowEndTime": null,
            "workflowCancelTime": null,
            "workflowCycleTime": 0,
            "status": "IN_PROGRESS"
        },
        {
            "instanceId": "e5cb6377-36b5-4277-a2dd-2bac9a6a2d5d",
            "modelId": "a8afdc89-9491-4ee4-b7c3-b9e9b86c0138",
            "version": "1.1.0",
            "creatorId": "8811501",
            "workflowStartTime": "2023-12-11T16:20:18.900Z",
            "workflowEndTime": null,
            "workflowCancelTime": null,
            "workflowCycleTime": 0,
            "status": "IN_PROGRESS"
        },
        {
            "instanceId": "0dee93c0-0bdf-442c-83f6-dc294aa577e1",
            "modelId": "a8afdc89-9491-4ee4-b7c3-b9e9b86c0138",
            "version": "1.1.0",
            "creatorId": "8811501",
            "workflowStartTime": "2023-12-11T16:19:49.956Z",
            "workflowEndTime": null,
            "workflowCancelTime": null,
            "workflowCycleTime": 0,
            "status": "IN_PROGRESS"
        },
        {
            "instanceId": "10d6138b-c814-406d-9ea0-99646d0bf467",
            "modelId": "a8afdc89-9491-4ee4-b7c3-b9e9b86c0138",
            "version": "1.1.0",
            "creatorId": "8811501",
            "workflowStartTime": "2023-12-11T16:20:33.930Z",
            "workflowEndTime": null,
            "workflowCancelTime": null,
            "workflowCycleTime": 0,
            "status": "IN_PROGRESS"
        },
        {
            "instanceId": "0acfc3c9-c3e8-420d-81a5-6d27f17c0bdf",
            "modelId": "a8afdc89-9491-4ee4-b7c3-b9e9b86c0138",
            "version": "1.1.0",
            "creatorId": "8811501",
            "workflowStartTime": "2023-11-15T15:28:59.950Z",
            "workflowEndTime": null,
            "workflowCancelTime": null,
            "workflowCycleTime": 0,
            "status": "FAILED"
        }
    ]
}
```
