---
stoplight-id: 3fpnl75cwqig9
---

<div class="col-md-12 content-panel">
                <h2>Net Promoter Score (NPS)</h2>
                <p></p><p>Thanks for installing and test-driving <span id="title">Net Promoter Score (NPS)</span>! This guide is intended to help you connect this app to your own data. The first step is to ensure that your data follows the same schema (or structure) of the sample datasets that are currently powering the app. Fortunately, Domo has created some powerful data transformation tools to help, along with the step-by-step instructions provided below.</p>
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
<td colspan="6"><strong>DataSet Name:</strong>&nbsp;<span class="value">NPS App Data Input</span></td>
</tr>
<tr>
<td><strong>Field Name</strong></td>
<td><strong>Data Type</strong></td>
<td><strong>Report Name / Object Name</strong></td>
<td><strong>Source </strong></td>
<td colspan="2"><strong>Description of Field</strong></td>
</tr>
<tr>
<td>Score</td>
<td>INT</td>
<td>NPS App Data Input</td>
<td>Any Survey Tool</td>
<td colspan="2">The score (0-10) given by survey takers to the question, “How likely are you to recommend us?” (10 being very likely)</td>
</tr>
<tr>
<td>Number of Responses</td>
<td>INT</td>
<td>NPS App Data Input</td>
<td>Any Survey Tool</td>
<td colspan="2">Number of survey takers who gave the associated scores</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
</tbody>
</table>
<p>NOTE:&nbsp;This is the only required dataset for this app; the dataflow behind this app will do the rest of the work. You simply need to use your dataset (in place of the sample dataset) as the input datasource for the associated dataflow.</p>
</div>
</div>
<p></p><div class="doc-row" id="Step%202:%20Connect%20Your%20Data">
                                    <h3 class="doc-row-title">Step 2: Connect Your Data</h3><div class="small-pad-bottom"><p>Once you’ve finished preparing your data as outlined in Step 1 you’re ready to connect it to your app. To do this, go to the page in Domo where the app is installed and click the “CONNECT YOUR DATA” button at the top of the page.</p>
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
</div></div>            </div>
