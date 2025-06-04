The checklist below will help in preparation to submit your apps to the Domo Appstore. Using this checklist will help prevent unnecessary app resubmissions and ensure faster approvals.

<hr />

<h4><span style="color: #99ccee;"><strong>Security (for App Dev Framework </strong></span><span style="color: #99ccee;"><strong>Apps only)</strong></span></h4>
<strong><span style="color: #333333;">Required:</span></strong>
<ul>
 	<li>Results from ESLint scan: no errors and/or warning allowed using the AirBnB rules configuration (<a href="https://www.npmjs.com/package/eslint-config-airbnb" target="_blank" rel="noopener">https://www.npmjs.com/package/eslint-config-airbnb</a>). Save results to 'lint_results.txt' in app main directory.</li>
 	<li>List of external libraries (name, version number, URI, and publisher) and other hosted resources in this application. Save this list as 'external_resources.txt' in the app main directory.</li>
 	<li>List of external data sources (source name, URI, publisher, justification) that are not routed through a Domo Connector, along with description of how this data is used. Save this list as 'external_datasources.txt' in the app main directory.</li>
 	<li>List of external resources or applications used to record, intercept, store, or process Domo or customer data, or used to access the Domo API. This includes UX analysis services such as SumoMe and Adobe Analytics. Save this list as 'external_services.txt' in the app main directory.</li>
 	<li>Security point-of-contact (POC) to field Domo inquiries and address concerns. Save this information as 'contacts.txt' in the app main directory.</li>
</ul>
&nbsp;
<h4><span style="color: #99ccee;"><strong>Metadata and Content</strong></span></h4>
<strong>Required:</strong>

- Name
- Subtitle
- Who is this app for?
- Setup effort
- Benefits—must be 75 characters each; max of 4
- Tags—check the [list of supported tags](../Domo-Marketplace/marketplace-data-resources.md#supported-tags) for details
- Description—must address the main business question and include high-level application of the app; check [Domo Appstore Requirements](../Domo-Marketplace/marketplace-requirements.md) for more details
- Icon—resolution must be 512 x 512
- Screenshots—resolution at least 1920 x 1080
- Video—should be less than 120 seconds
- Proof the app for spelling and grammar
- Professional—must not contain offensive or inappropriate language or content

<h4><strong><span style="color: #99ccee;">Data</span></strong></h4>
<strong>Required:</strong>
<ul>
 	<li>Beastmodes—if used, should not include scripts</li>
 	<li>DataFlow input—inputs cannot be another dataflow</li>
 	<li>DataFlows—if used should run in less than 1 hour</li>
 	<li>All sample data must be fictitious</li>
 	<li>Dataset names must begin with 'SAMPLE_' in their name</li>
</ul>
<strong>Recommended:</strong>
<ul>
 	<li>Webforms containing sample data should not exceed 1000 rows</li>
 	<li>DataFlows, if used, should include a detailed description</li>
 	<li>DataFlows, if used, should contain SQL comments to aid in understanding intentions</li>
</ul>

<hr />
