---
stoplight-id: 4w40o03817vij
---

# Hitting a Code Engine Function from an App

Code Engine is a Domo-native runtime environment that can execute JavaScript or Python code. In Code Engine, you can write, test, and distribute functions usable by Workflows and other Apps by Domo.

You may want to leverage Code Engine in your App if you'd like to:
- Hit Domo APIs outside of the App Framework.
- Hit APIs external to Domo.
- Run Python or JavaScript code securely server-side.


Domo provides a library of general packages and their related functions for common integrations and services that anyone can use. You can also create your own functions with custom code to perform automated services in your instance.

You can learn more about [setting up Code Engine functions in Domo's Knowledge Base](https://domo-support.domo.com/s/article/000005173?language=en_US).

In order to be able to hit a Code Engine function from an app, you need to add a `packageMapping` definition to your app’s [manifest file](manifest.md) and then wire up a code engine function to the app in the wiring screen. To be able to test your code engine function locally, please also make sure that you have [configured your app with a `proxyId`](manifest.md#getting-a-proxyid-advanced).

### Manifest
---
Add a `packageMapping` property to the manifest.json file that defines the workflow(s) using the following format:

```json

"packageMapping": [
    {
      "alias": "awesomeFunction",
      "parameters": [
        {
          "alias": "number1AppInput",
          "type": "number",
          "nullable": false,
          "isList": false,
          "children": null
        },
        {
          "alias": "number2AppInput",
          "type": "number",
          "nullable": false,
          "isList": false,
          "children": null
        }
      ],
      "output": {
        "alias": "sumAppOutput",
        "type": "number",
        "children": null
      }
    }
  ]

```

The `packageMapping` property takes an array of package mappings. A package mapping is an array of objects with the following properties:

- An `alias` (string) - the alias you'd like to use when you reference the Code Engine function in your code.
- A list of input `parameters` required to start the Code Engine function. These parameters include the following properties:
  - `alias`(string) - the alias of the parameter you are passing in to the function
  - `type` (string) - type of the parameter you are passing into the function. The valid options are:
    - `boolean`
    - `date`
    - `dateTime`
    - `decimal`
    - `duration`
    - `number`
    - `object`
    - `person`
    - `dataset`
    - `group`
    - `text`
    - `time`
  - `nullable` (boolean) - whether the input parameter accepts `null` input.
  - `isList` (boolean) - whether the input parameter is a list or not.
  - `children` (package mapping object) - if the parameter is a defined `object`, you can define the nested properties here.


### Calling a Code Engine Function: Code Example
---
```js
const startFunction = (functionAlias, inputParameters = {}) => {
    domo.post(`/domo/codeengine/v2/packages/${functionAlias}`, inputParameters
    ).then(data => {
        console.log(data);
    }).catch(err => {
        console.log(err);
    })
};

startFunction("awesomeFunction", {"number1AppInput": 4, "number2AppInput": 1} );

```

The `alias` parameter in the `startFunction` function is the alias that you defined in your manifest. 

The `body` parameter is an object where the keys match the `alias` keys defined in the `parameters` property of the package mapping definition in your manifest. 


### Wiring Screen
---
After publishing your app, you will need to wire it to the Code Engine function you want to hit by editing an existing app card, or creating a new one.

![Screenshot 2024-02-13 at 2.30.40 PM.png](<../../../../assets/images/Screenshot 2024-02-13 at 2.30.40 PM.png>)

First, choose which function you want to wire up. The function wiring options that appear in the wiring screen will be the package mappings defined in your `packageMapping` array in your manifest

![Screenshot 2024-02-13 at 2.31.16 PM.png](<../../../../assets/images/Screenshot 2024-02-13 at 2.31.16 PM.png>)


Next, click "Select Package". This will open a modal to choose your package.

![Screenshot 2024-02-13 at 2.32.29 PM.png](<../../../../assets/images/Screenshot 2024-02-13 at 2.32.29 PM.png>)


Finally, choose your package, version, function, and map input parameters.

![Screenshot 2024-02-13 at 2.34.02 PM.png](<../../../../assets/images/Screenshot 2024-02-13 at 2.34.02 PM.png>)


Once you're done, click "Save and Finish" and you should now be able to hit a Code Engine function from your app.
