---
stoplight-id: 9f2fe40b1bdb9
---

# Examples

This page contains code examples for the Custom Connector sections that require JavaScript. The Connector Dev Studio has several built-in functions to make the process easier for you. For a list of these built-in JavaScript functions, see [Reference](reference.md).

- [User Authentication](examples.md#user-authentication)
  - [No Authentication](examples.md#No_Authentication)
  - [Username and Password](examples.md#Username_and_Password)
  - [API Key](examples.md#API_Key)
  - [OAuth 2.0](examples.md#OAuth_2)
- [Discovery](examples.md#discovery) (used in Configure Selectable Reports / Advanced Mode)
  - [Dropdown](examples.md#Dropdown)
  - [Basic Tree Menu](examples.md#basic-tree-menu)
  - [Nested Tree Menu](examples.md#Nested_Tree_Menu)
- [Process Data Examples](examples.md#process-data-examples)
  - [Sample CRM](examples.md#sample-crm)
  - [Sample CRM using datagrid.magicParseCSV](examples.md#sample-crm-using-datagridmagicparsecsv)
  - [USGS](examples.md#usgs)

### User Authentication

---

#### No Authentication

No code is required. But if you would like, you can make an API call to check the connection.

```js
var res = httprequest.get(
  "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"
);

DOMO.log("res: " + res);

if (httprequest.getStatusCode() == 200) {
  auth.authenticationSuccess();
} else {
  auth.authenticationFailed("Error connecting to earthquake.usgs.gov");
}
```

#### Username and Password

Determine how your API endpoint needs to authenticate with the username and password. Most endpoints that use username and password will use the [Basic Authentication](https://en.wikipedia.org/wiki/Basic_access_authentication) standard. The username and password are stored in the `metadata.account` object.

Access the stored username and password

```js
metadata.account.username;
metadata.account.password;
```

Basic authentication with 64-bit encoding

```js
//This logging is here for testing! Remove before publishing your connector
DOMO.log("metadata.account.username: " + metadata.account.username);
DOMO.log("metadata.account.password: " + metadata.account.password);

var encodedData = DOMO.b64EncodeUnicode(
  metadata.account.username + ":" + metadata.account.password
);

httprequest.addHeader("Authorization", "Basic " + encodedData);

var res = httprequest.get("https://developer.domo.com/samplecrm");

if (httprequest.getStatusCode() == 200) {
  auth.authenticationSuccess();
} else {
  auth.authenticationFailed("Your username and password are incorrect");
}
```

#### API Key

An [API key](https://en.wikipedia.org/wiki/Application_programming_interface_key) is a token passed in as a header or a query parameter in an HTTP request. It uniquely identifies who is making the call and is often non-expiring. You will need to determine how the REST API you wish to call needs to send the API key. The API key is stored in the `metadata.account` object.

If your API endpoint requires it, the Connector Dev Studio includes functions for building a [JSON Web Token (JWT)](https://en.wikipedia.org/wiki/JSON_Web_Token).

Access the stored API key

```js
metadata.account.apikey;
```

Use the API key as a query parameter

```js
//This logging is here for testing! Remove before publishing your connector
DOMO.log("metadata.account.apiKey: " + metadata.account.apikey);

// Adding the api key. You need to know the key your api endpoint expects.
var res = httprequest.get(
  "https://samplecrm.domo.com/samplecrm?apikey=" + metadata.account.apikey
);

// Make sure to determine and set the authentication status to either success or failure.
if (httprequest.getStatusCode() == 200) {
  auth.authenticationSuccess();
} else {
  auth.authenticationFailed(
    "The api key you entered is invalid. Please try again with a valid key."
  );
}
```

Insert the API key into the header

```js
//This logging is here for testing! Remove before publishing your connector
DOMO.log("metadata.account.apiKey: " + metadata.account.apikey);

// Example of inserting API key into header. You need to know the key your api endpoint expects.
httprequest.addHeader("API-KEY", metadata.account.apikey);
var res = httprequest.get("https://developer.domo.com/samplecrm");

// Make sure to still determine and set the authentication status to either success or failure.
if (httprequest.getStatusCode() == 200) {
  auth.authenticationSuccess();
} else {
  auth.authenticationFailed(
    "The api key you entered is invalid. Please try again with a valid key."
  );
}
```

Build a JWT token

```js
//This logging is here for testing! Remove before publishing your connector
DOMO.log('metadata.account.apiKey: ' + metadata.account.apikey);

// Example of using the API key to create a JWT token
DOMO.jwtBuilder.algorithm = “HS256”;
DOMO.jwtBuilder.authKey = metadata.account.apikey;
DOMO.jwtBuilder.issuer = “DOMO”;
DOMO.jwtBuilder.subject = “12345670”;
DOMO.jwtBuilder.claims[“abc”] = “test”;
DOMO.jwtBuilder.expiration = “1530228571”

var token = DOMO.getJWT()

DOMO.log(token);

httprequest.addHeader(“JWT”, token);
var res = httprequest.get('https://samplecrm.domo.com/samplecrm');

// Make sure to still determine and set the authentication status to either success or failure.
if (httprequest.getStatusCode() == 200) {
  auth.authenticationSuccess();
} else {
  auth.authenticationFailed('The jwt token you entered is invalid. Please try again with a valid token.');
}
```

#### OAuth 2.0

[OAuth 2.0](https://oauth.net/2/) is the industry-standard for secure authentication. If your cloud API endpoint uses OAuth 2.0, you are in luck: Domo has automated the processes of using your stored data to retrieve your access token. After you have filled in the appropriate fields and clicked **Get Access Token**, your access token and code are stored in the `metadata.account` object.

Access the stored access token and code

```js
metadata.account.accesstoken;
metadata.account.code;
```

Set authentication success based on token

```js
//This logging is here for testing! Remove before publishing your connector
DOMO.log("accesstoken: " + metadata.account.accesstoken);
DOMO.log("code: " + metadata.account.code);

// Make sure token is in the metadata.account object.
if (metadata.account.accesstoken) {
  auth.authenticationSuccess();
} else {
  auth.authenticationFailed("Authentication has failed.");
}
```

Set authentication success based on call made with token

````js
//This logging is here for testing! Remove before publishing your connector
DOMO.log('accesstoken: ' + metadata.account.accesstoken);
DOMO.log('code: ' + metadata.account.code);

httprequest.addHeader('Authorization', 'OAuth ' +  metadata.account.accesstoken);
var res = httprequest.get('https://graph.facebook.com/v3.1/me?metadata=0&fields=id,name,accounts');

try {
  var name = JSON.parse(res).name;
  if (name) {
  auth.authenticationSuccess();
  } else {
  auth.authenticationFailed('Authentication has failed.');
  }
catch(err) {
  auth.authenticationFailed('Authentication has failed.');
}
}

### Discovery
---
When configuring your reports, if you add custom parameters and select the parameter type **Discovery**, you will need to write JavaScript code to build and populate the discovery object. This section gives examples for building a discovery dropdown and discovery trees. The data filled in by the user from any parameters you add are stored in the `metadata.parameters` object.

#### Access the parameter data
```js
metadata.parameters["<<Parameter Name>>"]
````

#### Dropdown

This example makes a call to the Facebook API to get all the pages controlled by this user. It inserts them as options into a discovery dropdown. This will allow a user to select just one Facebook page to run a report on.

Dropdown methods

```js
discovery.addOption(value, label);
```

Access dropdown parameter data

```js
metadata.parameters["<<Parameter Name>>"];
```

Dropdown discovery example

```js
// Call API
httprequest.addHeader("Authorization", "OAuth " + metadata.account.accesstoken);
var res = httprequest.get(
  "https://graph.facebook.com/v3.1/me?metadata=0&fields=id,name,accounts"
);

// Parse response
var data = JSON.parse(res).accounts.data;

for (let page in data) {
  // Add each Facebook page as a option to the dropdown
  discovery.addOption(data[page].value, data[page].name);
}
```

#### Basic Tree Menu

This example makes a call to the Facebook API to get all the pages controlled by this user. This will allow the user to select multiple Facebook pages to run a report on. To create a series of checkboxes, add each item as a leaf to the root node, `discovery.tree`. The results selected by the users are stored in a JavaScript array.

Access tree menu root node

```js
discovery.tree;
```

Tree menu methods

```js
discovery.addNode(parentNode, "<<Node Name>>");
discovery.addLeaf(parentNode, "<<Leaf Name>>");
discovery.publishTree();
```

Access tree menu parameter data

```js
metadata.parameters["<<Parameter Name>>"];
```

Basic tree menu discovery example

```js
// Call API
httprequest.addHeader("Authorization", "OAuth " + metadata.account.accesstoken);

var res = httprequest.get(
  "https://graph.facebook.com/v3.1/me?metadata=0&fields=id,name,accounts"
);

// Parse response
var data = JSON.parse(res).accounts.data;

for (let page in data) {
  // Add each Facebook page as a leaf to the root of the tree
  discovery.addLeaf(discovery.tree, data[page].name);
}

// Remember to call publishTree() when you have add all nodes and leaves!
discovery.publishTree();
```

#### Nested Tree Menu

You can nest checkboxes into categories by adding nodes to the `discovery.tree` root. If a user checks a parent checkbox, all the checkboxes nested in it will be selected. This example nests countries in parent nodes that represent regions. The results selected by the users are stored in a JavaScript array.

Access tree menu root node

```js
discovery.tree;
```

Tree menu methods

```js
discovery.addNode(parentNode, "<<Node Name>>");
discovery.addLeaf(parentNode, "<<Leaf Name>>");
discovery.publishTree();
```

Access tree menu parameter data

```js
metadata.parameters["<<Parameter Name>>"];
```

Nested tree menu discovery example

```js
// Create node using discovery.tree as the parent
var northAmerica = discovery.addNode(discovery.tree, "North America");
// Add Leaves
discovery.addLeaf(northAmerica, "Canada");
discovery.addLeaf(northAmerica, "USA");
discovery.addLeaf(northAmerica, "Mexico");

var centralAmerica = discovery.addNode(discovery.tree, "Central America");
discovery.addLeaf(centralAmerica, "Panama");
discovery.addLeaf(centralAmerica, "Costa Rica");

var southAmerica = discovery.addNode(discovery.tree, "South America");
// Nesting nodes in the southAmerica node
var west = discovery.addNode(southAmerica, "West");
var east = discovery.addNode(southAmerica, "East");
discovery.addLeaf(east, "Argentina");
discovery.addLeaf(west, "Chile");
discovery.addLeaf(west, "Peru");
discovery.addLeaf(east, "Brazil");

// Remember to publish the tree
discovery.publishTree();
```

### Process Data Examples

---

The Connector Dev Studio has a couple of example connectors provided to you: **Sample CRM** and **USGS**.

The following examples of data processing blocks are pulled from these sample connectors.

![Sample Custom Connector](https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2018/09/24120315/SampleCustom.png)

#### Sample CRM

- **Authentication type**: Username and password
- **Reports**: Opportunities
- **Parameters**: None
- **Endpoint data return format**: CSV

```js
//This logging is here for testing! Remove before publishing your connector
DOMO.log("metadata.account.username: " + metadata.account.username);
DOMO.log("metadata.account.password: " + metadata.account.password);
DOMO.log("metadata.report: " + metadata.report); // Opportunities

var encodedData = DOMO.b64EncodeUnicode(
  metadata.account.username + ":" + metadata.account.password
);

// Perform work per report
if (metadata.report == "Opportunities") {
  // Compose http request and call API Endpoint
  httprequest.addHeader("Authorization", "Basic " + encodedData);
  var res = httprequest.get("https://developer.domo.com/samplecrm");
  var code = httprequest.getStatusCode();

  // Check for successful http call
  if (code == 200) {
    // Parse Return
    var lines = res.split("r");
    var header = lines[0].split(",");

    // Store data in domo
    //Add Columns. There are four data types:
    //    datagrid.DATA_TYPE_STRING,
    //    datagrid.DATA_TYPE_DOUBLE
    //    datagrid.DATA_TYPE_DATETIME and
    //    datagrid.DATA_TYPE_DATE
    datagrid.addColumn("Account.Id", datagrid.DATA_TYPE_STRING);
    datagrid.addColumn("Account.Industry", datagrid.DATA_TYPE_STRING);
    datagrid.addColumn("Account.Name", datagrid.DATA_TYPE_STRING);
    datagrid.addColumn("Amount", datagrid.DATA_TYPE_DOUBLE);
    datagrid.addColumn("CloseDate", datagrid.DATA_TYPE_DATETIME);
    datagrid.addColumn("CreatedDate", datagrid.DATA_TYPE_DATETIME);
    datagrid.addColumn("Id", datagrid.DATA_TYPE_STRING);
    datagrid.addColumn("IsClosed", datagrid.DATA_TYPE_STRING);
    datagrid.addColumn("IsWon", datagrid.DATA_TYPE_STRING);
    datagrid.addColumn("LastActivityDate", datagrid.DATA_TYPE_DATETIME);
    datagrid.addColumn("LastModifiedDate", datagrid.DATA_TYPE_DATETIME);
    datagrid.addColumn("LeadSource", datagrid.DATA_TYPE_STRING);
    datagrid.addColumn("Name", datagrid.DATA_TYPE_STRING);
    datagrid.addColumn("NextStep", datagrid.DATA_TYPE_STRING);
    datagrid.addColumn("Probability", datagrid.DATA_TYPE_DOUBLE);
    datagrid.addColumn("StageName", datagrid.DATA_TYPE_STRING);
    datagrid.addColumn("Type", datagrid.DATA_TYPE_STRING);
    datagrid.addColumn("ForecastCategoryName", datagrid.DATA_TYPE_STRING);
    datagrid.addColumn("Strategic_Account__c", datagrid.DATA_TYPE_STRING);
    datagrid.addColumn("Forecasted_ACV__c", datagrid.DATA_TYPE_DOUBLE);
    datagrid.addColumn("Competitor__c", datagrid.DATA_TYPE_STRING);
    datagrid.addColumn("Owner.CreatedDate", datagrid.DATA_TYPE_DATETIME);
    datagrid.addColumn("Owner.Email", datagrid.DATA_TYPE_STRING);
    datagrid.addColumn("Owner.FullPhotoUrl", datagrid.DATA_TYPE_STRING);
    datagrid.addColumn("Owner.Id", datagrid.DATA_TYPE_STRING);
    datagrid.addColumn("Owner.IsActive", datagrid.DATA_TYPE_STRING);
    datagrid.addColumn("Owner.Manager", datagrid.DATA_TYPE_STRING);
    datagrid.addColumn("Owner.Name", datagrid.DATA_TYPE_STRING);
    datagrid.addColumn("Owner.UserRole.Name", datagrid.DATA_TYPE_STRING);

    // Add Rows
    for (var i = 1; i < lines.length; i++) {
      console.log("line: " + lines[i]);
      // For heavy logging, use browser console logging
      var rows = lines[i].split(",");
      // Add cells
      for (var j = 0; j < rows.length; j++) {
        // Ensure time string in right format. It needs to be yyyy-MM-dd'T'HH:mm:ss
        if (j == 4 || j == 9) {
          datagrid.addCell(rows[j] + "T00:00:00");
        } else {
          datagrid.addCell(rows[j]);
        }
      }
      // Make sure to end the row!
      datagrid.endRow();
    }
  } else {
    // Gracefully handle an http error
    DOMO.log("Received Http Error: " + code);
    datagrid.error(code, "Received HTTP error: " + code);
  }
} else {
  // Gracefully handle a report error
  DOMO.log(metadata.report + " is not a supported report.");
  datagrid.error(0, metadata.report + " is not a supported report.");
}
```

#### Sample CRM using datagrid.magicParseCSV

- Authentication type: Username and password
- Reports: Opportunities
- Parameters: None
- Endpoint data return format: CSV

```js
//This logging is here for testing! Remove before publishing your connector
DOMO.log("metadata.account.username: " + metadata.account.username);
DOMO.log("metadata.account.password: " + metadata.account.password);
DOMO.log("metadata.report: " + metadata.report); // Opportunities

var encodedData = DOMO.b64EncodeUnicode(
  metadata.account.username + ":" + metadata.account.password
);

// Perform work per report
if (metadata.report == "Opportunities") {
  // Compose http request and call API Endpoint
  httprequest.addHeader("Authorization", "Basic " + encodedData);
  var res = httprequest.get("https://developer.domo.com/samplecrm");
  var code = httprequest.getStatusCode();

  // Check for successful http call
  if (code == 200) {
    // Parse Return and store data in Domo
    console.log(res);
    datagrid.magicParseCSV(res);
  } else {
    // Gracefully handle an http error
    DOMO.log("Received Http Error: " + code);
    datagrid.error(code, "Received HTTP error: " + code);
  }
} else {
  // Gracefully handle a report error
  DOMO.log(metadata.report + " is not a supported report.");
  datagrid.error(0, metadata.report + " is not a supported report.");
}
```

#### USGS

- Authentication type: None
- Reports: Past Hour, Past Day, Past 7 Days, Past 30 Days, Pull data from the last X day(s)
- Parameters: None
- Endpoint data return format: JSON

```js
DOMO.log("metadata.report: " + metadata.report);

if (metadata.report == "Past Hour") {
  pastHour();
} else if (metadata.report == "Past Day") {
  pastDay();
} else if (metadata.report == "Past 7 Days") {
  past7Days();
} else if (metadata.report == "Past 30 Days") {
  past30Days();
} else if (metadata.report == "Pull data from the last X day(s)") {
  pastXDays();
} else {
  DOMO.log(metadata.report + " is not a supported report.");
  datagrid.error(0, metadata.report + " is not a supported report.");
}

// Report-specific functions
function pastHour() {
  DOMO.log("pastHour");
  processRecords(
    "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"
  );
}

function pastDay() {
  DOMO.log("pastDay");
  processRecords(
    "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"
  );
}

function past7Days() {
  DOMO.log("past7Days");
  processRecords(
    "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"
  );
}

function past30Days() {
  DOMO.log("past30Days");
  processRecords(
    "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson"
  );
}

function pastXDays() {
  DOMO.log("pastXDays");
  processRecords(
    "http://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=" +
      calculateEndDate() +
      "&endtime=" +
      currentDate()
  );
}

// Time calculation functions
function calculateEndDate() {
  var now = new Date(); // This will be UTC when running server side
  var end = new Date(now.getTime() - metadata.days * 1000 * 60 * 60 * 24);

  DOMO.log("Start: " + now);
  DOMO.log("End: " + end);

  return (
    end.getFullYear() +
    "-" +
    addOneLeadingZero(end.getMonth() + 1) +
    "-" +
    addOneLeadingZero(end.getDate())
  );
}

function currentDate() {
  var now = new Date(); // This will be UTC when running server side
  return (
    now.getFullYear() +
    "-" +
    addOneLeadingZero(now.getMonth() + 1) +
    "-" +
    addOneLeadingZero(now.getDate())
  );
}

function addOneLeadingZero(value) {
  if (value < 10 && value > -10) {
    value = "0" + value;
  }
  return value;
}

// Function to make call and build dataset
function processRecords(url) {
  var res = httprequest.get(url);
  var code = httprequest.getStatusCode();
  DOMO.log("code " + code);
  DOMO.log("res" + res);

  // Check for successful http call
  if (code == 200) {
    var data = JSON.parse(res).features;
    // Adding columns
    datagrid.addColumn("Place", datagrid.DATA_TYPE_STRING);
    datagrid.addColumn("Magnitude", datagrid.DATA_TYPE_STRING);
    datagrid.addColumn("Time", datagrid.DATA_TYPE_DATETIME); // date format needs to be yyyy-MM-dd'T'HH:mm:ss
    datagrid.addColumn("URL", datagrid.DATA_TYPE_STRING);

    DOMO.log("data: ");

    for (var i = 0; i < data.length; i++) {
      var quakeDetails = data[i].properties;
      // Adding data, cell by cell
      datagrid.addCell(quakeDetails.place);
      datagrid.addCell(quakeDetails.mag);
      datagrid.addCell(formatTime(quakeDetails.time));
      datagrid.addCell(quakeDetails.url);
      // REMEMBER TO END ROW!
      datagrid.endRow();
    }
  } else {
    // Gracefully handle an http error
    DOMO.log("Received Http Error: " + code);
    datagrid.error(code, "Received HTTP error: " + code);
  }
}

// Function to convert date format from USGA to date format required by Domo
function formatTime(value) {
  var d = new Date(value);
  return (
    d.getFullYear() +
    "-" +
    addOneLeadingZero(d.getMonth() + 1) +
    "-" +
    addOneLeadingZero(d.getDate()) +
    "T" +
    addOneLeadingZero(d.getHours()) +
    ":" +
    addOneLeadingZero(d.getMinutes()) +
    ":" +
    addOneLeadingZero(d.getSeconds())
  );
}
```
