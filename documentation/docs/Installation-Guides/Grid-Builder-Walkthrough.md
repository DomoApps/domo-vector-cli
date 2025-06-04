---
stoplight-id: iqd31a2msdhon
---

<div class="col-md-12 content-panel">
                <h2>Grid Builder Walkthrough</h2>
                <p></p><p>Welcome to the Grid Builder Walkthrough! In this guide you will learn&nbsp;about each part of the grid builder step-by-step and how each part is&nbsp;used.</p>
<p>The grid builder is basically an instructions sheet used by the dataflows that power our apps. Each column in the grid builder represents an instruction and each row represents a column from your data onto which these instructions will be applied. Let’s go through each column to find out what they do.</p>
<p>But before we do that, here is an example of&nbsp;the Grid Builder:</p>
<table style="height: 792px; border-color: #000000;" width="3603">
<tbody>
<tr>
<td width="96">GridId</td>
<td width="96">GridName</td>
<td width="96">C</td>
<td width="96">SELECT</td>
<td width="96">FROM</td>
<td width="96">WHERE</td>
<td width="96">GROUP BY</td>
<td width="96">AS</td>
<td width="96">Include</td>
<td width="96">JoinType</td>
<td width="96">JoinCondition</td>
<td width="96">MAJIK</td>
<td width="96">FilterId</td>
<td width="96">FilterName</td>
<td width="96">FilterInputType</td>
<td width="96">FilterIsPrimary</td>
<td width="96">FilterIsPrimaryGroup</td>
<td width="96">Description</td>
</tr>
<tr>
<td>1</td>
<td>Scorecard</td>
<td colspan="3">kamaji_calendar(1, @DB)</td>
<td></td>
<td></td>
<td></td>
<td></td>
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
<td>101</td>
<td>Date</td>
<td colspan="2">KAMAJI Calendar</td>
<td></td>
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
<td>102</td>
<td>ThisYear</td>
<td></td>
<td></td>
<td></td>
<td>This Fiscal Year</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td>1</td>
<td>Date Range</td>
<td colspan="2">Single Select</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>103</td>
<td>LastYear</td>
<td></td>
<td></td>
<td></td>
<td>Last Fiscal Year</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>104</td>
<td colspan="2">ThisQuarter</td>
<td></td>
<td></td>
<td>This Fiscal Quarter</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>105</td>
<td colspan="2">LastQuarter</td>
<td></td>
<td></td>
<td>Last Fiscal Quarter</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>106</td>
<td>ThisMonth</td>
<td></td>
<td></td>
<td></td>
<td>This Fiscal Month</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>107</td>
<td>LastMonth</td>
<td></td>
<td></td>
<td></td>
<td>Last Fiscal Month</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>108</td>
<td colspan="2">FMStartDate</td>
<td></td>
<td></td>
<td colspan="2">FMStartDate</td>
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
<td>201</td>
<td>`Rep`</td>
<td colspan="3">Sales Scorecard – Sample</td>
<td>Rep</td>
<td>1</td>
<td>INNER</td>
<td colspan="2">C101 = C205</td>
<td>2</td>
<td>Rep</td>
<td>Multi Select</td>
<td>1</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>202</td>
<td>`Team`</td>
<td></td>
<td></td>
<td></td>
<td>Team</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td>3</td>
<td>Team</td>
<td>Multi Select</td>
<td></td>
<td>1</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>203</td>
<td>`Region`</td>
<td></td>
<td></td>
<td></td>
<td>Region</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td>4</td>
<td>Region</td>
<td>Multi Select</td>
<td></td>
<td>2</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>204</td>
<td>`Role`</td>
<td></td>
<td></td>
<td></td>
<td>Role</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td>5</td>
<td>Role</td>
<td>Multi Select</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>205</td>
<td>`Date`</td>
<td></td>
<td></td>
<td></td>
<td>Date</td>
<td></td>
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
<td>206</td>
<td colspan="2">`Gross Sales`</td>
<td></td>
<td></td>
<td>Gross_Sales</td>
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
<td>207</td>
<td>`Net Sales`</td>
<td></td>
<td></td>
<td></td>
<td>Net_Sales</td>
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
<td>208</td>
<td colspan="2">`New Clients`</td>
<td></td>
<td></td>
<td>New_Clients</td>
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
<td>209</td>
<td colspan="2">`Avg Deal Size`</td>
<td></td>
<td></td>
<td>Avg_Deal_Size</td>
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
<td>210</td>
<td colspan="2">`Quota Attainment`</td>
<td></td>
<td></td>
<td>Quota_Attainment</td>
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
<td>211</td>
<td colspan="2">`Upsell Count`</td>
<td></td>
<td></td>
<td>Upsell_Count</td>
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
<td>212</td>
<td colspan="2">`Renewal Sales`</td>
<td></td>
<td></td>
<td>Renewal_Sales</td>
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
<td>213</td>
<td colspan="2">`Product Sales`</td>
<td></td>
<td></td>
<td>Product_Sales</td>
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
<td>214</td>
<td>`Leads`</td>
<td></td>
<td></td>
<td></td>
<td>Leads</td>
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
<td>215</td>
<td>`Demos`</td>
<td></td>
<td></td>
<td></td>
<td>Demos</td>
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
<td>216</td>
<td>‘ ‘</td>
<td></td>
<td></td>
<td></td>
<td>PhotoUrl</td>
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
</tbody>
</table>
<p>&nbsp;</p>
<p>It may seem like a lot of complicated instructions, but it gets much simpler as we break it down piece by piece.</p>
<p></p><div class="doc-row" id="1.%20The%20GridId%20and%20GridName%20columns">
                                    <h3 class="doc-row-title">1. The GridId and GridName columns</h3><div class="small-pad-bottom"><p>The grid builder takes your data and generates new tables formatted for the app that will use them. The GridId column is used to tell the grid builder when to start a new table, and the GridName column is where we name the tables that are generated. To fill out these columns, enter numbers in descending order on the first row where a new table is being created under GridId, and name your tables on the same row under the GridName column, as seen in the example below:</p>
<table style="height: 625px;" width="776">
<tbody>
<tr>
<td width="96">GridId</td>
<td width="96">GridName</td>
<td width="96">C</td>
<td width="96">SELECT</td>
<td width="96">FROM</td>
</tr>
<tr>
<td>1</td>
<td>opportunity</td>
<td>100</td>
<td>Amount</td>
<td>Opportunity</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>CloseDate</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>CreatedDate</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>Id</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>IsClosed</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>IsWon</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td colspan="2">LastActivityDate</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td colspan="2">LastModifiedDate</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>Probability</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>StageName</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>OwnerId</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>AccountId</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>Name</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>200</td>
<td>Name</td>
<td>User</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>Id</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>opportunity_history</td>
<td>300</td>
<td>CreatedDate</td>
<td>Opportunity History</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>Id</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td colspan="2">OpportunityId</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>StageName</td>
<td></td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<p>Notice that row 1 has a “1” under GridId to go along with “opportunity” in the next column, and row 16 has a “2” under GridId to go along with “opportunity_history” in the next column. That means that this Grid Builder will generate two tables, one called “opportunity” and the other called “opportunity_history”. The data referrenced from rows 1 to 15 will be included in the first table, and the data referrenced from row 16 to the end will be included in the second.</p>
<p><strong>Protip:</strong> As long as the GridName column is filled out, you can actually leave the GridId column blank and the grid builder will automatically infer an Id number for each table.</p>
<p><strong>Note:</strong> A lot of apps require specific names under the GridName field. Pay close attention to the app installation guides to know what table names need to be used in this column.</p>
</div></div><div class="doc-row" id="2.%20The%20" c"%20column"="">
                                    <h3 class="doc-row-title">2. The "C" column</h3><div class="small-pad-bottom"><p>The “C” column is used to give a unique identifier to each row that the grid builder can reference. There are two different ways this column can be filled out, but keep in mind that the way you choose to fill this column out changes the way the JoinCondition column is filled out later.</p>
<p><strong>Method 1:</strong> From top to bottom, starting with the number 101, increment by one and add the numbers in each following row as you go down. Ex. 101,102,103, etc. If you change source datasets in the FROM column, go to the next 100’s value and follow the same pattern. Ex. 201,202,203, etc. See the example below:</p>
<table style="height: 626px;" width="559">
<tbody>
<tr>
<td width="96">GridId</td>
<td width="96">GridName</td>
<td width="96">C</td>
<td width="139">SELECT</td>
<td width="96">FROM</td>
</tr>
<tr>
<td>1</td>
<td>opportunity</td>
<td>101</td>
<td>Amount</td>
<td>Opportunity</td>
</tr>
<tr>
<td></td>
<td></td>
<td>102</td>
<td>CloseDate</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>103</td>
<td>CreatedDate</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>104</td>
<td>Id</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>105</td>
<td>IsClosed</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>106</td>
<td>IsWon</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>107</td>
<td>LastActivityDate</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>108</td>
<td>LastModifiedDate</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>109</td>
<td>Probability</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>110</td>
<td>StageName</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>111</td>
<td>OwnerId</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>112</td>
<td>AccountId</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>113</td>
<td>Name</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>201</td>
<td>Name</td>
<td>User</td>
</tr>
<tr>
<td></td>
<td></td>
<td>202</td>
<td>Id</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>opportunity_history</td>
<td>301</td>
<td>CreatedDate</td>
<td>Opportunity History</td>
</tr>
<tr>
<td></td>
<td></td>
<td>302</td>
<td>Id</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>303</td>
<td>OpportunityId</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>304</td>
<td>StageName</td>
<td></td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<p><strong>Method 2:</strong> On the first row where each source dataset is listed in the FROM column, insert a multiple of 100 as you go down. Ex. 100 for the first dataset referenced, 200 for the second, etc. See the example below:</p>
<table width="580">
<tbody>
<tr>
<td width="96">GridId</td>
<td width="96">GridName</td>
<td width="96">C</td>
<td width="144">SELECT</td>
<td width="148">FROM</td>
</tr>
<tr>
<td>1</td>
<td>opportunity</td>
<td>100</td>
<td>Amount</td>
<td>Opportunity</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>CloseDate</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>CreatedDate</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>Id</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>IsClosed</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>IsWon</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>LastActivityDate</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>LastModifiedDate</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>Probability</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>StageName</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>OwnerId</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>AccountId</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>Name</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>200</td>
<td>Name</td>
<td>User</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>Id</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>opportunity_history</td>
<td>300</td>
<td>CreatedDate</td>
<td>Opportunity History</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>Id</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>OpportunityId</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>StageName</td>
<td></td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<p>We do this so that when we need to reference a certain row in other places in the grid builder (like the JoinCondition column) we can do so by referencing the “C” column value so that the grid builder knows what to look for. Ex. C101 = C201, or C100.Date = C200.Date etc. More on the JoinConditon column below.</p>
<p>Lastly, when we need to do dynamic date filtering in an app, as is the case with the Scorecard app family, the very first row of the “C” column is where we place a function call to a function called kamaji_calendar. We place the function call in the first row right after the filled-out GridId and GridName columns, but the rest of the cells on this row are left blank. See the example below:</p>
<table style="height: 231px;" width="1202">
<tbody>
<tr>
<td width="96">GridId</td>
<td width="96">GridName</td>
<td width="175">C</td>
<td width="96">SELECT</td>
<td width="96">FROM</td>
<td width="96">WHERE</td>
<td width="96">GROUP BY</td>
<td width="145">AS</td>
</tr>
<tr>
<td>1</td>
<td>Scorecard</td>
<td>kamaji_calendar(1, @DB)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>101</td>
<td>Date</td>
<td colspan="2">KAMAJI Calendar</td>
<td></td>
<td>Date</td>
</tr>
<tr>
<td></td>
<td></td>
<td>102</td>
<td>ThisYear</td>
<td></td>
<td></td>
<td></td>
<td>This Fiscal Year</td>
</tr>
<tr>
<td></td>
<td></td>
<td>103</td>
<td>LastYear</td>
<td></td>
<td></td>
<td></td>
<td>Last Fiscal Year</td>
</tr>
<tr>
<td></td>
<td></td>
<td>104</td>
<td>ThisQuarter</td>
<td></td>
<td></td>
<td></td>
<td>This Fiscal Quarter</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<p>Calling the kamaji_calendar function generates a calendar with different date filter options that we can pull into the app. The function takes two parameters, one of which you can change to get more options. The calling syntax is as follows: kamaji_calendar(1, @DB). Do not change the second parameter (@DB). This parameter references the database schema of the dataflow and the dataflow will not function if it is changed. The first parameter, “1” in this case, can be changed as follows to generate different date ranges for the calendar:</p>
<p>Kamaji Calendar includes every day of the current year plus the number of trailing years specified in the first parameter. If the argument is an integer less than 6, the function looks back that number of years. If the argument is an integer greater than or equal to six, the function looks back using months instead of years. If the argument is a date or date time, the function includes all dates between the argument date and the last day of the current year. If the argument is the number 445, 454 or 544, the function generates a retail calendar of that type looking back two fiscal years.<br>
Examples: kamaji_calendar([INTEGER, DATE, DATETIME, OR (445, 454 OR 544)], [DATABASE SCHEMA]);<br>
kamaji_calendar(2, @DB);<br>
kamaji_calendar(8, @DB));<br>
kamaji_calendar(‘2011-11-12’, @DB));<br>
kamaji_calendar(‘445’, @DB));</p>
<p>Check the index at the end of this guide to see what date filter options are generated with the calendar. These options can be referenced in the SELECT column when using dynamic date filtering as with the Scorecard app family.</p>
</div></div><div class="doc-row" id="3.%20The%20MYSQL%20columns%20(SELECT,%20FROM,%20WHERE,%20GROUP%20BY,%20AS)">
                                    <h3 class="doc-row-title">3. The MYSQL columns (SELECT, FROM, WHERE, GROUP BY, AS)</h3><div class="small-pad-bottom"><p>These 5 columns are the central part of the Grid Builder and they behave just like they would when writing a MYSQL statement.</p>
<p>1. Under the SELECT column, in each row list the column headers from your source data as they appear in your data. Include any columns from your data that contain data you want to display in the app, columns you may want to filter by, and any columns you may need to use to join to other tables. If your column name contains spaces or symbols, enclose the column names in backticks (`).</p>
<p>2. In the FROM column, in only the first row in each set of column names from a single data source, include the name of the source data table.</p>
<p>3. In the WHERE column, you can add any MYSQL conditional statements to filter your data. Ex. `Region` != ‘Ohio’. This would filter out all rows where ‘Ohio’ was the value in a `Region` column. Only include your conditional statements in the same row where you have filled out the FROM column for each table. If you need two different filtered sets from the same dataset, you can treat the second filtered set as a new table and then join it back to the original using the Join columns.</p>
<p>4. In the GROUP BY column, you can add any MYSQL Group By statements. Here, simply list the columns you would like to group by separated by commas. Ex. date, rep, region. If you need two different groupings from the same dataset, you can treat the second grouping as a new table and then join it back to the original using the Join columns. Again, only include your group by statements in the same row where you have filled out the FROM column for each table.</p>
<p>5. In the AS column, enter the name that you would like to call the metric listed in the SELECT column of the same row. We advise avoiding the use of spaces and using either camel-case or underscores in your metric names. Also avoid numerics, (ex. Metric 1, Last 2 Years etc.), spelling out numbers instead. Both of these things have caused unexpected errors in our past experiences with the grid builder.</p>
<p>Here is an example of these columns filled out correctly:</p>
<table style="height: 449px;" width="1218">
<tbody>
<tr>
<td width="96">C</td>
<td width="144">SELECT</td>
<td width="152">FROM</td>
<td width="173">WHERE</td>
<td width="120">GROUP BY</td>
<td width="96">AS</td>
<td width="96">Include</td>
</tr>
<tr>
<td>100</td>
<td>Amount</td>
<td>Opportunity</td>
<td>StageName = ‘StageTwo’</td>
<td>OwnerId</td>
<td>Amount</td>
<td>1</td>
</tr>
<tr>
<td></td>
<td>CloseDate</td>
<td></td>
<td></td>
<td></td>
<td>CloseDate</td>
<td>1</td>
</tr>
<tr>
<td></td>
<td>CreatedDate</td>
<td></td>
<td></td>
<td></td>
<td>CreatedDate</td>
<td>1</td>
</tr>
<tr>
<td></td>
<td>Id</td>
<td></td>
<td></td>
<td></td>
<td>Id</td>
<td>1</td>
</tr>
<tr>
<td></td>
<td>IsClosed</td>
<td></td>
<td></td>
<td></td>
<td>IsClosed</td>
<td>1</td>
</tr>
<tr>
<td></td>
<td>IsWon</td>
<td></td>
<td></td>
<td></td>
<td>IsWon</td>
<td>1</td>
</tr>
<tr>
<td></td>
<td>LastActivityDate</td>
<td></td>
<td></td>
<td></td>
<td>LastActivityDate</td>
<td>1</td>
</tr>
<tr>
<td></td>
<td colspan="2">LastModifiedDate</td>
<td></td>
<td></td>
<td>LastModifiedDate</td>
<td>1</td>
</tr>
<tr>
<td></td>
<td>Probability</td>
<td></td>
<td></td>
<td></td>
<td>Probability</td>
<td>1</td>
</tr>
<tr>
<td></td>
<td>StageName</td>
<td></td>
<td></td>
<td></td>
<td>StageName</td>
<td>1</td>
</tr>
<tr>
<td></td>
<td>OwnerId</td>
<td></td>
<td></td>
<td></td>
<td>OwnerId</td>
<td>0</td>
</tr>
<tr>
<td></td>
<td>AccountId</td>
<td></td>
<td></td>
<td></td>
<td>AccountId</td>
<td>0</td>
</tr>
<tr>
<td></td>
<td>Name</td>
<td></td>
<td></td>
<td></td>
<td>AccountName</td>
<td>1</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<p><strong>Protip:</strong> You can use CASE statements in the SELECT column to produce some awesome results. For example, you could use a case statement to create your own custom date range: CASE WHEN `Date` &gt;= (CURDATE() – INTERVAL 30 DAY) and `Date` &lt;= CURDATE() THEN 1 ELSE 0 END – This would create a last thirty days date range.</p>
<p><strong>Note:</strong> A majority of apps have certain fields that are required in order to function. In these cases, the metric names under the AS column need to be named something very specific. Pay close attention to the app installation guides to see which fields are required and what they need to be named.</p>
</div></div><div class="doc-row" id="4.%20The%20Include%20column">
                                    <h3 class="doc-row-title">4. The Include column</h3><div class="small-pad-bottom"><p>The Include column is used to signify which columns you would like to show in the final data. A value of “1” means to include and “0” will exclude a column. Generally, you will want to include most of your columns. Exceptions are when you only use columns to join and don’t want them to show in the app, or if you join and want to include the column, you would include one and not include the other so you don’t get duplicate data.</p>
<p><strong>Protip:</strong> If you leave the whole Include column blank, all entries will default to “1”.</p>
</div></div><div class="doc-row" id="5.%20The%20JoinType%20and%20JoinCondition%20columns">
                                    <h3 class="doc-row-title">5. The JoinType and JoinCondition columns</h3><div class="small-pad-bottom"><p>These two columns are where we give the grid builder instructions on how to do the joining of multiple tables. Fill out these two columns on the same row where you start a new table that needs to be joined to one you’ve already included. The first table you list in the grid builder will not use these columns and should be used as the base table that other tables are joined onto.</p>
<p>The JoinType column supports all types of MYSQL joins. Ex. INNER, LEFT, RIGHT, CROSS, etc. Generally when joining to a calendar, like the kamaji_calendar for example, you will want to use INNER, and then use LEFT for when you are joining additional tables. Omit the JOIN keyword in this column. The joins behave just like MYSQL joins so if you need a special join, feel free to play around!</p>
<p>The JoinCondition column behaves just like the ON part of a MYSQL join statement, but to reference the columns we want to join we have to use the “C” column to reference the columns. For example if you used method 1 for the “C” column above, you might enter C101 = C201. If you used method 2, you might enter C100.Date = C200.Date. See the example below:</p>
<table style="height: 579px;" width="1469">
<tbody>
<tr>
<td width="185">C</td>
<td width="139">SELECT</td>
<td width="179">FROM</td>
<td width="96">WHERE</td>
<td width="96">GROUP BY</td>
<td width="140">AS</td>
<td width="96">Include</td>
<td width="96">JoinType</td>
<td width="96">JoinCondition</td>
<td width="96">MAJIK</td>
</tr>
<tr>
<td>kamaji_calendar(1, @DB)</td>
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
<td>101</td>
<td>Date</td>
<td>KAMAJI Calendar</td>
<td></td>
<td></td>
<td>Date</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>102</td>
<td>ThisYear</td>
<td></td>
<td></td>
<td></td>
<td>This Fiscal Year</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>103</td>
<td>LastYear</td>
<td></td>
<td></td>
<td></td>
<td>Last Fiscal Year</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>104</td>
<td>ThisQuarter</td>
<td></td>
<td></td>
<td></td>
<td>This Fiscal Quarter</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>105</td>
<td>LastQuarter</td>
<td></td>
<td></td>
<td></td>
<td>Last Fiscal Quarter</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>106</td>
<td>ThisMonth</td>
<td></td>
<td></td>
<td></td>
<td>This Fiscal Month</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>107</td>
<td>LastMonth</td>
<td></td>
<td></td>
<td></td>
<td>Last Fiscal Month</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>108</td>
<td>FMStartDate</td>
<td></td>
<td></td>
<td></td>
<td>FMStartDate</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>201</td>
<td>`Rep`</td>
<td>Sales Scorecard – Sample</td>
<td></td>
<td></td>
<td>Rep</td>
<td>1</td>
<td>INNER</td>
<td>C101 = C205</td>
<td></td>
</tr>
<tr>
<td>202</td>
<td>`Team`</td>
<td></td>
<td></td>
<td></td>
<td>Team</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>203</td>
<td>`Region`</td>
<td></td>
<td></td>
<td></td>
<td>Region</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>204</td>
<td>`Role`</td>
<td></td>
<td></td>
<td></td>
<td>Role</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>205</td>
<td>`Date`</td>
<td></td>
<td></td>
<td></td>
<td>Date</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>206</td>
<td>`Gross Sales`</td>
<td></td>
<td></td>
<td></td>
<td>Gross_Sales</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<p>Note: If the “C” column was set up using the other method, the JoinCondition value above would be “C100.Date = C200.Date”.</p>
</div></div><div class="doc-row" id="6.%20The%20MAJIK%20column">
                                    <h3 class="doc-row-title">6. The MAJIK column</h3><div class="small-pad-bottom"><p>The MAJIK column has been depreciated and doesn’t currently serve any use for the apps, but I’m sure it was really <em>majikal</em> at one point. The dataflow procedures still look for it though, so keep the column in the grid builder, but leave all rows underneath it blank.</p>
</div></div><div class="doc-row" id="7.%20The%20Filter%20columns%20(FilterId,%20FilterName,%20FilterinputType,%20FilterIsPrimary,%20FilterIsPrimaryGroup)">
                                    <h3 class="doc-row-title">7. The Filter columns (FilterId, FilterName, FilterinputType, FilterIsPrimary, FilterIsPrimaryGroup)</h3><div class="small-pad-bottom"><p>The filter columns are used to tell the grid builder which columns you want to use as filters, what type of filter you want to use, and whether the filter is going to be displayed as a primary group in certain apps. Fill out these fields on the rows where you have selected the columns from your source data that you want to use a filters.</p>
<p>1. The FilterId column is used to assign a unique Id to each filter. On each row that you want to use as a filter, assign a number to each filter from top to bottom incrementing from 1 until each filter has an Id. Ex: 1,2,3 etc.<br>
Note: Single Select filters use multiple rows in the grid builder. Use the same Id on all rows used by a Single Select filter.</p>
<p>2. The FilterName column is where you can choose the name of the filter that will display in the app. For Single Select filters, only include the name on the first row included in the filter rows.</p>
<p>3. The FilterInputType column accepts two options: “Single Select” or “Multi Select”. Single select means that only one filter option can be chosen at a time, and multi select means that multiple filter values can be chosen simultaneously. Here is how to configure each type:</p>
<p>Multi Select: Filling out the FilterId, FilterName, and entering “Multi Select” under FilterInputType on a single row will make that row a filter for the app. The values that can be chosen in the filter are the individual values of the column referenced in the source data.</p>
<p>Single Select: Single Select filters require multiple columns in the source data. The columns that a Single Select filter references can only contain a 0 or 1 for their values in each row (Boolean), 0 meaning that the row in the source data is not included in the filter view and 1 meaning that the row is included.</p>
<p>For example, lets say we wanted to make a custom region-grouping filter and there were the following regions in the data: regionA, regionB, regionC, regionD, and regionE. Say we wanted three filter options: 1. regionA and regionB, 2. regionC and regionD, 3. regionE and regionA. We could use a MYSQL CASE statement beforehand to generate three new columns in the source data for these filter options. Ex. CASE WHEN `Region` IN (‘regionA’,’regionB’) THEN 1 ELSE 0 END as ‘GroupOne’. (Then two more like this for ‘GroupTwo’ and ‘GroupThree’)</p>
<p>We would then add these three new columns under the SELECT column in the grid builder, one row in the grid builder for each new column. We would then use the same Id for all three rows under the FilterId column, choose a name for the filter under the FilterName column (only on the topmost row of the three rows) and enter “Single Select” (again only on the topmost row of the three rows). This would create a single select filter where only one of the values, “GroupOne”, “GroupTwo”, or “GroupThree” could be chosen at a time. The data would then be filtered according to which rows had 1 values in the filter view option that was selected.</p>
<p>See the filter set-up example below:</p>
<table style="height: 518px;" width="850">
<tbody>
<tr>
<td width="140">AS</td>
<td width="96">Include</td>
<td width="96">JoinType</td>
<td width="96">JoinCondition</td>
<td width="96">MAJIK</td>
<td width="96">FilterId</td>
<td width="96">FilterName</td>
<td width="96">FilterInputType</td>
</tr>
<tr>
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
<td>Date</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>This Fiscal Year</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td>1</td>
<td>Date Range</td>
<td>Single Select</td>
</tr>
<tr>
<td>Last Fiscal Year</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td>1</td>
<td></td>
<td></td>
</tr>
<tr>
<td>This Fiscal Quarter</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td>1</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Last Fiscal Quarter</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td>1</td>
<td></td>
<td></td>
</tr>
<tr>
<td>This Fiscal Month</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td>1</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Last Fiscal Month</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td>1</td>
<td></td>
<td></td>
</tr>
<tr>
<td>FMStartDate</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Rep</td>
<td>1</td>
<td>INNER</td>
<td>C101 = C205</td>
<td></td>
<td>2</td>
<td>Rep</td>
<td>Multi Select</td>
</tr>
<tr>
<td>Team</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td>3</td>
<td>Team</td>
<td>Multi Select</td>
</tr>
<tr>
<td>Region</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td>4</td>
<td>Region</td>
<td>Multi Select</td>
</tr>
<tr>
<td>Role</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td>5</td>
<td>Role</td>
<td>Multi Select</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<p>Note: Only certain apps support the single select option. As of writing, the apps include the Scorecard family apps and the Google Maps Pinboard.</p>
<p>4. The FilterIsPrimary column is only used on certain apps where the primary view can be chosen from any column in the source data. As of the time of this writing, that is only the apps in the Scorecard family. To use this column place a “1” in this column in the row that represents the column that will be your primary view in the app. Ex. Sales Representative or Store etc.</p>
<p>5. Similarly to the previous column, the FilterIsPrimaryGroup column is only used in apps in the Scorecard family currently. This column is used when, in addition to the primary view, you want additional primary view options in the app. For example, your primary view is by Store but you want to view your data by district and region as well. To add those as main view options, add a number in this column starting with 1 and incrementing as you go from top to bottom on each row that you want to add as an additional primary view. Do not include the row you chose under the FilterIsPrimary column here.</p>
<p>Here is an example of using these two columns:</p>
<table width="616">
<tbody>
<tr>
<td width="96">FilterId</td>
<td width="96">FilterName</td>
<td width="123">FilterInputType</td>
<td width="124">FilterIsPrimary</td>
<td width="177">FilterIsPrimaryGroup</td>
</tr>
<tr>
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
<td></td>
<td></td>
</tr>
<tr>
<td>1</td>
<td>Date Range</td>
<td>Single Select</td>
<td></td>
<td></td>
</tr>
<tr>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Rep</td>
<td>Multi Select</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Team</td>
<td>Multi Select</td>
<td></td>
<td>1</td>
</tr>
<tr>
<td>4</td>
<td>Region</td>
<td>Multi Select</td>
<td></td>
<td>2</td>
</tr>
<tr>
<td>5</td>
<td>Role</td>
<td>Multi Select</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<p>Note: In the example above, Rep would be the primary filter view and Team and Region could be selected as optional primary views. All filters that have a number under FilterId will still display as standard&nbsp;filters, even if they are used as a primary group.</p>
</div></div><div class="doc-row" id="8.%20The%20Description%20column">
                                    <h3 class="doc-row-title">8. The Description column</h3><div class="small-pad-bottom"><p>The description column is included for documentation purposes. Many of the installation guides give descriptions here of what app-specific metrics they are looking for. You may fill them out with whatever information you would like to. The grid builder dataflow ignores this column.</p>
<p><strong>Protip:</strong> if multiple people will be looking at and changing the grid builder, this is a great place to leave change notes, metric descriptions, etc.</p>
</div></div><div class="doc-row" id="That's%20It!">
                                    <h3 class="doc-row-title">That's It!</h3><div class="small-pad-bottom"><p>Those are the different columns of the grid builder and how to use them! If you have any questions or suggestions for this guide, feel free to reach out to the Domo AppLabs team at <a href="mailto:DomoAppDeployment@domo.com">DomoAppDeployment@domo.com</a>. Thanks for Reading!</p>
</div></div><div class="doc-row" id="INDEX">
                                    <h3 class="doc-row-title">INDEX</h3><div class="small-pad-bottom"><h3>Kamaji_calendar date options</h3>
<p>Below is a list of all of the date filter options available in the kamaji calendar. These option names would be included in the SELECT column where columns are being selected from kamaji_calendar. This is used in apps from the Scorecard family as well as any app that uses dynamic date filtering.</p>
<p>Here are the values:</p>
<p>KEY:<br>
C stands for Calendar<br>
F stands for Fiscal<br>
D stands for Day<br>
W stands for Week<br>
M stands for Month<br>
Q stands for Quarter<br>
Y stands for Year<br>
O stands for “Of”</p>
<p>This field is used to join datasets by date, includes all dates in the range:<br>
Date</p>
<p>These are numeric values representing their value. For example: if the year of `Date` is 2017 then CY = 2017. If the month of `Date` is January then CM = 1:<br>
FY<br>
CY<br>
FQ<br>
CQ<br>
FM<br>
CM<br>
FWOY (ie. Fiscal week of Year 1-52)<br>
CWOY<br>
FWOQ<br>
CWOQ<br>
FWOM<br>
CWOM<br>
FDOY<br>
CDOY<br>
FDOQ<br>
CDOQ<br>
FDOM<br>
CDOM<br>
FDOW<br>
CDOW</p>
<p>These can be included if you need the specific date:<br>
FYStartDate<br>
FYEndDate<br>
CYStartDate<br>
CYEndDate<br>
FQStartDate<br>
FQEndDate<br>
CQStartDate<br>
CQEndDate<br>
FMStartDate<br>
FMEndDate<br>
CMStartDate<br>
CMEndDate<br>
FWStartDate<br>
FWEndDate<br>
CWStartDate<br>
CWEndDate</p>
<p>These can be included as date range filter options. They are all boolean columns where 1 means the date is included in the range and 0 means that it is not:<br>
CurrentFY<br>
PreviousFY<br>
2FYAgo<br>
CurrentAndPreviousFY<br>
CurrentAndPrevious2FY<br>
CurrentCY<br>
PreviousCY<br>
2CYAgo<br>
CurrentAndPreviousCY<br>
CurrentAndPrevious2CY<br>
CurrentFQ<br>
PreviousFQ<br>
2FQAgo<br>
CurrentAndPreviousFQ<br>
CurrentAndPrevious2FQ<br>
CurrentCQ<br>
PreviousCQ<br>
2CQAgo<br>
CurrentAndPreviousCQ<br>
CurrentAndPrevious2CQ<br>
CurrentFM<br>
PreviousFM<br>
2FMAgo<br>
CurrentAndPreviousFM<br>
CurrentAndPrevious2FM<br>
CurrentCM<br>
PreviousCM<br>
2CMAgo<br>
CurrentAndPreviousCM<br>
CurrentAndPrevious2CM<br>
CurrentFW<br>
PreviousFW<br>
2FWAgo<br>
CurrentAndPreviousFW<br>
CurrentAndPrevious2FW<br>
CurrentCW<br>
PreviousCW<br>
2CWAgo<br>
CurrentAndPreviousCW<br>
CurrentAndPrevious2CW<br>
ThisYear<br>
LastYear<br>
ThisQuarter<br>
LastQuarter<br>
ThisMonth<br>
LastMonth<br>
ThisWeek<br>
LastWeek<br>
ThisQuarterLastYear<br>
ThisMonthLastYear<br>
ThisWeekLastYear<br>
Today<br>
Yesterday<br>
Last7Days<br>
Last30Days<br>
Last90Days<br>
Last120Days</p>
<p>And here is an example of where to include them in the app:</p>
<table style="height: 494px;" width="1787">
<tbody>
<tr>
<td width="185">C</td>
<td width="167">SELECT</td>
<td width="179">FROM</td>
<td width="96">WHERE</td>
<td width="96">GROUP BY</td>
<td width="180">AS</td>
<td width="96">Include</td>
<td width="96">JoinType</td>
<td width="96">JoinCondition</td>
<td width="96">MAJIK</td>
<td width="96">FilterId</td>
<td width="96">FilterName</td>
<td width="123">FilterInputType</td>
</tr>
<tr>
<td>kamaji_calendar(1, @DB)</td>
<td></td>
<td></td>
<td></td>
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
<td>101</td>
<td>Date</td>
<td>KAMAJI Calendar</td>
<td></td>
<td></td>
<td>Date</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>102</td>
<td>ThisYear</td>
<td></td>
<td></td>
<td></td>
<td>This Fiscal Year</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td>1</td>
<td>Date Range</td>
<td>Single Select</td>
</tr>
<tr>
<td>103</td>
<td>LastYear</td>
<td></td>
<td></td>
<td></td>
<td>Last Fiscal Year</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td>1</td>
<td></td>
<td></td>
</tr>
<tr>
<td>104</td>
<td>ThisQuarter</td>
<td></td>
<td></td>
<td></td>
<td>This Fiscal Quarter</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td>1</td>
<td></td>
<td></td>
</tr>
<tr>
<td>105</td>
<td>LastQuarter</td>
<td></td>
<td></td>
<td></td>
<td>Last Fiscal Quarter</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td>1</td>
<td></td>
<td></td>
</tr>
<tr>
<td>106</td>
<td>ThisMonth</td>
<td></td>
<td></td>
<td></td>
<td>This Fiscal Month</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td>1</td>
<td></td>
<td></td>
</tr>
<tr>
<td>107</td>
<td>LastMonth</td>
<td></td>
<td></td>
<td></td>
<td>Last Fiscal Month</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td>1</td>
<td></td>
<td></td>
</tr>
<tr>
<td>108</td>
<td>Last30Days</td>
<td></td>
<td></td>
<td></td>
<td>Last Thirty Days</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td>1</td>
<td></td>
<td></td>
</tr>
<tr>
<td>109</td>
<td>CurrentAndPreviousFQ</td>
<td></td>
<td></td>
<td></td>
<td>Current And Previous FQ</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td>1</td>
<td></td>
<td></td>
</tr>
<tr>
<td>110</td>
<td>CurrentAndPreviousCY</td>
<td></td>
<td></td>
<td></td>
<td>Current And Previous CY</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td>1</td>
<td></td>
<td></td>
</tr>
<tr>
<td>111</td>
<td>2FWAgo</td>
<td></td>
<td></td>
<td></td>
<td>Two Fiscal Weeks Ago</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td>1</td>
<td></td>
<td></td>
</tr>
<tr>
<td>112</td>
<td>FMStartDate</td>
<td></td>
<td></td>
<td></td>
<td>FMStartDate</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
</div></div>            </div>
