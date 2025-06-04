---
stoplight-id: 1sirxqzlsb4sk
---

# Introduction to Code Engine

Code Engine is a Domo-native runtime environment that can securely execute server-side JavaScript or Python code. In Code Engine, you can write, test, and distribute serverless lambda functions that can be consumed by Workflows, Domo Apps, and API.


![Picture1.jpg](../../../assets/images/Picture1.jpg)

To learn more about how to access, configure, and manage Code Engine packages, see the [Code Engine article in Domo's Knowledge Base](https://domo-support.domo.com/s/article/000005173?language=en_US#code_engine_repository_list).



## Common Code Engine Use Cases

- **Workflows**: Workflows contain a series of steps – many of which are code engine functions (either global functions that Domo has written and maintains across all instances or custom ones that you write).

- **Apps**: Historically, Domo has limited the number of APIs that you can hit from an App to a small number that have been configured to work with Domo’s App Framework. However, now you can connect apps to any API securely (internal and external) by wiring the App to trigger a Code Engine function. See our guide to [hitting Code Engine functions from a Domo App](../App-Framework/Guides/hitting-code-engine-from-an-app.md).

<!-- theme: info -->
> #### Pro-tip
>
> Domo has a global package to start a DataFlow. Jupyter Notebooks in Domo can be scheduled as DataFlows. This means that you can spin up and run a Jupyter job via Code Engine, which can be useful when you'd like to do heavier data processing.


## Global vs. Custom Packages

Domo provides a library of general packages and their related functions for common integrations and services that anyone with access to Code Engine can use. You can also create functions with custom code to perform automated services in your instance.

### Global packages

![Picture1.png](../../../assets/images/Picture1.png)

Domo maintains a wide range of packages across all Domo instances. These global packages generally fall into two distinct categories:

1. Taking common actions in Domo by leveraging the Product APIs
2. Utility functions for manipulating small amounts of data


### Custom packages

By creating custom packages you can write functions beyond what is covered in the global packages. Common use-cases for custom packages are:
- to hit Domo APIs not covered by a global package
- to hit non-Domo APIs to trigger events in external systems
- to reshape inputs and outputs a across steps in a Workflow

For custom packages, you will also likely leverage a few key Code Engine specific functions.

`codeengine.sendRequest` provides a wrapper around internal Domo APIs and inherits authentication from the user making the request. You can [see an example Javascript request here](https://domo-support.domo.com/s/article/000005173?language=en_US#code_engine_send_request).

`codeengine.getAccount` securely reads in credentials stored in Domo's Account layer, which you can use in requests to external APIs. See a Javascript [example here](https://domo-support.domo.com/s/article/000005173?language=en_US#codeengine.getAccount).

`codeengine.axios` provides access to the [Axios library](https://axios-http.com/docs/intro), which you can use to send requests to external APIs and handle authentication yourself. This can be beneficial when you want to run a function:
- using a service account
- to hit Domo APIs across Domo instances
- to hit external APIs

## Key Limitations

Code Engine unlocks a lot of flexibility to programatically interact with Domo and with external systems; however, it is not the right tool in all scripting scenarios. 

Code Engine's key limitations are:
- **Compute**: Limited to 1 GB Memory and 5 min max runtime, which means they are not meant for heavy data processing.
- **Output**: Functions may only return a single output. More complex response types are typically handled by returning a single `object` type output
- **Dependencies**: There are a limited set of common libraries available in the JavaScript or Python environment.

Code Engine is ideal for simple, lightweight functions while Domo's Jupyter Workspace integration is ideal for more complex, heavier scripting tasks. 


## Troubleshooting

If you're running into errors building or executing Code Engine, it's often worth checking one of the follow most common gotchas:

- Ensure that the user has the appropriate [permissions](https://domo-support.domo.com/s/article/000005173?language=en_US#permissions) and [grants](https://domo-support.domo.com/s/article/000005173?language=en_US#required_grants) enabled.
- Ensure correct typing of both inputs and outputs in the function. This can get trickier if you're using lists or objects. If you are using a native Domo type like `Account`, `Dataset`, `Group`, or `Person` - you can pass the id of the resource as a string to your function.
- If you are sending SQL into your function as a string, please note that it is case sensitive.
- When you're debugging functions in custom packages, you can use the `console.log` or  `console.error` function to understand what is happening when you test your function.


