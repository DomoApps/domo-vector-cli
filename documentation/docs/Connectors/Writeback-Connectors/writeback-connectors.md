---
stoplight-id: cf8902150aae4
---

# Writeback Connectors

Writeback Connectors allow you to push DataSets to third-party file storage applications instead of pulling data from those applications into Domo.

<h4><strong>Next Steps:</strong></h4>

You can build your own Writeback Connector in Domo by starting with the [Connector Dev Studio >> Let’s Build](../Custom-Connectors/connector-dev-studio.md#lets-build) section.

You need to complete the following steps when building a custom Writeback Connector:
<ul>
 	<li>Create a new Writeback Connector</li>
 	<li>Upload Connector icon images</li>
 	<li>Configure user authentication</li>
 	<li>Configure selectable reports</li>
 	<li>Define how the data is processed</li>
</ul>
After you have completed these steps, you can submit the connector for publishing. Domo developers will review the connector, perform some engineering magic, and notify you when your connector is available for use.
<div id="Create%20a%20new%20Writeback%20connector" class="doc-row"></div>
&nbsp;

### Create a new Writeback Connector
---
<ul>
 	<li>Click the <strong>Build Now</strong> button at the bottom of the screen to create a new connector.</li>
 	<li><strong>My Connector Developer</strong> page will appear. Here, you will need to fill out the <strong>Custom Connector User Agreement</strong>.</li>
 	<li>After accepting the agreement, click on the <strong>Create New</strong>  button.</li>
</ul>
<img class="alignnone size-full" src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-dev-rriteback-1.png" />
<ul>
 	<li>Click on the <strong>Writeback Connector</strong> tile.</li>
</ul>
<img class="alignnone wp-image-3668" src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-dev-writeback-10.png" alt="" />
<ul>
 	<li><strong>Name your connector</strong> screen will appear. Provide a name for your Writeback Connector and click <strong>Create</strong> button.</li>
</ul>
<img class="alignnone " src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-dev-rriteback-2.png" />

### Upload Connector Icon images
---
<ul>
 	<li>Once you have created your Writeback Connector, you need to upload the Connector icon.</li>
</ul>
<img class="alignnone size-full" src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-dev-rriteback-3.png" />
<ul>
 	<li>Select the desired icon image for your connector and click Upload.</li>
</ul>

### Configure Domo authentication
---
You need to configure the Domo authentication after uploading the icon image for your Writeback Connector.

<img class="alignnone size-full" src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-dev-rriteback-4.png" />
<ul>
 	<li>Specify your Domo Client Key and Domo Client Secret, and click <strong>Next</strong>.</li>
</ul>

### Configure authentication
---
<ul>
 	<li>Select authentication credentials type as <strong>OAuth 2.0 </strong>and write the authentication script.</li>
</ul>
<img class="alignnone size-full" src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-dev-rriteback-5.png" />


### Define how data is processed
---
<ul>
 	<li>Write the data processing script.</li>
</ul>
<img class="alignnone size-full" src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-dev-rriteback-6.png" />


### Submit for publishing
---
After you have written and tested your connector, you are ready for publishing! You can choose to make the connector only available to your private company or available to any Domo user. Follow the guide below to submit the connector for approval. Once approved, your connector is ready to go!
<ul>
 	<li>Click <strong>Submit for Publishing</strong>.</li>
</ul>
<img class="alignnone size-full wp-image-3669" src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-dev-writeback-11.png" alt="" />

### Writeback methods
---

<strong id="listDatasets">DOMO.listDatasets();</strong> 

> Returns:   
> a list of all DOMO dataset IDs


<strong id="getDataset(datasetId)">DOMO.getDataset(datasetId);</strong> 
> datasetId = ID of dataset within DOMO that you’d like to pull data from.
Example:
```
id = metadata.parameters.datasetId; 
```

> Returns:   
> a full dataset object


<strong id="queryData(datasetId, query)">DOMO.queryData(datasetId, query);</strong>

> datasetId = ID of dataset within DOMO that you’d like to pull data from.
> query = the sql command you’d like to perform on returned data
Example: 
```
query = "select * from tbl where action = 'open'";
```
Best practices:
- let id = metadata.parameters.datasetId; 
- let query = "select * from tbl where action = 'open'"; 
- let data = DOMO.getDataset(id).queryData(query);

### Where can I find the DataSet ID?
---
You can find the DataSet ID in the URL of the dataset as shown below.

<img class="alignnone size-full" src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-dev-rriteback-8.png" />

### How can I access the DataSet ID?
---
<ul>
 	<li>Add a parameter named datasetId. Provide the attributes to it, like help text to be displayed for it.</li>
 	<li>Click <strong>Add Parameter</strong>.</li>
</ul>
<img class="alignnone size-full" src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-dev-rriteback-9.png" />


