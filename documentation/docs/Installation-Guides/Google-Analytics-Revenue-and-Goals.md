---
stoplight-id: bmyk9lpjpag35
---

<div class="col-md-12 content-panel">
                <h2>Google Analytics Revenue &amp; Goals</h2>
                <p></p><p>Thanks for installing and test-driving <span id="title">GA Revenue &amp; Goals</span>! This guide is intended to help you connect this app to your own data. The first step is to ensure that your data follows the same schema (or structure) of the sample datasets that are currently powering the app. Fortunately, Domo has created some powerful data transformation tools to help, along with the step-by-step instructions provided below.</p>
<div id="Step%201:%20Identify%20Required%20Data%20Fields" class="doc-row">
<h3 class="doc-row-title">Step 1: Prepare Your Data</h3>
<div class="small-pad-bottom">
<p>This app requires creating the following custom datasets. To do this, you’ll need to ensure that you have each of these fields in Domo. Then you’ll need to use transforms to create datasets that follow the exact structure or schema of the datasets below. For help with Dataflows, Magic ETL, or BeastModes, please visit <a href="https://university.domo.com/" target="_blank">Domo University</a>.</p>
</div>
<br>
<div id="custom-data-container">
<p><!--tr>


<td colspan="6"></td>


</tr-->
</p><table id="Base-Metrics">
<tbody>
<tr>
<td colspan="6"><strong>DataSet Name:</strong> <span class="value">Base Metrics</span></td>
</tr>
<tr>
<td><strong>Field Name</strong></td>
<td><strong>Data Type</strong></td>
<td><strong>Report Name / Object Name</strong></td>
<td><strong>Source </strong></td>
<td colspan="2"><strong>Description of Field</strong></td>
</tr>
<tr>
<td>Row Id</td>
<td>INT</td>
<td>Base Metrics</td>
<td>Google Analytics (Base Metrics)</td>
<td colspan="2">Row identifier</td>
</tr>
<tr>
<td>Account</td>
<td>STRING</td>
<td>Base Metrics</td>
<td>Google Analytics (Base Metrics)</td>
<td colspan="2">URL of the associated Google Analytics account</td>
</tr>
<tr>
<td>Web Property</td>
<td>STRING</td>
<td>Base Metrics</td>
<td>Google Analytics (Base Metrics)</td>
<td colspan="2">Web property (URL) of the associated Google Analytics account</td>
</tr>
<tr>
<td>View (Profile)</td>
<td>STRING</td>
<td>Base Metrics</td>
<td>Google Analytics (Base Metrics)</td>
<td colspan="2">Profile (URL) of the associated Google Analytics account</td>
</tr>
<tr>
<td>View Id</td>
<td>INT</td>
<td>Base Metrics</td>
<td>Google Analytics (Base Metrics)</td>
<td colspan="2">ID of the view</td>
</tr>
<tr>
<td>Date</td>
<td>DATE</td>
<td>Base Metrics</td>
<td>Google Analytics (Base Metrics)</td>
<td colspan="2">Date of the associated tracked metrics</td>
</tr>
<tr>
<td>Visits</td>
<td>INT</td>
<td>Base Metrics</td>
<td>Google Analytics (Base Metrics)</td>
<td colspan="2">Number of visits</td>
</tr>
<tr>
<td>Daily Visitors</td>
<td>INT</td>
<td>Base Metrics</td>
<td>Google Analytics (Base Metrics)</td>
<td colspan="2">Number of daily visitors</td>
</tr>
<tr>
<td>Pageviews</td>
<td>INT</td>
<td>Base Metrics</td>
<td>Google Analytics (Base Metrics)</td>
<td colspan="2">Number of pageviews</td>
</tr>
<tr>
<td>Time On Site</td>
<td>INT</td>
<td>Base Metrics</td>
<td>Google Analytics (Base Metrics)</td>
<td colspan="2">Amount of time users spent on site</td>
</tr>
<tr>
<td>Bounces</td>
<td>INT</td>
<td>Base Metrics</td>
<td>Google Analytics (Base Metrics)</td>
<td colspan="2">Number of bounces</td>
</tr>
<tr>
<td>New Visits</td>
<td>INT</td>
<td>Base Metrics</td>
<td>Google Analytics (Base Metrics)</td>
<td colspan="2">Number of new visits</td>
</tr>
<tr>
<td>Transactions</td>
<td>INT</td>
<td>Base Metrics</td>
<td>Google Analytics (Base Metrics)</td>
<td colspan="2">Number of transactions</td>
</tr>
<tr>
<td>Transaction Revenue</td>
<td>INT</td>
<td>Base Metrics</td>
<td>Google Analytics (Base Metrics)</td>
<td colspan="2">Amount of transaction revenue</td>
</tr>
<tr>
<td>Goal Completions All</td>
<td>INT</td>
<td>Base Metrics</td>
<td>Google Analytics (Base Metrics)</td>
<td colspan="2">Number of goal completions</td>
</tr>
<tr>
<td>Goal Value All</td>
<td>INT</td>
<td>Base Metrics</td>
<td>Google Analytics (Base Metrics)</td>
<td colspan="2">Value of associated goals</td>
</tr>
<tr>
<td>Sampled Data</td>
<td>BOOLEAN</td>
<td>Base Metrics</td>
<td>Google Analytics (Base Metrics)</td>
<td colspan="2">True or false statement determining if the data is sample data</td>
</tr>
</tbody>
</table>
<p><!--tr>


<td colspan="6"></td>


</tr-->
</p><table id="GA-Revenue-&amp;-Goal-Date-Range-Filter">
<tbody>
<tr>
<td colspan="6"><strong>DataSet Name:</strong> <span class="value">GA Revenue &amp; Goal Date Range Filter</span></td>
</tr>
<tr>
<td><strong>Field Name</strong></td>
<td><strong>Data Type</strong></td>
<td><strong>Report Name / Object Name</strong></td>
<td><strong>Source </strong></td>
<td colspan="2"><strong>Description of Field</strong></td>
</tr>
<tr>
<td>Date Range Filter</td>
<td>BOOLEAN</td>
<td>GA Revenue &amp; Goal Date Range Filter</td>
<td>Google Analytics (Base Metrics)</td>
<td colspan="2">Used for determining date range filter on the app. The user should place a “Y” next to the desired date filter option.</td>
</tr>
<tr>
<td>Date Range Filter Options</td>
<td>STRING</td>
<td>GA Revenue &amp; Goal Date Range Filter</td>
<td>Google Analytics (Base Metrics)</td>
<td colspan="2">List of date range filter options.</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
</div>
</div>
<p></p><div class="doc-row" id="Step%202:%20Connect%20Your%20Data">
                                    <h3 class="doc-row-title">Step 2: Connect Your Data</h3><div class="small-pad-bottom"><p>Once you’ve finished preparing your data as outlined in Step 1 you’re ready to connect it to your app. To do this, go to the page in Domo where the app is installed and click the “CONNECT YOUR DATA” button at the top of the page.</p>
<p>&nbsp;</p>
<p class="small-pad"><img loading="lazy" class="alignnone size-full wp-image-1207" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/03/14155707/Screen-Shot-2016-03-14-at-3.52.48-PM1.png" alt="Screen Shot 2016-03-14 at 3.52.48 PM" width="1158" height="71"></p>
<div id="ooyalaplayer-IyYTc1MjE61NwLdtrxXvZuhH-dSGbWnR" class="ooyalaplayer">
<div class="innerWrapper">
<div class="oo_error" style="display: none;"></div>
<div class="plugins" style="display: none;"></div>
<p><video class="video" style="left: -100000px;" src="http://player.ooyala.com/player/all/IyYTc1MjE61NwLdtrxXvZuhH-dSGbWnR.m3u8?targetBitrate=1200&amp;secure_ios_token=UzArNFNXNTRBbWp6dkdBdi85bmxYa3lpZlYyZy81dzN6aVRKbkRzUXJlSEdtME1jdldrMlVqZGZyUFZVCjIrcVBOSlVWU2VrUG1QcTZRTXROUE1IcTZRPT0K" preload="none" width="300" height="150"></video><video class="midroll" preload="none" width="300" height="150"></video></p>
<div class="oo_ads_countdown" style="display: none;"></div>
<div class="oo_promo" style="background-image: url('https://secure-cf-c.ooyala.com/IyYTc1MjE61NwLdtrxXvZuhH-dSGbWnR/3Gduepif0T1UGY8H4xMDoxOmFkOxyVqc');"></div>
<div class="oo_tap_panel" style="display: none;"></div>
<div class="oo_controls_wrap" style="display: none; position: relative; overflow: hidden; height: 100%; width: 100%;">
<div class="oo_controls oo_full_controls" style="display: none; bottom: -40px;">
<div class="oo_controls_inner vod">
<div class="oo_scrubber">
<div class="oo_label oo_currentTime">00:00</div>
<div class="oo_scrubber_track"></div>
<div class="oo_label oo_duration">00:00</div>
</div>
<div class="oo_button oo_toolbar_item oo_rewind"></div>
<div class="oo_button oo_toolbar_item oo_pause" style="display: none;"></div>
<div class="oo_button oo_toolbar_item oo_play"></div>
<div class="oo_button oo_toolbar_item oo_fullscreen oo_fullscreen_on"></div>
</div>
<div class="oo_controls_inner live">
<div class="oo_scrubber"></div>
<div class="oo_button oo_toolbar_item oo_rewind"></div>
<div class="oo_button oo_toolbar_item oo_pause" style="display: none;"></div>
<div class="oo_button oo_toolbar_item oo_play"></div>
<div class="oo_live_indicator oo_button oo_toolbar_item"></div>
<div class="oo_live_message oo_label oo_button oo_toolbar_item">
<p>LIVE</p>
<div class="oo_button_highlight"></div>
</div>
<div class="oo_button oo_toolbar_item oo_fullscreen oo_fullscreen_on"></div>
</div>
</div>
</div>
<div class="oo_spinner" style="display: none; margin-top: 165px; margin-left: 390px;"><img class="oo_spinner_img" style="width: 50px; height: 50px;" src="blob:https://developer.domo.com/a69720ca-de7d-4089-83ef-61ebcc8673fa" alt=""></div>
<div class="oo_end_screen" style="display: none; background-image: url('https://secure-cf-c.ooyala.com/IyYTc1MjE61NwLdtrxXvZuhH-dSGbWnR/3Gduepif0T1UGY8H4xMDoxOmFkOxyVqc');"><img class="oo_replay" src="blob:https://developer.domo.com/c1cdd102-f2c4-4c56-ba4f-91d303710ab1" alt=""><img class="oo_fullscreen" src="blob:https://developer.domo.com/1c2d0734-4222-4054-b754-4cf984849df1" alt=""></div>
</div>
</div>
<p><script>// <![CDATA[
OO.ready(function() { OO.Player.create("ooyalaplayer-IyYTc1MjE61NwLdtrxXvZuhH-dSGbWnR", "IyYTc1MjE61NwLdtrxXvZuhH-dSGbWnR", { height: 380 }); });
// ]]&gt;</script></p>
</div></div><div class="doc-row" id="Step%203:%20[OPTIONAL]%20Adjusting%20the%20Date%20Range%20Filter">
                                    <h3 class="doc-row-title">Step 3: [OPTIONAL] Adjusting the Date Range Filter</h3><div class="small-pad-bottom"><div class="small-pad-bottom">
<p>Users may want to visualize their fan sentiment in different time ranges (i.e. maybe only the last 7 days,<wbr>&nbsp;or a bigger frame like the last 90 days). In order to do this,<wbr>&nbsp;users will need to modify the “GA R&amp;G Date Range Filter” webform. By editing the “Date Range Filter” column,<wbr>&nbsp;users can place a Y next to the range they desire,<wbr>&nbsp;and the dataflow will adjust their content accordingly:</p>
<p><img loading="lazy" class="aligncenter wp-image-2155 size-full" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/05/16151741/Screen-Shot-2016-05-13-at-3.47.23-PM.png" alt="Screen Shot 2016-05-13 at 3.47.23 PM" width="481" height="709" srcset="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/05/16151741/Screen-Shot-2016-05-13-at-3.47.23-PM.png 481w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/05/16151741/Screen-Shot-2016-05-13-at-3.47.23-PM-204x300.png 204w" sizes="(max-width: 481px) 100vw, 481px"></p>
</div>
<p>Note that all content adjusts, including the app’s date grain and the title&nbsp;“Last 30 Days”</p>
<p><img loading="lazy" class="aligncenter wp-image-2157 size-large" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/05/16151741/Screen-Shot-2016-05-13-at-3.49.42-PM-1024x763.png" alt="Screen Shot 2016-05-13 at 3.49.42 PM" width="1024" height="763" srcset="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/05/16151741/Screen-Shot-2016-05-13-at-3.49.42-PM-1024x763.png 1024w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/05/16151741/Screen-Shot-2016-05-13-at-3.49.42-PM-300x224.png 300w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/05/16151741/Screen-Shot-2016-05-13-at-3.49.42-PM-768x573.png 768w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/05/16151741/Screen-Shot-2016-05-13-at-3.49.42-PM.png 1179w" sizes="(max-width: 1024px) 100vw, 1024px"></p>
<div class="small-pad-bottom">The user&nbsp;should only need to edit the “Date Range Filter” column, and as such only has the options listed in the “Date Range Filter Options Column”. Any edits outside of this first column could result in undesired results.</div>
<br>
<h3 class="doc-row-title">Additional help</h3>
<div class="small-pad-bottom">
<p>Need additional assistance? Visit the&nbsp;<a href="https://dojo.domo.com/apps">Domo Community</a></p>
</div>
</div></div>            </div>