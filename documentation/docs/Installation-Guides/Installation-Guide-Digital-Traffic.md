---
stoplight-id: l297mtf2k8wrm
---

<div class="col-md-12 content-panel">
                <h2>Installation Guide - Digital Traffic</h2>
                <p></p><p>Thanks for installing, test-driving, and purchasing Digital Traffic! This guide is intended to help you connect this app to your own data. If you have completed the purchasing process for this app then you will be able to go through all of the steps in this guide.</p>
<h3 class="doc-row-title">Prerequisites:</h3>
<p>To speed up the connection process for your data, this&nbsp;app utilizes Domo’s Grid Builder. If you are not already familiar with Grid Builder,&nbsp;please visit our&nbsp;<a href="http://player.ooyala.com/iframe.html?ec=xiY3hrNDE66fk814mw5EG4qPCAooAOGl&amp;pbid=b986320eb2af428485644819b233d43c" target="_blank">Grid Builder Training</a>.</p>
<p>Though not required – if your customer uses Google Analytics, generating the input datasets for the app will be easier.</p>
<div id="Step%201:%20Identify%20Required%20Data%20Fields" class="doc-row">
<h3 class="doc-row-title">Step 1: Prepare Your Data</h3>
<div class="small-pad-bottom">
<p>This app requires creating&nbsp;a custom dataset named “Digital Traffic – Grid Builder”.</p>
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
<li>Title the new dataset “Digital Traffic – Grid Builder”.</li>
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
<td>Traffic</td>
<td>100</td>
<td>Period</td>
<td colspan="2">Digital Traffic – Mobile Metrics<p></p>
<p>(or YourTableName)</p></td>
<td>Period,Devices,`Operating System`,`Report Suite Name`</td>
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
<td></td>
<td>SUM(`Mobile Views`)</td>
<td></td>
<td></td>
<td></td>
<td>Metric1</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Page Views</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>SUM(`Mobile Visits`)</td>
<td></td>
<td></td>
<td></td>
<td>Metric2</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Conversions</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td colspan="4">ROUND(SUM(`Mobile Visits`) / SUM(`Mobile Views`), 2)</td>
<td>Metric3</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2">Conversion Rate</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>Devices</td>
<td></td>
<td></td>
<td></td>
<td>Dimension1</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Browser</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>`Operating System`</td>
<td></td>
<td></td>
<td></td>
<td>Dimension2</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Device</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>`Report Suite Name`</td>
<td></td>
<td></td>
<td></td>
<td>Dimension3</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>State</td>
<td></td>
<td></td>
<td></td>
<td></td>
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
<li>The example data above correlates with the Google Analytics – Mobile Metrics report. Using the Google Analytics connector to generate this as an input dataset is recommended where possible.</li>
<li>Starting with row 1, adjust&nbsp;the ‘SELECT’ column with the field names exactly as they&nbsp;appear in your dataset.</li>
<li>Fill out the ‘FROM’ column with the name of the dataset exactly as it appears in your data center.</li>
<li>Adjustments might need to be made to the ‘WHERE’ and ‘GROUP BY’ columns as needed.</li>
</ul>
<h2>Step 1.5:&nbsp;Create Distribution Dataset</h2>
<p>One more dataset is required to make the app function.</p>
<p>If you have access to the Domo-Dimensions connector (Access is normally restricted as the connector is currently in alpha build), this Dataset can be generated there. If you do not have access contact applabs@domo.com for help.</p>
<p>As soon as you have access, follow these steps:</p>
<ul>
<li>Create a new dataset as seen above.</li>
<li>Search for and click on the Domo-Dimensions connector.</li>
<li>Under “Files” select “StandardNormalDistribution.csv”</li>
<li>Set it to update daily, early in the morning. – One reason for the inclusion of this dataset is to schedule the dataflow to run every morning so data stays up to date.</li>
<li>Name your DataSet: “Standard Normal Distribution”</li>
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
<li>Name the new DataFlow “Digital Traffic”.</li>
<li>Under “Input DataSets” add&nbsp;your newly populated Grid Builder called “Digital Traffic&nbsp;– Grid Builder”.</li>
<li>Add any datasets referenced by your Grid Builder.</li>
<li>Add the dataset called “Digital Traffic&nbsp;– Settings” which came with your app.</li>
<li>Add the “Standard Normal Distribution” dataset that you generated in step 1.5.</li>
</ul>
<p><img loading="lazy" class="alignnone wp-image-2471" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/24125443/3-Add-Grid-builder-data-set1-1024x802.png" alt="3 - Add Grid builder data set" width="688" height="539" srcset="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/24125443/3-Add-Grid-builder-data-set1-1024x802.png 1024w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/24125443/3-Add-Grid-builder-data-set1-300x235.png 300w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/24125443/3-Add-Grid-builder-data-set1-768x602.png 768w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/24125443/3-Add-Grid-builder-data-set1.png 1481w" sizes="(max-width: 688px) 100vw, 688px"></p>
<p><strong>Create one transform with the following text:</strong></p>
<blockquote>
<pre>CALL `global`.app_labs_digital_traffic(SCHEMA());</pre>
</blockquote>
<p>When creating your transform, make sure to de-select the green checkbox “Generate Output Table” in the lower left corner of your transform.</p>
<p><strong>Create four Output Datasets.</strong></p>
<ul>
<li>Call the first one “Digital Traffic – Date Summary” and set the query as follows:</li>
</ul>
<blockquote>
<pre>SELECT * FROM date_summary;</pre>
</blockquote>
<ul>
<li>Call the second one “Digital Traffic&nbsp;– Date Influencer”</li>
</ul>
<blockquote>
<pre>SELECT * FROM rank_influencer;</pre>
</blockquote>
<ul>
<li>Call the third one “Digital Traffic – Dimension Detail”</li>
</ul>
<blockquote>
<pre>SELECT * FROM dimension_detail;</pre>
</blockquote>
<ul>
<li>Call the fourth&nbsp;one “Digital Traffic – Log”</li>
</ul>
<blockquote>
<pre>SELECT * FROM dynamic_sql_log;</pre>
</blockquote>
<ul>
<li>Click the green boxes on all input datasets at the bottom of the page to run the DataFlow when the datasets are updated.</li>
<li>Save and run the DataFlow.</li>
<li>Once the DataFlow finishes running, compare&nbsp;your new output datasets to the sample datasets the original app was connected to and verify their&nbsp;formats match.</li>
<li>Go to the app, click the wrench icon in the upper right corner and select “Edit Card”.</li>
</ul>
<p><img loading="lazy" class="alignnone wp-image-2556" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/12141309/Change-AppData-1.png" alt="Change AppData 1" width="309" height="326" srcset="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/12141309/Change-AppData-1.png 623w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/12141309/Change-AppData-1-285x300.png 285w" sizes="(max-width: 309px) 100vw, 309px"></p>
<ul>
<li>Scroll down to the bottom of the page. You will find a list of grayed-out datasets the app uses to power itself.</li>
<li>Click each dataset and click the down-arrow to search for and swap out the sample datasets for the datasets newly created by your DataFlow.</li>
<li>Connect the appropriate datasets that the DataFlow you created generated; Date Summary, Date Influencer, and&nbsp;Dimension Detail</li>
<li>The app came with datasets for Date Filters, Settings, and Dimensions. These do not need to be changed</li>
<li>NOTE – Your app datasets may be named differently than the example found below:</li>
</ul>
<p><img loading="lazy" class="alignnone size-full wp-image-2652" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/11102850/DigitalTrafficScreen1.png" alt="DigitalTrafficScreen1" width="820" height="465" srcset="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/11102850/DigitalTrafficScreen1.png 820w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/11102850/DigitalTrafficScreen1-300x170.png 300w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/11102850/DigitalTrafficScreen1-768x436.png 768w" sizes="(max-width: 820px) 100vw, 820px"></p>
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
<li>Navigate to&nbsp;the “Digital Traffic – Grid Builder” webform for this app.</li>
<li>Edit the “FilterId”, “FilterName”, “FilterInputType”, “FilterIsPrimary”, and “FilterIsPrimaryGroup” columns.</li>
<li>Note: In some situations, not all filter columns are required to be populated.</li>
</ul>
<p>Some common filters for this app include:</p>
<ul>
<li>Any metric</li>
<li>Any dimension</li>
</ul>
<p>Note that all app content adjusts to whatever new filters the customer chooses to add, including the date grains within the app and the chart titles, where applicable.</p>
<p>Any edits that don’t meet&nbsp;the Grid Builder requirements&nbsp;could result in undesired results.</p>
</div></div><div class="doc-row" id="Step%204:%20[OPTIONAL]%20Adjusting%20the%20Settings">
                                    <h3 class="doc-row-title">Step 4: [OPTIONAL] Adjusting the Settings</h3><div class="small-pad-bottom"><p>Users may want to edit some of the settings for this app.</p>
<p>In order to do this,&nbsp;users will need to follow the steps below:</p>
<ul>
<li>Navigate to the “Digital Traffic – Settings” webform for this app.</li>
<li>Open this dataset and edit the “Value” column&nbsp;as desired.</li>
</ul>
<p>Some common settings that customers change for this app include:</p>
<ul>
<li>Metric Labels</li>
<li>Sample Size</li>
<li>Confidence Interval</li>
</ul>
<h3 class="doc-row-title">Additional help</h3>
<div class="small-pad-bottom">
<p>Need additional assistance? Visit the&nbsp;<a href="https://dojo.domo.com/apps">Domo Community</a>.</p>
</div>
</div></div>            </div>
