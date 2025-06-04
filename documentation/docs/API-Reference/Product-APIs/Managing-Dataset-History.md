---
stoplight-id: prt23r0zqw1vq
---

# Managing Dataset History

### Authentication

Requests to the endpoints in this document should be authenticated using an access token. The token should be passed using the `X-DOMO-Developer-Token` header. For information about generating an access token see https://domo-support.domo.com/s/article/360042934494?language=en_US.

### Listing Dataset Versions

This endpoint lists the data versions that are available for a dataset. Each dataversion records includes metadata indicating the following:

- uploadStatus - success, error, processing
- numRows - the number of rows in the upload
- numBytes - the size of the upload in bytes
- schemaId - the schema associated with the data
- recordedDate - the time at which the data was made available to the system
- uploadCompletedDate - the time the upload finished uploading

**Method:** `GET`  
**Endpoint:** `https://{instance}.domo.com/api/data/v2/datasources/<dataset-id>/dataversions`

#### Example Request

```
DOMAIN=yourdomain.domo.com
DATASET=your-dataset-id
ACCESS_TOKEN=accesstoken
curl --request GET \
  --url https://${DOMAIN}/api/data/v2/datasources/${DATASET}/dataversions \
  --header "X-DOMO-Developer-Token: ${ACCESS_TOKEN}"
```

#### Response

```json
[
  {
    "schemaId": 5,
    "dataId": 3,
    "uploadStatus": "success",
    "recordedDate": "2023-03-31T14:21:13Z",
    "uploadCompletedDate": "2023-03-31T14:21:13Z",
    "numRows": 18,
    "numBytes": 458
  },
  {
    "schemaId": 7,
    "dataId": 4,
    "uploadStatus": "success",
    "recordedDate": "2023-03-31T14:21:28Z",
    "uploadCompletedDate": "2023-03-31T14:21:28Z",
    "numRows": 499,
    "numBytes": 6890
  }
]
```

### Deleting Dataset Versions

This endpoint removes a set of data versions from Vault for a given dataset. This is a destructive operation and cannot be undone. A list of data versions to delete is supplied in the body of the request. The method returns an empty response with a `200 OK` http status if the delete was successful.

If you are deleting data versions that are part of the active data in Adrenaline you should include the `index=true` request parameter in order to remove the data from Adrenaline as well.

**Method:** `DELETE`  
**Endpoint:** `https://{instance}.domo.com/api/data/v2/datasources/<dataset-id>/dataversions?index=<true|false>`

#### Request Body

List of data versions.

```
[dataversion]
```

#### Example Request

```
DOMAIN=yourdomain.domo.com
DATASET=your-dataset-id
ACCESS_TOKEN=accesstoken
VERSION=2
curl --request DELETE \
  --url https://${DOMAIN}/api/data/v2/datasources/${DATASET}/dataversions \
  --header 'Content-Type: application/json' \
  --header "X-DOMO-Developer-Token: ${ACCESS_TOKEN}" \
  --data "[${VERSION}]"
```
