# REST QUERY

This is a simple library to create data query URLs for [getting Domo data](https://developer.domo.com/docs/dev-studio-references/data-api). Use in conjunction with [domo.js](https://developer.domo.com/docs/dev-studio/dev-studio-domo-js-reference).

## Dependencies

[Install](https://developer.domo.com/docs/dev-studio-tools/domo-js#Installation) `domo.js`. This is preinstalled on all [DDX Bricks](https://developer.domo.com/docs/ddx-bricks/ddx-bricks-overview)

## Installation

You can add this library to any project via npm:

```
npm install --save @domoinc/query
```


## Quick Reference

- [.select](#selecting-columns)
- [.where](#data-filtering)
- [.groupBy](#group-by)
- [.orderBy](#order-by)
- [.limit](#limit)
- [.offset](#offset)
- [.dateGrain](#date-grain)
- [.previousPeriod](#previous-period)
- [.rollingPeriod](#rolling-period)
- [.periodToDate](#period-to-date)
- [.useFiscalCalendar](#fiscal-calendar)
- [.useBeastModes](#beast-modes)
- [Aggregation](#aggregation)
- [Date filtering](#date-filtering)
- [Date range filtering](#date-range-filtering)

## Examples

```typescript
const datasetAlias = 'sales';

// build query and fetch data

const response = await new Query()
  .select(['col1', 'col2'])
  .groupBy('col1')
  .fetch(datasetAlias);

// example using TypeScript:
//   .fetch<{col1: string; col2: number}>(datasetAlias);

// Do something with the response data
...
```

```typescript
/**
 * Returns the max date
 */
async function getMaxDate() {
  return new Query()
    .select(['date'])
    .orderBy('date', 'descending')
    .limit(1)
    .fetch('datasetalias');

// example using Typescript:
//   .fetch<{date: string}>('datasetalias');
}

...

console.log(await getMaxDate());
```

```typescript
/**
 * Example using domo.js
 *
 * Return the brands for a given Engagement Segment
 */
function getEngagementSegmentBrands(engagementSegmentValue) {
  const esBrands = new Query()
    .select(['engagementSegmentBrandName', 'engagementSegmentBrandId'])
    .where('segmentValue').equals(engagementSegmentValue)
    .groupBy(['engagementSegmentBrandName', 'engagementSegmentBrandId']);

  return domo.get(esBrands.query('datasetalias'));
}

...

getEngagementSegmentBrands('Loyals').then((data) => {
  console.log(data);
});
```

## API

### Building a Query

This section will explain the options available to you for building queries. Here is an example of a complex query.

> Note:
>
> - Refer to the [**Date Range Filtering**](#date-range-filtering) section for accepted values for the `dateGrain` and `periodToDate` functions.
> - Refer to the [**Order By**](#order-by) section for accepted values for the `orderBy` function.

```typescript
import { default as Query, DateGrain } from '@domoinc/query';

// initialize query
const query = new Query();

// JavaScript example:
query
  .select(['col1', 'col2', 'col3', 'col4', 'col5'])
  .where('col1')
  .greaterThan(2)
  .groupBy('col2')
  .dateGrain('col4', 'day')
  .periodToDate('col5', 'week')
  .orderBy('col3', 'descending')
  .limit(10)
  .offset(2);

// example using Typescript:
//  .dateGrain('col4', DateGrain.DAY)
//  .periodToDate('col5', DateGrain.WEEK)
//  .orderBy('col3', OrderByDirection.DESCENDING)
```

#### Selecting Columns

Use `select` to specify the column names for the columns you want returned.

> Column names are the alias names specified in the manifest.json file.

```typescript
query.select(['col1', 'col2', 'col3']);
```

#### Data Filtering

Filter data by using the `where(columName)` function followed by the desired filter function.

```typescript
query
  .select(['col1', 'col2', 'col3'])
  .where('col1')
  .lessThan(10)
  .where('col2')
  .contains('foobar');
```

##### Filter Functions

```typescript
// Less than
.lt(value)
.lessThan(value)

// Less than or equal
.lte(value)
.lessThanOrEqual(value)

// Greater than
.gt(value)
.greaterThan(value)

// Greater than or equal
.gte(value)
.greaterThanOrEqual(value)

// Equals
.equals(value)

// Not equals
.notEquals(value)

// Between
.between(start, end)

// Contains
.contains(value)

// Does not contain
.notContains(value)

// In: values is an array
.in(values)

// Not in: values is an array
.notIn(values)
```

#### Date Filtering

The `lt`, `lte`, `gt`, `gte`, `between` filter functions will filter dates when used on a column that is a date. Other functions will treat the date as a string.

```typescript
query
  .select(['date', 'amount'])
  .where('date')
  .greaterThanOrEqual('2014-01-01T00:00:00')
  .where('date')
  .lessThan(new Date('2014-08-01'));
```

#### Date Range Filtering

Columns that are dates can be filtered using specific ranges: `previousPeriod`, `rollingPeriod`, `periodToDate`.

> NOTE: Only 1 date range filter may be used in a query.

A `DateGrain` enum and a `RollingDateGrain` enum are provided with the valid interval options. These are:

```typescript
// date grain
'day';
'week';
'month';
'quarter';
'year';

// rolling date grain
'days';
'weeks';
'months';
'quarters';
'years';
```

##### Previous Period

Data for last year, last month, etc can be requested by using the `previousPeriod` function. This is how you would get data from last year when the date column is named `salesdate`:

> Note:
>
> - Refer to the [**Date Range Filtering**](#date-range-filtering) section for accepted values for the `DateGrain` parameter.

```typescript
// TypeScript:
query.select(['salesdate']).previousPeriod('salesdate', DateGrain.YEAR);

// JavaScript:
query.select(['salesdate']).previousPeriod('salesdate', 'year');
```

##### Rolling Period

A rolling period can be requested by using the `rollingPeriod` function. For example, this is how you would get all data from the last 6 months when your date column is named `salesdate`:

> Note:
>
> - Refer to the [**Date Range Filtering**](#date-range-filtering) section for accepted values for the `RollingDateGrain` parameter.

```typescript
// TypeScript
query
  .select(['salesdate'])
  .rollingPeriod('salesdate', RollingDateGrain.MONTHS, 6);

// JavsScript
query.select(['salesdate']).rollingPeriod('salesdate', 'months', 6);
```

##### Period to Date

Period-to-date filtering is done using the `periodToDate` function. For example, this is how you would get year to date data when the date column is named `salesdate`:

> Note:
>
> - Refer to the [**Date Range Filtering**](#date-range-filtering) section for accepted values for the `DateGrain` parameter.

```typescript
// TypeScript
query.select(['salesdate']).periodToDate('sales date', DateGrain.YEAR);

// JavaScript
query.select(['salesdate']).periodToDate('sales date', 'year');
```

#### Group By

Data can be transformed to a group-by operation using the `groupBy` function.
Aggregations for columns can be specified in an object where the key is the column name, and the value is an `Aggregation`.

By default, columns are counted.

> Note:
>
> - Refer to the [**Aggregation**](#aggregation) section for accepted values for the `Aggregation` parameter.

```typescript
// TypeScript
query.select(['color', 'shape', 'quantity']).groupBy('color').groupBy({
  shape: Aggregation.COUNT,
  quantity: Aggregation.SUM,
});

// JavaScript
query.select(['color', 'shape', 'quantity']).groupBy('color').groupBy({
  shape: 'count',
  quantity: 'sum',
});
```

The grouping above would make this data:

| color  | shape    | quantity |
| ------ | -------- | -------- |
| red    | square   | 3        |
| green  | square   | 14       |
| blue   | square   | 4        |
| purple | square   | 9        |
| orange | circle   | 3        |
| red    | circle   | 14       |
| green  | circle   | 4        |
| blue   | circle   | 9        |
| purple | triangle | 3        |
| orange | triangle | 14       |
| red    | triangle | 4        |
| green  | triangle | 9        |
| blue   | square   | 3        |
| purple | square   | 14       |
| orange | square   | 4        |
| red    | square   | 9        |

Become aggregated like so:

| color  | shape | quantity |
| ------ | ----- | -------- |
| red    | 4     | 30       |
| orange | 3     | 21       |
| purple | 3     | 26       |
| green  | 3     | 27       |
| blue   | 3     | 16       |

#### Date Grain

Data can be "grained" by date by using the `dateGrain` function.
This is a special type of "group by".

> Note:
>
> - Only 1 column may be date grained in a query.
> - Refer to the [**Date Range Filtering**](#date-range-filtering) section for accepted values for the `DateGrain` parameter.

```typescript
import { default as Query, DateGrain } from '@domoinc/query';

// TypeScript
query.select(['salesdate']).dateGrain('salesdate', DateGrain.MONTH);

// JavaScript
query.select(['salesdate']).dateGrain('salesdate', 'month');
```

This query would group together all data in the data source by month. Each row in the returned data would represent a summary of that data for the month." Like `groupBy` column aggregations may be specified.

```typescript
// TypeScript
query
  .select(['salesdate', 'sales'])
  .dateGrain('salesdate', 'month', { sales: Aggregation.SUM });

// JavaScript
query
  .select(['salesdate', 'sales'])
  .dateGrain('salesdate', 'month', { sales: 'sum' });
```

#### Aggregation

Accepted aggregation values are `'count'`, `'sum'`, `'avg'`, `'min'`, `'max'`, or `'unique'`.

You can use data aggregations to

1. Consolidate all rows of a column into a single value.
2. Specify the aggregation type for date grain and group by queries.

This is done with the `aggregate` function. For example, to specify the aggregations for fields salesTotal and salesAmount as sum and average respectively:

```typescript
// TypeScript
query
  .select(['salesTotal', 'salesAmount'])
  .aggregate({ salesTotal: Aggregate.SUM, salesAmount: Aggregate.AVG });

// JavaScript
query
  .select(['salesTotal', 'salesAmount'])
  .aggregate({ salesTotal: Aggregate.SUM, salesAmount: 'avg' });
```

#### Order By

Rows can be ordered by any column in `'ascending'` or `'descending'` order using the `orderBy` function.

An enum (`OrderByDirection`) is provided to define the order by direction. Valid orderings:

```typescript
'ascending';
'descending';
```

```typescript
// TypeScript
query
  .select(['salesAmount', 'salesRepName'])
  .orderBy('salesAmount', OrderByDirection.ASCENDING)
  .orderBy('salesRepName', OrderByDirection.DESCENDING);

// JavaScript
query
  .select(['salesAmount', 'salesRepName'])
  .orderBy('salesAmount', 'ascending')
  .orderBy('salesRepName', 'descending');
```

#### Limit

For improved performance and latency, you can paginate data using `limit` and `offset`.

```typescript
// only receive the first 10 rows.
query
  .select(['salesAmount', 'salesRepName']);
  .limit(10)
```

#### Offset

To offset the data you get by a certain number, use `offset`.

```typescript
// you could request rows 11-20 like this.
query.select(['salesAmount', 'salesRepName']).limit(10).offset(10);
```

#### Fiscal Calendar

You can specify to use the instances fiscal calendar for date-related operations such as `previousPeriod` or `dateGrain` with `useFiscalCalendar(true)`. The standard calendar is used by default.

```typescript
query.select(['salesAmount', 'salesRepName']).useFiscalCalendar();
```

#### Beast Modes

You can enable beast modes in the query by calling the `useBeastMode`.
true

```typescript
query.select(['salesAmount', 'salesRepName']).useBeastMode();
```