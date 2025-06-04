---
stoplight-id: t96yq1sjeh4br
---

<div class="col-md-12 content-panel">
                <h2>Google Maps Pinboard</h2>
                <p></p><p>Thanks for installing and test-driving Google Maps Pinboard! This guide is intended to help you connect this app to your own data. The first step is to ensure that your data follows the same schema (or structure) of the sample datasets that are currently powering the app. Fortunately, Domo has created some powerful data transformation tools to help, along with the step-by-step instructions provided below.</p>
<h3 class="doc-row-title">Prerequisites:</h3>
<p>To speed up the connection process for your data, this&nbsp;app utilizes Domo’s Grid Builder. If you are not already familiar with Grid Builder,&nbsp;please visit our&nbsp;<a href="http://Link to Grid Builder Training" target="_blank">Grid Builder Training</a>.</p>
<p>Below is a diagram that shows the order in which&nbsp;the customer data will be fed through and output to the App.</p>
<p><img loading="lazy" class="alignnone wp-image-2587" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/07/22155201/data-flow-organization.png" alt="data flow organization" width="1284" height="359" srcset="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/07/22155201/data-flow-organization.png 2683w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/07/22155201/data-flow-organization-300x84.png 300w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/07/22155201/data-flow-organization-768x215.png 768w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/07/22155201/data-flow-organization-1024x286.png 1024w" sizes="(max-width: 1284px) 100vw, 1284px"></p>
<p><strong>Things to Know About This&nbsp;App:</strong></p>
<p>It is recommended that you become familiar with the customer’s input data and desired metrics before implementing this app.</p>
<div id="Step%201:%20Identify%20Required%20Data%20Fields" class="doc-row">
<h3 class="doc-row-title">Step 1: Prepare Your Data</h3>
<div class="small-pad-bottom">
<p>This app requires creating a custom dataset named “Google Maps Pinboard – Grid Builder”.</p>
<p>Please follow the step-by-step instructions provided below:</p>
<ul>
<li>Navigate to your Data Center.</li>
</ul>
<p><img loading="lazy" class="alignnone wp-image-2467" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/24125437/1-Navigate-to-Data-Center-1-801x1024.png" alt="1 - Navigate to Data Center" width="510" height="652" srcset="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/24125437/1-Navigate-to-Data-Center-1-801x1024.png 801w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/24125437/1-Navigate-to-Data-Center-1-235x300.png 235w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/24125437/1-Navigate-to-Data-Center-1-768x982.png 768w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/24125437/1-Navigate-to-Data-Center-1.png 1033w" sizes="(max-width: 510px) 100vw, 510px"></p>
<p>&nbsp;</p>
<ul>
<li>Click “+ New DataSet”.</li>
</ul>
<p><img loading="lazy" class="alignnone wp-image-2469" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/24125440/2-Click-Create-new-data-set1-1024x173.png" alt="2 - Click Create new data set" width="953" height="161" srcset="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/24125440/2-Click-Create-new-data-set1-1024x173.png 1024w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/24125440/2-Click-Create-new-data-set1-300x51.png 300w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/24125440/2-Click-Create-new-data-set1-768x130.png 768w" sizes="(max-width: 953px) 100vw, 953px"></p>
<p>&nbsp;</p>
<ul>
<li>Search for “Domo Online Form” and click “Connect”.</li>
</ul>
<p><img loading="lazy" class="alignnone wp-image-2466" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/24124311/4-Data_Connectors_drop_shadow-1024x488.png" alt="4 - Data_Connectors_drop_shadow" width="902" height="430" srcset="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/24124311/4-Data_Connectors_drop_shadow-1024x488.png 1024w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/24124311/4-Data_Connectors_drop_shadow-300x143.png 300w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/24124311/4-Data_Connectors_drop_shadow-768x366.png 768w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/24124311/4-Data_Connectors_drop_shadow.png 1527w" sizes="(max-width: 902px) 100vw, 902px"></p>
<p>&nbsp;</p>
<ul>
<li>Title the new data set “Google Maps Pinboard – Grid Builder”.</li>
<li>Use the following example table to copy and paste all fields into your newly created Grid Builder as they are shown below:</li>
</ul>
</div>
</div>
<table width="2778">
<tbody>
<tr>
<td width="73">GridId</td>
<td width="113">GridName</td>
<td width="48">C</td>
<td width="212">SELECT</td>
<td width="296">FROM</td>
<td width="84">WHERE</td>
<td width="116">GROUP BY</td>
<td width="120">AS</td>
<td width="84">Include</td>
<td width="96">JoinType</td>
<td width="145">JoinCondition</td>
<td width="69">MAJIK</td>
<td width="80">FilterId</td>
<td width="121">FilterName</td>
<td width="161">FilterInputType</td>
<td width="156">FilterIsPrimary</td>
<td width="219">FilterIsPrimaryGroup</td>
<td width="585">Description</td>
</tr>
<tr>
<td>1</td>
<td>Locations</td>
<td>100</td>
<td>&lt;‘RequiredField.1’&gt;</td>
<td>&lt;‘YourDataSetNameHere.1’&gt;</td>
<td></td>
<td></td>
<td>Id</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>STRING – Unique Store(or Location) ID</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>&lt;‘RequiredField.2’&gt;</td>
<td></td>
<td></td>
<td></td>
<td>Date</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>DATE – Date the observed metrics were measured. May use CURRENT_DATE() in SELECT field if unavailable</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>&lt;‘RequiredField.3’&gt;</td>
<td></td>
<td></td>
<td></td>
<td>Node</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>STRING – What you want each pin on the map to be called. Ex. Store (or Location) Name or ID</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>&lt;‘RequiredField.4’&gt;</td>
<td></td>
<td></td>
<td></td>
<td>Latitude</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>STRING – Latitude of store location</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>&lt;‘RequiredField.5’&gt;</td>
<td></td>
<td></td>
<td></td>
<td>Longitude</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>STRING – Longitude of store location</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>&lt;‘OptionalField.1’&gt;</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Example: INT – Store traffic on this day for this unique store ID</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>&lt;‘OptionalField.2’&gt;</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Example: INT – Store orders on this day for this unique store ID</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>&lt;‘OptionalField.3’&gt;</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Example: DECIMAL – Gross sales on this day for this unique store ID</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>&lt;‘OptionalField.4’&gt;</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Example: DECIMAL – Net sales on this day for this unique store ID</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>&lt;‘OptionalField.5’&gt;</td>
<td>&lt;‘YourOptionalDataSetNameHere.2’&gt;</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Example: INT – Employees working on this day at this store</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>&lt;‘OptionalField.6’&gt;</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>1</td>
<td>Category</td>
<td>Multi Select</td>
<td></td>
<td></td>
<td>Example: STRING – Store category</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>&lt;‘OptionalField.7’&gt;</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>2</td>
<td>Region</td>
<td>Multi Select</td>
<td></td>
<td></td>
<td>Example: STRING – Region of the associated store</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>&lt;‘OptionalField.8’&gt;</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>3</td>
<td>Owner</td>
<td>Multi Select</td>
<td></td>
<td></td>
<td>Example: STRING – Name of store owner</td>
</tr>
</tbody>
</table>
<div id="Step%201:%20Identify%20Required%20Data%20Fields" class="doc-row">
<div class="small-pad-bottom">
<p>&nbsp;</p>
<ul>
<li>You will need to ensure that you already have each of these data fields imported into the customer’s Data Center&nbsp;before you&nbsp;map out this&nbsp;existing data to the&nbsp;Grid Builder webform.&nbsp;Please bear in mind that the example provided <em>may differ significantly from your own data structure</em> within the Grid Builder.</li>
<li>The first five fields in the “AS” column are necessary for this app to function. The customer must have Latitude and Longitude data formatted as a number data type.</li>
<li>Important Note: Do not change any values in the ‘GridName’ or the first five row of the ‘AS’ columns. Doing so will cause your data to display incorrectly or not at all.</li>
<li>Fill&nbsp;out the ‘SELECT’ column with the field names as they&nbsp;appear in your data set.</li>
<li>Fill out the ‘FROM’ column with the name of the data set.</li>
<li>Fill out the ‘WHERE’ and ‘GROUP BY’ columns as needed.</li>
</ul>
<p>For additional help with Grid Builder please visit our&nbsp;<a href="http://Link to Grid Builder Training" target="_blank">Grid Builder Training</a>.</p>
</div>
<br>
<h3 class="doc-row-title">Step 1.5:&nbsp;Define Your Metrics</h3>
<p>We have created a powerful tool to help you define your metrics for this app.</p>
<p>In order to do this, you will need to navigate to your&nbsp;Data Center and follow the steps below:</p>
<ul>
<li>Create a dataset&nbsp;and name it “Google Maps Pinboard – Metrics”.</li>
<li>Edit the columns according to the guidelines below:</li>
</ul>
<table style="height: 183px;" width="581">
<tbody>
<tr>
<td><strong>Field Name</strong></td>
<td><strong>Instructions To Fill Out Associated Field</strong></td>
</tr>
<tr>
<td>Name</td>
<td>How the metric should be called in the app</td>
</tr>
<tr>
<td>Calculation</td>
<td>The calculation of the app according to “The Grid” datasource. This section supports SUM, MAX, MIN, AVG, QUOTA_ATTAINMENT as well as basic +,-,/,* between these functions. Integers are not supported.</td>
</tr>
<tr>
<td>DataType</td>
<td>Currency, Percent or Number</td>
</tr>
<tr>
<td>SortHighToLow</td>
<td>True or False</td>
</tr>
<tr>
<td>UnitOfMeasurement</td>
<td>The name of the metric units if the metric calls for it.</td>
</tr>
<tr>
<td>Description</td>
<td>Description of the app so the end user understands it</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
</div>
<ul>
<li class="doc-row">Remember to include the Id column, numbered from 1 through the number of metrics the customer needs. Make sure the column headers have the exact names as seen in the sample below.</li>
</ul>
<div class="doc-row">
<p>Please bear in mind that the example provided <em>may differ significantly from your own data structure</em> within the Metric webform. The following is an example of what your completed webform might look like:<a href="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/07/01135446/google-maps-pinboard-metrics.png"><img loading="lazy" class="aligncenter wp-image-2514 size-full" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/07/01135446/google-maps-pinboard-metrics.png" alt="google maps pinboard - metrics" width="2671" height="919" srcset="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/07/01135446/google-maps-pinboard-metrics.png 2671w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/07/01135446/google-maps-pinboard-metrics-300x103.png 300w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/07/01135446/google-maps-pinboard-metrics-768x264.png 768w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/07/01135446/google-maps-pinboard-metrics-1024x352.png 1024w" sizes="(max-width: 2671px) 100vw, 2671px"></a></p>
<p>Lastly, we need to create one more DataSet to allow the app to function. Follow these steps:</p>
<ul>
<li>Navigate to the Data Center and create a new DataSet using the Domo Online Form connector as seen above.</li>
<li>Name this dataset: “Google Maps Pinboard – Settings”.</li>
<li>Copy the table below into the webform:</li>
</ul>
<table style="height: 287px;" width="668">
<tbody>
<tr>
<td><strong>Name</strong></td>
<td><strong>Value</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr>
<td>Fiscal Quarter 1 Start Date</td>
<td>01-01</td>
<td>The date (mm-dd) the first quarter of your company’s fiscal year begins.</td>
</tr>
<tr>
<td>Fiscal Quarter 2 Start Date</td>
<td>04-01</td>
<td>The date (mm-dd) the second quarter of your company’s fiscal year begins.</td>
</tr>
<tr>
<td>Fiscal Quarter 3 Start Date</td>
<td>07-01</td>
<td>The date (mm-dd) the third quarter of your company’s fiscal year begins.</td>
</tr>
<tr>
<td>Fiscal Quarter 4 Start Date</td>
<td>10-01</td>
<td>The date (mm-dd) the fourth quarter of your company’s fiscal year begins.</td>
</tr>
<tr>
<td>Fiscal Calendar Offset Weeks</td>
<td>4</td>
<td>The offset for the start of your company’s fiscal calendar in weeks. Supports positive and negative integers. Only affects retail calendars.</td>
</tr>
<tr>
<td>Work Week Start Day</td>
<td>2</td>
<td>The day your company’s work week begins (1 = Mon, 2 = Tues, etc).</td>
</tr>
<tr>
<td>Currency Symbol</td>
<td>$</td>
<td>The symbol to be used when displaying currency ($, ¥, etc).</td>
</tr>
<tr>
<td>Currency Symbol Placement</td>
<td>Prepend</td>
<td>The placement method of the currency symbol relative to the currency amount (Prepend or Append).</td>
</tr>
<tr>
<td>useClusteringRadars</td>
<td>TRUE</td>
<td>This determines if the app will cluster pins that are near each other into radars.</td>
</tr>
</tbody>
</table>
</div>
<ul>
<li class="doc-row">Click the “Save and Continue” button.</li>
<li class="doc-row">This DataSet can be changed to alter the settings for the app. See additional&nbsp;information below in step 4.</li>
</ul>
<p></p><div class="doc-row" id="Step%202:%20Connect%20Your%20Data">
                                    <h3 class="doc-row-title">Step 2: Connect Your Data</h3><div class="small-pad-bottom">
                                    <br>
                                    <p>Once you have finished preparing your data as outlined&nbsp;you are ready to connect it to your app.</p>
<p>Please follow the step-by-step instructions provided below:</p>
<ul>
<li>Navigate&nbsp;to the Data Center and create&nbsp;a new DataFlow.</li>
</ul>
<p><img loading="lazy" class="alignnone wp-image-2468" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/24125439/1-Navigate-to-DataFlows1-1024x180.png" alt="1 - Navigate to DataFlows" width="882" height="155" srcset="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/24125439/1-Navigate-to-DataFlows1-1024x180.png 1024w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/24125439/1-Navigate-to-DataFlows1-300x53.png 300w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/24125439/1-Navigate-to-DataFlows1-768x135.png 768w" sizes="(max-width: 882px) 100vw, 882px"></p>
<p>&nbsp;</p>
<ul>
<li>Create a “MySQL” DataFlow.</li>
</ul>
<p><img loading="lazy" class="alignnone wp-image-2470" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/24125441/2-Data-Flow-type1-1024x445.png" alt="2 - Data Flow type" width="727" height="316" srcset="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/24125441/2-Data-Flow-type1-1024x445.png 1024w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/24125441/2-Data-Flow-type1-300x130.png 300w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/24125441/2-Data-Flow-type1-768x333.png 768w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/24125441/2-Data-Flow-type1.png 1815w" sizes="(max-width: 727px) 100vw, 727px"></p>
<p>&nbsp;</p>
<ul>
<li>Name the new DataFlow “Google Maps Pinboard”.</li>
<li>Under “Input DataSets” you will see a button titled “Select DatSets”.</li>
<li>Click that button to add any datasets referenced by your Grid Builder in the “FROM” column, as well as the “Google Maps Pinboard – Grid Builder” and “Google Maps Pinboard – Settings” DataSets that you created in step 1.</li>
</ul>
<p><img loading="lazy" class="alignnone wp-image-2471" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/24125443/3-Add-Grid-builder-data-set1-1024x802.png" alt="3 - Add Grid builder data set" width="688" height="539" srcset="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/24125443/3-Add-Grid-builder-data-set1-1024x802.png 1024w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/24125443/3-Add-Grid-builder-data-set1-300x235.png 300w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/24125443/3-Add-Grid-builder-data-set1-768x602.png 768w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/24125443/3-Add-Grid-builder-data-set1.png 1481w" sizes="(max-width: 688px) 100vw, 688px"></p>
<p><strong>Follow this process to populate the transforms and output datasets:</strong></p>
<ul>
<li>Create a dummy transform: Click the &nbsp;“+Add Transform” button. Enter the text: “Select 1” and click “Apply” as shown below.</li>
</ul>
<p><img loading="lazy" class="alignnone size-full wp-image-2761" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/30130423/PipeScreen3.png" alt="PipeScreen3" width="1230" height="616" srcset="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/30130423/PipeScreen3.png 1230w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/30130423/PipeScreen3-300x150.png 300w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/30130423/PipeScreen3-768x385.png 768w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/30130423/PipeScreen3-1024x513.png 1024w" sizes="(max-width: 1230px) 100vw, 1230px"></p>
<ul>
<li>Navigate to the top of the page and click the “Dev Tools” button.</li>
<li>As soon as the page loads, copy the JSON text below this image and paste it in the area that is highlighted&nbsp;in the&nbsp;image below. The selection to replace should be close to the bottom of the text:</li>
</ul>
<p><img loading="lazy" class="alignnone size-full wp-image-2762" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/30130426/PipeScreen4.png" alt="PipeScreen4" width="1335" height="579" srcset="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/30130426/PipeScreen4.png 1335w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/30130426/PipeScreen4-300x130.png 300w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/30130426/PipeScreen4-768x333.png 768w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/30130426/PipeScreen4-1024x444.png 1024w" sizes="(max-width: 1335px) 100vw, 1335px"></p>
<ul>
<li>Here is the JSON text:</li>
</ul>
<p><a href="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/09/30132206/GoogleMapsPinboard.txt">GoogleMapsPinboard</a></p>
<ul>
<li>Notes: Be careful what you replace. You should only be replacing the information for the dummy transform we created between the two curly braces “{” and “}”. Do not erase the bracket “]” at the end.</li>
<li>Click “Apply Source” to save.</li>
<li>You should see the DataFlow populated with transforms and and output datasets.</li>
</ul>
<ul>
<li>Check the boxes so that the DataFlow will run when any of the input datasets is updated.</li>
<li>Save and run the DataFlow.</li>
<li>Once the DataFlow finishes running, compare&nbsp;your new output datasets to the sample datasets the original app was connected to and verify their&nbsp;formats match.</li>
<li>Go to the app, click the wrench icon in the upper right corner and select “Edit Card”.</li>
</ul>
<p><img loading="lazy" class="alignnone wp-image-2556" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/12141309/Change-AppData-1.png" alt="Change AppData 1" width="309" height="326" srcset="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/12141309/Change-AppData-1.png 623w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/12141309/Change-AppData-1-285x300.png 285w" sizes="(max-width: 309px) 100vw, 309px"></p>
<ul>
<li>Scroll down to the bottom of the page. You will find a list of grayed-out datasets the app uses to power itself.</li>
<li>Click each dataset and click the down-arrow to search for and swap out the sample datasets for the datasets newly created by your DataFlow.</li>
</ul>
<p><img loading="lazy" class="alignnone size-full wp-image-2635" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/07/09135324/GoogleMapsScreen1.png" alt="GoogleMapsScreen1" width="327" height="183" srcset="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/07/09135324/GoogleMapsScreen1.png 327w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/07/09135324/GoogleMapsScreen1-300x168.png 300w" sizes="(max-width: 327px) 100vw, 327px"></p>
<ul>
<li>The BASE&nbsp;tab is where you will connect your “Google Maps Pinboard – Locations” output table, and the RATIOS tab is where you will connect your “Google Maps Pinboard – Metrics” table. Also connect your “Filters” and “Settings” datasets under the appropriate tab.</li>
</ul>
<p>Once you have finished this you may move on to step 3.</p>
<p><script>// <![CDATA[
OO.ready(function() { OO.Player.create("ooyalaplayer-IyYTc1MjE61NwLdtrxXvZuhH-dSGbWnR", "IyYTc1MjE61NwLdtrxXvZuhH-dSGbWnR", { height: 380 }); });
// ]]&gt;</script></p>
<br>
</div></div><div class="doc-row" id="Step%203:%20[OPTIONAL]%20Adjusting%20the%20Filters">
                                    <h3 class="doc-row-title">Step 3: [OPTIONAL] Adjusting the Filters</h3><div class="small-pad-bottom">
                                    <br>
                                    <p>You&nbsp;may want to visualize your&nbsp;app&nbsp;in different ways&nbsp;(i.e. maybe only see one region,&nbsp;or certain types of locations).</p>
<p>In order to do this, you&nbsp;will need to follow the steps below:</p>
<ul>
<li>Navigate to&nbsp;the “Google Maps Pinboard – Grid Builder” webform for this app.</li>
<li>Edit the “FilterId”, “FilterName”, “FilterInputType”, “FilterIsPrimary”, and “FilterIsPrimaryGroup” columns.</li>
<li>If using a primary filter, place a “1” under “FilterIsPrimary” under only one row. Make sure all filters have unique numbers under “FilterID”</li>
<li>Note: In some situations, not all filter columns are required to be populated.</li>
</ul>
<p>Some common filters for this app include:</p>
<ul>
<li>Category, Multi&nbsp;Select</li>
<li>Region, Multi Select</li>
<li>Owner, Multi Select</li>
</ul>
<p><img loading="lazy" class="alignnone size-full wp-image-2517" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/07/01140059/google-maps-pinboard-filters.png" alt="google maps pinboard - filters" width="1963" height="1110" srcset="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/07/01140059/google-maps-pinboard-filters.png 1963w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/07/01140059/google-maps-pinboard-filters-300x170.png 300w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/07/01140059/google-maps-pinboard-filters-768x434.png 768w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/07/01140059/google-maps-pinboard-filters-1024x579.png 1024w" sizes="(max-width: 1963px) 100vw, 1963px"></p>
<p>&nbsp;</p>
<p>Note that all app content adjusts to whatever new filters the customer chooses to add, including the date grains within the app and the chart titles, where applicable.</p>
<p>Any edits that don’t meet&nbsp;the Grid Builder requirements&nbsp;could result in undesired results.</p>
<br>
</div></div><div class="doc-row" id="Step%204:%20[OPTIONAL]%20Adjusting%20the%20Settings">
                                    <h3 class="doc-row-title">Step 4: [OPTIONAL] Adjusting the Settings</h3><div class="small-pad-bottom">
                                    <br>
                                    <p>You&nbsp;may want to edit some of the settings for this app.&nbsp;In order to do this, you&nbsp;will need to follow the steps below:</p>
<ul>
<li>Navigate to the “Google Maps Pinboard – Settings” webform for this app.</li>
<li>Edit the “Value” column as desired.</li>
<li>Use the “Description” column to better understand what are considered acceptable inputs&nbsp;for the “Value” column.</li>
</ul>
<p>Some common settings&nbsp;for this app include:</p>
<table width="1152">
<tbody>
<tr>
<td width="196">Name</td>
<td width="64">Value</td>
<td width="892">Description</td>
</tr>
<tr>
<td>Fiscal Quarter 1 Start Date</td>
<td>01-01</td>
<td>The date (mm-dd) the first quarter of your company’s fiscal year begins.</td>
</tr>
<tr>
<td>Fiscal Quarter 2 Start Date</td>
<td>04-01</td>
<td>The date (mm-dd) the second quarter of your company’s fiscal year begins.</td>
</tr>
<tr>
<td>Fiscal Quarter 3 Start Date</td>
<td>07-01</td>
<td>The date (mm-dd) the third quarter of your company’s fiscal year begins.</td>
</tr>
<tr>
<td>Fiscal Quarter 4 Start Date</td>
<td>10-01</td>
<td>The date (mm-dd) the fourth quarter of your company’s fiscal year begins.</td>
</tr>
<tr>
<td>Fiscal Calendar Offset Weeks</td>
<td>4</td>
<td>The offset for the start of your company’s fiscal calendar in weeks. Supports positive and negative integers. Only affects retail calendars.</td>
</tr>
<tr>
<td>Work Week Start Day</td>
<td>2</td>
<td>The day your company’s work week begins (1 = Mon, 2 = Tues, etc).</td>
</tr>
<tr>
<td>Currency Symbol</td>
<td>$</td>
<td>The symbol to be used when displaying currency ($, ¥, etc).</td>
</tr>
<tr>
<td>Currency Symbol Placement</td>
<td>Prepend</td>
<td>The placement method of the currency symbol relative to the currency amount (Prepend or Append).</td>
</tr>
<tr>
<td>useClusteringRadars</td>
<td>TRUE</td>
<td>This determines if the app will cluster pins that are near each other into radars.</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<p>&nbsp;</p>
<h3 class="doc-row-title">Additional help</h3>
<div class="small-pad-bottom">
<p>Need additional assistance? Visit the&nbsp;<a href="https://dojo.domo.com/apps">Domo Community</a>.</p>
</div>
</div></div>            </div>
