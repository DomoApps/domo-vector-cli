---
stoplight-id: c9db4daa8edfe
---

# Appstore Requirements

Every tool in Domo's Appstore has specific requirements. Please review the requirements before submission to the Appstore in order to ensure that the app is submitted without complications.

<img class="alignnone size-full" src="https://web-assets.domo.com/miyagi/images/product/product-feature-appstore-overview-all-apps-2x.png" width="1100" height="" />

## App Submission Requirements

All apps must adhere to Domo’s security requirements. Additionally, if an app is submitted to the Appstore it must adhere to Domo’s content, layout, data, support, and metadata requirements.

### Content
#### **Required**
1. App should clearly answer a business question
2. Business question needs to be stated in the collection title along with a description (Card Builder)
3. Text should be clear, concise, professional, and error free
4. No pornographic images or use of offensive or violent language
5. No capturing or storing personal identifiable information from app users

### Data
*Datasets that are pulled through Domo connectors or manually provided in a webform must adhere to Domo's standards. Datasets using DataFlows and Beast Modes must also follow the requirements listed below:*

#### **Required**

- Connectors, if used, should be supported by the Domo Appstore. See [supported connectors](#supported-connectors) for a list.
- DataFlows, if used, should NOT use their output dataset as an input (e.g., recursive DataFlows)
- DataFlows, if used, should NOT use the output dataset of another dataflow as an input
- DataFlows, if used, should use index fields appropriately when performing joins
- If webforms are used to power visualizations, all data must be sample fictitious data. No live data
 	- Beast Modes, if used, should not contain scripts
 	- DataFlows, if used, must run in less than 1 hour
 	- Data must be fictitious and must not include any sensitive data including: patient health data, personal financial data, insurance data, etc

#### **Recommended**
- Webforms containing sample data should not exceed 1,000 rows
- DataFlows, if used, should include a detailed description
- DataFlows, if used, should use SQL comments to aid in understanding intentions

### Layout
*Apps submitted to the Domo Appstore must follow Domo's minimum design and layout standards. Please ensure that your app adheres to the following:*

#### **Required**
- App should be built on a single page
- Collections should include a description
- App should not contain sub-pages
- Page should contain at least 1 app but no more than 75 total cards
- Apps can be submitted with a mixture of Card Builder, Design Studio, or Dev Studio cards on a page as a single app
- Every card in the App should be contained in one or more collections with the main business questions clearly stated in the collection titles
- Sumo, Notebook, Doc, Image, or Poll cards are not supported

#### **Recommended**
- Card descriptions should; 1) Describe the chart elements, 2) List the cards Key Business Requirement (KBR), and 3) Explain the strategic importance of the card
- Card collections should include a description
- Axis labels (if applicable) should describe the values being measured
- Where appropriate, hover values should be formatted (i.e. $, %, 0.00)
- The summary number title should contain the item being measured, and be short and concise
- Consider using drill paths to answer the next question a business user would logically ask

### Support
*App Publishers are required to provide ongoing customer support for apps they develop. Please ensure you are prepared with the following:*

#### **Required**
- Must provide a customer support email address and website
- Must respond to any customer contacts within 1 hour

#### **Recommended**
- Provide a support phone number

### App Metadata
*When submitting Apps to the Domo Appstore, App Publishers will be required to provide supporting information that will be used to populate the app detail page. Please ensure that the following items are created before you submit your App to the Domo Appstore:*

#### **Required**
1. App must contain a title
2. App must have an icon that adheres to the following:
	- PNG format
	- Resolution of 512px x 512px that is viewable down to 32px x 32px
	- Should be an abstract representation of the App, not a screenshot
	- Can NOT contain the Domo logo, or any derivative of it
	- Can NOT use Domo's main brand color blue (#99ccee) and white as the primary colors
	- Can NOT be a singular representation of a connector (e.g., Facebook icon)
	- Must comply with other companies branding and trademarks
	- Must be unique. You cannot use the same icon for multiple Apps
3. App must have Supported Tags for the following areas:
	- Industry
	- Department
	- Business Role
	- Activity
4. App must have a screenshot of solution with a resolution at least 1920x1080 pixels. (All Data must be fictitious)</li>
5. App must have a description with the following:
 	- A detailed description
 	- Main Business Questions addressed
 	- Credential Requirements
 	- Notes

## Supported Connectors
Below is a list of currently supported connectors by Domo’s Appstore:
<table style="border-collapse: collapse; width: 100%;" border="0">
<tbody>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Adobe Analytics</td>
<td style="width: 33.3333%; height: 24px;">Amazon MWS</td>
<td style="width: 33.3333%; height: 24px;">Associated Press</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">AWS Billing</td>
<td style="width: 33.3333%; height: 24px;">BambooHR</td>
<td style="width: 33.3333%; height: 24px;">BaseCamp</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Bazaarvoice</td>
<td style="width: 33.3333%; height: 24px;">Bing Ads</td>
<td style="width: 33.3333%; height: 24px;">Bitly</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Blue Hornet</td>
<td style="width: 33.3333%; height: 24px;">Box Analytics</td>
<td style="width: 33.3333%; height: 24px;">Bureau of Labor Statistics</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Cloud Health</td>
<td style="width: 33.3333%; height: 24px;">CNN RSS</td>
<td style="width: 33.3333%; height: 24px;">Comscore</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Conductor Searchlight</td>
<td style="width: 33.3333%; height: 24px;">Data.Gov</td>
<td style="width: 33.3333%; height: 24px;">Desk</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Docusign</td>
<td style="width: 33.3333%; height: 24px;">DropBox for Business</td>
<td style="width: 33.3333%; height: 24px;">EchoSign</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Eloqua</td>
<td style="width: 33.3333%; height: 24px;">Emma</td>
<td style="width: 33.3333%; height: 24px;">ExactTarget</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Facebook</td>
<td style="width: 33.3333%; height: 24px;">Facebook Ads</td>
<td style="width: 33.3333%; height: 24px;">Fitbit</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Fluid Survey</td>
<td style="width: 33.3333%; height: 24px;">Flurry</td>
<td style="width: 33.3333%; height: 24px;">FourSquare</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Google Analytics</td>
<td style="width: 33.3333%; height: 24px;">Google BigQuery</td>
<td style="width: 33.3333%; height: 24px;">Google+ Connector</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Hubspot</td>
<td style="width: 33.3333%; height: 24px;">Instagram</td>
<td style="width: 33.3333%; height: 24px;">Intacct</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Jira</td>
<td style="width: 33.3333%; height: 24px;">LinkedIn</td>
<td style="width: 33.3333%; height: 24px;">Lithium</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Loggly</td>
<td style="width: 33.3333%; height: 24px;">MailChimp</td>
<td style="width: 33.3333%; height: 24px;">Marketo Oauth</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Meetup</td>
<td style="width: 33.3333%; height: 24px;">NetSuite JDBC</td>
<td style="width: 33.3333%; height: 24px;">New Relic</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">NOAA Weather</td>
<td style="width: 33.3333%; height: 24px;">NOAA Weather Alerts</td>
<td style="width: 33.3333%; height: 24px;">Ooyala</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Open Exchange Rates</td>
<td style="width: 33.3333%; height: 24px;">Outbrain</td>
<td style="width: 33.3333%; height: 24px;">Pager Duty</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Pardot</td>
<td style="width: 33.3333%; height: 24px;">Picasa</td>
<td style="width: 33.3333%; height: 24px;">Pipedrive</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Qualtrics</td>
<td style="width: 33.3333%; height: 24px;">Quandl</td>
<td style="width: 33.3333%; height: 24px;">QuickBase</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">QuickBooks Online</td>
<td style="width: 33.3333%; height: 24px;">Radian6</td>
<td style="width: 33.3333%; height: 24px;">RallySoftware</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Rotten Tomatoes</td>
<td style="width: 33.3333%; height: 24px;">RunKeeper</td>
<td style="width: 33.3333%; height: 24px;">SailThru</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Salesforce</td>
<td style="width: 33.3333%; height: 24px;">ServiceNow</td>
<td style="width: 33.3333%; height: 24px;">Shopify</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">SmartSheet</td>
<td style="width: 33.3333%; height: 24px;">Squareup</td>
<td style="width: 33.3333%; height: 24px;">Strava</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">SugarCRM</td>
<td style="width: 33.3333%; height: 24px;">Sumo Logic</td>
<td style="width: 33.3333%; height: 24px;">SurveyGizmo</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">SurveyMonkey</td>
<td style="width: 33.3333%; height: 24px;">Taleo</td>
<td style="width: 33.3333%; height: 24px;">Toggl</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Trello</td>
<td style="width: 33.3333%; height: 24px;">Tumblr</td>
<td style="width: 33.3333%; height: 24px;">Twilio</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Twitter</td>
<td style="width: 33.3333%; height: 24px;">Twitter Ads</td>
<td style="width: 33.3333%; height: 24px;">Velocify</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Vimeo</td>
<td style="width: 33.3333%; height: 24px;">Webtrends</td>
<td style="width: 33.3333%; height: 24px;">Workfront</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Yammer</td>
<td style="width: 33.3333%; height: 24px;">Zendesk</td>
<td style="width: 33.3333%; height: 24px;">Zoo CRM</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Zuora</td>
<td style="width: 33.3333%; height: 24px;"></td>
<td style="width: 33.3333%; height: 24px;"></td>
</tr>
</tbody>
</table>

## Supported Tags
The Tag field in the App submission form currently allows entries from 5 areas: Industry, Department, Business Role, Activity, and Connectors that are supported by the App. Please choose the tags that are relevant for your App from the lists below:

&nbsp;
#### **Industry**

<table style="border-collapse: collapse; width: 100%;" border="0">
<tbody>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">All Industries</td>
<td style="width: 33.3333%; height: 24px;">Aerospace &amp; Defense</td>
<td style="width: 33.3333%; height: 24px;">Agriculture</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Automotive</td>
<td style="width: 33.3333%; height: 24px;">Communications</td>
<td style="width: 33.3333%; height: 24px;">Construction</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Consumer Goods</td>
<td style="width: 33.3333%; height: 24px;">Education</td>
<td style="width: 33.3333%; height: 24px;">Energy</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Environmental Services</td>
<td style="width: 33.3333%; height: 24px;">Financial Services</td>
<td style="width: 33.3333%; height: 24px;">Healthcare &amp; Health</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">High Tech</td>
<td style="width: 33.3333%; height: 24px;">Hotel &amp; Restaurant</td>
<td style="width: 33.3333%; height: 24px;">Insurance</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Life Sciences</td>
<td style="width: 33.3333%; height: 24px;">Logistics &amp; Freight</td>
<td style="width: 33.3333%; height: 24px;">Manufacturing</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Media</td>
<td style="width: 33.3333%; height: 24px;">Non Profit Organization</td>
<td style="width: 33.3333%; height: 24px;">Pro Services</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Public Sector</td>
<td style="width: 33.3333%; height: 24px;">Real Estate</td>
<td style="width: 33.3333%; height: 24px;">Retail</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Sports &amp; Leisure</td>
<td style="width: 33.3333%; height: 24px;">Travel &amp; Transport</td>
<td style="width: 33.3333%; height: 24px;">Utilities</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Wine &amp; Beer</td>
<td style="width: 33.3333%; height: 24px;">Other Industry</td>
<td style="width: 33.3333%; height: 24px;"></td>
</tr>
</tbody>
</table>

#### **Department**

<table style="border-collapse: collapse; width: 100%;" border="0">
<tbody>
<tr>
<td style="width: 33.3333%;">All Departments</td>
<td style="width: 33.3333%;">Customer Service</td>
<td style="width: 33.3333%;">Finance</td>
</tr>
<tr>
<td style="width: 33.3333%;">Human Resources</td>
<td style="width: 33.3333%;">IT</td>
<td style="width: 33.3333%;">Marketing</td>
</tr>
<tr>
<td style="width: 33.3333%;">Operations</td>
<td style="width: 33.3333%;">Sales</td>
<td style="width: 33.3333%;">Other Department</td>
</tr>
</tbody>
</table>
<h4></h4>
&nbsp;

#### **Business Role**
<table style="border-collapse: collapse; width: 100%;" border="0">
<tbody>
<tr>
<td style="width: 33.3333%;">CEO / President</td>
<td style="width: 33.3333%;">CMO / VP Marketing</td>
<td style="width: 33.3333%;">CFO / VP Finance</td>
</tr>
<tr>
<td style="width: 33.3333%;">CRO / VP Sales</td>
<td style="width: 33.3333%;">CIO / VP IT</td>
<td style="width: 33.3333%;">CTO / VP Engineering</td>
</tr>
<tr>
<td style="width: 33.3333%;">COO / VP Operations</td>
<td style="width: 33.3333%;">Analytics Executive</td>
<td style="width: 33.3333%;">VP HR</td>
</tr>
<tr>
<td style="width: 33.3333%;">VP – Other</td>
<td style="width: 33.3333%;">Director</td>
<td style="width: 33.3333%;">Manager</td>
</tr>
<tr>
<td style="width: 33.3333%;">Analyst</td>
<td style="width: 33.3333%;">Consultant</td>
<td style="width: 33.3333%;">Other Role</td>
</tr>
</tbody>
</table>
&nbsp;

#### **Activity**

<table style="border-collapse: collapse; width: 100%;" border="0">
<tbody>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Accounts Receivable</td>
<td style="width: 33.3333%; height: 24px;">Accounts Payable</td>
<td style="width: 33.3333%; height: 24px;">Asset Management</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">BI</td>
<td style="width: 33.3333%; height: 24px;">Business Analytics</td>
<td style="width: 33.3333%; height: 24px;">Business Automation</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Call Center</td>
<td style="width: 33.3333%; height: 24px;">Cloud Operations</td>
<td style="width: 33.3333%; height: 24px;">Consulting Services</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Conversion Funnel</td>
<td style="width: 33.3333%; height: 24px;">Creative Management</td>
<td style="width: 33.3333%; height: 24px;">CRM</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Customer Sentiment</td>
<td style="width: 33.3333%; height: 24px;">Customer Acquisition</td>
<td style="width: 33.3333%; height: 24px;">Data ETL</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Data Visualization</td>
<td style="width: 33.3333%; height: 24px;">Digital Marketing</td>
<td style="width: 33.3333%; height: 24px;">Document Management</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">E-commerce</td>
<td style="width: 33.3333%; height: 24px;">Employee Onboarding</td>
<td style="width: 33.3333%; height: 24px;">ERP</td>
</tr>
<tr>
<td style="width: 33.3333%;">Events</td>
<td style="width: 33.3333%;">Facilities</td>
<td style="width: 33.3333%;">Financial Planning</td>
</tr>
<tr>
<td style="width: 33.3333%;">Helpdesk</td>
<td style="width: 33.3333%;">Market Research</td>
<td style="width: 33.3333%;">Payment Processing</td>
</tr>
<tr>
<td style="width: 33.3333%;">Payroll</td>
<td style="width: 33.3333%;">Predictive Analysis</td>
<td style="width: 33.3333%;">Product Development</td>
</tr>
<tr>
<td style="width: 33.3333%;">Recruiting &amp; Hiring</td>
<td style="width: 33.3333%;">Sales Operations</td>
<td style="width: 33.3333%;">Security</td>
</tr>
<tr>
<td style="width: 33.3333%;">Social Media</td>
<td style="width: 33.3333%;">Supply Chain</td>
<td style="width: 33.3333%;">Talent Management</td>
</tr>
<tr>
<td style="width: 33.3333%;">Territory Management</td>
<td style="width: 33.3333%;">Ticket Resolution</td>
<td style="width: 33.3333%;">Web Analytics</td>
</tr>
<tr>
<td style="width: 33.3333%;">Other Activity</td>
<td style="width: 33.3333%;"></td>
<td style="width: 33.3333%;"></td>
</tr>
</tbody>
</table>
&nbsp;

#### **Connector**

<table style="border-collapse: collapse; width: 100%;" border="0">
<tbody>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Adobe Analytics</td>
<td style="width: 33.3333%; height: 24px;">Associated Press</td>
<td style="width: 33.3333%; height: 24px;">BambooHR</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Basecamp</td>
<td style="width: 33.3333%; height: 24px;">Bazaarvoice</td>
<td style="width: 33.3333%; height: 24px;">Bing Ads</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Box</td>
<td style="width: 33.3333%; height: 24px;">Box Analytics</td>
<td style="width: 33.3333%; height: 24px;">CNN</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">ConductorSearchlight</td>
<td style="width: 33.3333%; height: 24px;">DocuSign</td>
<td style="width: 33.3333%; height: 24px;">Dropbox For Business</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">EchoSign</td>
<td style="width: 33.3333%; height: 24px;">Eloqua</td>
<td style="width: 33.3333%; height: 24px;">Emma</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">ExactTarget</td>
<td style="width: 33.3333%; height: 24px;">Facebook</td>
<td style="width: 33.3333%; height: 24px;">Fitbit</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Fluid Surveys</td>
<td style="width: 33.3333%; height: 24px;">Foursquare</td>
<td style="width: 33.3333%; height: 24px;">Google Analytics</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Google+</td>
<td style="width: 33.3333%; height: 24px;">HubSpot</td>
<td style="width: 33.3333%; height: 24px;">Instagram</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">JIRA</td>
<td style="width: 33.3333%; height: 24px;">Labor Statistics</td>
<td style="width: 33.3333%; height: 24px;">LinkedIn</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Lithium</td>
<td style="width: 33.3333%; height: 24px;">Loggly</td>
<td style="width: 33.3333%; height: 24px;">MailChimp</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Marketo</td>
<td style="width: 33.3333%; height: 24px;">Meetup</td>
<td style="width: 33.3333%; height: 24px;">NOAA Weather</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">NetSuite</td>
<td style="width: 33.3333%; height: 24px;">New Relic</td>
<td style="width: 33.3333%; height: 24px;">Open Exchange Rates</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Outbrain</td>
<td style="width: 33.3333%; height: 24px;">PagerDuty</td>
<td style="width: 33.3333%; height: 24px;">Picasa</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Pipedrive</td>
<td style="width: 33.3333%; height: 24px;">Qualtrics</td>
<td style="width: 33.3333%; height: 24px;">Quandl</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">QuickBooks</td>
<td style="width: 33.3333%; height: 24px;">Rally Software</td>
<td style="width: 33.3333%; height: 24px;">Rotten Tomatoes</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">RunKeeper</td>
<td style="width: 33.3333%; height: 24px;">Salesforce</td>
<td style="width: 33.3333%; height: 24px;">Salesforce Desk</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Salesforce Pardot</td>
<td style="width: 33.3333%; height: 24px;">Salesforce Radian6</td>
<td style="width: 33.3333%; height: 24px;">Shopify</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Square</td>
<td style="width: 33.3333%; height: 24px;">Strava</td>
<td style="width: 33.3333%; height: 24px;">SugarCRM</td>
</tr>
<tr style="height: 24px;">
<td style="width: 33.3333%; height: 24px;">Sumo Logic</td>
<td style="width: 33.3333%; height: 24px;">SurveyGizmo</td>
<td style="width: 33.3333%; height: 24px;">SurveyMonkey</td>
</tr>
<tr>
<td style="width: 33.3333%;">Taleo</td>
<td style="width: 33.3333%;">Toggl</td>
<td style="width: 33.3333%;">Trello</td>
</tr>
<tr>
<td style="width: 33.3333%;">Twilio</td>
<td style="width: 33.3333%;">Twitter</td>
<td style="width: 33.3333%;">Twitter Ads</td>
</tr>
<tr>
<td style="width: 33.3333%;">Velocify</td>
<td style="width: 33.3333%;">Vimeo</td>
<td style="width: 33.3333%;">Webtrends</td>
</tr>
<tr>
<td style="width: 33.3333%;">Workfront</td>
<td style="width: 33.3333%;">Yammer</td>
<td style="width: 33.3333%;">Zendesk</td>
</tr>
<tr>
<td style="width: 33.3333%;">Zuora</td>
<td style="width: 33.3333%;">comScore</td>
<td style="width: 33.3333%;"></td>
</tr>
</tbody>
</table>
&nbsp;

### Input Validation
- There should be a centralized input validation routine for the application
- Specify proper character sets, such as UTF-8, for all sources of input
- Encode data to a common character set before validating (Canonicalize)
- All validation failures should result in input rejection
- Determine if the system supports UTF-8 extended character sets and if so, validate after UTF-8 decoding is completed
- Validate all client provided data before processing, including all parameters, URLs and HTTP header content (e.g. Cookie names and values). Be sure to include automated post backs from JavaScript
- Verify that header values in both requests and responses contain only ASCII characters
- Validate data from redirects (An attacker may submit malicious content directly to the target of the redirect, thus circumventing application logic and any validation performed before the redirect)
- Validate for expected data types
- Validate data range
- Validate data length
- Validate all input against a "white" list of allowed characters, whenever possible
- If any potentially hazardous characters must be allowed as input, be sure that you implement additional controls like output encoding, secure task specific APIs and accounting for the utilization of that data throughout the application. Examples of common hazardous characters include: &lt; &gt; " ' % ( ) &amp; + ' "
- If your standard validation routine cannot address the following inputs, then they should be checked discretely
 	- Check for null bytes (%00)
 	- Check for new line characters (%0d, %0a, r, n)
- Check for "dot-dot-slash" (../ or ..) path alterations characters. In cases where UTF-8 extended character set encoding is supported, address alternate representation like: %c0%ae%c0%ae/

### Output Encoding
- Encode all characters unless they are known to be safe for the intended interpreter
- Contextually sanitize all output of un-trusted data to queries for SQL, XML, and LDAP

### Session Management
- Set the domain and path for cookies to an appropriately restricted value for the site
- Close functionality should fully terminate the associated session or connection
- Establish a session inactivity timeout that is as short as possible, based on balancing risk and business functional requirements. In most cases it should be no more than several hours
- Do not expose session identifiers in URLs, error messages or logs. Session identifiers should only be located in the HTTP cookie header. For example, do not pass session identifiers as GET parameters
- Generate a new session identifier and deactivate the old one periodically. (This can mitigate certain session hijacking scenarios where the original identifier was compromised)
- Set the "secure" attribute for cookies transmitted over an TLS connection
- Set cookies with the HttpOnly attribute, unless you specifically require client-side scripts within your application to read or set a cookie's value

### Access Control
- Enforce application logic flows to comply with business rules
- Limit the number of transactions a single user or device can perform in a given period of time. The transactions/time should be above the actual business requirement, but low enough to deter automated attacks
- Use the "referrer" header as a supplemental check only, it should never be the sole authorization check, as it can be spoofed

### Error Handling and Logging
- Do not disclose sensitive information in error responses, including system details, session identifiers or account information
- Use error handlers that do not display debugging or stack trace information
- Implement generic error messages and use custom error pages
- The application should handle application errors and not rely on the server configuration
- Properly free allocated memory when error conditions occur
- Error handling logic associated with security controls should deny access by default
- Logging controls should support both success and failure of specified security events
- Utilize a master routine for all logging operations

### Data Protection
- Implement least privilege, restrict users to only the functionality, data and system information that is required to perform their tasks
- Do not store passwords, connection strings or other sensitive information in clear text or in any no cryptographically secure manner on the client side
- Remove comments in user accessible production code that may reveal backend system or other sensitive information
- Remove unnecessary application and system documentation as this can reveal useful information to attackers
- Do not include sensitive information in HTTP GET request parameters
- Disable client side caching on pages containing sensitive information. Cache-Control: no-store, may be used in conjunction with the HTTP header control "Pragma: no-cache", which is less effective, but is HTTP/1.0 backward compatible
- The application should support the removal of sensitive data when that data is no longer required. (e.g. personal information or certain financial data)

### Communication Security
- Implement encryption for the transmission of all sensitive information
- TLS certificates should be valid and have the correct domain name, not be expired, and be installed with intermediate certificates when required
- Failed TLS connections should not fall back to an insecure connection
- Utilize TLS connections for all content requiring authenticated access and for all other sensitive information
- Utilize TLS for connections to external systems that involve sensitive information or functions
- Utilize a single standard TLS implementation that is configured appropriately
- Specify character encodings for all connections
- Filter parameters containing sensitive information from the HTTP referrer, when linking to external sites

### System Configuration
- When exceptions occur, fail securely
- Remove all unnecessary functionality and files
- Remove test code or any functionality not intended for production, prior to deployment
- Define which HTTP methods, (Get or Post only), the application will support and whether it will be handled differently in different pages in the application

### Database Security
- Utilize input validation and output encoding and be sure to address meta characters. If these fail, do not run the database command
- Ensure that variables are strongly typed/encoded

### File Management
- Do not pass user supplied data directly to any dynamic include function
- Do not pass user supplied data into a dynamic redirect. If this must be allowed, then the redirect should accept only validated, relative path URLs
- Do not pass directory or file paths, use index values mapped to pre-defined list of paths

### Memory Management
- Utilize input and output control for un-trusted data
- Double check that the buffer is as large as specified
- When using functions that accept a number of bytes to copy, such as strncpy(), be aware that if the destination buffer size is equal to the source buffer size, it may not NULL-terminate the string
- Check buffer boundaries if calling the function in a loop and make sure there is no danger of writing past the allocated space
- Truncate all input strings to a reasonable length before passing them to the copy and concatenation functions
- Specifically close resources don’t rely on garbage collection. (e.g., connection objects, file handles, etc.)
- Properly free allocated memory upon the completion of functions and at all exit points (arrays, etc.)

### General Coding Practices
- Explicitly initialize all your variables and other data stores, either during declaration or just before the first usage
- Avoid calculation errors by understanding your programming language's underlying representation and how it interacts with numeric calculation. Pay close attention to byte size discrepancies, precision, signed/unsigned distinctions, truncation, conversion and casting between types, "not-a-number" calculations, and how your language handles numbers that are too large or too small for its underlying representation
- Do not pass user supplied data to any dynamic execution function
- Restrict users from generating new code or altering existing code
- Review all secondary applications, third party code and libraries to determine business necessity and validate safe functionality, as these can introduce new vulnerabilities
