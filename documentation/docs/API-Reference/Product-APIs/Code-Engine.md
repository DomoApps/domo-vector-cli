---
stoplight-id: fbhbpt1mt4gog
---

# Code Engine API

This API reference is useful if you are wanting to use your Code Engine functions **outside** of your Domo instance. 

<!-- theme: info -->
> #### Calling From _Inside_ Domo
>
> To call the Code Engine API from _inside_ your Domo instance, you can use
>
> - [a Pro-code app](/docs/Apps/App-Framework/Guides/hitting-code-engine-from-an-app.md)
> - [a Workflow](https://domo-support.domo.com/s/article/000005331?language=en_US#create_workflow_from_template)
>     - You can call that Workflow using [a button in an App Studio app](https://domo-support.domo.com/minasan/s/article/000005295?language=en_US#add_a_button).

Each function in Code Engine is a serverless function that can be run on demand. You can pass in input variables and get back a result. You can also choose to get logs from the function execution.

If you are unfamiliar, you'll need to familiarize yourself with [how to authenticate against Product APIs](/docs/Getting-Started/api-authentication.md#product-apis).

## Run Function

**Method**: `POST`  
**Endpoint**: `/api/codeengine/v2/packages/{{packageId}}/versions/{{version}}/functions/{{functionName}}`

**Example**:

```json
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/codeengine/v2/packages/756f0b19-5125-44f6-b541-058980ff6a94/versions/1.0.1/functions/getExecutionDetails",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": {
    "inputVariables": {
        "paramName": any // these should match your function input parameters
    },
    "settings": { "getLogs": boolean }
  }
}
```

**Response**:

```json
  HTTP/1.1 200 OK
  Content-Type: application/json;charset=UTF-8
{
    "executionId": string,
    "packageId": string,
    "version": string,
    "functionName": string,
    "status": string,
    "settings": {
        "getLogs": boolean
    },
    "startedOn": Date,
    "startedBy": string,
    "completedOn": Date,
    "result": any,
    "stdout": {
        "log": any[]
    },
    "stderr": {
        "log": any[]
    },
    "errorInformation": {
        "result": any,
        "expectedType": string,
        "actualType": string,
        "expectedIsList": boolean,
        "actualIsList": boolean,
        "expectedAllowNull": boolean,
        "errorMessages": string[]
    }
}
```
