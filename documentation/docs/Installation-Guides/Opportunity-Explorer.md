---
stoplight-id: sqjtafoz4h66v
---

<div class="col-md-12 content-panel">
                <h2>Opportunity Explorer</h2>
                <p></p><p>Thanks for installing, test-driving, and purchasing Opportunity Explorer! This guide is intended to help you connect this app to your own data. If you have completed the purchasing process for this app then you will be able to go through all of the steps in this guide.</p>
<h3 class="doc-row-title">Prerequisites:</h3>
<p>To speed up the connection process for your data, this&nbsp;app utilizes Domo’s Grid Builder. If you are not already familiar with Grid Builder,&nbsp;please visit our&nbsp;<a href="http://player.ooyala.com/iframe.html?ec=xiY3hrNDE66fk814mw5EG4qPCAooAOGl&amp;pbid=b986320eb2af428485644819b233d43c" target="_blank">Grid Builder Training</a>.</p>
<p>Though not required – if your customer uses Salesforce, generating the input datasets for the app will be easier.</p>
<div id="Step%201:%20Identify%20Required%20Data%20Fields" class="doc-row">
<h3 class="doc-row-title">Step 1: Prepare Your Data</h3>
<div class="small-pad-bottom">
<p>This app requires creating&nbsp;a custom dataset named “Opportunity Explorer – Grid Builder”.</p>
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
<li>Title the new dataset “Opportunity Explorer – Grid Builder”.</li>
<li>Follow these steps to copy all fields in the example table below and insert it into your Grid Builder:
<ul>
<li>Select and copy the table found below.</li>
<li>Paste this into&nbsp;Microsoft Excel or Google Sheets.</li>
<li>Copy from there.</li>
<li>Paste into your newly created Grid Builder.</li>
</ul>
</li>
<li>Verify that your Grid Builder is formatted exactly the same as the table below:</li>
</ul>
<table width="1853">
<tbody>
<tr>
<td width="85">GridId</td>
<td width="87">GridName</td>
<td width="87">C</td>
<td width="171">SELECT</td>
<td width="87">FROM</td>
<td width="87">WHERE</td>
<td width="87">GROUP BY</td>
<td width="87">AS</td>
<td width="87">Include</td>
<td width="87">JoinType</td>
<td width="87">JoinCondition</td>
<td width="87">MAJIK</td>
<td width="87">FilterId</td>
<td width="87">FilterName</td>
<td width="87">FilterInputType</td>
<td width="87">FilterIsPrimary</td>
<td width="87">FilterIsPrimaryGroup</td>
<td width="292">Description</td>
</tr>
<tr>
<td>1</td>
<td>Opportunity</td>
<td>100</td>
<td>Amount</td>
<td>Opportunity</td>
<td></td>
<td></td>
<td>Amount</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>DECIMAL: Value of Opportunity</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>CloseDate</td>
<td></td>
<td></td>
<td></td>
<td>CloseDate</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>DATE: Opportunity Close Date</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Competition</td>
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
<td></td>
<td>CreatedDate</td>
<td></td>
<td></td>
<td></td>
<td>CreatedDate</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>DATE: Opportunity Created Date</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>Id</td>
<td></td>
<td></td>
<td></td>
<td>Id</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>DECIMAL: Opportunity ID</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>Name</td>
<td></td>
<td></td>
<td></td>
<td>Name</td>
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
<td></td>
<td>IsClosed</td>
<td></td>
<td></td>
<td></td>
<td>IsClosed</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>BOOLEAN: Is the opportunity closed, true or false.</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>IsWon</td>
<td></td>
<td></td>
<td></td>
<td>IsWon</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>BOOLEAN: Is the opportunity won, true or false.</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>LastActivityDate</td>
<td></td>
<td></td>
<td></td>
<td>LastActivityDate</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>DATE: Date of last activity</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>LastModifiedDate</td>
<td></td>
<td></td>
<td></td>
<td>LastModifiedDate</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>DATE: Date last modified</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>NextStep</td>
<td></td>
<td></td>
<td></td>
<td>Notes</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>STRING: Notes or Next Step</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>Probability</td>
<td></td>
<td></td>
<td></td>
<td>Probability</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>DECIMAL:&nbsp; Win Probability</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>StageName</td>
<td></td>
<td></td>
<td></td>
<td>StageName</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td>3</td>
<td>Stage Name</td>
<td>Multi Select</td>
<td></td>
<td></td>
<td>STRING: Name of pipeline stage</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>Type</td>
<td></td>
<td></td>
<td></td>
<td>Type</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>STRING: Opportunity Type</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td colspan="4">CONCAT(‘https://&lt;yourdomainname&gt;.salesforce.com/’, Id)</td>
<td>URL</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>STRING: URL for User page</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>ForecastCategory</td>
<td></td>
<td></td>
<td></td>
<td>ForecastCategory</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>STRING: Forecast Category</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>StrategicAccount</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>STRING: Stategic Account</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>Amount</td>
<td></td>
<td></td>
<td></td>
<td>ForecastedACV</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>DECIMAL: Forecasted Amount</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>NextStep</td>
<td></td>
<td></td>
<td></td>
<td>NextSteps</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>STRING: Next Steps to take</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>OwnerId</td>
<td></td>
<td></td>
<td></td>
<td>OwnerId</td>
<td>0</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>DECIMAL: Owner ID Number</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>AccountId</td>
<td></td>
<td></td>
<td></td>
<td>AccountId</td>
<td>0</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>DECIMAL: Account ID</td>
</tr>
<tr>
<td></td>
<td></td>
<td>200</td>
<td>FullPhotoUrl</td>
<td>User</td>
<td></td>
<td></td>
<td>OwnerPhotoUrl</td>
<td>1</td>
<td>LEFT</td>
<td colspan="2">C200.Id = C100.OwnerId</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>STRING: URL for user image</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>Name</td>
<td></td>
<td></td>
<td></td>
<td>OwnerName</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>STRING: Owner Name</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>Email</td>
<td></td>
<td></td>
<td></td>
<td>OwnerEmail</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>STRING: Owner E-mail</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>Id</td>
<td></td>
<td></td>
<td></td>
<td>Id</td>
<td>0</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>DECIMAL: Owner ID Number</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>UserRoleId</td>
<td></td>
<td></td>
<td></td>
<td>UserRoleId</td>
<td>0</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>DECIMAL: Owner Role ID Number</td>
</tr>
<tr>
<td></td>
<td></td>
<td>300</td>
<td>Name</td>
<td>User Role</td>
<td></td>
<td></td>
<td>OwnerManager</td>
<td>1</td>
<td>LEFT</td>
<td colspan="2">C300.Id = C200.UserRoleId</td>
<td>2</td>
<td>Role</td>
<td>Single Select</td>
<td></td>
<td></td>
<td>STRING: Owner Roll Name</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>Id</td>
<td></td>
<td></td>
<td></td>
<td>Id</td>
<td>0</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>DECIMAL: Owner ID Number</td>
</tr>
<tr>
<td></td>
<td></td>
<td>400</td>
<td>Id</td>
<td>Account</td>
<td></td>
<td></td>
<td>AccountId</td>
<td>1</td>
<td>LEFT</td>
<td colspan="3">C400.AccountId = C100.AccountId</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>DECIMAL: Account ID</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>Industry</td>
<td></td>
<td></td>
<td></td>
<td>AccountIndustry</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td>1</td>
<td>Account Industry</td>
<td>Multi Select</td>
<td></td>
<td></td>
<td>STRING: Account Industry</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>Name</td>
<td></td>
<td></td>
<td></td>
<td>AccountName</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>STRING: Account Name</td>
</tr>
</tbody>
</table>
</div>
</div>
<div id="Step%201:%20Identify%20Required%20Data%20Fields" class="doc-row">
<div class="small-pad-bottom">
<ul>
<li>Ensure that you already have each of these data fields imported into your&nbsp;Data Center&nbsp;before you&nbsp;map out this&nbsp;existing data to the&nbsp;Grid Builder webform.</li>
<li>The example provided <em>may differ significantly from your own data structure</em> within the Grid Builder.</li>
</ul>
<p>&nbsp;</p>
<p><strong>Things to Know About This&nbsp;App:</strong></p>
<ul>
<li>Important Note: Do not change any values in the ‘AS’ column. Doing so will cause your data to display incorrectly or not at all.</li>
<li>Starting with row 1, fill&nbsp;out the ‘SELECT’ column with the field names exactly as they&nbsp;appear in your dataset. In the table above, examples are listed of what your field names might look like. Change them to match your dataset exactly.</li>
<li>Fill out the ‘FROM’ column with the name of the dataset exactly as it appears in your data center.</li>
<li>Fill out the ‘WHERE’ and ‘GROUP BY’ columns as needed.</li>
</ul>
<h2>STEP 1.5: Build Additional Datasets</h2>
<p>A handful of supplemental datasets need to be included in order for the app’s dataflow to function. Follow these steps to add the five following datasets:</p>
<ul>
<li>Create a Domo-Webform dataset as seen above.</li>
<li>Name the first one “Opportunity Explorer – Settings”.</li>
<li>Copy the following table into the webform and save it:</li>
</ul>
<table width="763">
<tbody>
<tr>
<td width="180">Name</td>
<td width="87">Value</td>
<td width="496">Description</td>
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
<td>Work Week Start Day</td>
<td>1</td>
<td>The day your company’s work week begins (1 = Mon, 2 = Tues, etc).</td>
</tr>
</tbody>
</table>
</div>
<ul>
<li>After this dataset is saved create another and name it “Opportunity Explorer – Default Groups”.</li>
<li>Copy the following table into the webform and save it:</li>
</ul>
<table width="693">
<tbody>
<tr>
<td width="47">ID</td>
<td width="336">Name</td>
<td width="116">AggregateKey</td>
<td width="52">Limit</td>
<td width="55">Order</td>
<td width="87">Present</td>
</tr>
<tr>
<td>1</td>
<td>Next # opptys closing</td>
<td>Amount</td>
<td>25</td>
<td>1</td>
<td>TRUE</td>
</tr>
<tr>
<td>2</td>
<td>Last # deals closed</td>
<td>Amount</td>
<td>25</td>
<td>2</td>
<td>TRUE</td>
</tr>
<tr>
<td>3</td>
<td>Opptys closing</td>
<td>Amount</td>
<td></td>
<td>4</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Neglected opptys (no activity past 30 days) closing</td>
<td>Amount</td>
<td></td>
<td>6</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>Biggest # deals closed</td>
<td>Amount</td>
<td>25</td>
<td>3</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>Strategic opptys</td>
<td>Amount</td>
<td></td>
<td>5</td>
<td></td>
</tr>
</tbody>
</table>
<div class="small-pad-bottom"></div>
<div class="small-pad-bottom">
<ul>
<li>The third dataset you need to create should be named “Opportunity Explorer – Default Conditions”.</li>
<li>Create a new webform, copy the following table into it, and save the dataset:</li>
</ul>
<table width="387">
<tbody>
<tr>
<td width="84">GroupID</td>
<td width="135">Key</td>
<td width="116">Type</td>
<td width="52">Value</td>
</tr>
<tr>
<td>1</td>
<td>IsClosed</td>
<td>equals</td>
<td>FALSE</td>
</tr>
<tr>
<td>1</td>
<td>ForecastCategory</td>
<td>not equal</td>
<td>Closed</td>
</tr>
<tr>
<td>1</td>
<td>Amount</td>
<td>greater than</td>
<td>0</td>
</tr>
<tr>
<td>2</td>
<td>ForecastCategory</td>
<td>equals</td>
<td>Closed</td>
</tr>
<tr>
<td>2</td>
<td>Amount</td>
<td>greater than</td>
<td>0</td>
</tr>
<tr>
<td>3</td>
<td>Amount</td>
<td>greater than</td>
<td>0</td>
</tr>
<tr>
<td>4</td>
<td>IsClosed</td>
<td>equals</td>
<td>FALSE</td>
</tr>
<tr>
<td>4</td>
<td>DaysNeglected</td>
<td>greater than</td>
<td>30</td>
</tr>
<tr>
<td>4</td>
<td>ForecastCategory</td>
<td>not equal</td>
<td>Closed</td>
</tr>
<tr>
<td>4</td>
<td>Amount</td>
<td>greater than</td>
<td>0</td>
</tr>
<tr>
<td>5</td>
<td>Amount</td>
<td>greater than</td>
<td>0</td>
</tr>
<tr>
<td>5</td>
<td>ForecastCategory</td>
<td>equals</td>
<td>Closed</td>
</tr>
</tbody>
</table>
</div>
<ul>
<li>Name the fourth dataset “Opportunity Explorer – Highlights”.</li>
<li>Copy the following table into the webform and save the dataset:</li>
</ul>
<table width="384">
<tbody>
<tr>
<td width="140">FieldName</td>
<td width="71">Value</td>
<td width="69">Order</td>
<td width="104">DisplayName</td>
</tr>
<tr>
<td>ForecastCategory</td>
<td>Omitted</td>
<td>0</td>
<td>Omitted</td>
</tr>
<tr>
<td>ForecastCategory</td>
<td>Pipeline</td>
<td>1</td>
<td>Pipeline</td>
</tr>
<tr>
<td>ForecastCategory</td>
<td>Closed</td>
<td>2</td>
<td>Closed</td>
</tr>
</tbody>
</table>
<ul>
<li>Name the final dataset “Opportunity Explorer – Default Order”.</li>
<li>Copy the following table into the webform and save the dataset:</li>
</ul>
<table width="442">
<tbody>
<tr>
<td width="84">GroupID</td>
<td width="135">Key</td>
<td width="116">Value</td>
<td colspan="2" width="107">KeyName</td>
</tr>
<tr>
<td>1</td>
<td>CloseDate</td>
<td>asc</td>
<td colspan="2">Close Date</td>
</tr>
<tr>
<td>2</td>
<td>CloseDate</td>
<td>desc</td>
<td colspan="2">Close Date</td>
</tr>
<tr>
<td>3</td>
<td>CloseDate</td>
<td>asc</td>
<td colspan="2">Close Date</td>
</tr>
<tr>
<td>4</td>
<td>DaysNeglected</td>
<td>desc</td>
<td colspan="2">Days Neglected</td>
</tr>
<tr>
<td>5</td>
<td>Amount</td>
<td>desc</td>
<td colspan="2">Amount</td>
</tr>
<tr>
<td>6</td>
<td>CloseDate</td>
<td>asc</td>
<td colspan="2">Close Date</td>
</tr>
</tbody>
</table>
<div class="small-pad-bottom"></div>
<p>After you have created all of these datasets, you may&nbsp;move on to step 2.</p>
<div class="small-pad-bottom">
<p>For additional help with Grid Builder please visit our&nbsp;<a href="http://player.ooyala.com/iframe.html?ec=xiY3hrNDE66fk814mw5EG4qPCAooAOGl&amp;pbid=b986320eb2af428485644819b233d43c" target="_blank">Grid Builder Training</a>.</p>
</div>
</div>
<p></p><div class="doc-row" id="Step%202:%20Connect%20Your%20Data">
                                    <h3 class="doc-row-title">Step 2: Connect Your Data</h3><div class="small-pad-bottom"><p>Once you have finished preparing your data as outlined in Step 1 you are ready to connect it to your app.</p>
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
<li>Name the new DataFlow “Opportunity Explorer”.</li>
<li>Under “Input DataSets” add&nbsp;your newly populated Grid Builder called “Opportunity Explorer – Grid Builder”.</li>
<li>Add any datasets referenced by your Grid Builder.</li>
<li>Add the datasets called “Opportunity Explorer – Settings”, &nbsp;“Opportunity Explorer – Default Groups”, “Opportunity Explorer – Default Conditions”, and”Opportunity Explorer – Default Order” which you created in step 1.5.</li>
<li>We will use the “Opportunity Explorer – Highlights” dataset later to power up the app, don’t include it here.</li>
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
<p><a href="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/09/30131339/OpportunityExplorer.txt">OpportunityExplorer</a></p>
<ul>
<li>Notes: Be careful what you replace. You should only be replacing the information for the dummy transform we created between the two curly braces “{” and “}”. Do not erase the bracket “]” at the end.</li>
<li>Click “Apply Source” to save.</li>
<li>You should see the DataFlow populated with transforms and and output datasets.</li>
</ul>
<ul>
<li>Save and run the DataFlow.</li>
<li>Once the DataFlow finishes running, compare&nbsp;your new output datasets to the sample datasets the original app was connected to and verify their&nbsp;formats match.</li>
<li>Go to the app, click the wrench icon in the upper right corner and select “Edit Card”.</li>
</ul>
<p><img loading="lazy" class="alignnone wp-image-2556" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/12141309/Change-AppData-1.png" alt="Change AppData 1" width="309" height="326" srcset="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/12141309/Change-AppData-1.png 623w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/12141309/Change-AppData-1-285x300.png 285w" sizes="(max-width: 309px) 100vw, 309px"></p>
<ul>
<li>Scroll down to the bottom of the page. You will find a list of grayed-out datasets the app uses to power itself.</li>
<li>Click each dataset and click the down-arrow to search for and swap out the sample datasets for the datasets newly created by your DataFlow.</li>
<li>Connect the four appropriate datasets that the DataFlow generated and that you created; Default Groups, Highlights, Opportunities – Under the “Sales” tab, and&nbsp;Filters</li>
<li>NOTE – Your app datasets may be named differently than the example found below:</li>
</ul>
<p><img loading="lazy" class="alignnone size-full wp-image-2661" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/11133627/OpportunityExplorerScreen1.png" alt="OpportunityExplorerScreen1" width="439" height="413" srcset="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/11133627/OpportunityExplorerScreen1.png 439w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/11133627/OpportunityExplorerScreen1-300x282.png 300w" sizes="(max-width: 439px) 100vw, 439px"></p>
<ul>
<li>Once you have done this for each dataset, you may move to Step 3.</li>
</ul>
<p><script>// <![CDATA[
OO.ready(function() { OO.Player.create("ooyalaplayer-IyYTc1MjE61NwLdtrxXvZuhH-dSGbWnR", "IyYTc1MjE61NwLdtrxXvZuhH-dSGbWnR", { height: 380 }); });
// ]]&gt;</script></p>
</div></div><div class="doc-row" id="Step%203:%20[OPTIONAL]%20Adjusting%20the%20Filters">
                                    <h3 class="doc-row-title">Step 3: [OPTIONAL] Adjusting the Filters</h3><div class="small-pad-bottom"><p>Users may want to visualize their app&nbsp;in different ways&nbsp;(i.e. maybe only the last 7 days,&nbsp;or a bigger frame like the last 90 days).</p>
<p>In order to do this,&nbsp;users will need to follow the steps below:</p>
<ul>
<li>Navigate to&nbsp;the “Opportunity Explorer – Grid Builder” webform for this app.</li>
<li>Edit the “FilterId”, “FilterName”, “FilterInputType”, “FilterIsPrimary”, and “FilterIsPrimaryGroup” columns.</li>
<li>Note: In some situations, not all filter columns are required to be populated.</li>
</ul>
<p>Some common filters for this app include:</p>
<ul>
<li>Role, Multi Select</li>
<li>Industry, Multi Select</li>
<li>Stage Name, Multi Select</li>
</ul>
<p>Note that all app content adjusts to whatever new filters the customer chooses to add, including the date grains within the app and the chart titles, where applicable.</p>
<p>Any edits that don’t meet&nbsp;the Grid Builder requirements&nbsp;could result in undesired results.</p>
</div></div><div class="doc-row" id="Step%204:%20[OPTIONAL]%20Adjusting%20the%20Settings">
                                    <h3 class="doc-row-title">Step 4: [OPTIONAL] Adjusting the Settings</h3><div class="small-pad-bottom"><p>Users may want to edit some of the settings for this app.</p>
<p>In order to do this,&nbsp;users will need to follow the steps below:</p>
<ul>
<li>Navigate to the “Opportunity Explorer – Settings” webform for this app.</li>
<li>Open this dataset and edit the “Value” column&nbsp;as desired.</li>
</ul>
<p>Some common settings that customers change for this app include:</p>
<ul>
<li>Fiscal quarter start dates</li>
<li>Work week start day</li>
</ul>
<h3 class="doc-row-title">Additional help</h3>
<div class="small-pad-bottom">
<p>Need additional assistance? Visit the&nbsp;<a href="https://dojo.domo.com/apps">Domo Community</a>.</p>
</div>
</div></div>            </div>