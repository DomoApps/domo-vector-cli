---
stoplight-id: 7145a85ea3589
---

# Build Your Own Writeback Connector (Beta)

You can build your own Writeback connector in Domo in the <strong>Connector Dev Studio &gt;&gt; Let's Build! </strong>section.

You need to complete the following steps when building a custom Writeback connector:
<ol>
 	<li>Create a new Writeback connector</li>
 	<li>Upload connector icon images</li>
 	<li>Configure user authentication</li>
 	<li>Configure selectable reports</li>
 	<li>Define how the data is processed</li>
</ol>
After you have completed these steps, you can submit the connector for publishing. Domo developers will review the connector, perform some engineering magic, and notify you when your connector is available for use.

You can build your own Writeback connector only when it is enabled  for you.

### Create a new Writeback connector
---
<ul>
 	<li>Click the <strong>Build Now</strong> button at the bottom of the screen to create a new connector.</li>
 	<li><strong>My Connector Developer</strong> page will appear. Here, you will need to fill up the <strong>Custom Connector User Agreement</strong>.</li>
 	<li>After accepting the agreement, click on the <strong>Create New</strong>  button.</li>
</ul>
<img class="alignnone size-full wp-image-3837" src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-dev-rriteback-1.png" alt=""  />
<ul>
 	<li>Click on the <strong>Writeback Connector</strong> tile.</li>
</ul>
<img class="alignnone size-full wp-image-3838" src="https://web-assets.domo.com/blog/wp-content/uploads/2022/02/DevWriteback-10.png" alt="" />
<ul>
 	<li><strong>Name your connector</strong> screen will appear. Provide a name for your Writeback connector and click <strong>Create</strong> button.</li>
</ul>
<img class="alignnone size-full" src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-dev-rriteback-2.png"  />


### Upload Connector Icon images
---
<ul>
 	<li>Once you have created your Writeback connector, you need to upload the connector icon.</li>
</ul>
<img class="alignnone size-full" src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-dev-rriteback-3.png" />
<ul>
 	<li>Select the desired icon image for your connector and click Upload.</li>
</ul>

### Configure Domo authentication
---
You need to configure the Domo authentication after uploading the icon image for your Writeback connector.

<img class="alignnone size-full" src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-dev-rriteback-4.png" />
<ul>
 	<li>Specify your Domo Client Key and Domo Client Secret, and click <strong>Next</strong>.</li>
</ul>

### Configure authentication
---
Select authentication credentials type as OAuth 2.0 and write the authentication script.

<img class="alignnone size-full" src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-dev-rriteback-5.png" />

### Define how data is processed
---
Write the data processing script.

<img class="alignnone size-full" src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-dev-rriteback-6.png" />

### Submit for publishing
---
After you have written and tested your connector, you are ready for publishing! You can choose to make the connector only available to your private company or available to any Domo user. Follow the guide below to submit the connector for approval. Once approved, your connector is ready to go!
<ul>
 	<li>Click <strong>Submit for Publishing</strong>.</li>
</ul>
<img class="alignnone size-full" src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-dev-rriteback-7.png" />

### Writeback Methods
---

<strong id="listDatasets">DOMO.listDatasets();</strong> 

> Returns:   
> a list of all DOMO dataset IDs

<strong id="getDataset(datasetId)">DOMO.getDataset(datasetId);</strong> 
> datasetId = ID of dataset within DOMO that you’d like to pull data from.
Example:
```js
id = 'cd64fdef-6106-48c2-948a-2b5e160cad2d'; 
```

> Returns:   
> a full dataset object


<strong id="queryData(datasetId, query)">DOMO.queryData(datasetId, query);</strong>

> datasetId = ID of dataset within DOMO that you’d like to pull data from.
> query = the sql command you’d like to perform on returned data
Example: 
```js
query = "select * from tbl where action = 'open'";

```
Best practices:
- let id = 'cd64fdef-6106-48c2-948a-2b5e160cad2d'; 
- let query = "select * from tbl where action = 'open'"; 
- let data = DOMO.getDataset(id).queryData(query);

### Where can I find the DataSet ID?
---
<ul>
 	<li>You can find the DataSet ID in the URL of the dataset.</li>
</ul>
<img class="alignnone size-full" src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-dev-rriteback-8.png" />


### How can I access the DataSet ID?
---
<ul>
 	<li>Add a parameter named datasetId. Provide the attributes to it, like help text to be displayed for it.</li>
 	<li>Click <strong>Add Parameter</strong>.</li>
</ul>
<img class="alignnone size-full" src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-dev-rriteback-9.png" />
<h4></h4>
<h4><strong id="metadata.parameters.datasetId">DOMO.getDataset(id).queryData(query);</strong></h4>

> datasetId = ID of dataset within DOMO that you’d like to pull data from.
> query = the sql command you’d like to perform on returned data
Example: 
```js
id = 'metadata.parameters.datasetId';
```
Best practice:
- let id = 'metadata.parameters.datasetId';
- let query = "select * from tbl where action = 'open'"; 
- let data = 'Domo.getDataset(id).queryData(query)';
