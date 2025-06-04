# Code Engine JavaScript Libraries Reference

Below is a comprehensive list of JavaScript libraries available for use in Code Engine.

| **Library**         | **Description**                                                                |
| ------------------- | ------------------------------------------------------------------------------ |
| `codeengine`        | Interfaces with the Code Engine system to manage workflows and data processes. |
| `axios`             | A promise-based HTTP client for making external API requests.                  |
| `googleAuthLibrary` | Handles Google authentication and authorization flows.                         |

## Functions in the `codeengine` library

| **Function**                  | **Description**                                                             |
| ----------------------------- | --------------------------------------------------------------------------- |
| `getPersonDetails`            | Retrieves detailed information about a person from your system.             |
| `getAccount`                  | Fetches account-related data, including access tokens and account settings. |
| `getExecutionDetails`         | Provides details about workflow execution.                                  |
| [`sendRequest`](#sendrequest) | Sends HTTP requests for interacting with internal Domo APIs.                |

### sendRequest

This function will send an authenticated API request to any of Domo's product APIs.

#### Parameters

| Property Name | Type   | Required | Description                                                |
| ------------- | ------ | -------- | ---------------------------------------------------------- |
| method        | String | Required | The HTTP method - can be 'GET', 'POST', 'PUT', or 'DELETE' |
| url           | String | Required | The request url                                            |
| body          | Object | Optional | The request body                                           |
| headers       | Object | Optional | The request headers                                        |
| contentType   | Object | Optional | The request contentType ('application/json' by default)    |

#### Code Example

```javascript
const codeengine = require("codeengine");

async function handleRequest(
  method,
  url,
  body = null,
  headers = null,
  contentType = null
) {
  try {
    return await codeengine.sendRequest(
      method,
      url,
      body,
      headers,
      contentType
    );
  } catch (error) {
    console.error(`Error with ${method} request to ${url}:`, error);
    throw error;
  }
}
```
