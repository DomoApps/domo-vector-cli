---
stoplight-id: eb00606e6f114
---

# Format Data to Import

To upload data in CSV format, the Domo specification used for representing data grids in CSV format closely follows the RFC standard for CSV (RFC-4180). We extend the RFC in the following ways:
<ol>
 	<li>Optionally use line feeds without a carriage return as a row separator.</li>
 	<li>Support of Unicode characters.</li>
</ol>
All data uploaded in this format must comply with a schema that is supplied separately from the upload. For example the CSV must comply with the correct number of columns and field types.

#### Specifications:
<ul>
 	<li><strong>file</strong> = [header CRLF] record *(CRLF record) [CRLF]</li>
 	<li><strong>header</strong> = name *(COMMA name)</li>
 	<li><strong>record</strong> = field *(COMMA field)</li>
 	<li><strong>name</strong> = field</li>
 	<li><strong>field</strong> = (escaped | +--escaped)</li>
 	<li><strong>escaped</strong> = DQUOTE *(TEXTDATA | COMMA | CR | LF | 2DQUOTE) DQUOTE</li>
 	<li><strong>non-escaped</strong> = *TEXTDATA</li>
 	<li><strong>COMMA</strong> = %x2C</li>
 	<li><strong>DQUOTE</strong> = %x22</li>
 	<li><strong>2DQUOTE</strong> = DQUOTE DQUOTE</li>
 	<li><strong>CRLF</strong> = CR LF | LF</li>
 	<li><strong>CR</strong> = %x0D</li>
 	<li><strong>LF</strong> = %x0A</li>
 	<li><strong>TEXTDATA</strong> = ![COMMA | CR | LF | DQUOTE]</li>
</ul>
&nbsp;

#### Examples
<table class="confluenceTable">
<tbody>
<tr>
<th class="confluenceTh">CSV</th>
<th class="confluenceTh">Comment</th>
</tr>
<tr>
<td class="confluenceTd">a,b,c</td>
<td class="confluenceTd">One row with three columns</td>
</tr>
<tr>
<td class="confluenceTd">"a",b,c</td>
<td class="confluenceTd">Escaped first column. Quotes do not count as part of the field</td>
</tr>
<tr>
<td class="confluenceTd">"a,a",b,c</td>
<td class="confluenceTd">One row with three columns. The first field is escaped and contains a comma as part of its text.</td>
</tr>
<tr>
<td class="confluenceTd">"a <br class="atl-forced-newline" />a",b,c</td>
<td class="confluenceTd">One row with three columns. The first field is escaped and contains a line feed as part of its text.</td>
</tr>
<tr>
<td class="confluenceTd">"a""a",b,c</td>
<td class="confluenceTd">The first field is escaped and contains an escaped quote as part of its text.</td>
</tr>
<tr>
<td class="confluenceTd">???,b,c</td>
<td class="confluenceTd">Unicode characters as part of the first field.</td>
</tr>
<tr>
<td class="confluenceTd">a,b,c</td>
<td class="confluenceTd">One row with the optional terminating line feed. It is recommended that all uploads to Domo include the optional terminating line feed. <br class="atl-forced-newline" />If not supplied Domo may automatically include the linefeed.</td>
</tr>
<tr>
<td class="confluenceTd">a,b,c <br class="atl-forced-newline" />a,b,c</td>
<td class="confluenceTd">Multiple rows.</td>
</tr>
<tr>
<td class="confluenceTd">,,</td>
<td class="confluenceTd">One row with three null values.</td>
</tr>
<tr>
<td class="confluenceTd">"","",""</td>
<td class="confluenceTd">One row with three empty string values.</td>
</tr>
</tbody>
</table>
&nbsp;

&nbsp;

#### Examples of Invalid CSV:
<table class="confluenceTable">
<tbody>
<tr>
<th class="confluenceTh">CSV</th>
<th class="confluenceTh">Comment</th>
</tr>
<tr>
<td class="confluenceTd">a",b,c</td>
<td class="confluenceTd">Quote appearing in a non-escaped field.</td>
</tr>
<tr>
<td class="confluenceTd">"a"a",b,c</td>
<td class="confluenceTd">Unescaped quoted appearing in a non-escaped field.</td>
</tr>
<tr>
<td class="confluenceTd">a, <br class="atl-forced-newline" />b,c</td>
<td class="confluenceTd">Line feed appearing in a non-escaped field. This could also be considered missing columns in row one and two.</td>
</tr>
<tr>
<td class="confluenceTd">a,b,c <br class="atl-forced-newline" /><br class="atl-forced-newline" />a,b,c</td>
<td class="confluenceTd">Missing fields in the second row.</td>
</tr>
</tbody>
</table>

### Next Steps
---
Explore more about the DataSet API now that you know how to import and export data.

- [DataSet API Reference](../../API-Reference/Domo-APIs/DataSet-API.yaml)
- [Stream API Reference](../../API-Reference/Domo-APIs/Stream-API.yaml)

### Need additional help?
---
No problem, we'd love to help. Explore our [documentation](https://knowledge.domo.com), answers to [frequently asked questions](https://dojo.domo.com/main), or join other developers in Domo's [Developer Forum](https://dojo.domo.com/main).  For further help, feel free to [email us](mailto:support@domo.com) or [contact our sales team](mailto:sales@domo.com).
