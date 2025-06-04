---
stoplight-id: 842ac09f65853
---

# Start leveraging Domo's API Actions

With the Action API you can build an automated action to trigger events across business systems, whether those actions originate in Domo or somewhere else.​

### Create an API Action
---
<h4><strong>Step 1. Login to the Connector IDE</strong></h4>

Login to the Connector IDE at [https://api.domo.com/builder/index.html#!/](https://api.domo.com/builder/index.html#!/). When you login, the prompt asks for which Domo domain you want to develop against: enter your instance name, ex. domo.

<h4><strong>Step 2. Click Create New and then select API Action</strong></h4>

<img class="alignnone size-full" src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-APIActions1.png" />

<img class="alignnone " src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-APIActions2.png" />

<h4><strong>Step 3. Upload Connector Icons</strong></h4>

<img class="alignnone " src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-APIActions3.png" />

<h4><strong>Step 4. Enter Domo Client Key and Domo Client Secret</strong></h4>

<img class="alignnone " src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-APIActions4.png" />

<h4><strong>Step 5. Configure authentication to third party API</strong></h4>

<h4><strong>Step 6. Define how data is processed</strong></h4>
Sample code:

```js
car data = DOMO.getDataset(metadata.parameters.datasetId).queryData("select * from tbl")
Domo.log(data)
datagrid.addColumn("Response");
datagrid.addCell(JSON.stringify(data));
datagrid.endrow( );
```

<h4><strong>Step 7. Submit for publishing</strong></h4>
<img class="alignnone " src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-APIActions5.png" />

### Domo Methods
---

<h4><strong>DOMO.listDatasets(); </strong></h4>

- Returns list of all DOMO dataset IDs

<h4><strong>DOMO.getDataset(datasetId);</strong></h4>

- datasetID = ID of dataset within DOMO that you'd like to pull data from.

Example: let id = ''cd64fdef-6106-48c2-948a-2b5e160cad2d';

- returns full dataset object

<h4><strong>DOMO.queryData(datasetId, query);</strong></h4>

- datasetId = ID of dataset within DOMO that you'd like to pull data from.

- query = the sql command you'd like to perform on returned data

Example: let query= "select * from tbl where action = 'open'";

<h4><strong>Best Practice</strong></h4>

Sample code:

```
let id = 'cd64fdef-6106-48c2-948a-2b5e160cad2d'; 
let query = "select * from tbl where action = 'open'"; 
let data = DOMO.getDataset(id).queryData(query);
datagrid.addColumn("Response");
datagrid.addCell(JSON.stringify(data));
datagrid.endRow();
```

### Execute an API Action
---
<h4><strong>What Actions are available?</strong></h4>
<strong>GET</strong>
<ul>
 	<li>https://api.domo.com/v1/domoactions</li>
 	<li><strong>Authorization:</strong> Bearer &lt;your-valid-oauth-access-token&gt;</li>
</ul>
Returns a JSON array of action objects.

```json
[
    {
        "name": "My API Action 1 ",
        "guid": "fc1e465e-186d-4510-9d0a-dea560eef054",
        "version": 3
    },
    {
        "name": "My API Action 2",
        "guid": "c3925edd-c72b-4394-ad0c-2110dfce90b2",
        "version": 7
    },
…
]
```

<h4><strong>How do I execute the Action?</strong></h4>

<strong>POST</strong>


- [https://api.domo.com/v1/domoactions/{guid}/process?account={accountId}](https://api.domo.com/v1/domoactions/{guid}/process?account={accountId})
- guide: action guid from previous response
- accountId: numerical ID associated with Domo API action account. You must have access to this account to execute the code.
- **Authorization:** Bearer &lt;your-valid-oauth-access-token&gt;
- **Accept:** application/json, application/xml, application/x-yaml or text/csv (required)
- **Content-Type:** application/json
- **Body:** {"datasetId":"486718db-7ca1-4d47-9fc7-c229996c8578"}

Returns the response defined in the first cell of the datagrid of the action JavaScript.

<h4><strong>How do I create an account?</strong></h4>
Add an account in Data Center -&gt; Accounts -&gt; Add Account -&gt; API Actions

<img class="alignnone size-full" src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-APIActionsExecute1.png" />


<h4><strong>Where do I find my account ID?</strong></h4>

<strong>GET</strong>


- [https://api.domo.com/v1/accounts/?offset=0&amp;limit=1](https://api.domo.com/v1/accounts/?offset=0&amp;limit=1)
- limit: The number of Accounts to return in the list. The default is 50 and the maximum is 500. (Optional)
- offset: The offset of Accounts to begin the list of Accounts within the response.
- **Accept:** application/json
- **Host:** api.domo.com
- **Authorization:** bearer &lt;your-valid-oauth-access-token&gt;


### API Action FAQs
---
<h4><strong><span lang="EN-IN">How do I create a Client ID and Secret?</span></strong></h4>
Developer.domo.com -&gt; My Account -&gt; New Client

<img class="alignnone size-full" src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-APIActions-FAQ1.png" />

<h4><strong><span lang="EN-IN">Where can I find the DataSet ID?</span></strong></h4>
In the URL of the dataset:

<img class="alignnone size-full" src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-dev-rriteback-8.png" />


