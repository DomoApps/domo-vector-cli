---
stoplight-id: nnbtrcttoml2q
---

<div class="col-md-12 content-panel">
                <h2>Facebook Fan Sentiment</h2>
                <p></p><p>Thanks for installing and test-driving <span id="title">Facebook Fan Sentiment</span>! This guide is intended to help you connect this app to your own data. The first step is to ensure that your data follows the same schema (or structure) of the sample datasets that are currently powering the app. Fortunately, Domo has created some powerful data transformation tools to help, along with the step-by-step instructions provided below.</p>
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
</p><table id="Page-Posts">
<tbody>
<tr>
<td colspan="6"><strong>DataSet Name:</strong> <span class="value">Page Posts</span></td>
</tr>
<tr>
<td><strong>Field Name</strong></td>
<td><strong>Data Type</strong></td>
<td><strong>Report Name / Object Name</strong></td>
<td><strong>Source </strong></td>
<td colspan="2"><strong>Description of Field</strong></td>
</tr>
<tr>
<td>Id</td>
<td>STRING</td>
<td>Page Posts</td>
<td>Facebook</td>
<td colspan="2">Id of the associated post</td>
</tr>
<tr>
<td>Page Id</td>
<td>INT</td>
<td>Page Posts</td>
<td>Facebook</td>
<td colspan="2">Page id</td>
</tr>
<tr>
<td>Page Username</td>
<td>STRING</td>
<td>Page Posts</td>
<td>Facebook</td>
<td colspan="2">Username of the associated page</td>
</tr>
<tr>
<td>Page Global Name</td>
<td>STRING</td>
<td>Page Posts</td>
<td>Facebook</td>
<td colspan="2">Unique global page name</td>
</tr>
<tr>
<td>From Id</td>
<td>INT</td>
<td>Page Posts</td>
<td>Facebook</td>
<td colspan="2">Id of the posting account</td>
</tr>
<tr>
<td>From Name</td>
<td>STRING</td>
<td>Page Posts</td>
<td>Facebook</td>
<td colspan="2">Name of the posting account</td>
</tr>
<tr>
<td>Message</td>
<td>STRING</td>
<td>Page Posts</td>
<td>Facebook</td>
<td colspan="2">Post message</td>
</tr>
<tr>
<td>Picture</td>
<td>STRING</td>
<td>Page Posts</td>
<td>Facebook</td>
<td colspan="2">Url to the post picture</td>
</tr>
<tr>
<td>Link</td>
<td>STRING</td>
<td>Page Posts</td>
<td>Facebook</td>
<td colspan="2">Link used in the post</td>
</tr>
<tr>
<td>Type</td>
<td>STRING</td>
<td>Page Posts</td>
<td>Facebook</td>
<td colspan="2">Post type (link, photo, etc.)</td>
</tr>
<tr>
<td>Status Type</td>
<td>STRING</td>
<td>Page Posts</td>
<td>Facebook</td>
<td colspan="2">Type of status (shared_story, added_photos, etc.)</td>
</tr>
<tr>
<td>Object Id</td>
<td>INT</td>
<td>Page Posts</td>
<td>Facebook</td>
<td colspan="2">Id of associated object</td>
</tr>
<tr>
<td>Likes</td>
<td>INT</td>
<td>Page Posts</td>
<td>Facebook</td>
<td colspan="2">Number of likes</td>
</tr>
<tr>
<td>Comments</td>
<td>INT</td>
<td>Page Posts</td>
<td>Facebook</td>
<td colspan="2">Number of comments</td>
</tr>
<tr>
<td>Shares</td>
<td>INT</td>
<td>Page Posts</td>
<td>Facebook</td>
<td colspan="2">Number of shares</td>
</tr>
<tr>
<td>Created Time</td>
<td>DATE</td>
<td>Page Posts</td>
<td>Facebook</td>
<td colspan="2">Date the post was created</td>
</tr>
<tr>
<td>Updated Time</td>
<td>DATE</td>
<td>Page Posts</td>
<td>Facebook</td>
<td colspan="2">Date the post was last updated</td>
</tr>
<tr>
<td>Story</td>
<td>STRING</td>
<td>Page Posts</td>
<td>Facebook</td>
<td colspan="2">Associated post story</td>
</tr>
<tr>
<td>Description</td>
<td>STRING</td>
<td>Page Posts</td>
<td>Facebook</td>
<td colspan="2">Post description</td>
</tr>
<tr>
<td>Privacy</td>
<td>STRING</td>
<td>Page Posts</td>
<td>Facebook</td>
<td colspan="2">Privacy (public, private, etc.)</td>
</tr>
<tr>
<td>Application</td>
<td>STRING</td>
<td>Page Posts</td>
<td>Facebook</td>
<td colspan="2">Associated application</td>
</tr>
<tr>
<td>Caption</td>
<td>STRING</td>
<td>Page Posts</td>
<td>Facebook</td>
<td colspan="2">Associated caption</td>
</tr>
</tbody>
</table>
<p><!--tr>


<td colspan="6"></td>


</tr-->
</p><table id="Page-Interactions">
<tbody>
<tr>
<td colspan="6"><strong>DataSet Name:</strong> <span class="value">Page Interactions</span></td>
</tr>
<tr>
<td><strong>Field Name</strong></td>
<td><strong>Data Type</strong></td>
<td><strong>Report Name / Object Name</strong></td>
<td><strong>Source </strong></td>
<td colspan="2"><strong>Description of Field</strong></td>
</tr>
<tr>
<td>Date</td>
<td>DATE</td>
<td>Page Interactions</td>
<td>Facebook</td>
<td colspan="2">Date of tracked metrics</td>
</tr>
<tr>
<td>ID</td>
<td>INT</td>
<td>Page Interactions</td>
<td>Facebook</td>
<td colspan="2">Page id</td>
</tr>
<tr>
<td>PageID</td>
<td>INT</td>
<td>Page Interactions</td>
<td>Facebook</td>
<td colspan="2">Page id</td>
</tr>
<tr>
<td>Page Name</td>
<td>STRING</td>
<td>Page Interactions</td>
<td>Facebook</td>
<td colspan="2">Number of page name</td>
</tr>
<tr>
<td>Page Username</td>
<td>STRING</td>
<td>Page Interactions</td>
<td>Facebook</td>
<td colspan="2">Username of the associated page</td>
</tr>
<tr>
<td>Page Global Name</td>
<td>STRING</td>
<td>Page Interactions</td>
<td>Facebook</td>
<td colspan="2">Unique global page name</td>
</tr>
<tr>
<td>New Photo Posts</td>
<td>INT</td>
<td>Page Interactions</td>
<td>Facebook</td>
<td colspan="2">Number of new photo posts</td>
</tr>
<tr>
<td>New Video Posts</td>
<td>INT</td>
<td>Page Interactions</td>
<td>Facebook</td>
<td colspan="2">Number of new video posts</td>
</tr>
<tr>
<td>New Shares</td>
<td>INT</td>
<td>Page Interactions</td>
<td>Facebook</td>
<td colspan="2">Number of new shares</td>
</tr>
<tr>
<td>Photo Views</td>
<td>INT</td>
<td>Page Interactions</td>
<td>Facebook</td>
<td colspan="2">Number of photo views</td>
</tr>
<tr>
<td>Video Views</td>
<td>INT</td>
<td>Page Interactions</td>
<td>Facebook</td>
<td colspan="2">Number of video views</td>
</tr>
<tr>
<td>Link Clicks</td>
<td>INT</td>
<td>Page Interactions</td>
<td>Facebook</td>
<td colspan="2">Number of link clicks</td>
</tr>
<tr>
<td>Other Clicks</td>
<td>INT</td>
<td>Page Interactions</td>
<td>Facebook</td>
<td colspan="2">Number of other clicks</td>
</tr>
<tr>
<td>Likes</td>
<td>INT</td>
<td>Page Interactions</td>
<td>Facebook</td>
<td colspan="2">Number of likes</td>
</tr>
<tr>
<td>Comments</td>
<td>INT</td>
<td>Page Interactions</td>
<td>Facebook</td>
<td colspan="2">Number of comments</td>
</tr>
<tr>
<td>Links</td>
<td>INT</td>
<td>Page Interactions</td>
<td>Facebook</td>
<td colspan="2">Number of links</td>
</tr>
<tr>
<td>Answers</td>
<td>INT</td>
<td>Page Interactions</td>
<td>Facebook</td>
<td colspan="2">Number of answers</td>
</tr>
<tr>
<td>Claims</td>
<td>INT</td>
<td>Page Interactions</td>
<td>Facebook</td>
<td colspan="2">Number of claims</td>
</tr>
<tr>
<td>RSVPs</td>
<td>INT</td>
<td>Page Interactions</td>
<td>Facebook</td>
<td colspan="2">Number of rsvps</td>
</tr>
<tr>
<td>People Who Clicked Like</td>
<td>INT</td>
<td>Page Interactions</td>
<td>Facebook</td>
<td colspan="2">Number of people who clicked like</td>
</tr>
<tr>
<td>People Who Commented</td>
<td>INT</td>
<td>Page Interactions</td>
<td>Facebook</td>
<td colspan="2">Number of people who commented</td>
</tr>
<tr>
<td>People Who Linked</td>
<td>INT</td>
<td>Page Interactions</td>
<td>Facebook</td>
<td colspan="2">Number of people who linked</td>
</tr>
<tr>
<td>People Who Answered</td>
<td>INT</td>
<td>Page Interactions</td>
<td>Facebook</td>
<td colspan="2">Number of people who answered</td>
</tr>
<tr>
<td>People Who Claimed Offers</td>
<td>INT</td>
<td>Page Interactions</td>
<td>Facebook</td>
<td colspan="2">Number of people who claimed offers</td>
</tr>
<tr>
<td>People Who RSVPed</td>
<td>INT</td>
<td>Page Interactions</td>
<td>Facebook</td>
<td colspan="2">Number of people who rsvped</td>
</tr>
<tr>
<td>Hide All Button Clicks</td>
<td>INT</td>
<td>Page Interactions</td>
<td>Facebook</td>
<td colspan="2">Number of hide all button clicks</td>
</tr>
<tr>
<td>Hide Button Clicks</td>
<td>INT</td>
<td>Page Interactions</td>
<td>Facebook</td>
<td colspan="2">Number of hide button clicks</td>
</tr>
<tr>
<td>Unlike Button Clicks</td>
<td>INT</td>
<td>Page Interactions</td>
<td>Facebook</td>
<td colspan="2">Number of unlike button clicks</td>
</tr>
<tr>
<td>Report As Spam Button Clicks</td>
<td>INT</td>
<td>Page Interactions</td>
<td>Facebook</td>
<td colspan="2">Number of report as spam button clicks</td>
</tr>
<tr>
<td>People Who Viewed Photos</td>
<td>INT</td>
<td>Page Interactions</td>
<td>Facebook</td>
<td colspan="2">Number of people who viewed photos</td>
</tr>
<tr>
<td>People Who Viewed Videos</td>
<td>INT</td>
<td>Page Interactions</td>
<td>Facebook</td>
<td colspan="2">Number of people who viewed videos</td>
</tr>
<tr>
<td>People Who Clicked Links</td>
<td>INT</td>
<td>Page Interactions</td>
<td>Facebook</td>
<td colspan="2">Number of people who clicked links</td>
</tr>
<tr>
<td>People Clicking Elsewhere</td>
<td>INT</td>
<td>Page Interactions</td>
<td>Facebook</td>
<td colspan="2">Number of people clicking elsewhere</td>
</tr>
<tr>
<td>People Clicking Hide All Button</td>
<td>INT</td>
<td>Page Interactions</td>
<td>Facebook</td>
<td colspan="2">Number of people clicking hide all button</td>
</tr>
<tr>
<td>People Clicking Hide Button</td>
<td>INT</td>
<td>Page Interactions</td>
<td>Facebook</td>
<td colspan="2">Number of people clicking hide button</td>
</tr>
<tr>
<td>People Clicking Report As Spam Button</td>
<td>INT</td>
<td>Page Interactions</td>
<td>Facebook</td>
<td colspan="2">Number of people clicking report as spam button</td>
</tr>
<tr>
<td>People Clicking Unlike Page Button</td>
<td>INT</td>
<td>Page Interactions</td>
<td>Facebook</td>
<td colspan="2">Number of people clicking unlike page button</td>
</tr>
<tr>
<td>Engaged Users</td>
<td>INT</td>
<td>Page Interactions</td>
<td>Facebook</td>
<td colspan="2">Number of engaged users</td>
</tr>
</tbody>
</table>
<p><!--tr>


<td colspan="6"></td>


</tr-->
</p><table id="FB-Sentiment-Date-Range-Filter---Specs">
<tbody>
<tr>
<td colspan="6"><strong>DataSet Name:</strong> <span class="value">FB Sentiment Date Range Filter – Specs</span></td>
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
<td>FB Sentiment Date Range Filter – Specs</td>
<td>Facebook</td>
<td colspan="2">Used for determining date range filter on the app. The user should place a “Y” next to the desired date filter option.</td>
</tr>
<tr>
<td>Date Range Filter Options</td>
<td>STRING</td>
<td>FB Sentiment Date Range Filter – Specs</td>
<td>Facebook</td>
<td colspan="2">List of date range filter options.</td>
</tr>
</tbody>
</table>
</div>
<div class="doc-row medium-pad-top">
<h3 class="doc-row-title">Step 2: Connect Your Data</h3>
<div class="small-pad-bottom">
<p>Once you’ve finished preparing your data as outlined in Step 1 you’re ready to connect it to your app. To do this, go to the page in Domo where the app is installed and click the “CONNECT YOUR DATA” button at the top of the page.</p>
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
<div class="oo_spinner" style="display: none; margin-top: 165px; margin-left: 390px;"><img class="oo_spinner_img" style="width: 50px; height: 50px;" src="data:image/gif;base64,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" alt=""></div>
<div class="oo_end_screen" style="display: none; background-image: url('https://secure-cf-c.ooyala.com/IyYTc1MjE61NwLdtrxXvZuhH-dSGbWnR/3Gduepif0T1UGY8H4xMDoxOmFkOxyVqc');"><img class="oo_replay" src="data:image/png;base64,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" alt=""><img class="oo_fullscreen" src="data:image/png;base64,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" alt=""></div>
</div>
</div>
<p><script>// <![CDATA[
OO.ready(function() { OO.Player.create("ooyalaplayer-IyYTc1MjE61NwLdtrxXvZuhH-dSGbWnR", "IyYTc1MjE61NwLdtrxXvZuhH-dSGbWnR", { height: 380 }); });
// ]]&gt;</script></p>
</div>
<div class="doc-row medium-pad-top">
<h3 class="doc-row-title">Step&nbsp;3: [OPTIONAL] Adjusting the Date Range Filter</h3>
<div class="small-pad-bottom">
<p>Users may want to visualize their fan sentiment in different time ranges (i.e. maybe only the last 7 days, or a bigger frame like the last 90 days). In order to do this, users will need to modify the “FB Sentiment Date Range Filter” webform. By editing the “Date Range Filter” column, users can place a Y next to the range they desire, and the dataflow will adjust their content accordingly:</p>
<br>
<p><img loading="lazy" class="aligncenter wp-image-2148 size-full" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/05/10194235/Screen-Shot-2016-05-10-at-3.01.32-PM.png" alt="Screen Shot 2016-05-10 at 3.01.32 PM" width="413" height="710" srcset="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/05/10194235/Screen-Shot-2016-05-10-at-3.01.32-PM.png 413w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/05/10194235/Screen-Shot-2016-05-10-at-3.01.32-PM-175x300.png 175w" sizes="(max-width: 413px) 100vw, 413px"></p>
<p>&nbsp;</p>
</div>
<p>Note that all content adjusts, including the date grain in the horizontal bar chart and the title “Last Year”:</p>
<br>
<p><img loading="lazy" class="aligncenter wp-image-2149 size-large" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/05/10194235/Screen-Shot-2016-05-10-at-3.04.49-PM-1024x762.png" alt="Screen Shot 2016-05-10 at 3.04.49 PM" width="1024" height="762" srcset="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/05/10194235/Screen-Shot-2016-05-10-at-3.04.49-PM-1024x762.png 1024w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/05/10194235/Screen-Shot-2016-05-10-at-3.04.49-PM-300x223.png 300w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/05/10194235/Screen-Shot-2016-05-10-at-3.04.49-PM-768x572.png 768w, https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/05/10194235/Screen-Shot-2016-05-10-at-3.04.49-PM.png 1061w" sizes="(max-width: 1024px) 100vw, 1024px"></p>
<div class="small-pad-bottom">The user&nbsp;should only need to edit the “Date Range Filter” column, and as such only has the options listed in the “Date Range Filter Options Column”. Any edits outside of this first column could result in undesired results.</div>
<br>
<h3 class="doc-row-title">Additional help</h3>
<div class="small-pad-bottom">
<p>Need additional assistance? Visit the <a href="https://dojo.domo.com/apps">Domo Community</a></p>
</div>
</div>
</div>
</div>
<p></p>            </div>
