# Return the schema for a specified Dataset

**Method**: `GET`  
**Endpoint**: `/api/data/v2/datasources/<DATASET_ID>/schemas/latest`

**Example**:

```json
{
  "method": "GET",
  "url": "https://{instance}.domo.com/api/data/v2/datasources/<DATASET_ID>/schemas/latest",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body":
}
```

**Response**:  
Description of the Response with an example of the data

```json
200:

{
    "schema": {
        "columns": [
            {
                "type": "<TYPE>",
                "name": "<NAME>",
                "id": "<ID>",
                "visible": true,
                "metadata": {
                    "colLabel": "<LABEL>",
                    "colFormat": "",
                    "isEncrypted": false
                }
            }
        ]
    }
}

```
