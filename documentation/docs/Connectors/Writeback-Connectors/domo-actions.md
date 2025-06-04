---
stoplight-id: fc62ced09f56e
---

# Domo Actions (Beta)

A Domo Action is a kind of writeback Connector that updates only a specific item, instead of bulk updating all items. For example, a user could use a Domo Action to change the status of a specific opportunity in Salesforce.

<!-- theme: info -->

> #### Note
> Domo Actions development is currently in beta. To be included in the beta and start building Domo Actions please contact us at [Beta.admin@domo.com](mailto:Beta.admin@domo.com).

<h4><strong>Requirements:</strong></h4>

Your domain needs to have the Domo Actions and Writeback features enabled.

## Overview

### Creating a Domo Action
---
A Domo Action can be created in the Connector IDE at developer.domo.com. Please email [Beta.admin@domo.com](mailto:Beta.admin@domo.com) to have the feature enabled.

To create a Domo Action you will need to:
<ol>
 	<li>Login to the Connector IDE</li>
 	<li>Upload images and configure user authentication</li>
 	<li>Configure the parameters</li>
 	<li>Define how the data is processed</li>
 	<li>Submit the Domo Action Connector for publishing</li>
</ol>

### Login to the Connector IDE
---
1. Login to the Connector IDE at [https://api.domo.com/builder/index.html#!/](https://api.domo.com/builder/index.html#!/). When you login, the prompt asks for which Domo domain you want to develop against: enter your instance name, ex. domo.

2. Click Create New Connector, then click Domo Action:

<img class="alignnone size-full" src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-domoactions1-1.png"  />


<img class="alignnone size-full" src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-domoactions1-2.png" />


### Upload images
---
Icons allow users to quickly identify your action. The four images you need for an action are:
<ul>
 	<li>Icon with background (512 x 512 pixels, png)</li>
 	<li>Icon, no background (512 x 512 pixels, png)</li>
 	<li>Logo with background (512 x 512 pixels, png)</li>
 	<li>Logo banner, no background (1024 x 512 pixels, png)</li>
</ul>

<!-- theme: info -->

> #### Note
> You can move on to other steps before completing this step, but icons are required before you submit your action for publishing.

<img class="alignnone size-full" src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-domoactions1-3.png" />

### Configure User Authentication
---
The Action Builder provides four different authentication methods:
<ul>
 	<li>No authentication</li>
 	<li>Username and password</li>
 	<li>API Key</li>
 	<li>OAuth 2.0</li>
</ul>
Here is an example of the authentication process for username and password. For a detailed description of the different methods, see the Configure Authentication section. For code examples, see Examples.

After selecting an authentication method and filling out the authentication fields, write a code block to validate the API’s credentials.

<!-- theme: info -->

> #### Note
> The code block needs to determine and set the authentication to either auth.authenticationSuccess() or auth.authenticationFailed(‘&lt;&lt;Insert your message&gt;&gt;’).

<img class="alignnone size-full" src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-domoactions1-4.png" />

<h4><strong>Code Example:</strong></h4>

```js
//This logging is here for testing! Remove before publishing your connectors
DOMO.log('metadata.account.username: ' + metadata.account.username); 
DOMO.log('metadata.account.password: ' + metadata.account.password);

var encodedData = DOMO.b64EncodeUnicode(metadata.account.username + ':' + metadata.account.password);
httprequest.addHeader('Authorization', 'Basic ' + encodedData);
var res = httprequest.get('https://developer.domo.com/samplecrm');  

if(res.indexOf('Account.Name') > 0){
	auth.authenticationSuccess();
} else {
	auth.authenticationFailed('Your username and password are incorrect');
}
```

<h4><strong>Best Practices:</strong></h4>
<ul>
 	<li>Ensure the script runs in ‘strict mode’ to avoid any unexpected behavior.</li>
 	<li>If you get errors saying “Expected JSON, but found...”, put your httprequest calls in a ‘try-catch’ block to handle errors gracefully.</li>
</ul>


### Configure the parameters
---
Configure the parameters your action will use:

<img class="alignnone size-full" src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-domoactions1-5.png" />


### Define how the data is processed
---
<div class="page" title="Page 5">
<div class="layoutArea">
<div class="column">

<strong>Sample data processing:</strong>

</div>
</div>
</div>

```js
httprequest.addHeader('Authorization', 'Bearer ' + metadata.account.access token); httprequest.addHeader('Content-Type', 'application/json');
let baseURL = 'https://na73.salesforce.com/services/data/v22.0/sobjects/'; 
let url = baseURL + "Opportunity/" + metadata.parameters["Opportunity ID"]
+ "?_HttpMethod=PATCH" let req = JSON.stringify({ 
      "StageName" : metadata.parameters["Stage Name"]
});
let res = httprequest.post(url, req); DOMO.log(res); 
var result = JSON.stringify({
      "status": httprequest.getStatusCode() 
});
datagrid.addColumn('Response', datagrid.DATA_TYPE_STRING); 
datagrid.addCell(result);
datagrid.endRow();
```

<img class="alignnone size-full" src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-domoactions1-6.png"  />

### Submit the Domo Action for publishing
---

1. Click **Submit for Publishing**. Domo automatically checks your action for some required work and notifies you of any missing fields. If everything checks out, the action submission modal will appear.

<img class="alignnone size-full wp-image-4052" src="https://developer.domo.com/wp-content/uploads/2017/03/Connector-Submission-Old-image.png" alt=""  />

2. In the **Additional Instructions** field, include any information needed to test and validate your action. If your action uses OAuth 2 for validation, please include a username and password. Our engineers will only use these for testing and validation.


3. Select your action visibility.

    - Select **Shared with your company** to keep the action for exclusive use in your company’s Domo instance.
    - Select **Public to all companies** to make your action available to all Domo users.

4. Click <strong>Continue Submission</strong>.

   - If you chose to make your action public: **Congratulations!** You’ve successfully submitted your action. Domo will begin the 30-day review process and will contact you with any questions. You can expect an update within 3 business days after submission.


5. Click the <strong>View Status</strong> or the <strong>Overview</strong> tab to see the status of your action review. You will also be sent email updates about your action’s status in the review process.

<img class="alignnone size-full wp-image-4048" src="https://developer.domo.com/wp-content/uploads/2017/03/Connector-Submission.png" alt=""  />

<!-- theme: info -->

> #### Note
> To withdraw your action from submission, open the action. Click <strong>View Status.</strong> In the status window, click <strong>Withdraw</strong>.


### Review Process
---
Your action code passes through several phases of review.

**1. Automated Tests:** The code is syntax checked, smoke tested, and verified for compliance to policies. We check that:

  - XMLHttpRequest is not used. Use httprequest.get() or httprequest.post() instead.
   - Code is not minified.
   - Credentials are not hard coded.
   - Information is not redirected to an external API.

**2. Security Test:** Domo engineers ensure that all security protocols are being followed, in addition to those listed above.

**3. Performance Tests:** Tests are run to make sure that the action speed relative to the number of records processed is acceptable: over 1,000 records per 5 minutes.

**4. Code review:** The code is reviewed by one of our developers to ensure that the code is readable and clean.

Click **View Status** in the **Develop** tab or select the **Overview** tab to see the status of your action review. You will also be sent email updates about your action’s status in the review process.


## Execute a Domo Action

<h4><strong>Scope</strong></h4>

Domo Actions have three possible scopes: personal, customer and global. Newly created Domo Actions have a personal scope, which means they can only be executed by the user who published that Domo Action. Once an action is published it will have a customer scope, which means all users in the customer instance can execute the Action. A global scope means anyone using the Domo platform will be able to use the action.

As of now, Domo Actions are changed to a global scope manually. Contact Diane Stewart at [diane.stewart@domo.com](mailto:diane.stewart@domo.com) to change to a global scope.

### Using Domo Actions with a Custom App
---

1. Add the `accountMapping` property to your `manifest.json`. The data-provider key will be provided to you when your action is published. Your `manifest.json` will look something like the following:

<img class="alignnone " src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-domo-actions-code.png" />

This account mapping provides an account picker for the user of the app to select which account they want to use in their instance of the app.

<img class="alignnone size-full" src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-domoactions2-1.png" />

2. Use your account mapping alias, and action GUID to execute your action.

<strong>Sample processAction function:</strong>

```js
processAction = () => {
    let actionGUID = 'ff859375-e27f-40f7-afc8-bdebbbc0720b'; return fetch(`/domo/actions/v1/${actionGUID}/process?
    accountAlias=googleSheetsAccount&scope=personal`, //the accountAlias value is defined in the manifest.
json
    {
    method: "POST", 
    headers: {
        "Content-Type": "application/json" 
    },
    body: JSON.stringify({ 
        "sheetID": this.state.sheetID
}) })

    .then(response => response.json()); 
}
```
<strong>Sample Domo App:</strong>

```js
handleSave(data) {
let actionGUID = '0ca46ccc-f4e1-4227-8d89-95397ed4fe7a';
let accountId = '57658'
return fetch(`/domo/actions/v1/${actionGUID}/process?account=${accountId}&scope=personal`,
    {
    method: "POST", headers:{
    "Content-Type": "application/json" },
    body: JSON.stringify({ "Opportunity ID": data.id,
    "Stage Name": data.stage 
}) });
}
```

Screenshots of Domo Action in action in the Domo App:

<img class="alignnone size-full" src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-domoactions2-2.png" />

<img class="alignnone size-full" src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-domoactions2-3.png"  />

<img class="alignnone size-full" src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-domoactions2-4.png"  />

<img class="alignnone size-full" src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-domoactions2-5.png"  />


### Q & A
---

<strong>Why can't we just call Salesforce directly within the Domo app? Why do we need to wrap that code in a Domo Action?</strong>

Accounts. Domo Actions are essentially connectors, so they know about data providers, how to consume accounts and refresh tokens. By passing in the Domo Account ID into the Domo Action, it handles all of those account details so you don't need to do so within your app.

