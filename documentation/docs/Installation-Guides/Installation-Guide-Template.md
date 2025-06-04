---
stoplight-id: qosb8bvjtrepd
---

<div class="col-md-12 content-panel">
                <h2>Installation Guide Template</h2>
                <p></p><p>Thanks for installing and test-driving <span id="title">Customer Satisfaction</span>! This guide is intended to help you connect this app with your own data. The first step is to ensure that your data follows the same schema (or structure) of the sample datasets that currently power the App. Fortunately, Domo has created some powerful data transformation tools to help, along with the step-by-step instructions provided below.</p>
<table>
<tbody>
<tr>
<td><strong>Publisher Name:</strong></td>
<td>Domo</td>
</tr>
<tr>
<td><strong>Support Email:</strong></td>
<td>support@domo.com</td>
</tr>
<tr>
<td><strong>Support Phone:</strong></td>
<td>801-805-9505</td>
</tr>
<tr>
<td><strong>Support Web Address:</strong></td>
<td><a href="http://www.domo.com/client-services/domo-support" target="_blank">www.domo.com/client-services/domo-support</a></td>
</tr>
</tbody>
</table>
<div id="Step%201:%20Identify%20Required%20Data%20Fields" class="doc-row">
<h3 class="doc-row-title">Step 1: Prepare Your Data</h3>
<div class="small-pad-bottom">
<p>The first step in connecting this app to your own data is ensuring you have the required&nbsp;datasets in Domo.</p>
<h4>Connector Datasets</h4>
</div>
<div class="small-pad-bottom">
<p>This app uses the following reports&nbsp;from Domo’s standard connectors. &nbsp;To connect this app to your own data you’ll need to ensure that you have proper access and/or credentials to these&nbsp;reports before connecting this app to your data:</p>
<table>
<tbody>
<tr>
<td><strong>Connector Report Name</strong></td>
<td><strong>Connector Name</strong></td>
<td><strong>Current&nbsp;Dataset Name (Sample Data)</strong></td>
</tr>
<tr>
<td>Page Likes</td>
<td>Facebook</td>
<td>&nbsp;Facebook Likes_234</td>
</tr>
<tr>
<td>Posts</td>
<td>Facebook</td>
<td>&nbsp;Facebook Posts_234</td>
</tr>
</tbody>
</table>
<h4>&nbsp;<strong>Custom Datasets</strong></h4>
<p>This app requires creating the following custom datasets. To do this, you’ll need to ensure that you have each of these fields in Domo. Then you’ll need to use transforms to create datasets that follow the exact structure or schema of the datasets below. &nbsp;For help with Dataflows, Magic ETL or BeastModes, please visit <a href="https://university.domo.com/" target="_blank">Domo University</a> within Domo.</p>
<div id="custom-data-container">
<table id="SAMPLE_Customer-Satisfaction">
<tbody>
<tr>
<td colspan="3"><strong>DataSet Name:</strong></td>
<td class="value" colspan="3">SAMPLE_Customer Satisfaction</td>
</tr>
<tr>
<td colspan="3"><strong>What is the DataSet used for?</strong></td>
<td class="value" colspan="3">unknown</td>
</tr>
<tr>
<td colspan="6"></td>
</tr>
<tr>
<td><strong>Field Name</strong></td>
<td><strong>Data Type</strong></td>
<td><strong>Report Name / Object Name</strong></td>
<td><strong>Source </strong></td>
<td colspan="2"><strong>Description of Field</strong></td>
</tr>
<tr>
<td>AS_OF_rolling_DATE</td>
<td>DATE</td>
<td>SAMPLE_Customer Satisfaction</td>
<td>Salesforce Desk,Zendesk</td>
<td colspan="2">Date of tracked metrics</td>
</tr>
<tr>
<td>Agent</td>
<td>STRING</td>
<td>SAMPLE_Customer Satisfaction</td>
<td>Salesforce Desk,Zendesk</td>
<td colspan="2">Agent</td>
</tr>
<tr>
<td>Helpdesk Location</td>
<td>STRING</td>
<td>SAMPLE_Customer Satisfaction</td>
<td>Salesforce Desk,Zendesk</td>
<td colspan="2">Helpdesk location</td>
</tr>
<tr>
<td>Helpdesk Team</td>
<td>STRING</td>
<td>SAMPLE_Customer Satisfaction</td>
<td>Salesforce Desk,Zendesk</td>
<td colspan="2">Helpdesk team</td>
</tr>
<tr>
<td>Manager</td>
<td>STRING</td>
<td>SAMPLE_Customer Satisfaction</td>
<td>Salesforce Desk,Zendesk</td>
<td colspan="2">Name of manager</td>
</tr>
<tr>
<td>Ticket Marketing Channel</td>
<td>STRING</td>
<td>SAMPLE_Customer Satisfaction</td>
<td>Salesforce Desk,Zendesk</td>
<td colspan="2">Ticket marketing channel</td>
</tr>
<tr>
<td>Customer Satisfaction Score_amount</td>
<td>LONG</td>
<td>SAMPLE_Customer Satisfaction</td>
<td>Salesforce Desk,Zendesk</td>
<td colspan="2">Customer satisfaction score</td>
</tr>
</tbody>
</table>
<h3 class="doc-row-title"></h3>
<h3 class="doc-row-title">Step 2: Connect the App to Your&nbsp;Data</h3>
<div class="small-pad-bottom">
<div class="small-pad-bottom">
<div class="small-pad-bottom">
<p>Once you’ve finished preparing your data as outlined in Step 1 you’re ready to connect it to your app. &nbsp;To do this, go to the page in Domo where the app is&nbsp;installed and click the “CONNECT YOUR DATA” button at the top of the page.</p>
</div>
</div>
<p><img loading="lazy" class="alignnone size-full wp-image-1207" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/03/14155707/Screen-Shot-2016-03-14-at-3.52.48-PM1.png" alt="Screen Shot 2016-03-14 at 3.52.48 PM" width="1158" height="71"></p>
<h3 class="doc-row-title"></h3>
<div class="small-pad-bottom"></div>
</div>
</div>
</div>
</div>
<p></p>            </div>
