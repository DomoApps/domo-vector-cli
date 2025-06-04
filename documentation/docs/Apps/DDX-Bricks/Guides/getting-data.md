---
stoplight-id: 2efe8599c6ad9
---

# Getting Data in Domo Bricks

### Method 1 - Using the SQL Endpoint
---
This method allows you to use traditional SQL to query. This method currently only returns an “array-of-arrays” (see output formats below):

```js
var query = 'SELECT SUM(amount) as Sales FROM dataset0';
domo.post('/sql/v1/myDatasetAlias', query, {contentType: 'text/plain'}).then(function(result) { … });
```

To use a column name with spaces in your query, wrap the column name with back-ticks, for example:

```js
var query = 'SELECT SUM(`Store Sales`) as Sales FROM dataset0';
```

### Method 2 - Using the Data Endpoint
---
This is the traditional method for getting data out of Domo:

```js
var query = `fields=amount&sum=amount`;
domo.get('/data/v1/myDatasetAlias?' + query)
  .then(function(result)
     { … }
  );
```

Here are some references and examples to get you started:

- [Data Queries example code](../../App-Framework/Guides/querying-data.md)
- [Data API deep dive](../../../Domo-App-APIs/Data-API.md)


#### Output Formats
The default data endpoint output format may not always be the format you need. Supported formats are:

- `array-of-objects` (default)
- `array-of-arrays`
- `excel`
- `csv`

You can specify the format like this:

```js
domo.get('/data/v1/dataset?' + query, {format: 'csv'})
  .then(function(result)
    { … }
  );
```


