# Guide to Using the Global Code Engine Package `Start Workflow in Remote Instance`

### Function Overview

The `startWorkflowInRemoteInstance` function initiates a workflow in a remote Domo instance by sending a request via Domo's Workflow API.

There is also a `startWorkflowInRemoteInstanceWithJSONString` function, which you can pass in text data as a JSON string to start the workflow. This allows you to use String Builder in a Workflow to dynamically generate a JSON string to start the remote Workflow.

### Parameters

- **`domoAccessToken`**: Your "Domo Access Token" account, added in the Data Center. The token is generated in the admin section of your Domo instance.
- **`domain`**: A string representing the Domo domain (e.g., `"example.domo.com"`, or just `"example"`).
- **`workflowId`**: The UUID (string) Workflow model ID you wish to start.
- **`workflowVersion`**: The version (string) of your Workflow.
- **`startObject`**: An object containing data that will be passed to the workflow start. The object should match the workflow start inputs. For example, if you have a workflow that takes in a `userId` of type Text, a `role` of type Number, and a `name` of type Text, your `startObject` should look like this:

```json
{
  "userId": "123",
  "role": 1,
  "name": "John Doe"
}
```

### How It Works

1. **Domain Clean-Up**: Removes the `.domo.com` part, if passed in, from the domain to create the base API URL.
2. **Generate URLs**:
   - `getStartUrl`: Constructs the URL to retrieve the workflow’s start details.
   - `startWorkflowUrl`: Constructs the URL to post the workflow start request.
3. **Access Token Retrieval**: Fetches the actual access token (`ACCESS_TOKEN`) using `ce.getAccount`.
4. **Headers Configuration**: Sets up headers for API calls using the `X-DOMO-Developer-Token`.
5. **Workflow Start**: Retrieves the name of the message to start the workflow with a GET request.
6. **Workflow Execution**: Initiates the workflow by posting to the `startWorkflowUrl` with the workflow data in `startBody`.

### Important Notes

- Ensure the `domoAccessToken` provided has sufficient permissions to start workflows.
- Validate that `workflowId` and `workflowVersion` are correct and available in your Domo instance.
- Check to see that your `startObject` matches the workflow start inputs names and types exactly.
- Make sure that if you're using the function `startWorkflowInRemoteInstanceWithJSONString`, the JSON string is correctly formatted.
