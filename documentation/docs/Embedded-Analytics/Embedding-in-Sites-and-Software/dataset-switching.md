---
stoplight-id: j83p65ecrjtr1
---

# Dataset Switching

Dataset switching redirects dynamically change the underlying data of embedded dashboards. As long as column schema is consistent, server-side code can swap out the template dataset for the table relevant for the viewer. Most customers prefer to combine a master dataset across multiple customers and personalize the row access with PDP. However, dataset switching is helpful when that combined dataset simply is not an option.

## Dataset switching redirect with no programmatic filters for rows

```js

visualization1: {
  clientId: process.env.CLIENT_ID, clientSecret: process.env.CLIENT_SECRET, embedId: process.env.EMBED_ID1,
    datasetRedirects: {
                          "originalDataSet1":"targetDataSet1",
                          "originalDataset2":"targetDataSet2"
    },
},

```

## Dataset switching redirect layered with programmatic filters for rows

```js

visualization1: {
    clientId: process.env.CLIENT_ID, clientSecret: process.env.CLIENT_SECRET, embedId: process.env.EMBED_ID1,
    datasetRedirects: {
      "a19d0ef1-ca31-4bfd-b168-018b93109671":"a19d0ef1-ca31-4bfd-b168-018b93109672"
      "a19d0ef1-ca31-4bfd-b168-018b93109673":"a19d0ef1-ca31-4bfd-b168-018b93109674"
    },
    filters: [
      {"column": "Color", "operator": "IN", "values": ["Red"]},
      {"column": "Model", "operator": "IN", "values": ["Mountain","Road","Commuter"]}
    ],
}
```