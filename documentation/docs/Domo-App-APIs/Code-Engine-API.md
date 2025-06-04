---
stoplight-id: p48phjy7wwtw8
---

# Code Engine API

Code Engine is a Domo-native runtime environment that can execute JavaScript or Python code. In Code Engine, you can write, test, and distribute functions usable by Workflows and other Apps by Domo.

Domo provides a library of global packages and their related functions for common integrations and services that anyone can use in their Domo instance. You can also create your own functions with custom code to perform automated services in your instance.

You can learn more about [setting up Code Engine functions in Domo's Knowledge Base](https://domo-support.domo.com/s/article/000005173?language=en_US).

If you haven't leveraged Code Engine functions from within Apps before, checkout [the guide on hitting Code Engine from an App](../Apps/App-Framework/Guides/hitting-code-engine-from-an-app.md), which details how to configure your `manifest.json` file and wire up Code Engine packages to your app.


### Run Code Engine Function
---
Runs a Code Engine function and returns output of that function.


#### Code Example

```js
const startFunction = (functionAlias, inputParameters = {}) => {
    domo.post(`/domo/codeengine/v2/packages/${functionAlias}`, inputParameters
    ).then(data => {
        console.log(data);
    }).catch(err => {
        console.log(err);
    })
};
  ```

#### Arguments
| Property Name| Type | Required | Description |
| --- | --- | --- | --- |
|functionAlias	|String	|Required	|The name given to the Code Engine package in the manifest|

#### HTTP Request
```text
POST /domo/codeengine/v2/packages/{functionAlias}
```

#### Request Body

The request body accepts an object containing the input parameters required to run the code engine function. These parameters are also defined in the `manifest.json` file and properties in the object should correspond to the `alias` of the parameter.

```json
{"parameter1": parameter1, "parameter2": parameter2}
```

#### HTTP Response

Returns the result of the Code Engine function. This result is defined in the [Code Engine function and function configuration](https://domo-support.domo.com/s/article/000005173?language=en_US#function_configuration) "Output" tab. This output should also be defined in the `output` property of the `packageMapping` object in the manifest file.
