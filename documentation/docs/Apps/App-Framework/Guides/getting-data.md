---
stoplight-id: 6a5d7a2870145
---

# Getting Data

Custom Apps can request data by making an HTTP GET or POST request. The manifest.json file helps manage the data that your app is using.

Learn more in the manifest [reference](manifest.md) documentation.

&nbsp;

### Sample Mapping
---
Data is requested by making XHR requests to the following data API endpoint:

```
/data/v1/[DataSet Alias]
```

where `[DataSet Alias]` is replaced with the desired DataSet alias from your design's [manifest.json file](manifest.md).

So, if your app manifest had an alias named `sales`, your app could request data from the following URL:

```
GET /data/v1/sales
```

For the examples in this section, we will consider a design using the following mapping in the manifest.json file.

```json
"mapping": [
  {
    "alias": "sales",
    "dataSetId": "5168da8d-1c72-4e31-ba74-f609f73071dd",
    "fields": []
  }
]
```

The following data fetching examples show how one could compute the sum of the `amount` column in the `sales` DataSet from the above sample mapping.


### SQL API
---

You can also query your DataSet with the SQL API using the following endpoint:

```
/sql/v1/[DataSet Alias]
```

So, if your app manifest had an alias named `sales`, your app could request data from the following URL:

```
POST /data/v1/sales
```

To get compute the sum of the `amount` column in the `sales` DataSet from the above sample mapping you could make a request with the [domo.js library](domo.js.md) in the following way:

```js
domo.post('/sql/v1/sales', "SELECT SUM(amount) FROM sales", {contentType: 'text/plain'}).then(function(total) { console.log({total}); });
```

### Examples
---
#### [domo.js](domo.js.md) (recommended)

```js
domo.get('/data/v1/sales').then(function(sales){
  var salesSum = 0;
  sales.forEach(function(sale){
    salesSum += sale.amount;
  });
})
```

#### XHR

```javascript
var xhr = new XMLHttpRequest();
xhr.open('GET', '/data/v1/sales', true);
xhr.onload = function(e) {
  if (this.status === 200) {
    var json = JSON.parse(xhr.response);
    var salesSum = 0;
    for(var i = 0; i < json.length; i++) {
      salesSum += json[i].amount
    }
  }
};
xhr.send();
```

#### jQuery

```javascript
$.get( '/data/v1/sales', function(json) {
  var salesSum = 0;
  for(var i = 0; i < json.length; i++) {
    salesSum += json[i].amount;
  }
});
```

#### Oboe.js

```javascript
  var salesSum = 0;
  oboe('/data/v1/sales')
    .node('!.*', function(obj) {
      salesSum += obj.amount;
    });
```

#### Angular

```javascript
$http.get('/data/v1/sales').
  success(function(data, status, headers, config) {
    for(var i = 0; i < data.length; i++)
      $scope.salesSum += data[i].amount;
  });
```
