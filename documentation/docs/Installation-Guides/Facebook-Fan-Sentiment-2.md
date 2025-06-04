---
stoplight-id: w1ktzfoqoyxfd
---

<div class="col-md-12 content-panel">
                <h2>Facebook Fan Sentiment</h2>
                <p></p><p>Thank you for installing, test-driving, and purchasing Facebook Fan Sentiment! This guide is intended to help you connect this app to your own data. If you have completed the purchasing process for this app then you will be able to go through all of the steps in this guide. Check the prerequisites below to make sure you have everything you need to power up your app.</p>
<h3 class="doc-row-title"><strong>Prerequisites:</strong></h3>
<ul>
<li>You will need access to the appropriate Facebook&nbsp;sign-in credentials.</li>
<li>A knowledge of how Domo DataFlows function is recommended.</li>
</ul>
<div id="Step%201:%20Identify%20Required%20Data%20Fields" class="doc-row">
<div class="small-pad-bottom">
<p><strong>Things to Know About This&nbsp;App:</strong></p>
<ul>
<li>This app provides summary and trending values driven by statistics pulled from Facebook, and presents them in an easy to read and visually appealing way.</li>
</ul>
</div>
</div>
<p></p><div class="doc-row" id="Step%201:%20Connect%20Your%20Data">
                                    <h3 class="doc-row-title">Step 1: Connect Your Data</h3><div class="small-pad-bottom"><p>Once you have the appropriate credentials&nbsp;you are ready to connect it to your app.</p>
<p>Please follow the step-by-step instructions provided below:</p>
<ul>
<li>Navigate&nbsp;to the Data Center and create&nbsp;a new DataSet.</li>
</ul>
<p><img loading="lazy" class="alignnone size-full wp-image-2617" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/05154705/GAIScreenshot11.png" alt="GAIScreenshot1" width="416" height="342" srcset="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/05154705/GAIScreenshot11.png 416w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/05154705/GAIScreenshot11-300x247.png 300w" sizes="(max-width: 416px) 100vw, 416px"></p>
<p><img loading="lazy" class="alignnone wp-image-2612" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/05152414/ScreenShot2.png" alt="ScreenShot2" width="1475" height="199" srcset="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/05152414/ScreenShot2.png 1475w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/05152414/ScreenShot2-300x40.png 300w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/05152414/ScreenShot2-768x104.png 768w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/05152414/ScreenShot2-1024x138.png 1024w" sizes="(max-width: 1475px) 100vw, 1475px"></p>
<ul>
<li>Enter “Facebook” in the search bar and click on the Facebook&nbsp;connector.</li>
</ul>
<p><img loading="lazy" class="alignnone size-full wp-image-2676" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/18161841/FB-Sent1.png" alt="FB Sent1" width="913" height="435" srcset="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/18161841/FB-Sent1.png 913w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/18161841/FB-Sent1-300x143.png 300w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/18161841/FB-Sent1-768x366.png 768w" sizes="(max-width: 913px) 100vw, 913px"></p>
<ul>
<li>Click the “Connect” button and enter the appropriate&nbsp;Facebook&nbsp;credentials.</li>
</ul>
<p><img loading="lazy" class="alignnone size-full wp-image-2677" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/18161900/FB-Sent2.png" alt="FB Sent2" width="1301" height="532" srcset="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/18161900/FB-Sent2.png 1301w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/18161900/FB-Sent2-300x123.png 300w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/18161900/FB-Sent2-768x314.png 768w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/18161900/FB-Sent2-1024x419.png 1024w" sizes="(max-width: 1301px) 100vw, 1301px"></p>
<ul>
<li>Under the Data Selection menu, first choose “Page Posts” under report. We will later repeat this step once&nbsp;more to get the “Page Interactions” report as well.</li>
</ul>
<p><img loading="lazy" class="alignnone size-full wp-image-2678" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/18161921/FB-Sent3.png" alt="FB Sent3" width="1365" height="392" srcset="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/18161921/FB-Sent3.png 1365w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/18161921/FB-Sent3-300x86.png 300w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/18161921/FB-Sent3-768x221.png 768w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/18161921/FB-Sent3-1024x294.png 1024w" sizes="(max-width: 1365px) 100vw, 1365px"></p>
<ul>
<li>You will be prompted to set how often the DataSet updates. Choose your preference then click the “Next” button.</li>
<li>Here you will be prompted to enter a name and description for the DataSet. In order for the DataFlow to function properly, name each table exactly after the report it came from. Ex. “Page Posts” or “Page Interactions”</li>
<li>Click “Save” then repeat this process until you have both&nbsp;DataSets: “Page Posts” and “Page Interactions”</li>
</ul>
<p>We will need to make one additional dataset to help power this app’s DataFlow. Follow the steps below:</p>
<ul>
<li>Navigate to the Data Center and create a new dataset as you did above.</li>
<li>When prompted to choose a connector choose Domo Online Form as the option.</li>
<li>Name the dataset “FB Sentiment Date Range Filter” then copy the table below into the webform:</li>
</ul>
<table width="307">
<tbody>
<tr>
<td width="131">Date Range Filter</td>
<td width="176">Date Range Filter Options</td>
</tr>
<tr>
<td>N</td>
<td>Last 7 Days</td>
</tr>
<tr>
<td>N</td>
<td>Last 30 Days</td>
</tr>
<tr>
<td>Y</td>
<td>Last 60 Days</td>
</tr>
<tr>
<td>N</td>
<td>Last 90 Days</td>
</tr>
<tr>
<td>N</td>
<td>Last Year</td>
</tr>
<tr>
<td>N</td>
<td>Last 2 Years</td>
</tr>
</tbody>
</table>
<ul>
<li>Click save to save your dataset.</li>
</ul>
<p>Once you have created these&nbsp;DataSets&nbsp;you may move to Step 2.</p>
<p><script>// <![CDATA[
OO.ready(function() { OO.Player.create("ooyalaplayer-IyYTc1MjE61NwLdtrxXvZuhH-dSGbWnR", "IyYTc1MjE61NwLdtrxXvZuhH-dSGbWnR", { height: 380 }); });
// ]]&gt;</script></p>
</div></div><div class="doc-row" id="Step%202:%20Insert%20the%20DataSets%20into%20the%20DataFlow">
                                    <h3 class="doc-row-title">Step 2: Insert the DataSets into the DataFlow</h3><div class="small-pad-bottom"><h2>Create a Dataflow: Add the Input Datasets</h2>
<p>To power the app, you need to create a new DataFlow.&nbsp;Follow the steps below:</p>
<ul>
<li>Navigate to DataFlows in the Data Center and click the “+ New DataFlow” button.</li>
</ul>
<p><img loading="lazy" class="alignnone size-full wp-image-2468" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/24125439/1-Navigate-to-DataFlows1.png" alt="1 - Navigate to DataFlows" width="2423" height="427" srcset="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/24125439/1-Navigate-to-DataFlows1.png 2423w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/24125439/1-Navigate-to-DataFlows1-300x53.png 300w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/24125439/1-Navigate-to-DataFlows1-768x135.png 768w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/24125439/1-Navigate-to-DataFlows1-1024x180.png 1024w" sizes="(max-width: 2423px) 100vw, 2423px"></p>
<ul>
<li>Create a MySQL DataFlow.</li>
</ul>
<p><img loading="lazy" class="alignnone size-full wp-image-2470" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/24125441/2-Data-Flow-type1.png" alt="2 - Data Flow type" width="1815" height="788" srcset="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/24125441/2-Data-Flow-type1.png 1815w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/24125441/2-Data-Flow-type1-300x130.png 300w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/24125441/2-Data-Flow-type1-768x333.png 768w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/24125441/2-Data-Flow-type1-1024x445.png 1024w" sizes="(max-width: 1815px) 100vw, 1815px"></p>
<ul>
<li>Click the “Select Dataset” button and add the three datasets you created in step 1 as input datasets.</li>
<li>These include “Page Posts”, “Page Interactions”, and “FB Sentiment Date Range Filter”.</li>
</ul>
<p><img loading="lazy" class="alignnone size-full wp-image-2679" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/18162018/FB-Sent4.png" alt="FB Sent4" width="690" height="250" srcset="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/18162018/FB-Sent4.png 690w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/18162018/FB-Sent4-300x109.png 300w" sizes="(max-width: 690px) 100vw, 690px"></p>
<h2>Add the Transform</h2>
<ul>
<li>After you have added all four&nbsp;DataSets, add a single transform with the following text:</li>
</ul>
<blockquote>
<pre>CALL `global`.app_labs_fb_fan_sentiment(SCHEMA());</pre>
</blockquote>
<ul>
<li>Make sure that the green box labeled “Generate Output Table” is un-clicked.</li>
</ul>
<h2>Add the Output Datasets</h2>
<ul>
<li>Create the six following output datasets:</li>
<li>Call the first one “FB Sentiment Trending” and use the following text:</li>
</ul>
<blockquote>
<pre>SELECT * FROM fan_sentiment_trending;</pre>
</blockquote>
<ul>
<li>Call the second&nbsp;one “FB Sentiment Summary” and use the following text:</li>
</ul>
<blockquote>
<pre>SELECT * FROM pos_neg_summary;</pre>
</blockquote>
<ul>
<li>Call the third&nbsp;one “FB Sentiment Summary Values” and use the following text:</li>
</ul>
<blockquote>
<pre>SELECT * FROM all_summaries;</pre>
</blockquote>
<ul>
<li>Call the fourth&nbsp;one “FB Sentiment Dynamic Messages” and use the following text:</li>
</ul>
<blockquote>
<pre>SELECT * FROM all_dynamic_messages;</pre>
</blockquote>
<ul>
<li>Call the fifth one “FB Sentiment Table Data” and use the following text:</li>
</ul>
<blockquote>
<pre>SELECT * FROM final_table_data;</pre>
</blockquote>
<ul>
<li>Call the final&nbsp;one “FB Sentiment Line Graph Data” and use the following text:</li>
</ul>
<blockquote>
<pre>SELECT * FROM grouped_date_trend_percentages;</pre>
</blockquote>
<ul>
<li>Click “Save and Run”</li>
<li>After the DataFlow finishes running, which may take a few minutes, you are ready to “wire-up” the app.</li>
</ul>
<h2>Connect Your Data to the App’s Widgets</h2>
<p>Using the six&nbsp;output datasets that the dataflow created, you will connect the data to the app. Follow these steps:</p>
<ul>
<li>Navigate to the page of the app.</li>
<li>When you hover your mouse over the app a wrench will appear. Click the wrench and then click “Edit Card”</li>
</ul>
<p><img loading="lazy" class="alignnone size-full wp-image-2556" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/12141309/Change-AppData-1.png" alt="Change AppData 1" width="623" height="656" srcset="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/12141309/Change-AppData-1.png 623w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/12141309/Change-AppData-1-285x300.png 285w" sizes="(max-width: 623px) 100vw, 623px"></p>
<ul>
<li>Examine the app and locate each widget. Widgets range from charts to single value text or number fields to company or platform logos.</li>
</ul>
<p><img loading="lazy" class="alignnone size-full wp-image-2680" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/18162039/FB-Sent5.png" alt="FB Sent5" width="1196" height="761" srcset="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/18162039/FB-Sent5.png 1196w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/18162039/FB-Sent5-300x191.png 300w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/18162039/FB-Sent5-768x489.png 768w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/18162039/FB-Sent5-1024x652.png 1024w" sizes="(max-width: 1196px) 100vw, 1196px"></p>
<ul>
<li>Become familiar with how the data is organized in the six&nbsp;datasets the dataflow created.</li>
<li>Click on each widget and connect the appropriate dataset to it. You may&nbsp;need to filter or group by certain columns in some cases.</li>
</ul>
<p><img loading="lazy" class="alignnone size-full wp-image-2681" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/18162501/FB-Sent6.png" alt="FB Sent6" width="2019" height="346" srcset="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/18162501/FB-Sent6.png 2019w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/18162501/FB-Sent6-300x51.png 300w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/18162501/FB-Sent6-768x132.png 768w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/18162501/FB-Sent6-1024x175.png 1024w" sizes="(max-width: 2019px) 100vw, 2019px"></p>
<ul>
<li>After this is finished, unless you want to change the Date Filter Option for the app, you are finished! Enjoy your new app!</li>
</ul>
</div></div><div class="doc-row" id="Step%203:%20[OPTIONAL]%20Adjusting%20the%20Date%20Filter%20Settings">
                                    <h3 class="doc-row-title">Step 3: [OPTIONAL] Adjusting the Date Filter Settings</h3><div class="small-pad-bottom"><p>Users may want to edit the Date Filter options for this app.</p>
<p>In order to do this,&nbsp;users will need to follow the steps below:</p>
<ul>
<li>Navigate to the DataSet named “FB Sentiment Date Range Filter” which is the webform mentioned above that you created in step 1.</li>
<li>Open this dataset and edit its contents. Only one option may be chosen at a time. Simply change the cell next to your desired option to “Y” and make sure all of the other options have “N”.</li>
</ul>
<p>The Date Filter Options for this app&nbsp;include:</p>
<p><img loading="lazy" class="alignnone size-full wp-image-2631" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/09095506/GAIScreen3-1.png" alt="GAIScreen3-1" width="398" height="289" srcset="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/09095506/GAIScreen3-1.png 398w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/08/09095506/GAIScreen3-1-300x218.png 300w" sizes="(max-width: 398px) 100vw, 398px"></p>
<p>&nbsp;</p>
<h3 class="doc-row-title">Additional help</h3>
<div class="small-pad-bottom">
<p>Need additional assistance? Visit the&nbsp;<a href="https://dojo.domo.com/apps">Domo Community</a>.</p>
</div>
</div></div>            </div>
