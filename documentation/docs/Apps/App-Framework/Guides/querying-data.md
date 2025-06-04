---
stoplight-id: 6fa7587d4c2ea
---

# Querying Data

The following is a short list of examples on how to create complex queries of your data. This is not intended to be an all-encompassing list so be sure you familiarize yourself with all of the possible query parameters documented in the Data API [documentation](../../../Domo-App-APIs/Data-API.md).

<strong>Note</strong>: All of these examples leverage ES6 arrow notation, template strings, and the [domo.js](domo.js.md) library.

### Select All
---
```js
domo
  .get('data/v1/sales')
  // do something with the results
  .then(console.table);
```

### GroupBy
---
Selecting all the data typically isn't practical, especially as you start working with large datasets. Keeping with best practices, you should aim to only get the data you need. Let's change our query so we summarize sales by sales rep

```js
domo
  .get('/data/v1/sales?fields=rep,amount&groupby=rep')
  // do something with the results
  .then(console.table);
```

### Filters
---
#### Rolling Date

Performance for all time might just give long-time employees the advantage. How about total sales for the last 3 months?

```js
const select = ['rep', 'amount'];
const where = ['date last 3 months'];
const groupBy = ['rep'];

const query = `/data/v1/sales?fields=${select.join()}
  &filter=${where.join()}
  &groupby=${groupBy.join()}`;

domo
  .get(query)
  // do something with the results
  .then(console.table);
```

#### Contains

What if I only want reps with a specific name? 

```js
const select = ['rep', 'amount'];
const where = ['rep ~ ax', 'date last 3 months'];
const groupBy = ['rep'];

const query = `/data/v1/sales?fields=${select.join()}
  &filter=${where.join()}
  &groupby=${groupBy.join()}
`;

domo
  .get(query)
  // do something with the results
  .then(console.table);
```

#### Equal & Dategrain

How about getting monthly sales for a specific sales rep? 

```js
// be sure you include the date field in the `fields` 
// if you want the month grain returned.
const select = ['rep', 'amount', 'date'];
const where = ['rep = Dione Miu'];
const dategrain = ['date by month'];
const groupBy = ['rep'];

const query = `/data/v1/sales?fields=${select.join()}
    &filter=${where.join()}
    &dategrain=${dategrain.join()}
    &groupby=${groupBy.join()}
    &orderby=date
`;

domo
  .get(query)
  // do something with the results
  .then(console.table);
```

### OrderBy
---
Who had the top 10 biggest sales for the last month?

```js
const select = ['rep', 'client', 'amount'];
const where = ['date last 1 month'];
const orderBy = ['amount descending'];

const query = `/data/v1/sales?fields=${select.join()}
  &filter=${where.join()}
  &orderby=${orderBy.join()}
  &limit=10
`;

domo
  .get(query)
  // do something with the results
  .then(console.table);
```

### OrderBy an Aggregation
---
How about getting the Top 10 Reps by the totals sales in the current quarter?

```js
const select = ['rep', 'amount'];
const where = ['stage == closed/won', 'date last 1 quarter'];
const groupby = ['rep'];

const query = `/data/v1/sales?fields=${select.join()}
  &filter=${where.join()}
  &groupby=${groupby.join()}
  &sum=amount
  &calendar=fiscal
`;

return domo.get(query).then(res => {
  // KNOWN LIMITATION: will need to order the results
  // and limit the list on the client side
  return res
    .sort((a, b) => b.amount - a.amount) // sort descending
    .slice(0, 10);	
});
```

### Distinct
---
#### Simple

While there's not a `DISTINCT` option like you'd find in SQL, you can accomplish the same result leveraging `groupby`

```js
domo
  .get('/data/v1/sales?fields=rep&groupby=rep')
  // do something with the results
  .then(console.table);
```

#### Multi-Dimension List

Add you can make it more complex by just adding additional fields to both the `fields` and `groupby` parameters.

```js
domo
  .get('/data/v1/sales?fields=office,territory,state&groupby=office,territory,state')
  // do something with the results
  .then(console.table);
```

