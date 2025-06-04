---
stoplight-id: edfe96df76c42
---

# Publish Connector

After you have written and tested your connector, you are ready for publishing! You can choose to make the connector only available to your private company or available to any Domo user. Follow the guide below to submit the connector for approval. Once approved, your connector is ready to go!

### Submit for Publishing
---
<ol>
 	<li>Click <strong>Submit</strong>. Domo automatically checks your connector for some required work and notifies you of any missing fields. If everything checks out, the Connector Submission modal will appear.</li>
</ol>

<img src="https://developer.domo.com/wp-content/uploads/2017/03/Connector-Submission-Old-image.png" alt=""  />

<ol start="2">
 	<li>In the <strong>Additional Instructions</strong> field, include any information needed to test and validate your connector. If your connector uses OAuth 2 for validation, please include a username and password. Our engineers will only use these for testing and validation.</li>
 	<li>Select your connector visibility.
<ul>
 	<li>Select <strong>Shared with your company</strong> to keep the connector for exclusive use in your company's Domo instance. The connector will not be listed on the Data Center page; a private URL is provided for accessing the connector. If you select this option, you will also have the option to self-publish the connector for 14 days, allowing you to personally review and test a beta version of the connector.</li>
 	<li>Select <strong>Public to all companies</strong> to make your connector available to all Domo users.</li>
</ul>
</li>
 	<li>Click <strong>Continue Submission</strong>.
<ul>
 	<li>If you chose to make your connector public: <strong>Congratulations!</strong> You’ve successfully submitted your connector. Domo will begin the 30-day review process and will contact you with any questions.</li>
 	<li>If you chose to keep your connector private, continue to <a href="#Self%20Publish%20Your%20Private%20Connector">Self Publish Your Private Connector</a>.</li>
 	<li>The self-publish option is not available for custom connectors that use OAuth 2.0 in the authentication process or use discovery parameter types in Configure Reports / Advanced Mode.</li>
</ul>
</li>
 	<li>Click the <strong>View Status</strong> or the <strong>Overview</strong> tab to see the status of your connector review. You will also be sent email updates about your connector's status in the review process.</li>
</ol>
<img src="https://developer.domo.com/wp-content/uploads/2017/03/Connector-Submission-1.png" alt="" />

<strong>Note</strong>: To withdraw your connector from submission, open the connector. Click <strong>View Status</strong>. In the status window, click <strong>Withdraw</strong>.

### Self Publish Your Private Connector
---
If your custom connector meets the following criteria, your connector could be available for immediate use:
<ul>
 	<li>You are <strong>sharing your custom connector only with your company</strong></li>
 	<li>Your custom connector <strong>does not use OAuth 2.0</strong> in the authentication process</li>
 	<li>Your custom connector <strong>does not use the discovery</strong> parameter type in Configure Reports / Advanced Mode</li>
</ul>
If your connector meets these criteria, you now can choose to self publish. This will allow you to review a beta version of your connector for 30 days while Domo is reviewing your submission.
<ol>
 	<li>After you have submitted your connector for publication, click <strong>Self Publish</strong>. A modal will appear with a URL to a beta version of your connector.</li>
</ol>
<img class="alignnone size-full wp-image-3324" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2017/03/14125350/IDE-4.png" alt=""  />
<ol start="2">
 	<li>Use the URL to access your beta connector. <strong>Well done!</strong> Your connector has now been self-published for Beta review during the Domo review process.</li>
</ol>
<img class="alignnone size-full wp-image-3326" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2017/03/14125522/IDE-6.png" alt="" />

### Review Process
---
Your connector code passes through several phases of review.
<ol>
 	<li><em>Automated Tests</em>: The code is syntax checked, smoke tested, and verified for compliance to policies. We check that:
<ul>
 	<li>XMLHttpRequest is not used. Use httprequest.get() or httprequest.post() instead.</li>
 	<li>Code is not minified.</li>
 	<li>Credentials are not hard coded.</li>
 	<li>Information is not redirected to an external API.</li>
</ul>
</li>
 	<li><em>Security Test</em>: Domo engineers ensure that all security protocols are being followed, in addition to those listed above.</li>
 	<li><em>Performance Tests</em>: Tests are run to make sure that the connector speed relative to the number of records processed is acceptable: over 1000 records per 5 minutes.</li>
 	<li><em>Code review</em>: The code is reviewed by one of our developers to ensure that the code is readable and clean.</li>
</ol>
After your code has passed through every review process, your connector is approved and is either published to all of Domo through the Data Center or privately to the URL provided.

Click <strong>View Status</strong> in the <strong>Develop</strong> tab or select the <strong>Overview</strong> tab to see the status of your connector review. You will also receive email updates about your connector's status in the review process.

### View Code in Read-Only Mode
---
You can view the code (processdata script) in the read-only mode while the connector is submitted for review.

To check the script, click on the <b>View Status</b> tab and then <b>View Code</b>.

<img class="alignnone size-full wp-image-4049" src="https://developer.domo.com/wp-content/uploads/2017/03/View-Code-in-Read-Only-Mode.png" alt="" />



