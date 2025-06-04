# Managing DataSets in Domo

DataSets enable visualizations, alerts, and user collaboration that ultimately allows businesses to make data driven decisions and then take action.  Since data a foundation to the Domo platform, it is important to maintain the accuracy and ownership of datasets. The [DataSet API](../API-Reference/Domo-APIs/DataSet-API.yaml) enables you to automate processes to ensure DataSets have the correct information, access, and ownership.

> **NOTE:** 
> Only DataSets created with the API can be updated via APIs.

### Changing DataSet owner
---
Often there may be a case where an owner of a DataSet has changed companies and has had their access removed or simply changed roles in a company and is no longer responsible for the maintenance of a DataSet.  In these cases, the DataSet API allows you to programmatically make updates by first querying for all DataSets owned by a user and then updating each with the new owner's user ID.


#### Sample Request

See this sample request in <a href="https://github.com/domoinc/domo-java-sdk/blob/master/domo-java-sdk-all/src/test/java/com/domo/sdk/datasets/ImportDataExample.java" target="_blank" rel="noopener">Java</a>, <a href="https://github.com/domoinc/domo-python-sdk/blob/master/examples/dataset.py" target="_blank" rel="noopener">Python</a>.

```HTTP
PUT https://api.domo.com/v1/datasets/317970a1-6a6e-4f70-8e09-44cf5f34cf44
Content-Type: application/json
Accept: application/json
Authorization: bearer <your-valid-oauth-access-token>

{
  "name": "Leonhard Euler Birthday Bash",
  "description": "VIP Guest List",
  "owner": {
    "id": 28,
    "name": "Carl Friedrich Gauss"
  },
}
```
Domo will return a response of success or error for the outcome of data being imported into DataSet.

### Sample Response
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": "4405ff58-1957-45f0-82bd-914d989a3ea3",
  "name": "Leonhard Euler Birthday Bash",
  "description": "VIP Guest List",
  "rows": 0,
  "columns": 0,
  "schema": {
    "columns": [ {
      "type": "STRING",
      "name": "Friend"
    }, {
      "type": "STRING",
      "name": "Attending"
    } ]
  },
  "owner": {
    "id": 28,
    "name": "Carl Friedrich Gauss"
  },
  "createdAt": "2016-06-21T17:20:36Z",
  "updatedAt": "2016-06-21T17:48:41Z",
"pdpEnabled": true,
  "policies": [ {
    "id": 8,
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
  } ]
}
```

### Updating a DataSet schema
---

At times, it is necessary to update the DataSet's schema.<!-- Please note that if a DataSet's schema. This sentence was not finished in original docs-->

#### Sample Request

See this sample request in <a href="https://github.com/domoinc/domo-java-sdk/blob/master/domo-java-sdk-all/src/test/java/com/domo/sdk/datasets/ImportDataExample.java" target="_blank" rel="noopener">Java</a>, <a href="https://github.com/domoinc/domo-python-sdk/blob/master/examples/dataset.py" target="_blank" rel="noopener">Python</a>.

```HTTP
PUT https://api.domo.com/v1/datasets/317970a1-6a6e-4f70-8e09-44cf5f34cf44
Content-Type: application/json
Accept: application/json
Authorization: bearer <your-valid-oauth-access-token>

{
  "name": "Leonhard Euler Birthday Bash",
  "description": "VIP Guest List",
  "pdpEnabled": true,
  "schema": {
    "columns": [ {
      "type": "STRING",
      "name": "Friend"
    }, {
      "type": "STRING",
      "name": "Address"
    }, {
      "type": "STRING",
      "name": "Attending"
    } ]
  },
}
```

Domo will return a response of success or error for the outcome of data being imported into DataSet.

#### Sample Response
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": "4405ff58-1957-45f0-82bd-914d989a3ea3",
  "name": "Leonhard Euler Birthday Bash",
  "description": "VIP Guest List",
  "rows": 0,
  "columns": 0,
  "schema": {
    "columns": [ {
      "type": "STRING",
      "name": "Friend"
    }, {
      "type": "STRING",
      "name": "Address"
    }, {
      "type": "STRING",
      "name": "Attending"
    } ]
  },
  "owner": {
    "id": 27,
    "name": "DomoSupport"
  },
  "createdAt": "2016-06-21T17:20:36Z",
  "updatedAt": "2016-06-21T17:48:41Z",
"pdpEnabled": true,
  "policies": [ {
    "id": 8,
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
  } ]
}
```

### Next Steps
Now that you’ve learned more ways to automate your management of DataSets in Domo, read more about extending data management using Personalized Data Permissions (PDP):
- [Personalized Data Permissions](pdp.md)

### Have additional questions?
No problem, we'd love to help. Explore [additional guides and articles](https://domo-support.domo.com/s/knowledge-base?language=en_US) or join other developers in Domo's [Developer Forum](https://dojo.domo.com/main).  For further help, feel free to [email us](mailto:support@domo.com) or [contact our sales team](mailto:sales@domo.com).
