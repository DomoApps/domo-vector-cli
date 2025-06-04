---
stoplight-id: lg90juvy85xd5
---

<div class="col-md-12 content-panel">
                <h2>Sales Leaderboard</h2>
                <p></p><p>Thanks for installing, test-driving, and purchasing Sales Leaderboard! This guide is intended to help you connect this app to your own data. If you have completed the purchasing process for this app then you will be able to go through all of the steps in this guide.</p>
<h3 class="doc-row-title">Prerequisites:</h3>
<p>To speed up the connection process for your data, this&nbsp;app utilizes Domo’s Grid Builder. If you are not already familiar with Grid Builder,&nbsp;please visit our&nbsp;<a href="http://player.ooyala.com/iframe.html?ec=xiY3hrNDE66fk814mw5EG4qPCAooAOGl&amp;pbid=b986320eb2af428485644819b233d43c" target="_blank">Grid Builder Training</a>.</p>
<div id="Step%201:%20Identify%20Required%20Data%20Fields" class="doc-row">
<h3 class="doc-row-title">Step 1: Prepare Your Data</h3>
<div class="small-pad-bottom">
<p>This app requires creating&nbsp;a custom dataset named “Sales Leaderboard&nbsp;– Grid Builder”.</p>
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
<li>Title the new dataset “Sales Leaderboard&nbsp;– Grid Builder”.</li>
<li>Follow these steps to copy all fields in the example table below and insert it into your Grid Builder:
<ul>
<li>Select and copy the table found below.</li>
<li>Paste this into&nbsp;Microsoft Excel or Google Sheets.</li>
<li>Copy from here.</li>
<li>Paste into your newly created Grid Builder.</li>
</ul>
</li>
<li>Verify that your Grid Builder is formatted exactly the same as the table below:</li>
</ul>
<table width="2290">
<tbody>
<tr>
<td width="87">GridId</td>
<td width="87">GridName</td>
<td width="87">C</td>
<td width="137">SELECT</td>
<td width="87">FROM</td>
<td width="87">WHERE</td>
<td width="99">GROUP BY</td>
<td width="120">AS</td>
<td width="87">Include</td>
<td width="87">JoinType</td>
<td width="87">JoinCondition</td>
<td width="87">MAJIK</td>
<td width="87">FilterId</td>
<td width="87">FilterName</td>
<td width="87">FilterInputType</td>
<td width="87">FilterIsPrimary</td>
<td width="87">FilterIsPrimaryGroup</td>
<td width="716">Description</td>
</tr>
<tr>
<td>1</td>
<td>Opportunity</td>
<td>100</td>
<td>Name</td>
<td>Opportunity</td>
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
<td>The name of the account associated with the opportunity.</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>Amount</td>
<td></td>
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
<td>The cash value of the opportunity.</td>
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
<td>The date the opportunity closed or is projected to close.</td>
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
<td>The date the opportunity was created.</td>
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
<td>The value of this field will be ‘true’ if the opportunity has closed and ‘false’ if it has not.</td>
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
<td>The value of this field will be ‘true’ if the opportunity has been won and ‘false’ if it has not.</td>
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
<td>The percent probability that the opportunity will be won.</td>
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
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>The ID of the opportunity owner.</td>
</tr>
<tr>
<td></td>
<td></td>
<td>200</td>
<td>Id</td>
<td>User</td>
<td></td>
<td></td>
<td>UserId</td>
<td></td>
<td>LEFT</td>
<td colspan="3">C200.UserId = C100.OwnerId</td>
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
<td>IsActive</td>
<td></td>
<td></td>
<td></td>
<td>OwnerIsActive</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td>1</td>
<td>IsActive</td>
<td>Multi Select</td>
<td></td>
<td></td>
<td>The value of this field will be ‘true’ if the opportunity owner’s user is active in Salesforce and ‘false’ if it is not.</td>
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
<td>The full name of the opportunity owner.</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>CreatedDate</td>
<td></td>
<td></td>
<td></td>
<td>OwnerCreatedDate</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>The date the owner of the opportunity began their employment.</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>FullPhotoUrl</td>
<td></td>
<td></td>
<td></td>
<td>OwnerPhotoUrl</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>A URL to a photo of the opportunity owner.</td>
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
<td>300</td>
<td>Id</td>
<td>User Role</td>
<td></td>
<td></td>
<td>RoleId</td>
<td></td>
<td>LEFT</td>
<td colspan="3">C300.RoleId = C200.UserRoleId</td>
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
<td>Name</td>
<td></td>
<td></td>
<td></td>
<td>OwnerRole</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td>2</td>
<td>Role</td>
<td>Multi Select</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<ul>
<li>Ensure that you already have each of these data fields imported into your&nbsp;Data Center&nbsp;before you&nbsp;map out this&nbsp;existing data to the&nbsp;Grid Builder webform. In the example above, three Salesforce input datasets are referenced. Make sure the input data has similar fields to what you see in the example above.</li>
</ul>
</div>
</div>
<div id="Step%201:%20Identify%20Required%20Data%20Fields" class="doc-row">
<div class="small-pad-bottom">
<ul>
<li>The example provided <em>may differ significantly from your own data structure</em> within the Grid Builder.</li>
</ul>
<p><strong>Create the settings dataset:</strong></p>
<ul>
<li>We will need to create one more dataset to prepare the data for the app. Use the same process listed above to navigate to the data center an create a new dataset. Name this one “Sales Leaderboard – Settings”.</li>
<li>Copy the table below into the dataset:</li>
</ul>
<table width="944">
<tbody>
<tr>
<td width="212">Name</td>
<td width="69">Value</td>
<td width="663">Description</td>
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
<td>The day your company’s work week begins (1 = Mon, 2 = Tue, etc.)</td>
</tr>
<tr>
<td>Currency Symbol</td>
<td>$</td>
<td>The symbol to be used when displaying currency values ($, ¥, etc.)</td>
</tr>
<tr>
<td>Currency Symbol Placement</td>
<td>Prepend</td>
<td>The placement method of the currency symbol relative to the currency value (Prepend or Append).</td>
</tr>
</tbody>
</table>
<ul>
<li>Save the dataset.</li>
</ul>
</div>
<div class="small-pad-bottom">
<p><strong>Things to Know About This&nbsp;App:</strong></p>
<ul>
<li>Important Note: Do not change any values in the ‘AS’ column. Doing so will cause your data to display incorrectly or not at all.</li>
<li>Starting with row 1, fill&nbsp;out the ‘SELECT’ column with the field names exactly as they&nbsp;appear in your dataset.</li>
<li>Fill out the ‘FROM’ column with the name of the dataset exactly as it appears in your data center.</li>
<li>Fill out the ‘WHERE’ and ‘GROUP BY’ columns as needed.</li>
</ul>
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
<li>Name the new DataFlow “Sales Leaderboard”.</li>
<li>Under “Input DataSets” add&nbsp;your newly populated Grid Builder called “Sales Leaderboard – Grid Builder”.</li>
<li>Add any datasets referenced by your Grid Builder.</li>
<li>Add the dataset called “Sales Leaderboard – Settings” which we created above.</li>
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
<p><a href="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/10/11144929/SalesLeaderboard.txt">SalesLeaderboard</a></p>
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
<li>NOTE – Your app datasets may be named differently than the example found below:</li>
</ul>
<p><img loading="lazy" class="alignnone size-full wp-image-2788" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/10/11145528/Leaderboard-Screen.png" alt="Leaderboard Screen" width="469" height="435" srcset="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/10/11145528/Leaderboard-Screen.png 469w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/10/11145528/Leaderboard-Screen-300x278.png 300w" sizes="(max-width: 469px) 100vw, 469px"></p>
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
<li>Navigate to&nbsp;the “Sales Leaderboard – Grid Builder” webform for this app.</li>
<li>Edit the “FilterId”, “FilterName”, “FilterInputType”, “FilterIsPrimary”, and “FilterIsPrimaryGroup” columns.</li>
<li>Note: In some situations, not all filter columns are required to be populated.</li>
</ul>
<p>Note that all app content adjusts to whatever new filters the customer chooses to add, including the date grains within the app and the chart titles, where applicable.</p>
<p>Any edits that don’t meet&nbsp;the Grid Builder requirements&nbsp;could result in undesired results.</p><br>
</div></div><div class="doc-row" id="Step%204:%20[OPTIONAL]%20Adjusting%20the%20Settings">
                                    <h3 class="doc-row-title">Step 4: [OPTIONAL] Adjusting the Settings</h3><div class="small-pad-bottom"><p>Users may want to edit some of the settings for this app.</p>
<p>In order to do this,&nbsp;users will need to follow the steps below:</p>
<ul>
<li>Navigate to the “Sales Leadboard – Settings” webform for this app.</li>
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
