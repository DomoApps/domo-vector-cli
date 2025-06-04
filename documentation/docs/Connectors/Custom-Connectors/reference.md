---
stoplight-id: e415bb99d21b2
---

# Reference

These methods are provided by Domo in the Connector Dev Studio to make it easier for you to build your custom connector.

### Auth
---
These methods are specifically used in the authentication code block.
<table style="width: 900px;">
<thead>
<tr>
<td><strong>Method</strong></td>
<td><strong>Parameters</strong></td>
<td><strong>Return</strong></td>
<td><strong>Description</strong></td>
</tr>
</thead>
<tbody>
<tr>
<td><a href="#authauthenticationsuccess">auth.authenticationSuccess()</a></td>
<td>none</td>
<td>none</td>
<td>Set during the authentication process to indicate that the credentials have been successfully validated.</td>
</tr>
<tr>
<td><a href="#authauthenticationfailederrormessage">auth.authenticationFailed(errorMessage)</a></td>
<td>errorMessage</td>
<td>none</td>
<td>Set during the authentication process to indicate that the credentials could not be validated.</td>
</tr>
</tbody>
</table>
&nbsp;

### Datagrid
---
Domo provides methods and constants to help you insert your data into Domo. These methods and constants are specifically used in the data processing code block.

These constants are used to define the data type of a column in a datagrid.
<table style="width: 900px;">
<tbody>
<tr>
<td><strong>Name</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr>
<td><a href="#datagriddata_type_string">datagrid.DATA_TYPE_STRING</a></td>
<td>Set a column dataType to receive a string.</td>
</tr>
<tr>
<td><a href="#datagriddata_type_double">datagrid.DATA_TYPE_DOUBLE</a></td>
<td>Set a column dataType to receive a number.</td>
</tr>
<tr>
<td><a href="#datagriddata_type_datetime">datagrid.DATA_TYPE_DATETIME</a></td>
<td>Set a column dataType to receive a date/time.
Dates inserted into the table need to be formatted <em>yyyy-MM-dd’T’HH:mm:ss</em>.</td>
</tr>
<tr>
<td><a href="#datagriddata_type_date">datagrid.DATA_TYPE_DATE</a></td>
<td>Set a column dataType to receive a date.
Dates inserted into the table need to be formatted <em>yyyy-MM-dd</em>.</td>
</tr>
</tbody>
</table>
&nbsp;

These methods are used when storing data from your API endpoint in Domo.
<table style="width: 900px;">
<tbody>
<tr>
<td><strong>Method</strong></td>
<td><strong>Parameters</strong></td>
<td><strong>Return</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr>
<td><a href="#datagridaddcolumncolumnname-datatype">datagrid.addColumn(columnName, dataType)</a></td>
<td>columnName, dataType</td>
<td>none</td>
<td>Adds a column to a table. Defines the data type used by the column.</td>
</tr>
<tr>
<td><a href="#datagridaddcellcelldata">datagrid.addCell(cellData)</a></td>
<td>cellData</td>
<td>none</td>
<td>Adds data to one cell in the table. Columns must be defined first.</td>
</tr>
<tr>
<td><a href="#datagridendrow">datagrid.endRow()</a></td>
<td>none</td>
<td>none</td>
<td>Indicates a row of data is complete and a new row in the table needs to be started.</td>
</tr>
<tr>
<td><a href="#datagriderrorcode-errormessage">datagrid.error(code, errorMessage)</a></td>
<td>code, errorMessage</td>
<td>none</td>
<td>Ends the processing of data and returns an error message to the user.</td>
</tr>
<tr>
<td><a href="#datagridmagicparsecsvcsvstring">datagrid.magicParseCSV(csvString)</a></td>
<td> csvString</td>
<td> none</td>
<td>Populates the entire datagrid when passed a properly formatted string of comma-separated values.</td>
</tr>
<tr>
<td><a href="#datagridmagicparsejsonjsonstring">datagrid.magicParseJSON(jsonString)</a></td>
<td> jsonString</td>
<td> none</td>
<td>Populates the entire datagrid when passed a string representation of properly formatted JSON.</td>
</tr>
<tr>
<td><a href="#datagridmagicparsexmlxmlstring">datagrid.magicParseXML(xmlString)</a></td>
<td>xmlString</td>
<td>none</td>
<td>Populates the entire datagrid when passed a string representation of properly formatted XML.</td>
</tr>
</tbody>
</table>

### Discovery
---
If you are using the Discovery option in Advanced Mode in the Configure Reports step, Domo provides methods and constants to help you. These methods and constants are specifically used in the discovery code block.

This constant is used when building a discovery tree menu.
<table style="width: 900px;">
<tbody>
<tr>
<td><strong>Name</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr>
<td><a href="#discoverytree">discovery.tree</a></td>
<td>Used with a discovery tree. This references the root node in a discovery tree.</td>
</tr>
</tbody>
</table>
&nbsp;

These methods are used when building a discovery tree or discovery dropdown.
<table style="width: 900px;">
<tbody>
<tr style="height: 24px;">
<td style="height: 24px;"><strong>Method</strong></td>
<td style="height: 24px;"><strong>Parameters</strong></td>
<td style="height: 24px;"><strong>Return</strong></td>
<td style="height: 24px;"><strong>Description</strong></td>
</tr>
<tr style="height: 48px;">
<td style="height: 48px;"><a href="#discoveryaddoptionoptionvalue">discovery.addOption(optionValue)</a></td>
<td style="height: 48px;">optionValue</td>
<td style="height: 48px;">none</td>
<td style="height: 48px;">Used with a discovery dropdown. Adds an option to the dropdown menu.</td>
</tr>
<tr>
<td><a href="#discoveryaddoption">discovery.addOption(optionName,optionValue)</a></td>
<td>optionName, optionValue</td>
<td>none</td>
<td>Used with a discovery dropdown. Adds an option to the dropdown menu. Option name appears as label, option value is used in the code.</td>
</tr>
<tr style="height: 96px;">
<td style="height: 96px;"><a href="#discoveryaddnodeparentnode-nodename">discovery.addNode(parentNode, nodeName)</a></td>
<td style="height: 96px;">parentNode, nodeName</td>
<td style="height: 96px;">createdNode</td>
<td style="height: 96px;">Used with a discovery tree. Creates a new child node within the node that is passed as a parameter. Returns a reference to the newly created node.</td>
</tr>
<tr style="height: 72px;">
<td style="height: 72px;"><a href="#discoveryaddleafparentnode-leafname">discovery.addLeaf(parentNode, leafName)</a></td>
<td style="height: 72px;">parentNode, leafName</td>
<td style="height: 72px;">none</td>
<td style="height: 72px;">Used with a discovery tree. Creates a new child leaf within the node that is passed as a parameter.</td>
</tr>
<tr style="height: 72px;">
<td style="height: 72px;"><a href="#discoverypublishtree">discovery.publishTree()</a></td>
<td style="height: 72px;">none</td>
<td style="height: 72px;">none</td>
<td style="height: 72px;">Used with a discovery tree. This method indicates that you have finished constructing a discovery tree.</td>
</tr>
</tbody>
</table>

### Domo
---
These methods may be useful in any code block.
<table style="width: 900px;">
<tbody>
<tr style="height: 24px;">
<td style="height: 24px;"><strong>Method</strong></td>
<td style="height: 24px;"><strong>Parameters</strong></td>
<td style="height: 24px;"><strong>Return</strong></td>
<td style="height: 24px;"><strong>Description</strong></td>
</tr>
<tr style="height: 144px;">
<td style="height: 144px;"><a href="#domologvalue">DOMO.log(value)</a></td>
<td style="height: 144px;">value</td>
<td style="height: 144px;">none</td>
<td style="height: 144px;">Prints to the Dev Studio console. Make sure you remove any credentials that you are logging for testing before you submit your connector.</td>
</tr>
<tr style="height: 48px;">
<td style="height: 48px;"><a href="#domosleepmilliseconds">DOMO.sleep(milliseconds)</a></td>
<td style="height: 48px;">milliseconds</td>
<td style="height: 48px;">none</td>
<td style="height: 48px;">Can be used to space out HTTP requests.</td>
</tr>
<tr style="height: 48px;">
<td style="height: 48px;"><a href="#domogetstatekey">DOMO.getState(key)</a></td>
<td style="height: 48px;">key</td>
<td style="height: 48px;">value</td>
<td style="height: 48px;">Returns the value of the requested state.</td>
</tr>
<tr style="height: 96px;">
<td style="height: 96px;"><a href="#domosetstatekey-value">DOMO.setState(key, value)</a></td>
<td style="height: 96px;">key, value</td>
<td style="height: 96px;">none</td>
<td style="height: 96px;">Can be used to set a state value which can be returned using DOMO.getState(key).</td>
</tr>
<tr style="height: 48px;">
<td style="height: 48px;"><a href="#domoparsexmlxmlstring">DOMO.parseXML(xmlString)</a></td>
<td style="height: 48px;">xmlString</td>
<td style="height: 48px;">jsonObject</td>
<td style="height: 48px;">Used to convert XML to JSON for easier parsing.</td>
</tr>
<tr style="height: 56px;">
<td style="height: 56px;"><a href="#domogetstartdatemetadataparametersdate">DOMO.getStartDate(metadata.parameters["Date"])</a></td>
<td style="height: 56px;"><span class="code-quote">Date</span></td>
<td style="height: 56px;">date</td>
<td style="height: 56px;">Used to set the start date.</td>
</tr>
<tr style="height: 56px;">
<td style="height: 56px;"><a href="#domogetenddatemetadataparametersdate">DOMO.getEndDate(metadata.parameters["Date"])</a></td>
<td style="height: 56px;"><span class="code-quote">Date</span></td>
<td style="height: 56px;">date</td>
<td style="height: 56px;">Used to set the end date.</td>
</tr>
</tbody>
</table>
&nbsp;
<table style="width: 900px;">
<tbody>
<tr>
<td><strong>Encoding Method</strong></td>
<td><strong>Parameters</strong></td>
<td><strong>Return</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr> 
<td><a href="#domob64encodeunicodestringtoencode">DOMO.b64EncodeUnicode(stringToEncode)</a></td>
<td>stringToEncode</td>
<td>encodedString</td>
<td>Encodes a string using base64 encoding.</td>
</tr>
<tr>
<td><a href="#domob64decodeunicodestringtodecode">DOMO.b64DecodeUnicode(stringToDecode)</a></td>
<td>stringToDecode</td>
<td>decodedString</td>
<td>Decodes a string using base64 decoding.</td>
</tr>
<tr>
<td><a href="#domohmacsha1stringtoencode-key">DOMO.hmacSHA1(stringToEncode, key)</a></td>
<td>stringToEncode, key</td>
<td>encodedString</td>
<td>Encodes a string using the provided key to create a hmac-SHA1 hash.</td>
</tr>
<tr>
<td><a href="#domohmacsha256stringtoencode-key">DOMO.hmacSHA256(stringToEncode, key)</a></td>
<td>stringToEncode, key</td>
<td>encodedString</td>
<td>Encodes a string using the provided key to create a hmac-SHA256 hash.</td>
</tr>
<tr>
<td><a href="#domomd5stringtoencode">DOMO.md5(stringToEncode)</a></td>
<td>stringToEncode</td>
<td>encodedString</td>
<td>Encodes a string using the md5 algorithm.</td>
</tr>
<tr>
<td><a href="#domogetjwt">DOMO.getJWT()</a></td>
<td> none</td>
<td> tokenString</td>
<td>Creates a JSON web token (JWT) using the assigned algorithm signed with the provided key.
<strong>Note</strong>: You must set the algorithm, key, issuer, subject, expiration, and other claims. See the provided <a href="#getJWT" target="_blank" rel="noopener">code example</a>.
<strong>Supported algorithms</strong>: HS256, RS256, ES256</td>
</tr>
</tbody>
</table>

### HTTP Request
---
When making your HTTP requests, use the following methods to add headers and parameters, and to make HTTP calls.

<strong>Note</strong>: All URLs must use https.
<table style="width: 900px;">
<tbody>
<tr style="height: 24px;">
<td style="width: 265px; height: 24px;"><strong>Method</strong></td>
<td style="width: 97px; height: 24px;"><strong>Parameters</strong></td>
<td style="width: 107px; height: 24px;"><strong>Return</strong></td>
<td style="width: 403px; height: 24px;"><strong>Description</strong></td>
</tr>
<tr style="height: 96px;">
<td style="width: 265px; height: 96px;"><a href="#httprequestaddheaderkey-value">httprequest.addHeader(key, value)</a></td>
<td style="width: 97px; height: 96px;"> key, value</td>
<td style="width: 107px; height: 96px;">none</td>
<td style="width: 403px; height: 96px;">Add a header to your HTTP request. This is how you can add an Authorization header or any other header you need to your HTTP request. Add headers and parameters before you make the HTTP request.</td>
</tr>
<tr style="height: 48px;">
<td style="width: 265px; height: 48px;"><a href="#httprequestaddparameterkey-value">httprequest.addParameter(key, value)</a></td>
<td style="width: 97px; height: 48px;"> key, value</td>
<td style="width: 107px; height: 48px;">none</td>
<td style="width: 403px; height: 48px;">Add a parameter to a base URL. Add headers and parameters before you make the HTTP request.</td>
</tr>
<tr style="height: 48px;">
<td style="width: 265px; height: 48px;"><a href="#httprequestclearparameters">httprequest.clearParameters()</a></td>
<td style="width: 97px; height: 48px;"> none</td>
<td style="width: 107px; height: 48px;">none</td>
<td style="width: 403px; height: 48px;">Remove any parameters you have added to an HTTP request object.</td>
</tr>
<tr style="height: 48px;">
<td style="width: 265px; height: 48px;"><a href="#httprequestclearheaders">httprequest.clearHeaders()</a></td>
<td style="width: 97px; height: 48px;"> none</td>
<td style="width: 107px; height: 48px;">none</td>
<td style="width: 403px; height: 48px;">Remove any headers you have added to an HTTP request object.</td>
</tr>
<tr style="height: 72px;">
<td style="width: 265px; height: 72px;"><a href="#httprequestgetheaderkey">httprequest.getHeader(key)</a></td>
<td style="width: 97px; height: 72px;">key</td>
<td style="width: 107px; height: 72px;">headerValue</td>
<td style="width: 403px; height: 72px;">Get a string containing a particular header's value from your HTTP request. If you have added headers using the httprequest.addHeader method, you can use this method to retrieve that value.</td>
</tr>
<tr style="height: 120px;">
<td style="width: 265px; height: 120px;"><a href="#httprequestgetresponseheaderkey">httprequest.getResponseHeader(key)</a></td>
<td style="width: 97px; height: 120px;">key</td>
<td style="width: 107px; height: 120px;">headerValue</td>
<td style="width: 403px; height: 120px;">Get the string containing a particular header’s value from your HTTP response. If there are multiple response headers with the same name, then their values are returned as a single concatenated string, where each value is separated by a pair of comma and space.</td>
</tr>
<tr style="height: 120px;">
<td style="width: 265px; height: 120px;"><a href="#httprequestgetstatuscode">httprequest.getStatusCode()</a></td>
<td style="width: 97px; height: 120px;">none</td>
<td style="width: 107px; height: 120px;">responseCode</td>
<td style="width: 403px; height: 120px;">Get the HTTP response code from your HTTP request. After you make a httprequest.get, httprequest.post, or httprequest.post call, the HTTP response will have a number code. Usually 200 is used if the request has succeeded. For more information, see <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Status" target="_blank" rel="noopener">here</a>.</td>
</tr>
<tr style="height: 96px;">
<td style="width: 265px; height: 96px;"><a href="#httprequestgeturl">httprequest.get(url)</a></td>
<td style="width: 97px; height: 96px;"> url</td>
<td style="width: 107px; height: 96px;">responseString</td>
<td style="width: 403px; height: 96px;">Make an HTTP GET request. Any headers or parameters added before making the request will be included by Domo when making the get request. All URLs must use https.</td>
</tr>
<tr style="height: 96px;">
<td style="width: 265px; height: 96px;"><a href="#httprequestposturl">httprequest.post(url)</a></td>
<td style="width: 97px; height: 96px;"> url</td>
<td style="width: 107px; height: 96px;">responseString</td>
<td style="width: 403px; height: 96px;">Make an HTTP POST request without any request body. Any headers or parameters added before making the request will be included by Domo when making the post request. All URLs must use https.</td>
</tr>
<tr style="height: 96px;">
<td style="width: 265px; height: 96px;"><a href="#httprequestposturl-bodystring">httprequest.post(url, bodyString)</a></td>
<td style="width: 97px; height: 96px;"> url, bodyString</td>
<td style="width: 107px; height: 96px;">responseString</td>
<td style="width: 403px; height: 96px;">Make an HTTP POST request with a request body. Any headers or parameters added before making the request will be included by Domo when making the post request. All URLs must use https.</td>
</tr>
<tr style="height: 96px;">
<td style="width: 265px; height: 96px;"><a href="#httprequestputurl-bodystring">httprequest.put(url, bodyString)</a></td>
<td style="width: 97px; height: 96px;"> url, bodyString</td>
<td style="width: 107px; height: 96px;">responseString</td>
<td style="width: 403px; height: 96px;">Make an HTTP PUT request with a request body. Any headers or parameters added before making the request will be included by Domo when making the put request. All URLs must use https.</td>
</tr>
</tbody>
</table>

### Metadata
---
Information you may need to run your connector will be stored in a metadata JavaScript object. Access data from the metadata object in the same way you would access data from any JavaScript object.

#### Metadata object structure

```json
{  
   "account":{  
      "username": <<null or data from authentication>>,
      "password": <<null or data from authentication>>,
      "apikey": <<null or data from authentication>>,
      "clientKey": <<null or data from authentication>>,
      "clientSecret": <<null or data from authentication>>,
      "authorizationURL": <<null or data from authentication>>,
      "accessTokenURL": <<null or data from authentication>>,
      "scope": <<null or data from authentication>>,
      "additionalParameters": <<null or data from authentication>>,
      "accesstokenMethod": <<null or data from authentication>>,
      "tokenAddlParams": <<null or data from authentication>>,
      "accesstoken": <<null or data from authentication>>,
      "code": <<null or data from authentication>>
   },
   "report":<<name of selected report>>,
   "days":1,
   "parameters":{  
      <<key/value pairs
        key = parameter name 
        value = selected parameter value (or array of values)>>
   },
   "discovery":{

   },
   "baseurl":"https://api.domo.com"
}
```

#### Metadata access examples
```js
//Access accessToken in the account object.
var token = metadata.account.accesstoken;

//Access a parameter named "Region in United States"
//This will return an array of strings if the parameter type is a discovery tree. This will return a string if it's any other parameter type.
var region = metadata.parameter["Region in United States"];
```

### SQL
---
These SQL methods are used in the data processing code block. They are specifically used in the cases that require the state to be saved between runs.
<table style="height: 366px; width: 906px; border-collapse: collapse; border-style: none;">
<tbody>
<tr style="height: 24px;">
<td style="width: 352px; height: 24px;"><strong>Method</strong></td>
<td style="width: 205px; height: 24px;"><strong>Parameters</strong></td>
<td style="width: 145px; height: 24px;"><strong>Return</strong></td>
<td style="width: 191px; height: 24px;"><strong>Description</strong></td>
</tr>
<tr style="height: 48px;">
<td style="width: 352px; height: 48px;">sql.createTable(tableName, schema, (optional) addIfNotExists)</td>
<td style="width: 205px; height: 48px;">(tableName, schema, (optional) addIfNotExists)</td>
<td style="width: 145px; height: 48px;">none</td>
<td style="width: 191px; height: 48px;">Create a table and define its columns</td>
</tr>
<tr style="height: 72px;">
<td style="width: 352px; height: 72px;">sql.select(columns, from, (optional) where, (optional) useDistinct)</td>
<td style="width: 205px; height: 72px;">(columns, from, (optional) where, (optional) useDistinct)</td>
<td style="width: 145px; height: 72px;">jsonArray</td>
<td style="width: 191px; height: 72px;">Return columns from database table</td>
</tr>
<tr style="height: 48px;">
<td style="width: 352px; height: 48px;">sql.update(tableName, values, (optional) where)</td>
<td style="width: 205px; height: 48px;">(tableName, values, (optional) where)</td>
<td style="width: 145px; height: 48px;">none</td>
<td style="width: 191px; height: 48px;">Update values in a database table</td>
</tr>
<tr style="height: 48px;">
<td style="width: 352px; height: 48px;">sql.insert(table, values)</td>
<td style="width: 205px; height: 48px;">(table, values)</td>
<td style="width: 145px; height: 48px;">none</td>
<td style="width: 191px; height: 48px;">Insert values in a database table</td>
</tr>
<tr style="height: 48px;">
<td style="width: 352px; height: 48px;">sql.delete(tableName, (optional) where)</td>
<td style="width: 205px; height: 48px;">(tableName, (optional) where)</td>
<td style="width: 145px; height: 48px;">none</td>
<td style="width: 191px; height: 48px;">Delete values in a database table</td>
</tr>
<tr style="height: 48px;">
<td style="width: 352px; height: 48px;">sql.export()</td>
<td style="width: 205px; height: 48px;">none</td>
<td style="width: 145px; height: 48px;">none</td>
<td style="width: 191px; height: 48px;">Export the current state of the database</td>
</tr>
</tbody>
</table>
&nbsp;

To store the state of the database between runs, the 'Save Database Between Runs' checkbox must be checked.

<img class="alignnone size-full wp-image-3466" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2018/09/22040052/Screen-Shot5.png" alt="" />

### AWS
---
These AWS methods are used specifically to create S3 AWS client, to put the content under the specified name at the defined path, and to get the content of the specified file at the defined path.
<table style="height: 366px; width: 906px; border-collapse: collapse; border-style: none;">
<tbody>
<tr style="height: 24px;">
<td style="width: 259px; height: 24px;"><strong>Method</strong></td>
<td style="width: 149px; height: 24px;"><strong>Parameters</strong></td>
<td style="width: 82px; height: 24px;"><strong>Return</strong></td>
<td style="width: 403px; height: 24px;"><strong>Description</strong></td>
</tr>
<tr style="height: 48px;">
<td style="width: 259px; height: 61px;">aws.createClient(region, key, secret)</td>
<td style="width: 149px; height: 61px;">(region, key, secret)</td>
<td style="width: 82px; height: 61px;">none</td>
<td style="width: 403px; height: 61px;">Creates an AWS S3 client</td>
</tr>
<tr style="height: 72px;">
<td style="width: 259px; height: 10px;">aws.put(path, name, value)</td>
<td style="width: 149px; height: 10px;">(path, name, value)</td>
<td style="width: 82px; height: 10px;">none</td>
<td style="width: 403px; height: 10px;">Puts the value content under the specified name at the defined path</td>
</tr>
<tr style="height: 48px;">
<td style="width: 259px; height: 48px;">aws.get(path, name)</td>
<td style="width: 149px; height: 48px;">(path, name)</td>
<td style="width: 82px; height: 48px;">String</td>
<td style="width: 403px; height: 48px;">Gets the content of the named file at the defined path</td>
</tr>
</tbody>
</table>

#### Examples
```js
aws.createClient(metadata.account.region, metadata.account.key, metadata.account.secret)

aws.put("project/documents", "test.json", '{"hello": "world"}')

var res = aws.get("project/documents", "test.json");
```

### Method Details

---
#### Auth Methods

These methods are specifically used in the authentication code block.

#### auth.authenticationSuccess() 

*Set during the authentication process to indicate that the credentials have been successfully validated.*

> Parameters:  
>  - None

> Returns:   
> - None

Example:
```
if(httprequest.getStatusCode() == 200){
  auth.authenticationSuccess();
} else {
  auth.authenticationFailed('Your username and password are incorrect');
}
```

#### auth.authenticationFailed(errorMessage)
*Set during the authentication process to indicate that the credentials could not be validated.*

> Parameters:  
>  - **errorMessage**: Message indicating why the authentication failed. 

> Returns:   
> - None

Example:
```js
if(httprequest.getStatusCode() == 200){
  auth.authenticationSuccess();
} else {
  auth.authenticationFailed('Error connecting to earthquake.usgs.gov');
}
```


#### Datagrid Constants
--- 

These constants are specifically used in the data processing code block to define the type of your data in each of your datagrid columns.

#### datagrid.DATA_TYPE_STRING

*Set a column dataType to receive a string.*

Example:
```js
datagrid.addColumn(‘Account ID’, datagrid.DATA_TYPE_STRING);
```

#### datagrid.DATA_TYPE_DOUBLE

*Set a column dataType to receive a number.*

Example:
```js
datagrid.addColumn(‘Amount’, datagrid.DATA_TYPE_DOUBLE);
```

#### datagrid.DATA_TYPE_DATETIME

*Set a column dataType to receive a string. Dates inserted into the table need to be formatted yyyy-MM-dd’T’HH:mm:ss.*

Example:
```js
datagrid.addColumn(‘Date Created’, datagrid.DATA_TYPE_DATETIME);
```

#### datagrid.DATA_TYPE_DATE

*Set a column dataType to receive a string. Dates inserted into the table need to be formatted yyyy-MM-dd*

Example:
```js
datagrid.addColumn(‘Date Created’, datagrid.DATA_TYPE_DATE);
```

#### Datagrid Methods
These methods are specifically used in the data processing code block to insert your data into Domo.

----------

#### datagrid.addColumn(columnName, dataType) 
*Adds a column to a table. Defines the data type used by the column.*

> Parameters:
> - **columnName**: The column name that the user will see when they look at the table.
> - **dataType**: The Domo data type. It may be datagrid.DATA_TYPE_STRING, datagrid.DATA_TYPE_DOUBLE, datagrid.DATA_TYPE_DATETIME, or datagrid.DATA_TYPE_DATE. 

> Returns:   
> - None

Example:
```js
datagrid.addColumn(‘Name’, datagrid.DATA_TYPE_STRING);
```

----------
#### datagrid.addCell(cellData) 
*Adds data to one cell in the table. Columns must be defined first.*

> Parameters:  
> - **cellData**: The datum to be inserted into this table cell. The type of the data should match the type in the column.

> Returns:   
> - None

Example:
```js
datagrid.addCell(‘Jane Jones’);
```


----------
#### datagrid.endRow()

*Indicates a row of data is complete and a new row in the table needs to be started.*

> Parameters:  
>  - None

> Returns:   
> - None

Example:
```js
datagrid.addColumn('Name', datagrid.DATA_TYPE_STRING);
datagrid.addColumn('Birthday', datagrid.DATA_TYPE_DATE);

datagrid.addCell('Jane Jones');
datagrid.addCell('2017-10-25');
datagrid.endRow();
```

----------

#### datagrid.error(code, errorMessage) 
*Ends the processing of data and returns an error message to the user.*

> Parameters:  
> - **code**: A integer code you would like to use to define the error.
> - **errorMessage**: An error message that will be returned to the user.

> Returns:   
> - None

Example:
```js
datagrid.error(0, metadata.report + ‘ is not a supported report.’);
```

----------

#### datagrid.magicParseCSV(csvString) 

*Populates the entire datagrid when passed a properly formatted string of comma-separated values. The magicParse automatically determines type, and leaves any undetermined types as strings.*

> Parameters:  
>  - **csvString**: A string containing a comma-separated values. The first line should contain the comma-separated column names.

> Returns:   
> - None

Example:
```js
var res = `Name,Birthday,Department
"Jane Jones",1981-03-04,"Engineering"
"Peter Paul",1975-08-09,"Marketing"`;

datagrid.magicParseCSV(res);
```

Result:
<img src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2017/03/25124149/datagridMagicParseCSV.png" />

#### datagrid.magicParseJSON(jsonString)

*Populates the entire datagrid when passed a  string representation of properly formatted JSON. The magicParse automatically determines type, and leaves any undetermined types as strings.*

> Parameters:  
>  - **jsonString**: A string representation of a properly formatted JSON. The magicParseJSON method only works for JSON table data presented in key/value pairs.

> Returns:   
> - None

Example:
```js
var res = `[{
  "Name": "Jane Jones",
  "Data": {
    "Birthday": "1981-03-04",
    "Department": "Engineering" }
},{
  "Name": "Peter Paul",
  "Data": {
    "Birthday": "1975-08-09",
    "Department": "Marketing" }
}]`;
  
datagrid.magicParseJSON(res);
```

Result:
<img src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2017/03/25131237/datagridMagicParseJSON.png" />

#### datagrid.magicParseXML(xmlString)

*Populates the entire datagrid when passed a  string representation of properly formatted XML. The magicParse automatically determines type, and leaves any undetermined types as strings.*

> Parameters:  
>  - **xmlString**: A string representation of a properly formatted XML. 

> Returns:   
> - None

Example:
```js
var res = `
<BirthdayList>
  <Entry>
    <Name>Jane Jones</Name>
    <Birthday>1981-03-04</Birthday>
    <Department>Engineering</Department>
  </Entry>
  <Entry>
    <Name>Peter Paul</Name>
    <Birthday>1975-08-09</Birthday>
    <Department>Marketing</Department>
  </Entry>
</BirthdayList>
`;

datagrid.magicParseXML(res);
```

Result:
<img src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2017/03/25124149/datagridMagicParseCSV.png" />


#### Discovery Constants
---

This constant is used when building a discovery tree menu in the Configure Reports Advanced Mode.

#### discovery.tree

*Used with a discovery tree. This references the root node in a discovery tree.*

Example:
```js
discovery.addLeaf(discovery.tree, "Jane Jones");

discovery.addNode(discovery.tree, "Marketing");
```

#### Discovery Methods
--- 

These methods are used when building a discovery tree or discovery dropdown in the Configure Reports Advanced Mode.

#### discovery.addOption(optionValue)

*Used with a discovery dropdown. Adds an option to the dropdown menu.*

> Parameters:  
>  - **optionValue**: The value to be displayed in the dropdown menu.

> Returns:   
> - None

Example:
```js
var data = ["Alice", "Jane", "Jim"];

for (let name of data){
  discovery.addOption(name);
}
```

Result:
<img src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2017/03/25154856/discoveryAddOption.png" />

#### discovery.addNode(parentNode, nodeName) 
*Used with a discovery tree. Creates a new child node within the node that is passed as a parameter. To create a node at the root level, you must use discovery.tree as the node parameter.*

> Parameters:  
> - **parentNode**: An existing node object in the discovery tree.
> - **nodeName**: The name displayed on the new node.

> Returns:   
> - **createdNode**: A reference to the newly created node object.

Example:
```js
var data = {
  "Marketing": ["Alice", "Jane", "Jim"], 
  "Engineering": ["Samantha", "George", "Peter"]
};

for (let department in data){
  DOMO.log(department);
  let node = discovery.addNode(discovery.tree, department);
  for (let name of data[department]){
    DOMO.log(name);
    discovery.addLeaf(node, name);
  }
}

discovery.publishTree();
```

Result:
<img src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2017/03/25161621/discoveryAddNode.png" />

----------
#### discovery.addLeaf(parentNode, leafName)

*Used with a discovery tree. Creates a new child leaf within the node that is passed as a parameter.*

> Parameters:  
> - **parentNode**: An existing node object in the discovery tree.
> - **leafName**: The name displayed on the new leaf.

> Returns:   
> - None

Example:
```js
var data = ["Alice", "Jane", "Jim"];

for (let name of data){
  discovery.addLeaf(discovery.tree, name);
}

discovery.publishTree();
```

Result:
<img src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2017/03/25155851/discoveryAddLeaf.png" />

#### discovery.publishTree()

*Used with a discovery tree. This method indicates when you have finished constructing a discovery tree.*

> Parameters:  
> - None

> Returns:   
> - None

Example:
```js
var data = ["Alice", "Jane", "Jim"];

for (let name of data){
  discovery.addLeaf(discovery.tree, name);
}

discovery.publishTree();
```

#### discovery.addOption()
*Used with a discovery dropdown. Adds an option to the dropdown menu. Option name appears as label, option value is used in the code.*

> Parameters:  
> - optionName, optionValue

> Returns:   
> - None


#### Domo Methods
--- 

These methods may be useful in any code block.

#### DOMO.log(value)

*Prints to the Dev Studio console. Make sure you remove any credentials that you are logging for testing before you submit your connector.*

> Parameters:  
>  - **value**: The value to print. In JavaScript, this can be a string, but it doesn't have to be.

> Returns:   
> - None

Example:
```js
//To log a JavaScript object, just log the object. Just like console.log. :)
DOMO.log(metadata);
DOMO.log(‘metadata.report: ‘ + metadata.report);
```

#### DOMO.sleep(milliseconds)
*Can be used to space out http requests.*

> Parameters:  
> - **milliseconds**: An integer value representing the number of milliseconds you want your connector to sleep.

> Returns:   
> - None

Example:
```js
DOMO.sleep(5000);
```

#### DOMO.getState(key)
*If you have set a state for your connector, this method returns the value of the requested state.*

> Parameters:  
> - **key**: The key to the state.

> Returns:   
> - **value**: The value stored with that key.

Example:
```js
DOMO.setState("key", "value");

var value = DOMO.getState("key");
DOMO.log(value);
```

#### DOMO.setState(key, value)

*If you need to set a state for your connector, this method can be used to set a state value which can be returned using DOMO.getState(key).*

> Parameters:  
> - **key**: The key to the state.
> - **value**: The value stored with that key.

> Returns:   
> - None

Example:
```js
DOMO.setState(1, 123456);

var value = DOMO.getState(1);
DOMO.log(value);
```

#### DOMO.parseXML(xmlString)

*Used to convert XML to JSON for easier parsing.*

> Parameters:  
> - **xmlString**: The key to the state.

> Returns:   
> - **jsonObject**: A JSON object.

Example:
```js
var res = `
<BirthdayList>
  <Entry>
    <Name>Jane Jones</Name>
    <Birthday>1981-03-04</Birthday>
    <Department>Engineering</Department>
  </Entry>
  <Entry>
    <Name>Peter Paul</Name>
    <Birthday>1975-08-09</Birthday>
    <Department>Marketing</Department>
  </Entry>
</BirthdayList>
`;

var jsonObject = DOMO.parseXML(res);
DOMO.log(jsonObject);
```

Result:
```js
{  
   "BirthdayList":{  
      "Entry":[  
         {  
            "Department":"Engineering",
            "Birthday":"1981-03-04",
            "Name":"Jane Jones"
         },
         {  
            "Department":"Marketing",
            "Birthday":"1975-08-09",
            "Name":"Peter Paul"
         }
      ]
   }
}
```

#### DOMO.getStartDate(metadata.parameters["Date"])

*Used to set the start date.*

> Parameters:  
> - **Date**: The start date.

> Returns:   
> - Date

Example:
```js
var startDate = DOMO.getStartDate(metadata.parameters["Date"]);
```

#### DOMO.getEndDate(metadata.parameters["Date"])

*Used to set the end date.*

> Parameters:  
> - **Date**: The end date.

> Returns:   
> - Date

Example:
```js
var endDate = DOMO.getEndDate(metadata.parameters["Date"]);
```

#### Domo Encoding Methods
--- 

These methods may be useful in any code block to encode data.

#### DOMO.b64EncodeUnicode(stringToEncode)

*Encodes a string using base64 encoding. Base64 encoding is used in the Basic Authentication process, and most endpoints that use username and password will use the Basic Authentication standard.*

> Parameters:  
>  - **stringToEncode**: The string you wish to encode with base-64 encoding.

> Returns:   
> - **encodedString**: The base-64 encoded string.

Example:
```js
var encodedString = DOMO.b64EncodeUnicode(metadata.account.username + ‘:’ + metadata.account.password);
```

#### DOMO.hmacSHA1(stringToEncode, key)

*Encodes a string using the provided key to create a hmac-SHA1 hash.*

> Parameters:  
> - **stringToEncode**: The string you wish to encode.
> - **key**: The string used to create the hmac-SHA1 hash.

> Returns:   
> - **encodedString**: The hmac-SHA1 encoded string.

Example:
```js
var encodedString = DOMO.hmacSHA1(“password”, “key”);
```

#### DOMO.hmacSHA256(stringToEncode, key)
*Encodes a string using the provided key to create a hmac-SHA256 hash.*

> Parameters:  
> - **stringToEncode**: The string you wish to encode.
> - **key**: The string used to create the hmac-SHA256 hash.

> Returns:   
> - **encodedString**: The hmac-SHA256 encoded string.

Example:
```js
var encodedString = DOMO.hmacSHA256(“password”, “key”);
```

----------

#### DOMO.md5(stringToEncode)

*Encodes a string with the md5 algorithm.*

> Parameters:  
> - **stringToEncode**: The string you wish to encode with md5 encoding.

> Returns:   
> - **encodedString**: The md5 encoded string.

Example:
```js
var encodedString = DOMO.md5(“password”);
```

#### DOMO.getJWT()

*Creates a JSON web token (JWT) token using the assigned algorithm signed with the provided key.
**Note**: You must set the algorithm, key, issuer, subject, expiration, and other claims.
**Supported algorithms**: HS256, RS256, ES256*

> Parameters:  
> - None

> Returns:   
> - **tokenString**: The JWT token.

Example:
```js
//Choose the algorithm, Set the authorization key, issuer, subject, claims, and expiration
DOMO.jwtBuilder.algorithm = “HS256”;
DOMO.jwtBuilder.authKey = "DD558ECE4B3DF7FD31DE964E4F07E43B";
DOMO.jwtBuilder.issuer = "DOMO";
DOMO.jwtBuilder.subject = "12345670";
DOMO.jwtBuilder.claims["abc"] = "test";
DOMO.jwtBuilder.expiration = "1530228571";

//Get the token
var token = DOMO.getJWT();
```

#### Domo Decoding Method
--- 

This method may be useful in any code block to decode data.

#### DOMO.b64DecodeUnicode(stringToDecode)
*Decodes a string using base64 decoding. Base64 decoding is used in the Basic Authentication process, and most endpoints that use username and password will use the Basic Authentication standard.*

> Parameters:
> - **stringToDecode**: The string you wish to decode with base-64 decoding.

> Returns:
> - **decodedString**: The base-64 decoded string.

Example:
````js

var decodedString = DOMO.b64DecodeUnicode(metadata.account.username + ‘:’ + metadata.account.password);
````

#### HTTP Request Methods
--- 
These methods may be useful in any code block. When making your HTTP requests, use the following methods to add headers and parameters, and to make HTTP calls. 
**Note**: All URLs must use https.

#### httprequest.addHeader(key, value) 
*Add a header to your HTTP request. This is how you can add an Authorization header or any other header you need to your HTTP request. Add headers and parameters before you make the HTTP request.*

> Parameters:  
>  - **key**: A string that is the header key.
>  - **value**: A string that is the header value.

> Returns:   
> - None

Example:
```js
var encodedData = DOMO.b64EncodeUnicode(metadata.account.username + ':' + metadata.account.password);

httprequest.addHeader('Authorization', 'Basic ' + encodedData);

var res = httprequest.get('https://developer.domo.com/samplecrm');  
```

#### httprequest.addParameter(key, value)
*Add a parameter to a base URL. Add headers and parameters before you make the HTTP request.*

> Parameters:  
>  - **key**: A string that is the parameter key.
>  - **value**: A string that is the parameter value.

> Returns:   
> - None

Example:
```js
httprequest.addHeader('Authorization', 'OAuth ' + metadata.account.accesstoken);
httprequest.addParameter('metadata', '0');
httprequest.addParameter('fields', 'id,name,accounts');

//The parameters added above will be automatically added to the URL
//Resulting URL: https://graph.facebook.com/v3.1/me?metadata=0&fields=id,name,accounts
var res = httprequest.get('https://graph.facebook.com/v3.1/me');
```

#### httprequest.clearParameters()
*Remove all parameters you have added to an httprequest object.*

> Parameters:  
> - None

> Returns:   
> - None

Example:
```js
httprequest.addHeader('Authorization', 'OAuth ' + metadata.account.accesstoken);
httprequest.addParameter('metadata', '0');
httprequest.addParameter('fields', 'id,name,accounts');

//The parameters added above will be automatically added to the URL
//Resulting URL: https://graph.facebook.com/v3.1/me?metadata=0&fields=id,name,accounts
var res = httprequest.get('https://graph.facebook.com/v3.1/me');

//Clear the parameters to make a different call with the same URL
httprequest.clearParameters();
```

#### httprequest.clearHeaders() 
*Remove all headers you have added to an httprequest object.*

> Parameters:  
> - None

> Returns:   
> - None

Example:
```js
var encodedData = DOMO.b64EncodeUnicode(metadata.account.username + ':' + metadata.account.password);

httprequest.addHeader('Authorization', 'Basic ' + encodedData);

var res = httprequest.get('https://developer.domo.com/samplecrm');

//Clearing header to make call with different header information
httprequest.clearHeaders();
```

#### httprequest.getHeader(key)
*Get a string containing a particular header's value from your HTTP request. If you have added headers using the httprequest.addHeader method, you can use this method to retrieve that value.*

> Parameters:  
> - **key**: A string that is the parameter key.

> Returns:   
> - **headerValue**: A string that is the value associated with the provided key.

Example:
```js
var encodedData = DOMO.b64EncodeUnicode(metadata.account.username + ':' + metadata.account.password);

httprequest.addHeader('Authorization', 'Basic ' + encodedData);
httprequest.addHeader('Agent', metadata.account.agent);

//validate the header value before request
DOMO.log(httprequest.getHeader('Agent'));

var res = httprequest.get('https://developer.domo.com/samplecrm');
```

#### httprequest.getResponseHeader(key)
 
*When you make an HTTP request, the response will usually include a header containing a set of key/value pairs. Use this method to get the string containing a particular header’s value from your HTTP response. If there are multiple response headers with the same name, then their values are returned as a single concatenated string, where each value is separated by a pair of comma and space.*

> Parameters:  
> - **key**: A string that is the parameter key.

> Returns:   
> - **headerValue**: A string that is the value associated with the provided key.

Example:
```js
var encodedData = DOMO.b64EncodeUnicode(metadata.account.username + ':' + metadata.account.password);

httprequest.addHeader('Authorization', 'Basic ' + encodedData);

var res = httprequest.get('https://developer.domo.com/samplecrm');

var expires = httprequest.getResponseHeader('Expires');
```

#### httprequest.getStatusCode()

*Get the HTTP response code from your HTTP request. After you make a httprequest.get, httprequest.post, or httprequest.post call, the HTTP response will have a number code. Usually 200 is used if the request has succeeded. For more information, see <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Status" target="_blank" rel="noopener">here</a>. You can use the response code to gracefully handle failed HTTP requests.*

> Parameters:  
> - None
> Returns:   
> - **responseCode**: The status code that indicates whether your HTTP request has been successfully completed.

Example:
```js
var encodedData = DOMO.b64EncodeUnicode(metadata.account.username + ':' + metadata.account.password);

httprequest.addHeader('Authorization', 'Basic ' + encodedData);

var res = httprequest.get('https://developer.domo.com/samplecrm');
var code = httprequest.getStatusCode();

DOMO.log('Code: ' + code);

if (code == 200){
    //DO WORK
}
else {
    //HANDLE FAILED HTTP REQUEST
}
```

#### httprequest.get(url)

*Make an http get request. Any headers or parameters added before making the request will be included by Domo when making the get request.
**Note**: All URLs must use https.*

> Parameters:  
> - **url**: The URL you would like to use to make an HTTP get request.

> Returns:   
> - **responseString**: The response from the endpoint you called.

Example:
```js
var encodedData = DOMO.b64EncodeUnicode(metadata.account.username + ':' + metadata.account.password);

httprequest.addHeader('Authorization', 'Basic ' + encodedData);

var res = httprequest.get('https://developer.domo.com/samplecrm');
```

#### httprequest.post(url)
*Make an HTTP post request without any request body. Any headers or parameters added before making the request will be included by Domo when making the post request.
**Note**: All URLs must use https.*

> Parameters:  
> - **url**: The URL you would like to use to make an HTTP post request.

> Returns:   
> - **responseString**: The response from the endpoint you called.

Example:
```js
var encodedData = DOMO.b64EncodeUnicode(metadata.account.username + ':' + metadata.account.password);

httprequest.addHeader('Authorization', 'Basic ' + encodedData);

var res = httprequest.post('https://developer.domo.com/samplecrm');
```

#### httprequest.post(url, bodyString)

*Make an HTTP post request with a request body. Any headers or parameters added before making the request will be included by Domo when making the post request. 
**Note**: All URLs must use https.*

> Parameters:  
> - **url**: The URL you would like to use to make an HTTP post request.
> - **bodyString**: The body of your HTTP post request.

> Returns:   
> - **responseString**: The response from the endpoint you called.

Example:
```js
var encodedData = DOMO.b64EncodeUnicode(metadata.account.username + ':' + metadata.account.password);

httprequest.addHeader('Authorization', 'Basic ' + encodedData);

var res = httprequest.post('https://developer.domo.com/samplecrm', 'This is my request body');
```

#### httprequest.put(url, bodyString)

*Make an HTTP put request with a request body. Any headers or parameters added before making the request will be included by Domo when making the put request.
**Note**: All URLs must use https.*

> Parameters:  
> - **url**: The URL you would like to use to make an HTTP get request.
> - **bodyString**: The body of your HTTP post request.

> Returns:   
> - **responseString**: The response from the endpoint you called.

Example:
```js
var encodedData = DOMO.b64EncodeUnicode(metadata.account.username + ':' + metadata.account.password);

httprequest.addHeader('Authorization', 'Basic ' + encodedData);

var res = httprequest.put('https://developer.domo.com/samplecrm', 'this is my request body');
```
