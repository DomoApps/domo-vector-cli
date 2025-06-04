---
stoplight-id: 8s3y9eldnjq8d
---

# Data API

### Base URL

---

```text
GET /data/v1/:alias?:queryOperators
```

- **alias**: the name you provided for the dataset mapping in your app's manifest
- **queryOperators**: URL parameters that enable you to create custom queries of the mapped dataset. Possible query operators are:
- avg
- calendar
- count
- dategrain
- fields
- filter
- groupby
- limit
- max
- min
- offset
- orderby
- sum
- unique

### aggregations

---

Consolidate all rows of a column into a single value or override the default aggregations for `dategrain` and `groupby` clauses. Multiple fields can be specified by delimiting with commas.

```text
GET /data/v1/:alias?{avg|count|max|min|sum|unique}=:fieldAlias1,:fieldAlias2
```

When aggregations are requested without a `groupby` or `dategrain`, then a single row of data will be returned with the aggregated fields **only**.

### calendar

---

Specify which calendar to use for date-related operations such as `todate`, `last`, and `dategrain`.

```text
GET /data/v1/:alias?calendar={fiscal|standard}
```

### dategrain

---

Perform a `groupby` with predefined date grains. By default, numerical columns are summed and unique entries of non-numerical columns are counted. Can be combined with an [aggregation](8s3y9eldnjq8d-data-api#aggregations) to override this default behavior.

```text
GET /data/v1/:alias?dategrain=:dateField by {day|week|month|quarter|year}
```

**Note**: dategrain adds new columns

When graining by "week", "month", or "quarter", a column named `CalendarXXXX` will be returned with the data (e.g. CalendarMonth for month date graining). Date graining by "day" will return a column `Date`, and date graining by "year" will return a column `Year`.

If you already have a column with that name, it will be overridden by this new date field. In addition, the column you request as the date grain will not be present in the result by its original name.

### fields

---

Limit the result set to specific columns from the dataset by providing either the field alias or the original column name (if no alias was defined in the manifest). Multiple fields can be combined into a comma separated string.

```text
GET /data/v1/:alias?fields=:fieldAlias1,:fieldAlias2,:fieldAlias3
```

### filter

---

Limit the rows returned by the request by providing more fine-grained filters. Multiple filter parameters can be combined into a single comma separated string.

```text
GET /data/v1/:alias?filter=amount > 1000, name contains 'Foobar'
```

#### Operators

```text
Op1  Op2         Description
===  ===         ===========
<                Less than
<=               Less than or equals
>                Greater than
>=               Greater than or equals
=    ==          Equals
!=               Not equals
~    contains    Contains
!~   !contains   Doesn't contain
in               In an array of values. ie ["foo", "bar"]
!in              Not in an array of values. ie ["foo", "bar"]
todate           Period to date: eg :dateField todate {day|week|month|quarter|year}
last             Rolling Period: eg :dateField last :int {hours|days|weeks|months|quarters|years}
```

### groupby

---

Aggregates identical data into groups. By default, numerical columns are summed and unique entries of non-numerical columns are counted. Can be combined with an [aggregation](8s3y9eldnjq8d-data-api#aggregations) to override this default behavior. Multiple columns can be grouped by delimiting each with a comma.

```text
GET /data/v1/:alias?fields=color,shape,qty&groupby=color,shape
```

### limit & offset

---

Provides the ability to paginate the query results.

```text
GET /data/v1/:alias?offset=:int&limit=:int
```

### orderby

---

Rows can be ordered by any column in `ascending` or descending order. The order defaults to ascending and a multi-column order can be defined by delimiting each order clause with a comma.

```text
GET /data/v1/:alias?orderby=:fieldName {ascending|descending}
```

**Note**: You cannot order on an aggregation

### Data Formats

---

You can control the format of the data returned from this endpoint by setting the request `Accept` header. If leveraging the [domo.js](e947d87e17547-domo-js) library, the same can be accomplished by passing a `format` option in the request. Please refer to the [domo.get()](e947d87e17547-domo-js#domoget) documentation for further details.

array-of-objects

#### Header

```js
XMLHttpRequest.setRequestHeader('Accept', 'array-of-objects');
```

#### domo.js

```js
domo.get('my-alias', { format: 'array-of-objects' });
```

#### Example Response

```json
[
  { "first": "Joe", "last": "Jacobs", "age": 39 },
  { "first": "Henry", "last": "Woolington", "age": 23 }
]
```

CSV

#### Header

```js
XMLHttpRequest.setRequestHeader('Accept', 'text/csv');
```

#### domo.js

```js
domo.get('my-alias', { format: 'csv' });
```

#### Example Response

```js
'first', 'last', 'age';
'Joe', 'Jacobs', '39';
'Henry', 'Woolington', '23';
```

Excel

#### Header

```js
XMLHttpRequest.setRequestHeader(
  'Accept',
  'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
);
```

#### domo.js

```js
domo.get('my-alias', { format: 'excel' });
```

Detailed JSON

#### Header

```js
XMLHttpRequest.setRequestHeader('Accept', 'application/json');
```

#### domo.js

```js
domo.get('my-alias', { format: 'array-of-arrays' });
```

#### Example Response

```json
{
  "columns": ["first", "last", "age"],
  "datasource": "93a5b974-1aac-49fc-ba9a-a67dff658be6",
  "device": "ad3-prod1-03",
  "duration": "35",
  "fromcache": "true",
  "metadata": [
    {
      "dataSourceId": "93a5b974-1aac-49fc-ba9a-a67dff658be6",
      "type": "STRING"
    },
    {
      "dataSourceId": "93a5b974-1aac-49fc-ba9a-a67dff658be6",
      "type": "STRING"
    },
    { "dataSourceId": "93a5b974-1aac-49fc-ba9a-a67dff658be6", "type": "LONG" }
  ],
  "numColumns": 3,
  "numRows": 2,
  "queryUrl": "/query/training/93a5b974-1aac-49fc-ba9a-a67dff658be6",
  "rows": [
    ["Joe", "Jacobs", 39],
    ["Henry", "Woolington", 23]
  ]
}
```

### Beast Modes

---

Previously a known limitation of the Data API, you can now optionally use beast modes in your queries. In order to use beast modes in your data request, the `useBeastMode` query parameter must be set to true.

#### Basic Example

The following example shows a query that returns only a beast mode column (as noted by the `fields` operator). You'll notice that the `useBeastMode=true` query string parameter is added to this request.

```js
domo
  .get('/data/v1/dataAlias?useBeastMode=true&fields=beastModeAlias')
  .then(function (data) {
    console.log('data', data);
  });
```

In this example, the `beastModeAlias` field is the alias provided to the column in your manifest that maps to a beast mode that has been wired up on the wiring page of an app.

<!-- theme: danger -->

> #### Warning
>
> By adding the `useBeastMode=true` query string parameter to your data calls, some built-in query functionality is disabled.

Traditionally, when not using beast modes in your request, if you provide a groupby operator but don't specify an aggregation operator, Domo will automatically sum the other columns for you (if they are numbers) or count them (if they are strings or dates). When beast mode is enabled, you must explicitly provide some sort of aggregation any time you use a groupby operator. That can either be by using an aggregation operator in the query string or by providing an aggregation function in the formula of your beast mode calculation. It must be thought of as structuring a SQL query, wherein if you create a SQL query that has a group by but not all fields in the SELECT statement were aggregated or included in the group by, SQL will throw an error. It might look something like this:

```text
ERROR: column “MY_TABLE.MY_COLUMN” must appear in the GROUP BY clause or be used in an aggregate function
```

The reason that the Data API's default functionality must be turned off when using beast modes is that a beast mode can have its own aggregation in a calculation. If a sum or a count is assumed, as it would be traditionally, and the beast mode already contained an aggregate function in its calculation, then you would run into an "aggregation within an aggregation error."

#### Aggregation Example

If you want to sum a beast mode that does not already contain any aggregation functions in its formula and group by another column, you can use a request similar to the following. Note that if you use an aggregation operator on a beast mode column that already has an aggregation function in its formula, it will cause an error to occur (aggregate within an aggregate).

```js
domo
  .get(
    '/data/v1/dataAlias?useBeastMode=true&fields=beastModeAlias,reps&sum=beastModeAlias&groupby=reps',
  )
  .then(function (data) {
    console.log('data', data);
  });
```

If you want to obtain the same results but your beast mode already contains a sum function in its formula, then you can exclude the sum operator as a query parameter. Note that if your beast mode does contain an aggregation in its formula and you are including multiple fields in your query, you must specify a `groupby` operator so that the query knows how to group the results of the beast mode's aggregation function.

```js
domo
  .get(
    '/data/v1/dataAlias?useBeastMode=true&fields=beastModeAlias,reps&groupby=reps',
  )
  .then(function (data) {
    console.log('data', data);
  });
```

<!-- theme: info -->

> #### Known Limitation
>
> You cannot use the filter operator on a beast mode that contains an aggregate function (the equivalent of a having clause which is not supported in Domo today).

### SQL API

---

You can now use SQL to query your Domo DataSet as an alternative to using the Data API. You can use the same SQL you're used to except JOINs and trigonometric functions. For example:

```js
domo
  .post('/sql/v1/dataAlias', 'SELECT * FROM dataAlias limit 100', {
    contentType: 'text/plain',
  })
  .then(function (data) {
    console.log({ data });
  });
```

<!-- theme: danger -->

> #### Warning
>
> The SQL API does not currently support page filters.
