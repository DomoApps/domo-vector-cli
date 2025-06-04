---
stoplight-id: lpt9ibe7diiov
---

<div class="col-md-12 content-panel">
                <h2>Marketing ROI</h2>
                <p></p><p>Thanks for installing, test-driving, and purchasing Marketing ROI! This guide is intended to help you connect this app to your own data. If you have completed the purchasing process for this app then you will be able to go through all of the steps in this guide.</p>
<h3 class="doc-row-title">Prerequisites:</h3>
<p>To speed up the connection process for your data, this&nbsp;app utilizes Domo’s Grid Builder. If you are not already familiar with Grid Builder,&nbsp;please visit our&nbsp;<a href="http://player.ooyala.com/iframe.html?ec=xiY3hrNDE66fk814mw5EG4qPCAooAOGl&amp;pbid=b986320eb2af428485644819b233d43c" target="_blank">Grid Builder Training</a>.</p>
<p>Though not required – if your customer uses Salesforce, generating the input datasets for the app will be easier.</p>
<div id="Step%201:%20Identify%20Required%20Data%20Fields" class="doc-row">
<h3 class="doc-row-title">Step 1: Prepare Your Data</h3>
<div class="small-pad-bottom">
<p>This app requires creating&nbsp;a custom dataset named “Marketing ROI – Grid Builder”.</p>
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
<li>Title the new dataset “Marketing ROI&nbsp;– Grid Builder”.</li>
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
<table width="1977">
<tbody>
<tr>
<td width="87">GridId</td>
<td width="87">GridName</td>
<td width="87">C</td>
<td width="144">SELECT</td>
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
<td width="441">Description</td>
</tr>
<tr>
<td>1</td>
<td>Opportunity</td>
<td>100</td>
<td>&lt;‘REQUIREDField1’&gt;</td>
<td>Opportunity</td>
<td></td>
<td></td>
<td>Amount</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>DECIMAL: Amount of the opportunity</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>&lt;‘REQUIREDField2’&gt;</td>
<td></td>
<td></td>
<td></td>
<td>CloseDate</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>DATE: Close date of the opportunity</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>&lt;‘REQUIREDField3’&gt;</td>
<td></td>
<td></td>
<td></td>
<td colspan="2">CreatedDate</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>DATE: Created date of the opportunity</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>&lt;‘REQUIREDField4’&gt;</td>
<td></td>
<td></td>
<td></td>
<td>IsClosed</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>BOOLEAN: Opportunity close? True or false.</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>&lt;‘REQUIREDField5’&gt;</td>
<td></td>
<td></td>
<td></td>
<td>IsWon</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>BOOLEAN: Opportunity won? True or false.</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>&lt;‘REQUIREDField6’&gt;</td>
<td></td>
<td></td>
<td></td>
<td>LeadSource</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>STRING: Name of Leadsource</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>&lt;‘REQUIREDField7’&gt;</td>
<td></td>
<td></td>
<td></td>
<td>Probability</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>DECIMAL: Probability of winning opportunity</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>&lt;‘REQUIREDField8’&gt;</td>
<td></td>
<td></td>
<td></td>
<td>StageName</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>STRING: Stage Name of opportunity</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Category</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>STRING: Optional category name</td>
</tr>
<tr>
<td>2</td>
<td>Opportunity History</td>
<td>100</td>
<td>&lt;‘REQUIREDField9’&gt;</td>
<td colspan="2">Opportunity History</td>
<td></td>
<td colspan="2">CreatedDate</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>DATE: Created date of the opportunity</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>&lt;‘REQUIREDField10’&gt;</td>
<td></td>
<td></td>
<td></td>
<td colspan="2">OpportunityId</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>DECIMAL: ID of the opportunity</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>&lt;‘REQUIREDField11’&gt;</td>
<td></td>
<td></td>
<td></td>
<td>StageName</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>STRING: Stage Name of opportunity</td>
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
<li>Name the new DataFlow “Marketing ROI”.</li>
<li>Under “Input DataSets” add&nbsp;your newly populated Grid Builder called “Marketing ROI – Grid Builder”.</li>
<li>Add any datasets referenced by your Grid Builder.</li>
<li>Add the dataset called “Marketing ROI – Settings” which came with your app.</li>
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
<p><a href="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/09/30142046/MarketingROI.txt">MarketingROI</a></p>
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
<li>Connect the four appropriate datasets that the DataFlow generated; Marketing ROI, Filters, Labels, and&nbsp;Stage Order</li>
<li>The other four datasets came with your app and don’t need to be switched out; Buckets, Leadsources, Bookmarks, and Settings.</li>
<li>NOTE – Your app datasets may be named differently than the example found below:</li>
</ul>
<p><img loading="lazy" class="alignnone size-full wp-image-2654" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/11110318/MarketingROIScreen1.png" alt="MarketingROIScreen1" width="994" height="457" srcset="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/11110318/MarketingROIScreen1.png 994w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/11110318/MarketingROIScreen1-300x138.png 300w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/11110318/MarketingROIScreen1-768x353.png 768w" sizes="(max-width: 994px) 100vw, 994px"></p>
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
<li>Navigate to&nbsp;the “Marketing ROI – Grid Builder” webform for this app.</li>
<li>Edit the “FilterId”, “FilterName”, “FilterInputType”, “FilterIsPrimary”, and “FilterIsPrimaryGroup” columns.</li>
<li>Note: In some situations, not all filter columns are required to be populated.</li>
</ul>
<p>Some common filters for this app include:</p>
<ul>
<li>Stage Name, Multi Select</li>
</ul>
<p>Note that all app content adjusts to whatever new filters the customer chooses to add, including the date grains within the app and the chart titles, where applicable.</p>
<p>Any edits that don’t meet&nbsp;the Grid Builder requirements&nbsp;could result in undesired results.</p>
</div></div><br>
<div class="doc-row" id="Step%204:%20[OPTIONAL]%20Adjusting%20the%20Settings">
                                    <h3 class="doc-row-title">Step 4: [OPTIONAL] Adjusting the Settings</h3><div class="small-pad-bottom"><p>Users may want to edit some of the settings for this app.</p>
<p>In order to do this,&nbsp;users will need to follow the steps below:</p>
<ul>
<li>Navigate to the “Marketing ROI – Settings” webform for this app.</li>
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
