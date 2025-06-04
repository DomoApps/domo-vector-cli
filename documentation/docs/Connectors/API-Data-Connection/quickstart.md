---
stoplight-id: 278e9d611eaa6
---

# Quickstart

Creating a DataSet, importing data, and creating a Personalized Data Permission (PDP) policy within the DataSet is straightforward and only requires three steps:
<ol>
 	<li>Create a DataSet</li>
 	<li>Import data into a DataSet</li>
 	<li>Create a Personalized Data Permission (PDP) policy for a DataSet</li>
</ol>
After creating a DataSet, you can continue to import data if needed or create multiple PDP policies to filter specific data within a DataSet for various sets of users.

<!-- theme: info -->

> #### Note
> In order to utilize this Quickstart you will need to obtain an [access token](../../API-Reference/Domo-APIs/API-Authentication.yaml) or you can leverage any of [Domo's SDKs](../../Getting-Started/sdks.md) which will also handle authentication.

### Step 1: Create a DataSet
---

DataSets represent the data extracted from a data source; the extracted data is used as the foundation to create visualizations within Domo.  Within Domo you can leverage data further by using Domo's data pipeline to transform, process, and aggregate for richer content and insight. 

This code creates a DataSet via the [DataSet](../../API-Reference/Domo-APIs/DataSet-API.yaml) API:

#### Sample Request

See this sample request in [Java](https://github.com/domoinc/domo-java-sdk/blob/master/domo-java-sdk-all/src/test/java/com/domo/sdk/datasets/CreateExample.java), [Python](https://github.com/domoinc/domo-python-sdk/blob/master/examples/dataset.py).

```HTTP
POST https://api.domo.com/v1/datasets
Content-Type: application/json
Accept: application/json
Authorization: bearer <your-valid-oauth-access-token>

{
  "name" : "Leonhard Euler Party",
  "description" : "Mathematician Guest List",
  "rows" : 0,
  "schema" : {
    "columns" : [ {
      "type" : "STRING",
      "name" : "Friend"
    }, {
      "type" : "STRING",
      "name" : "Attending"
    } ]
  }
}
```
Domo returns a new `DataSet` object with all the relevant details:

#### Sample Response
```HTTP
HTTP/1.1 201 Created
Content-Type: application/json

{
  "id" : "4405ff58-1957-45f0-82bd-914d989a3ea3",
  "name" : "Leonhard Euler Party",
  "description" : "Mathematician Guest List",
  "rows" : 0,
  "columns" : 0,
  "schema" : {
    "columns" : [ {
      "type" : "STRING",
      "name" : "Friend"
    }, {
      "type" : "STRING",
      "name" : "Attending"
    } ]
  },
  "owner" : {
    "id" : 27,
    "name" : "DomoSupport"
  },
  "createdAt" : "2016-06-21T17:20:36Z",
  "updatedAt" : "2016-06-21T17:20:36Z"
}
```

Once you've created the DataSet, store its `id` value somewhere to utilize when importing additional data or applying data permissions.

### Step 2: Import data into a DataSet
---
With the recently created DataSet `id`, you can import data into the DataSet:

#### Sample Request
See this sample request in [Java](https://github.com/domoinc/domo-java-sdk/blob/master/domo-java-sdk-all/src/test/java/com/domo/sdk/datasets/ImportDataExample.java), [Python](https://github.com/domoinc/domo-python-sdk/blob/master/examples/dataset.py).

```HTTP
PUT https://api.domo.com/v1/datasets/4405ff58-1957-45f0-82bd-914d989a3ea3/data
Content-Type: text/csv
Authorization: bearer <your-valid-oauth-access-token>

Pythagoras,FALSE
Alan Turing,TRUE
George Boole,TRUE
Pythagoras,FALSE
Alan Turing,TRUE
George Boole,TRUE
```

Domo will return a response of success or error for the outcome of data being imported into the DataSet.

#### Sample Response
```HTTP
HTTP/1.1 204 No Content
```

### Step 3: Create a Personalized Data Permission
---
Once you've created a DataSet that has data, you can now create a Personalized Data Permission (PDP) policy to restrict access to rows of data within the DataSet. Please note that users and groups must exist before creating a PDP policy.

#### Sample Request
See this sample request in [Java](https://github.com/domoinc/domo-java-sdk/blob/master/domo-java-sdk-all/src/test/java/com/domo/sdk/datasets/CreateExample.java), [Python](https://github.com/domoinc/domo-python-sdk/blob/master/examples/dataset.py).

```HTTP
POST https://api.domo.com/v1/datasets/4405ff58-1957-45f0-82bd-914d989a3ea3/policies
Content-Type: application/json
Accept: application/json
Authorization: bearer <your-valid-oauth-access-token>

{
  "name" : "Only Show Attendees",
  "filters" : [ {
    "column" : "Attending",
    "values" : [ "TRUE" ],
    "operator" : "EQUALS"
  } ],
  "users" : [ 27 ]
}
```

Domo returns a subset of the DataSet object specific to the data permission policy.

#### Sample Response
```HTTP
HTTP/1.1 201 Created
Content-Type: application/json


{
  "id" : 8,
  "type": "user",
  "name": "Only Show Attendees",
  "filters": [ {
    "column": "Attending",
    "values": [ "TRUE" ],
    "operator": "EQUALS",
    "not": false
  } ],
  "users": [ 27 ],
  "groups": [ ]
}
```

<!-- theme: info -->
> #### PDP Off By Default
>
> Since PDP is off by default in new DataSets, when you're ready, you can turn it on with the [Update DataSet Details endpoint](https://developer.domo.com/portal/b96e1dbabff23-update-data-set-details).

### Next steps
---
Congrats! You now have a DataSet with data you've uploaded with the DataSet API.

You may want to learn how to manage DataSets in more detail, or explore these other topics, here:

- [Import and Export Data](import-and-export-data.md)
- [Manage DataSets](managing-datasets.md)
- [Create Personalized Data Permissions (PDP)](personalized-data-permissions.md)
- [DataSet API Reference](../../API-Reference/Domo-APIs/DataSet-API.yaml)

### Need additional help?
---
No problem, we'd love to help. Explore our [documentation](https://knowledge.domo.com), answers to [frequently asked questions](https://community-forums.domo.com/main), or join other developers in Domo's [Developer Forum](https://community-forums.domo.com/main).  For additional support, feel free to [email us](mailto:support@domo.com) or [contact our sales team](mailto:sales@domo.com).



