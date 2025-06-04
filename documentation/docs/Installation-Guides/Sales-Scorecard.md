---
stoplight-id: a1iyqntxocm4n
---

<div class="col-md-12 content-panel">
                <h2>Sales Scorecard</h2>
                <p></p><p>Thank you for installing, test-driving, and purchasing Sales&nbsp;<span id="title">Scorecard</span>! This guide is intended to help you connect this app to your own data. If you have completed the purchasing process for this app then you will be able to go through all of the steps in this guide. The first step is to ensure that your data follows the same schema (or structure) of the sample datasets that are currently powering the app. Fortunately, Domo has created some powerful data transformation tools to help, along with the step-by-step instructions provided below.</p>
<h3 class="doc-row-title">Prerequisites:</h3>
<p>To speed up the connection process for your data, this&nbsp;app utilizes Domo’s Grid Builder. If you are not already familiar with Grid Builder,&nbsp;please visit our&nbsp;<a href="http://player.ooyala.com/iframe.html?ec=xiY3hrNDE66fk814mw5EG4qPCAooAOGl&amp;pbid=b986320eb2af428485644819b233d43c" target="_blank">Grid Builder Training</a>.</p>
<p>Below is a diagram that shows the order in which&nbsp;the customer data will be fed through and output to the App.</p>
<p><img loading="lazy" class="alignnone wp-image-2587" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/07/22155201/data-flow-organization.png" alt="data flow organization" width="1284" height="359" srcset="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/07/22155201/data-flow-organization.png 2683w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/07/22155201/data-flow-organization-300x84.png 300w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/07/22155201/data-flow-organization-768x215.png 768w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/07/22155201/data-flow-organization-1024x286.png 1024w" sizes="(max-width: 1284px) 100vw, 1284px"></p>
<p>Please note that in order to create the most useful app possible, it is necessary to start by defining the final metrics the customer wants in their app and then work backwards to fill out the Grid Builder webform we will create.</p>
<div id="Step%201:%20Identify%20Required%20Data%20Fields" class="doc-row">
<h3 class="doc-row-title">Step 1:&nbsp;Define Your Metrics</h3>
<p>You will start by defining the metrics that you want to show up in the app. We have created a powerful tool to help you do this.</p>
<p>Users will need to navigate to their&nbsp;Data Center and follow the steps below:</p>
<ul>
<li>Navigate to or create a webform called “Sales Scorecard – Metrics”.</li>
<li>If it exists, delete all info in the columns – your form will be structured differently than the sample data considering the metrics should point to your field names and not sample ones.</li>
<li>Choose what metrics you have in your existing data that you want this app to display for you.</li>
<li>In the app, clicking the Metric Editor button – shown below circled in red – displays which metrics are currently visible in the app. Up to 7 metrics are visible at a time.</li>
</ul>
<p><img loading="lazy" class="alignnone size-full wp-image-2646" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/10143120/SScorecard1.png" alt="SScorecard1" width="1197" height="759" srcset="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/10143120/SScorecard1.png 1197w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/10143120/SScorecard1-300x190.png 300w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/10143120/SScorecard1-768x487.png 768w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/10143120/SScorecard1-1024x649.png 1024w" sizes="(max-width: 1197px) 100vw, 1197px"></p>
<ul>
<li>Editing the Name and Calculation columns will change&nbsp;what you see on the main page of the app and in the Metric Editor&nbsp;menu.</li>
<li>The “Calculation” column contains calculations with field names that correlate to&nbsp;field names in your existing data.</li>
<li>You will need to ensure that you already have each of these data fields imported into your&nbsp;Data Center&nbsp;before you&nbsp;map out this&nbsp;existing data to the Metrics&nbsp;webform.</li>
<li>Edit the Metrics webform columns according to the guidelines below:</li>
</ul>
<table width="581">
<tbody>
<tr>
<td width="168"><strong>Field Name</strong></td>
<td width="413"><strong>Instructions To Fill Out Associated Field</strong></td>
</tr>
<tr>
<td width="168">Name</td>
<td width="413">How the metric should be called in the app</td>
</tr>
<tr>
<td>Calculation</td>
<td width="413">The calculation of the app according to “The Grid” datasource. This section supports SUM, MAX, MIN, AVG, DISTINCT, UNIQUE as well as basic +,-,/,* between these functions. Integers are not supported.<p></p>
<p>Whatever fields you use in your calculations&nbsp;must&nbsp;later be entered into your Grid Builder “AS” column and labeled exactly as they are in your Scorecard Metrics “Calculation” column.</p></td>
</tr>
<tr>
<td>DataType</td>
<td width="413">“Currency”, “Percent” or “Number”</td>
</tr>
<tr>
<td>SortHighToLow</td>
<td width="413">True or False</td>
</tr>
<tr>
<td>UnitOfMeasurement</td>
<td width="413">The name of the metric units if the metric calls for it.</td>
</tr>
<tr>
<td>Description</td>
<td width="413">Description of the metric&nbsp;so the end user understands it</td>
</tr>
<tr>
<td>Bookmarks</td>
<td width="413">The comma separated list of bookmarks that this metric&nbsp;should be a part of. Do not put a space after the comma.</td>
</tr>
<tr>
<td>Decimal</td>
<td>The integer number of places&nbsp;to be included after the decimal point</td>
</tr>
<tr>
<td>IsDetail</td>
<td>True or False. When “True” this metric will appear as a detail when an individual data point is clicked on.</td>
</tr>
<tr>
<td>DetailType</td>
<td>Indicates what kind of chart the detail will be displayed as. This section supports “Single-value”, “Pie”, “Line”, “Text”,&nbsp;“Currency”, “Percent” or “Number”</td>
</tr>
<tr>
<td>DetailGroup</td>
<td><em>Leave blank unless you need a pie chart or line chart to appear in the detail pane</em></td>
</tr>
<tr>
<td>DetailItem</td>
<td><em><em>Leave blank unless you need a pie chart or line chart to appear in the detail pane.&nbsp;</em></em>This section supports GROUP_BY(metricName), DATE_GRAIN(metricName)</td>
</tr>
<tr>
<td>DetailValue</td>
<td>The calculation of the associated detail. This section supports SUM, MAX, MIN, AVG, DISTINCT, UNIQUE as well as basic +,-,/,* between these functions.</td>
</tr>
<tr>
<td>DetailDimensions</td>
<td>Comma separate list of dimensions whereon this detail item should appear in the detail list. A dimension is the same as the ‘FilterName’ in the grid builder for the ‘IsPrimaryFilter’ and ‘IsPrimaryFilterGroup’ fields.</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<p>Please bear in mind that the example provided <em>may differ significantly from your own data structure</em> within the Metric webform. The following is an example of what your completed webform might look like:</p>
<p><img loading="lazy" class="alignnone size-full wp-image-2647" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/10143148/SScorecard3.png" alt="SScorecard3" width="1921" height="467" srcset="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/10143148/SScorecard3.png 1921w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/10143148/SScorecard3-300x73.png 300w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/10143148/SScorecard3-768x187.png 768w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/10143148/SScorecard3-1024x249.png 1024w" sizes="(max-width: 1921px) 100vw, 1921px"></p>
<h3 class="doc-row-title"></h3>
<h3 class="doc-row-title">Step 2: Prepare Your Data</h3>
<div class="small-pad-bottom">
<p>This app requires creating a custom dataset named “Sales Scorecard – Grid Builder” which may not have been created when you downloaded this app.</p>
<p>&nbsp;</p>
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
<li>Title the new data set “Sales Scorecard&nbsp;– Grid Builder”. It MUST&nbsp;contain “- Grid Builder” at the end of the title.</li>
<li>Use the following example table and&nbsp;copy all fields.</li>
<li>IMPORTANT: Due to formatting issues you will first need to paste this into Microsoft Excel or Google Sheets. Then copy from there and paste it into&nbsp;your newly created Grid Builder.</li>
<li>Verify that your Grid Builder is the same as the table below:</li>
</ul>
<table width="2401">
<tbody>
<tr>
<td width="49">GridId</td>
<td width="75">GridName</td>
<td width="213">C</td>
<td width="163">SELECT</td>
<td width="216">FROM</td>
<td width="57">WHERE</td>
<td width="77">GROUP BY</td>
<td width="201">AS</td>
<td width="56">Include</td>
<td width="65">JoinType</td>
<td width="97">JoinCondition</td>
<td width="49">MAJIK</td>
<td width="55">FilterId</td>
<td width="84">FilterName</td>
<td width="77">FilterInputType</td>
<td width="103">FilterIsPrimary</td>
<td width="144">FilterIsPrimaryGroup</td>
<td width="620">Description</td>
</tr>
<tr>
<td>1</td>
<td>Scorecard</td>
<td>kamaji_calendar(1, @DB)</td>
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
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>101</td>
<td>Date</td>
<td>KAMAJI Calendar</td>
<td></td>
<td></td>
<td>Date</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>102</td>
<td>ThisYear</td>
<td></td>
<td></td>
<td></td>
<td>This Fiscal Year</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td>1</td>
<td>Date Range</td>
<td>Single Select</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>103</td>
<td>LastYear</td>
<td></td>
<td></td>
<td></td>
<td>Last Fiscal Year</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>104</td>
<td>ThisQuarter</td>
<td></td>
<td></td>
<td></td>
<td>This Fiscal Quarter</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>105</td>
<td>LastQuarter</td>
<td></td>
<td></td>
<td></td>
<td>Last Fiscal Quarter</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>106</td>
<td>ThisMonth</td>
<td></td>
<td></td>
<td></td>
<td>This Fiscal Month</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>107</td>
<td>LastMonth</td>
<td></td>
<td></td>
<td></td>
<td>Last Fiscal Month</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>108</td>
<td>FMStartDate</td>
<td></td>
<td></td>
<td></td>
<td>FMStartDate</td>
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
</tr>
<tr>
<td></td>
<td></td>
<td>201</td>
<td>&lt;‘OptionalField.1’&gt;</td>
<td>&lt;‘YourDataSetNameHere.1’&gt;</td>
<td></td>
<td></td>
<td>Rep</td>
<td>1</td>
<td>INNER</td>
<td>C101 = C205</td>
<td></td>
<td>2</td>
<td>Rep</td>
<td>Multi Select</td>
<td>1</td>
<td></td>
<td>STRING – Name of agent</td>
</tr>
<tr>
<td></td>
<td></td>
<td>202</td>
<td>&lt;‘OptionalField.2’&gt;</td>
<td></td>
<td></td>
<td></td>
<td>Team</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td>3</td>
<td>Team</td>
<td>Multi Select</td>
<td></td>
<td>1</td>
<td>STRING – Specialty of associated agent</td>
</tr>
<tr>
<td></td>
<td></td>
<td>203</td>
<td>&lt;‘OptionalField.3’&gt;</td>
<td></td>
<td></td>
<td></td>
<td>Region</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td>4</td>
<td>Region</td>
<td>Multi Select</td>
<td></td>
<td>2</td>
<td>STRING – Team of associated agent</td>
</tr>
<tr>
<td></td>
<td></td>
<td>204</td>
<td>&lt;‘OptionalField.4’&gt;</td>
<td></td>
<td></td>
<td></td>
<td>Role</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td>5</td>
<td>Role</td>
<td>Multi Select</td>
<td></td>
<td></td>
<td>STRING – Role&nbsp;of associated agent</td>
</tr>
<tr>
<td></td>
<td></td>
<td>205</td>
<td>&lt;‘REQUIREDField.5’&gt;</td>
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
<td>DATE – Date the agent was working</td>
</tr>
<tr>
<td></td>
<td></td>
<td>206</td>
<td>&lt;‘OptionalField.6’&gt;</td>
<td></td>
<td></td>
<td></td>
<td>Gross_Sales</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Example: DECIMAL –&nbsp;Rep’s Gross Sales</td>
</tr>
<tr>
<td></td>
<td></td>
<td>207</td>
<td>&lt;‘OptionalField.7’&gt;</td>
<td></td>
<td></td>
<td></td>
<td>Net_Sales</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Example: DECIMAL – Rep’s Net Sales</td>
</tr>
<tr>
<td></td>
<td></td>
<td>208</td>
<td>&lt;‘OptionalField.8’&gt;</td>
<td></td>
<td></td>
<td></td>
<td>New_Clients</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Example: DECIMAL – Number of new clients</td>
</tr>
<tr>
<td></td>
<td></td>
<td>209</td>
<td>&lt;‘OptionalField.9’&gt;</td>
<td></td>
<td></td>
<td></td>
<td>Avg_Deal_Size</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Example: DECIMAL&nbsp;–&nbsp;Average deal size</td>
</tr>
<tr>
<td></td>
<td></td>
<td>210</td>
<td>&lt;‘OptionalField.10’&gt;</td>
<td></td>
<td></td>
<td></td>
<td>Quota_Attainment</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Example: DECIMAL –&nbsp;Rep’s Quota Attainment</td>
</tr>
<tr>
<td></td>
<td></td>
<td>211</td>
<td>&lt;‘OptionalField.11’&gt;</td>
<td></td>
<td></td>
<td></td>
<td>Upsell_Count</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Example: DECIMAL –&nbsp;Number of Upsells</td>
</tr>
<tr>
<td></td>
<td></td>
<td>212</td>
<td>&lt;‘OptionalField.12’&gt;</td>
<td></td>
<td></td>
<td></td>
<td>Renewall_Count</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Example: DECIMAL –&nbsp;Number of Renewalls</td>
</tr>
<tr>
<td></td>
<td></td>
<td>213</td>
<td>&lt;‘OptionalField.13’&gt;</td>
<td></td>
<td></td>
<td></td>
<td>Product_Sales</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Example: DECIMAL –&nbsp;Rep’s product sales</td>
</tr>
<tr>
<td></td>
<td></td>
<td>214</td>
<td>&lt;‘OptionalField.14’&gt;</td>
<td></td>
<td></td>
<td></td>
<td>Leads</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Example: DECIMAL –&nbsp;Number of Leads</td>
</tr>
<tr>
<td></td>
<td></td>
<td>215</td>
<td>&lt;‘REQUIREDField.15’&gt;</td>
<td></td>
<td></td>
<td></td>
<td>PhotoUrl</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Example: STRING –&nbsp;URL to Store&nbsp;photo/logo.&nbsp;If you do not have avatar images you wish to use in this app, then set PhotoUrl to an empty string.</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<ul>
<li>You will need to ensure that you already have each of these data fields imported into your&nbsp;Data Center&nbsp;before you&nbsp;map out this&nbsp;existing data to the&nbsp;Grid Builder webform.</li>
<li>Please bear in mind that the example provided <em>may differ significantly from your own data structure</em> within the Grid Builder.</li>
<li>Your Grid Builder my contain as many or as few ‘OptionalFields’ as you would like.</li>
</ul>
<p>&nbsp;</p>
<p><strong>Things to Know About This&nbsp;App:</strong></p>
<ul>
<li>This app requires two fields called “Date” in the AS column. One in the ‘KAMAJI Calendar’ dataset and one in your own data (under “Sales Scorecard – Sample” in the sample data). Without them&nbsp;the app will break.</li>
<li>This app requires a field called “PhotoUrl” which contains a url where avatar images are hosted publicly. If you do not have avatar images you wish to use in this app, then set PhotoUrl to an empty string.</li>
<li>We recommend you do not alter&nbsp;rows 2 – 9 from the Kamaji Calendar dataset. Doing so will may cause unexpected results unless you are intimately familiar with this dataset that Domo provides.</li>
<li>Starting with row 10, Fill&nbsp;out the ‘SELECT’ column with the field names as they&nbsp;appear in your data set.</li>
<li>Fill out the ‘FROM’ column with the name of the data set.</li>
<li>Fill out the ‘WHERE’ and ‘GROUP BY’ columns as needed.</li>
<li>Fill out the ‘AS’ column to contain the field names you wish to use in the app metrics or filters.
<ul>
<li>You must include every field that you used&nbsp;in the “Sales Scorecard – Metrics” webform under the “Calculation” column.</li>
</ul>
</li>
<li>Values in the ‘AS’ column must not contain any spaces, $ or # symbols or the metrics may not calculate properly.</li>
<li>‘FilterInputType’ can be either “Single Select” or “Multi Select”</li>
<li>‘FilterIsPrimary’ should have a “1” for one and only one field. This indicates the core dimension of the app, be it “Sales Rep”, “Store”, or “Helpdesk Agent” for example.</li>
<li>Custom Date Filters: To create a custom date filter, add a row to the KAMAJI Calendar section and place a CASE statement under the SELECT column. Name your custom date filter in the AS column.&nbsp;For the CASE statement, it needs to be written to select 1 for the days you want to include and 0 for the ones that you don’t. &nbsp;Ex: CASE WHEN month(curdate()) = month(`Date`) AND `Date` &lt; curdate() THEN 1 ELSE 0 END – This would be a Month to Date Filter.</li>
</ul>
<p>For additional help with Grid Builder please visit our&nbsp;<a href="http://player.ooyala.com/iframe.html?ec=xiY3hrNDE66fk814mw5EG4qPCAooAOGl&amp;pbid=b986320eb2af428485644819b233d43c" target="_blank">Grid Builder Training</a>.</p>
</div>
</div>
<p></p><div class="doc-row" id="Step%203:%20Connect%20Your%20Data">
                                    <h3 class="doc-row-title">Step 3: Connect Your Data</h3><div class="small-pad-bottom"><p>Once you have finished preparing your data as outlined in Steps 1 and 2 you are ready to connect it to your app.</p>
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
<li>Name the new DataFlow “Sales Scorecard”.</li>
<li>Under “Input DataSets” add&nbsp;your newly populated Grid Builder called “Sales Scorecard – Grid Builder”.</li>
<li>Add any datasets referenced in the “FROM” column in your Grid Builder.</li>
<li>Add the dataset called “Sales Scorecard – Settings” which came with your app.</li>
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
<p><a href="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/09/30131952/Scorecard.txt">Scorecard</a></p>
<ul>
<li>Notes: Be careful what you replace. You should only be replacing the information for the dummy transform we created between the two curly braces “{” and “}”. Do not erase the bracket “]” at the end.</li>
<li>Click “Apply Source” to save.</li>
<li>You should see the DataFlow populated with transforms and and output datasets.</li>
</ul>
<p>&nbsp;</p>
<ul>
<li>Check the boxes so that the dataflow will run when any of the input datasets is updated.</li>
<li>Save and run the DataFlow.</li>
<li>Once the DataFlow finishes running, compare&nbsp;your new output datasets to the sample datasets the original app was connected to and verify their&nbsp;formats match.</li>
<li>Go to the app, click the wrench icon in the upper right corner and select “Edit Card”.</li>
</ul>
<p><img loading="lazy" class="alignnone wp-image-2556" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/12141309/Change-AppData-1.png" alt="Change AppData 1" width="309" height="326" srcset="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/12141309/Change-AppData-1.png 623w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/12141309/Change-AppData-1-285x300.png 285w" sizes="(max-width: 309px) 100vw, 309px"></p>
<ul>
<li>Scroll down to the bottom of the page. You will find a list of grayed-out datasets the app uses to power itself.</li>
<li>Click each dataset and click the down-arrow to search for and swap out the sample datasets for the datasets newly created by your DataFlow.</li>
<li>The FINAL tab is where you will connect your “Sales Scorecard – Data” output table.</li>
<li>NOTE – Your app datasets may be named differently than the example found below:</li>
</ul>
<p><img loading="lazy" class="alignnone wp-image-2557" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/12143231/Change-AppData-2.png" alt="Change AppData 2" width="585" height="427" srcset="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/12143231/Change-AppData-2.png 890w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/12143231/Change-AppData-2-300x219.png 300w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/12143231/Change-AppData-2-768x561.png 768w" sizes="(max-width: 585px) 100vw, 585px"></p>
<ul>
<li>Once you have done this for each dataset, you may move to Step 4.</li>
</ul>
<p><script>// <![CDATA[
OO.ready(function() { OO.Player.create("ooyalaplayer-IyYTc1MjE61NwLdtrxXvZuhH-dSGbWnR", "IyYTc1MjE61NwLdtrxXvZuhH-dSGbWnR", { height: 380 }); });
// ]]&gt;</script></p>
</div></div><div class="doc-row" id="Step%204:%20[OPTIONAL]%20Adjusting%20the%20Filters">
                                    <h3 class="doc-row-title">Step 4: [OPTIONAL] Adjusting the Filters</h3><div class="small-pad-bottom"><br>
                                    <p>Users may want to visualize their app&nbsp;in different ways&nbsp;(i.e. maybe only view reps&nbsp;in a certain region, or a handful of reps).</p>
<p>In order to do this,&nbsp;users will need to follow the steps below:</p>
<ul>
<li>Navigate to&nbsp;the “Sales Scorecard – Grid Builder” webform for this app.</li>
<li>Edit the “FilterId”, “FilterName”, “FilterInputType”, “FilterIsPrimary”, and “FilterIsPrimaryGroup” columns.</li>
<li>Note: In some situations, not all filter columns are required to be populated.</li>
</ul>
<p>Some common filters for this app include:</p>
<ul>
<li>Rows 3-8 – Date Range, Single Select – IT IS HIGHLY RECOMMENDED THAT YOU LEAVE THIS FILTER HERE.</li>
<li>Row 10 – Rep, Multi Select</li>
<li>Row 11 – Team, Multi Select</li>
<li>Row 12 – Region, Multi Select</li>
<li>Row 13 – Role, Multi Select</li>
</ul>
<p><img loading="lazy" class="alignnone size-full wp-image-2648" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/10143648/SScorecard2.png" alt="SScorecard2" width="726" height="451" srcset="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/10143648/SScorecard2.png 726w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/10143648/SScorecard2-300x186.png 300w" sizes="(max-width: 726px) 100vw, 726px"></p>
<p>&nbsp;</p>
<p>Note that all app content adjusts to whatever new filters the customer chooses to add, including the date grains within the app and the chart titles, where applicable.</p>
<p>Any edits that don’t meet&nbsp;the Grid Builder requirements&nbsp;could result in undesired results.</p>
<p>&nbsp;</p>
<div class="small-pad-bottom"></div>
</div></div><div class="doc-row" id="Step%204:%20[OPTIONAL]%20Adjusting%20the%20Settings">
                                    <h3 class="doc-row-title">Step 5: [OPTIONAL] Adjusting the Settings</h3><div class="small-pad-bottom"><br>
                                    <p>Users may want to edit some of the settings for this app.</p>
<p>In order to do this,&nbsp;users will need to follow the steps below:</p>
<ul>
<li>Navigate to the “Sales Scorecard – Settings” which is a webform that came with this app.</li>
<li>Open this dataset and edit its contents as desired.</li>
</ul>
<p>Some common settings that customers change for this app include:</p>
<ul>
<li>Changing fiscal quarter start dates</li>
<li>App Header text</li>
</ul>
<p>&nbsp;</p>
<h3 class="doc-row-title">Additional help</h3>
<div class="small-pad-bottom">
<p>Need additional assistance? Visit the&nbsp;<a href="https://dojo.domo.com/apps">Domo Community</a>.</p>
</div>
</div></div>            </div>
