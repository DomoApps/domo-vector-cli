---
stoplight-id: sijccaynadtc2
---

# Overtime Analysis

Thanks for installing and test-driving Overtime Analysis! This guide is intended to help you connect this app with your own data. The first step is to ensure that your data follows the same schema (or structure) of the sample datasets that currently power the App. Fortunately, Domo has created some powerful data transformation tools to help, along with the step-by-step instructions provided below. For help with Dataflows, Magic ETL or BeastModes, please visit [Domo University](https://www.domo.com/university/training) within Domo.

### Step 1: Identify Required Data Fields

The first step in preparing your data is understanding the fields and datasets that are required by this App. Here are the datasets required by this App:

#### Custom Datasets

This App requires creating the following custom datasets. To do this, you’ll need to ensure that you have each of these fields in Domo. Then you’ll need to use transforms to create datasets that follow the exact structure or schema of the datasets below:



<table id="SAMPLE_Sales-Data" style="height: 704px;" width="914">
<tbody>
<tr>
<td colspan="3"><strong>DataSet Name:&nbsp;</strong></td>
<td class="value" colspan="3">edt_list</td>
</tr>
<tr>
<td colspan="3"><strong>What is the DataSet used for?&nbsp;</strong></td>
<td class="value" colspan="3">To pull record type information, payroll information, such as pay date, record amounts, wages, etc.</td>
</tr>
<tr>
<td><strong>Field Name</strong></td>
<td><strong>Data Type</strong></td>
<td><strong>Report Name / Object Name</strong></td>
<td><strong>Source </strong></td>
<td colspan="2"><strong>Description of Field</strong></td>
</tr>
<tr>
<td>Employee Id</td>
<td></td>
<td>EDT LIST</td>
<td>Beyond Payroll / Kronos</td>
<td colspan="2"></td>
</tr>
<tr>
<td>Payroll Name</td>
<td></td>
<td>EDT LIST</td>
<td>Beyond Payroll / Kronos</td>
<td colspan="2"></td>
</tr>
<tr>
<td>Pay Date</td>
<td></td>
<td>EDT LIST</td>
<td>Beyond Payroll / Kronos</td>
<td colspan="2"></td>
</tr>
<tr>
<td>Record Type</td>
<td></td>
<td>EDT LIST</td>
<td>Beyond Payroll / Kronos</td>
<td colspan="2"></td>
</tr>
<tr>
<td>E/D/T Name</td>
<td></td>
<td>EDT LIST</td>
<td>Beyond Payroll / Kronos</td>
<td colspan="2"></td>
</tr>
<tr>
<td>Record Hours</td>
<td></td>
<td>EDT LIST</td>
<td>Beyond Payroll / Kronos</td>
<td colspan="2"></td>
</tr>
<tr>
<td>Record Amount</td>
<td></td>
<td>EDT LIST</td>
<td>Beyond Payroll / Kronos</td>
<td colspan="2"></td>
</tr>
<tr>
<td>Record Amount (ER)</td>
<td></td>
<td>EDT LIST</td>
<td>Beyond Payroll / Kronos</td>
<td colspan="2"></td>
</tr>
<tr>
<td>Gross Sub Wages</td>
<td></td>
<td>EDT LIST</td>
<td>Beyond Payroll / Kronos</td>
<td colspan="2"></td>
</tr>
<tr>
<td>Sub Wages</td>
<td></td>
<td>EDT LIST</td>
<td>Beyond Payroll / Kronos</td>
<td colspan="2"></td>
</tr>
<tr>
<td>Gross Sub Wages(ER)</td>
<td></td>
<td>EDT LIST</td>
<td>Beyond Payroll / Kronos</td>
<td colspan="2"></td>
</tr>
<tr>
<td>Sub Wages(ER)</td>
<td></td>
<td>EDT LIST</td>
<td>Beyond Payroll / Kronos</td>
<td colspan="2"></td>
</tr>
<tr>
<td>Gross Wages</td>
<td></td>
<td>EDT LIST</td>
<td>Beyond Payroll / Kronos</td>
<td colspan="2"></td>
</tr>
<tr>
<td>Gross Wages(ER)</td>
<td></td>
<td>EDT LIST</td>
<td>Beyond Payroll / Kronos</td>
<td colspan="2"></td>
</tr>
<tr>
<td>Employee Name</td>
<td></td>
<td>EDT LIST</td>
<td>Beyond Payroll / Kronos</td>
<td colspan="2"></td>
</tr>
<tr>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
</tbody>
</table>



<table id="SAMPLE_Sales-Data" style="height: 704px;" width="914">
<tbody>
<tr>
<td colspan="3"><strong>DataSet Name:&nbsp;</strong></td>
<td class="value" colspan="3">EDT Roster</td>
</tr>
<tr>
<td colspan="3"><strong>What is the DataSet used for?&nbsp;</strong></td>
<td class="value" colspan="3">To pull record type information, payroll information, such as pay date, record amounts, wages, etc.</td>
</tr>
<tr>
<td><strong>Field Name</strong></td>
<td><strong>Data Type</strong></td>
<td><strong>Report Name / Object Name</strong></td>
<td><strong>Source </strong></td>
<td colspan="2"><strong>Description of Field</strong></td>
</tr>
<tr>
<td>Employee Id</td>
<td></td>
<td>EDT Roster</td>
<td>Beyond Payroll / Kronos</td>
<td colspan="2"></td>
</tr>
<tr>
<td>Badge</td>
<td></td>
<td>EDT Roster</td>
<td>Beyond Payroll / Kronos</td>
<td colspan="2"></td>
</tr>
<tr>
<td>Username</td>
<td></td>
<td>EDT Roster</td>
<td>Beyond Payroll / Kronos</td>
<td colspan="2"></td>
</tr>
<tr>
<td>First Name</td>
<td></td>
<td>EDT Roster</td>
<td>Beyond Payroll / Kronos</td>
<td colspan="2"></td>
</tr>
<tr>
<td>Last Name</td>
<td></td>
<td>EDT Roster</td>
<td>Beyond Payroll / Kronos</td>
<td colspan="2"></td>
</tr>
<tr>
<td>Employee Status</td>
<td></td>
<td>EDT Roster</td>
<td>Beyond Payroll / Kronos</td>
<td colspan="2"></td>
</tr>
<tr>
<td>Gender</td>
<td></td>
<td>EDT Roster</td>
<td>Beyond Payroll / Kronos</td>
<td colspan="2"></td>
</tr>
<tr>
<td>In Payroll</td>
<td></td>
<td>EDT Roster</td>
<td>Beyond Payroll / Kronos</td>
<td colspan="2"></td>
</tr>
<tr>
<td>Locked</td>
<td></td>
<td>EDT Roster</td>
<td>Beyond Payroll / Kronos</td>
<td colspan="2"></td>
</tr>
<tr>
<td>Sub Wages</td>
<td></td>
<td>EDT Roster</td>
<td>Beyond Payroll / Kronos</td>
<td colspan="2"></td>
</tr>
<tr>
<td>Email</td>
<td></td>
<td>EDT Roster</td>
<td>Beyond Payroll / Kronos</td>
<td colspan="2"></td>
</tr>
<tr>
<td>Work Phone</td>
<td></td>
<td>EDT Roster</td>
<td>Beyond Payroll / Kronos</td>
<td colspan="2"></td>
</tr>
<tr>
<td>Cell Phone</td>
<td></td>
<td>EDT Roster</td>
<td>Beyond Payroll / Kronos</td>
<td colspan="2"></td>
</tr>
<tr>
<td>Home Phone</td>
<td></td>
<td>EDT Roster</td>
<td>Beyond Payroll / Kronos</td>
<td colspan="2"></td>
</tr>
<tr>
<td>Holiday Profile</td>
<td></td>
<td>&nbsp;EDT Roster</td>
<td>Beyond Payroll / Kronos</td>
<td colspan="2"></td>
</tr>
<tr>
<td>Security Profile</td>
<td></td>
<td>EDT Roster</td>
<td>Beyond Payroll / Kronos</td>
<td colspan="2"></td>
</tr>
<tr>
<td>Timesheet Profile</td>
<td></td>
<td>&nbsp;EDT Roster</td>
<td>&nbsp;Beyond Payroll / Kronos</td>
<td colspan="2"></td>
</tr>
<tr>
<td>Pay Period Profile</td>
<td></td>
<td>&nbsp;EDT Roster</td>
<td>&nbsp;Beyond Payroll / Kronos</td>
<td colspan="2"></td>
</tr>
<tr>
<td>Accrual Profile</td>
<td></td>
<td>EDT Roster</td>
<td>&nbsp;Beyond Payroll / Kronos</td>
<td colspan="2"></td>
</tr>
<tr>
<td>Date Hired</td>
<td></td>
<td>&nbsp;EDT Roster</td>
<td>&nbsp;Beyond Payroll / Kronos</td>
<td colspan="2"></td>
</tr>
<tr>
<td>Manager</td>
<td></td>
<td>&nbsp;EDT Roster</td>
<td>&nbsp;Beyond Payroll / Kronos</td>
<td colspan="2"></td>
</tr>
<tr>
<td>Date Re-Hired</td>
<td></td>
<td>&nbsp;EDT Roster</td>
<td>&nbsp;Beyond Payroll / Kronos</td>
<td colspan="2"></td>
</tr>
<tr>
<td>Location</td>
<td></td>
<td>&nbsp;EDT Roster</td>
<td>&nbsp;Beyond Payroll / Kronos</td>
<td colspan="2"></td>
</tr>
<tr>
<td>Manager Name</td>
<td></td>
<td>&nbsp;EDT Roster</td>
<td>&nbsp;Beyond Payroll / Kronos</td>
<td colspan="2"></td>
</tr>
<tr>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
</tbody>
</table>