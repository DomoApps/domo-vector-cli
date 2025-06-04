---
stoplight-id: 5d8f965eb3469
---

# Overview

You need to complete four steps when building a custom connector:
<ol>
 	<li>Upload connector icon images</li>
 	<li>Configure user authentication</li>
 	<li>Configure selectable reports</li>
 	<li>Define how the data is processed</li>
</ol>
After you have completed these steps, you can submit the connector for publishing. Domo developers will review the connector, perform some engineering magic, and notify you when your connector is available for use.


<button class="domo-cta-button">
  <a href="https://api.domo.com/builder/index.html">Build a Custom Connector</a>
</button>

This section will review the process using the <strong>Sample CRM</strong> custom connector provided in Connector Dev Studio.

### Upload Icon Images
---
Icons allow users to quickly identify your connector. The four images you need for a connector are:
<ul>
 	<li>Icon with background (512 x 512 pixels, png)</li>
 	<li>Icon, no background (512 x 512 pixels, png)</li>
 	<li>Logo with background (512 x 512 pixels, png)</li>
 	<li>Logo banner, no background (1024 x 512 pixels, png)</li>
</ul>
<strong>Note: </strong>You can move on to other steps before completing this step, but icons are required before you submit your connector for publishing.

<img class="alignnone size-full wp-image-3359" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2017/03/10161752/UserIcon.png" alt="" />

### Configure User Authentication
---
The Connector Builder supports four different authentication methods:
<ul>
 	<li>No authentication</li>
 	<li>Username and password</li>
 	<li>API Key</li>
 	<li>OAuth 2.0</li>
</ul>

Here is an example of writing authentication code for an API that uses <strong>username and password</strong>. For a detailed description of the different methods, see the [Configure Authentication](configure-authentication.md) section. For code examples, see [Examples](examples.md).

Selecting an authentication method determines the metadata available to use in your authentication script.  After selecting an authentication method and filling out the authentication fields, write a code block to validate the API's credentials.

<!-- theme: info -->

> #### Note
>The code block needs to determine and set the status of the API credential validation code to either <em>`auth.authenticationSuccess()`</em> or <em>`auth.authenticationFailed('Insert your message')`</em>.  The messsage provided to the <em>auth.authenticationFailed</em> method will be displayed to users when the connector is run if the authentication fails.

<img class="alignnone size-full wp-image-3975" src="https://web-assets.domo.com/blog/wp-content/uploads/2022/02/UserAuth.png" alt="" width="1160" height="523" />

Code:

```js
//This logging is here for testing! Remove before publishing your connectors
DOMO.log('metadata.account.username: ' + metadata.account.username); 
DOMO.log('metadata.account.password: ' + metadata.account.password);

var encodedData = DOMO.b64EncodeUnicode(metadata.account.username + ':' + metadata.account.password);
httprequest.addHeader('Authorization', 'Basic ' + encodedData);

var res = httprequest.get('https://developer.domo.com/samplecrm');  

if(httprequest.getStatusCode() == 200){
    auth.authenticationSuccess();
} else {
    auth.authenticationFailed('Your username and password are incorrect.');
}
```

<strong>Best Practices: </strong>
<ul>
 	<li>Ensure the script runs in 'strict mode' to avoid any unexpected behavior.</li>
 	<li>If you get errors saying "Expected JSON, but found…", put your httprequest calls in a 'try-catch' block to handle errors gracefully.</li>
</ul>


### Configure Selectable Reports
---
Each connector can contain multiple reports. Reports allow a developer to call different API endpoints or perform different work on the data received. In this step, you will define the reports that a user can select when using this connector in Domo. These reports will appear in the Report dropdown menu after the connector is published.

If you would like the ability for users to provide custom parameters that you can use when making your API calls, click <strong>Enable Advanced Mode</strong>. See [confingure Reports](configure-reports.md) for instructions on how to use this feature. For code examples, see [Examples](examples.md).

<img class="alignnone size-full wp-image-3360" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2017/03/10162606/UserReports.png" alt=""/>


### Define How the Data Is Processed
---
In this step, you will define how to process the data returned from the API endpoint. This is frequently done per report. Your script will need to retrieve the data, parse it, and store it in Domo. To store the data in Domo, first define the columns with a column name and data type, then add the data, one row at a time, one cell at a time.

See [Process Data](process-data.md) for more detailed instructions. For code examples, see [Examples](examples.md).

<img class="alignnone size-full wp-image-3363" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2017/03/11112751/UserData1.png" alt="" />

```js
//This logging is here for testing! Remove before publishing your connectors
DOMO.log('metadata.account.username: ' + metadata.account.username); 
DOMO.log('metadata.account.password: ' + metadata.account.password); 

DOMO.log('metadata.report: ' + metadata.report); // Opportunities

var encodedData = DOMO.b64EncodeUnicode(metadata.account.username + ':' + metadata.account.password);

// Perform work per report
if(metadata.report == 'Opportunities'){
	// Call API Endpoint
	httprequest.addHeader('Authorization', 'Basic ' + encodedData);
	var res = httprequest.get('https://developer.domo.com/samplecrm');

	// Parse Return
	var lines = res.split('r');
	var header = lines[0].split(',');
	
	// Add Columns. There are three data types: 
    //    datagrid.DATA_TYPE_STRING,
    //    datagrid.DATA_TYPE_DOUBLE and 
    //    datagrid.DATA_TYPE_DATETIME
	datagrid.addColumn('Account.Id', datagrid.DATA_TYPE_STRING);
	datagrid.addColumn('Account.Industry', datagrid.DATA_TYPE_STRING);
	datagrid.addColumn('Account.Name', datagrid.DATA_TYPE_STRING); 
	datagrid.addColumn('Amount', datagrid.DATA_TYPE_DOUBLE);
	datagrid.addColumn('CloseDate', datagrid.DATA_TYPE_DATETIME);
	datagrid.addColumn('CreatedDate', datagrid.DATA_TYPE_DATETIME);
	datagrid.addColumn('Id', datagrid.DATA_TYPE_STRING);
	datagrid.addColumn('IsClosed', datagrid.DATA_TYPE_STRING);
	datagrid.addColumn('IsWon', datagrid.DATA_TYPE_STRING);
	datagrid.addColumn('LastActivityDate', datagrid.DATA_TYPE_DATETIME);
	datagrid.addColumn('LastModifiedDate', datagrid.DATA_TYPE_DATETIME);
	datagrid.addColumn('LeadSource', datagrid.DATA_TYPE_STRING);
	datagrid.addColumn('Name', datagrid.DATA_TYPE_STRING);
	datagrid.addColumn('NextStep', datagrid.DATA_TYPE_STRING);
	datagrid.addColumn('Probability', datagrid.DATA_TYPE_DOUBLE);
	datagrid.addColumn('StageName', datagrid.DATA_TYPE_STRING);
	datagrid.addColumn('Type', datagrid.DATA_TYPE_STRING);
	datagrid.addColumn('ForecastCategoryName', datagrid.DATA_TYPE_STRING);
	datagrid.addColumn('Strategic_Account__c', datagrid.DATA_TYPE_STRING);
	datagrid.addColumn('Forecasted_ACV__c', datagrid.DATA_TYPE_DOUBLE);
	datagrid.addColumn('Competitor__c', datagrid.DATA_TYPE_STRING);
	datagrid.addColumn('Owner.CreatedDate', datagrid.DATA_TYPE_DATETIME);
	datagrid.addColumn('Owner.Email', datagrid.DATA_TYPE_STRING);
	datagrid.addColumn('Owner.FullPhotoUrl', datagrid.DATA_TYPE_STRING);
	datagrid.addColumn('Owner.Id', datagrid.DATA_TYPE_STRING);
	datagrid.addColumn('Owner.IsActive', datagrid.DATA_TYPE_STRING);
	datagrid.addColumn('Owner.Manager', datagrid.DATA_TYPE_STRING);
	datagrid.addColumn('Owner.Name', datagrid.DATA_TYPE_STRING);
	datagrid.addColumn('Owner.UserRole.Name', datagrid.DATA_TYPE_STRING);

	// Add Rows
	for(var i = 1; i < lines.length; i++){
		console.log('line: ' +  lines[i]); 
        // For heavy logging, use browser console logging
		var rows = lines[i].split(',');
		// Add cells
		for(var j = 0; j < rows.length; j++){ 
		// Ensure time string in right format. It needs to be yyyy-MM-dd'T'HH:mm:ss
			if (j == 4 || j ==9){
				datagrid.addCell(rows[j] + 'T00:00:00');
			} else {
				datagrid.addCell(rows[j]);
			}
		}
		// Make sure to end the row!
		datagrid.endRow();
	}
} else {
	// Gracefully handle a report error
	DOMO.log(metadata.report + ' is not a supported report.');
	datagrid.error(0, metadata.report + ' is not a supported report.');
}
```

<strong>Best Practices: </strong>
<ul>
 	<li>Ensure the script runs in ‘strict mode’ to avoid any unexpected behavior.</li>
 	<li>Dates inserted into the table need to be formatted <em>yyyy-MM-dd'T'HH:mm:ss</em>.</li>
 	<li>When adding a row, remember to call <em>datagrid.endRow()</em> when then row is complete.</li>
 	<li>Click <strong>Run Script</strong> anytime you want to test your code.</li>
</ul>

### Send Data to Domo
---
After you have completed defining how the data will be processed, you can ensure the data is correctly represented in Domo by sending your generated data to Domo.
<ol>
 	<li>Click <strong>SEND TO DOMO</strong> to view the <strong>Create/Update Dataset</strong> check box.</li>
 	<li>Check <strong>Create/Update Dataset</strong>.</li>
 	<li>Click <strong>Run Script</strong>. A success or error message about the process will appear next to the <strong>Run Script</strong> button.</li>
 	<li>If successful, the dataset will be published in your Domo instance. A pop-up window will provide a link directly to the dataset (this may be blocked by a pop-up blocker).</li>
</ol>
<img class="alignnone size-full wp-image-3362" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2017/03/10173244/UserData2.png" alt="" />

In your Domo instance, you can verify that your datatypes and values are correct.

<!-- theme: info -->

> #### Note
> These datasets cannot be scheduled. The connector must be published to schedule dataset updates.

<img class="alignnone size-full wp-image-3364" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2017/03/11132648/UserDataCenter.png" alt="" />

### Connector Submission
---
After you have completed all four steps and ensured that the connector is behaving the way you want, click <strong>Submit For Publishing</strong>.

<img class="alignnone size-full wp-image-3365" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2017/03/11133551/UserPublish.png" alt=""/>

- The review process for a custom connector may take up to 30 days.
- For <strong>status inquiries &amp; questions </strong>pertaining to these custom connectors, please contact [3rdpartyconnectorhelp@domo.com](mailto:3rdpartyconnectorhelp@domo.com).
- If you select to self-publish a trial version of the custom connector, it will be available for 30 days for review and refinement.
- The self-publish option is not available for custom connectors that use OAuth 2.o in the authentication process or use discovery parameter types in Configure Reports / Advanced Mode.

See [Publish Connector](publish-connector.md) for more detailed instructions and information on this process.


<button class="domo-cta-button">
  <a href="https://api.domo.com/builder/index.html">Build a Custom Connector</a>
</button>

