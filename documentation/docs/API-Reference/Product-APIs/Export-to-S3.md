## Export to S3

Export a DataSet to an S3 bucket.

Export your DataSets to an S3 device of your choosing (this is an asynchronous call). You can check the status of your export by calling `/api/query/v1/export/{datasetId}`. Only one active export can run per DataSet at a time. If the data in the DataSet hasn’t changed since the last export, this endpoint returns the export information for the previous export instead of creating a new download. Use temporary AWS credentials whenever possible; if credentials are temporary, provide an AWS session token.

### Security Considerations

To export a datasource, consumers must have at least read access to the DataSet. Any PDP policies applied will be enforced during the export. Once data is uploaded, security depends on the AWS S3 bucket settings. Ensure secure upload locations to prevent unauthorized access.

**Example:** An administrator initiates an export of sensitive compensation data to an S3 location accessible by the entire company, bypassing internal security measures.

### Cross-Region Exports

Cross-region exports are currently unsupported. Ensure that the `REGION` setting in the payload matches the S3 bucket's region.

---

### Create Export

**Method**: `POST`  
**Endpoint**: `/api/query/v1/export/<DATASOURCE_ID>`

#### Request Example

```json
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/query/v1/export/<DATASOURCE_ID>",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json",
    "Charset": "UTF-8"
  },
  "body": {
    "awsAccessKey": "<AWS_KEY>",
    "awsAccessSecret": "<AWS_SECRET>",
    "bucket": "<BUCKET>",
    "path": "<PATH>",
    "region": "<REGION>",
    "queryRequest": {
      "includeBOM": true,
      "useCache": true,
      "query": {
        "columns": [
          { "column": "Customer ID", "exprType": "COLUMN" },
          { "column": "Cardholder ID", "exprType": "COLUMN" },
          { "column": "Sex of Patient", "exprType": "COLUMN" },
          { "column": "Date Filled", "exprType": "COLUMN" },
          { "column": "Label Name", "exprType": "COLUMN" },
          { "column": "Metric Quantity", "exprType": "COLUMN" },
          { "column": "Days Supply", "exprType": "COLUMN" }
        ],
        "groupByColumns": [],
        "orderByColumns": []
      }
    }
  }
}
```

#### Response Examples

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
{
   "bucket": "string",
   "compression": "none",
   "errorCode": "string",
   "exportFormat": "csv",
   "exportId": "97d1244b-8ec4-45f8-a721-ae9602a9fa77",
   "exportStatus": "none",
   "finished": "2019-09-19T15:09:10.086Z",
   "message": "string",
   "started": "2019-09-19T15:09:10.086Z",
   "urlRowCountMap": { "additionalProp1": 0, "additionalProp2": 0 }
}
```

---

### Export Status

**Method**: `GET`  
**Endpoint**: `/api/query/v1/export/<DATASOURCE_ID>`

#### Request Example

```json
{
  "method": "GET",
  "url": "https://{instance}.domo.com/api/query/v1/export/<DATASOURCE_ID>",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json",
    "Charset": "UTF-8"
  },
  "body": {}
}
```

#### Response Example

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
[
  {
    "bucket": "string",
    "compression": "none",
    "errorCode": "string",
    "exportFormat": "csv",
    "exportId": "97d1244b-8ec4-45f8-a721-ae9602a9fa77",
    "exportStatus": "success",
    "finished": "2019-09-19T15:06:46.112Z",
    "message": "string",
    "started": "2019-09-19T15:06:46.112Z",
    "urlRowCountMap": { "additionalProp1": 0, "additionalProp2": 0 }
  }
]
```

---

### Error Status Codes

| Status Code | Meaning                                           |
|--------------|---------------------------------------------------|
| **200**     | Request successful. Export initiated or retrieved.|
| **201**     | Resource created.                                |
| **400**     | Invalid request. Export cannot be created.       |
| **401**     | Access denied. Token is invalid or expired.      |
| **403**     | Insufficient permissions for export access.      |
| **404**     | Dataset ID not found in the customer instance.   |
| **500**     | Unexpected server error.                         |

