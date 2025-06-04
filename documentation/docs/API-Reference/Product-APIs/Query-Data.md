## Query Dataset

**Method**: `POST`  
**Endpoint**: `api/query/v1/execute/export/<DATASET_ID>?includeHeader=true`

**Example**:

```json
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/query/v1/execute/export/<DATASET_ID>?includeHeader=true",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": { "sql": "SELECT * FROM `<DATASET_ID>` WHERE status='error'" }
}
```

**Response**:  
Description of the Response with an example of the data

```json
200:

{
    "datasource": "<DATASET_ID>",
    "columns": [
    ],
    "metadata": [
    ],
    "numColumns": 10,
    "rows": [
    ],
    "numRows": 15
}

```
