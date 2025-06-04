# App DB API

The App DB API allows developers to interact with AppDB, a NoSQL database for storing arbitrary JSON documents. This API supports CRUD operations, querying, and aggregation, enabling developers to manage data efficiently within their Domo applications.

## Features

- **CRUD Operations**: Create, read, update, and delete documents in AppDB collections.
- **Collection Management**: Programmatically update collections.

## Endpoints

### Get Document

**Description**: Retrieve a specific document from a collection.

**HTTP Request**:

```http
GET /api/datastores/v1/collections/{collectionId}/documents/{documentId}
```

**Headers**:

- `X-DOMO-Developer-Token`: `<developer token here>`
- `Accept`: `application/json`
- `Content-Type`: `application/json`

**Response**:

```http
HTTP/1.1 200 OK
```

```json
{
  "id": "12345678-7949-1234-82bb-bd3e533e4c7d",
  "datastoreId": "12345678-2484-1234-af98-c60131367cf2",
  "collectionId": "12345678-78a9-1234-b641-7afc39ba2e84",
  "syncRequired": true,
  "owner": "123456789",
  "createdBy": "123456789",
  "createdOn": "2024-05-08T19:39:00.708226378Z",
  "updatedOn": "2024-05-08T19:39:00.708226378Z",
  "updatedBy": "123456789",
  "content": {}
}
```

### Query Document

**Description**: Retrieve a specific document from a collection via query.

**HTTP Request**:

```http
POST /api/datastores/v2/collections/{collectionId}/documents/query
```

**Headers**:

- `X-DOMO-Developer-Token`: `<developer token here>`
- `Accept`: `application/json`
- `Content-Type`: `application/json`

**Request Body**:

```json
{
  "content.userId": {
    "$eq": "123456789"
  }
}
```

**Response**:

```http
HTTP/1.1 200 OK
```

```json
[
    {
        "id": "12345678-8683-4aa8-a3ca-3ad2c5c4cc47",
        "datastoreId": "12345678-3366-4b4e-b968-48c1b0a453f4",
        "collectionId": "12345678-ef0b-4c2d-8f39-db29042dad57",
        "syncRequired": true,
        "owner": "123456789",
        "createdBy": "123456789",
        "createdOn": "2023-09-26T20:46:10.290Z",
        "updatedOn": "2025-05-08T20:52:33.176Z",
        "updatedBy": "123456789",
        "content": {
            "listId": "12345678-4865-457e-ab4a-6e5ce70a7c69",
            "userId": "123456789",
            "listTitle": "New Test"
        }
    },
    ...
]
```

### List Documents

**Description**: Retrieve all documents from a specified collection. Note there is an upper limit of 10,000 documents. We recommend using pagination to retrieve large sets of documents.

**HTTP Request**:

```http
GET /api/datastores/v1/collections/{collectionId}/documents
```

**Headers**:

- `X-DOMO-Developer-Token`: `<developer token here>`
- `Accept`: `application/json`
- `Content-Type`: `application/json`

**Response**:

```http
HTTP/1.1 200 OK
```

```json
[
  {
    "id": "12345678-7949-1234-82bb-bd3e533e4c7d",
    "datastoreId": "12345678-2484-1234-af98-c60131367cf2",
    "collectionId": "12345678-78a9-1234-b641-7afc39ba2e84",
    "syncRequired": true,
    "owner": "123456789",
    "createdBy": "123456789",
    "createdOn": "2024-05-08T19:39:00.708226378Z",
    "updatedOn": "2024-05-08T19:39:00.708226378Z",
    "updatedBy": "123456789",
    "content": {}
  },
  ...
]
```

### Create Document

**Description**: Add a new document to a specified collection.

**HTTP Request**:

```http
POST /api/datastores/v1/collections/{collectionId}/documents/
```

**Headers**:

- `X-DOMO-Developer-Token`: `<developer token here>`
- `Accept`: `application/json`
- `Content-Type`: `application/json`

**Request Body**:

```json
{
  "content": {
    // content goes here
  }
}
```

**Response**:

```http
HTTP/1.1 200 OK
```

```json
{
  "id": "12345678-7949-1234-82bb-bd3e533e4c7d",
  "datastoreId": "12345678-2484-1234-af98-c60131367cf2",
  "collectionId": "12345678-78a9-1234-b641-7afc39ba2e84",
  "syncRequired": true,
  "owner": "123456789",
  "createdBy": "123456789",
  "createdOn": "2024-05-08T19:39:00.708226378Z",
  "updatedOn": "2024-05-08T19:39:00.708226378Z",
  "updatedBy": "123456789",
  "content": {}
}
```

### Update Document

**Description**: Modify an existing document in a collection.

**HTTP Request**:

```http
PUT /api/datastores/v1/collections/{collectionId}/documents/{documentId}
```

**Headers**:

- `X-DOMO-Developer-Token`: `<developer token here>`
- `Accept`: `application/json`
- `Content-Type`: `application/json`

**Request Body**:

```json
{
  "content": {
    // content goes here
  }
}
```

**Response**:

```http
HTTP/1.1 200 OK
```

```json
{
  "id": "12345678-7949-1234-82bb-bd3e533e4c7d",
  "datastoreId": "12345678-2484-1234-af98-c60131367cf2",
  "collectionId": "12345678-78a9-1234-b641-7afc39ba2e84",
  "syncRequired": true,
  "owner": "123456789",
  "createdBy": "123456789",
  "createdOn": "2024-05-08T19:39:00.708226378Z",
  "updatedOn": "2024-05-08T19:39:00.708226378Z",
  "updatedBy": "123456789",
  "content": {}
}
```

### Delete Document

**Description**: Remove a document from a collection.

**HTTP Request**:

```http
DELETE /api/datastores/v1/collections/{collectionId}/documents/{documentId}
```

**Headers**:

- `X-DOMO-Developer-Token`: `<developer token here>`
- `Accept`: `application/json`
- `Content-Type`: `application/json`

**Response**:

```http
HTTP/1.1 204 No Content
```

### Bulk Delete Documents

**Description**: Remove multiple documents from a collection in a single request.

_Please note, this will end up reaching the maximum url length limit of your browser/client. If you have a large number of documents to delete, this can be done in batches._

**HTTP Request**:

```http
DELETE /api/datastores/v1/collections/{collectionId}/documents/bulk?ids=[ids]
```

**Headers**:

- `X-DOMO-Developer-Token`: `<developer token here>`
- `Accept`: `application/json`
- `Content-Type`: `application/json`

**Response**:

```http
HTTP/1.1 200 OK
```

```json
{
  "Deleted": 1
}
```

### Update Collection Schema

**Description**: Update the schema of a collection.

**HTTP Request**:

```http
PUT /api/datastores/v1/collections/{collectionId}
```

**Headers**:

- `X-DOMO-Developer-Token`: `<developer token here>`
- `Accept`: `application/json`
- `Content-Type`: `application/json`

**Request Body**:

```json
{
  "schema": {
    "columns": [
      {
        "type": "STRING",
        "name": "username",
        "visible": true
      },
      {
        "type": "STRING",
        "name": "band",
        "visible": true
      },
      {
        "type": "STRING",
        "name": "favorite color",
        "visible": true
      }
    ]
  },
  "syncEnabled": true
}
```

**Response**:

```http
HTTP/1.1 200 OK
```

```json
{
  "id": "12345678-7949-1234-82bb-bd3e533e4c7d",
  "datastoreId": "12345678-a8ee-4ef7-a235-87b77993a33d",
  "defaultPermissions": null,
  "requiredAuthorities": null,
  "owner": 123456789,
  "name": "CollectionName",
  "datasourceId": null,
  "schema": {
    "columns": [
      {
        "type": "STRING",
        "name": "username"
      },
      {
        "type": "STRING",
        "name": "band"
      },
      {
        "type": "STRING",
        "name": "favorite color"
      }
    ]
  },
  "filters": null,
  "syncEnabled": true,
  "syncRequired": true,
  "fullReplaceRequired": false,
  "lastSync": null,
  "createdOn": "2022-06-07T21:35:18.736Z",
  "updatedOn": "2024-05-08T19:55:32.158402516Z",
  "updatedBy": 123456789
}
```

### Update Collection Permissions

**Description**: Update permissions for a collection as it relates to a specific Custom App. Proxy ID is available in the Asset Library

**Parameter Options**:

| **Permission**   | **Name**       | **Description**                                                                |
| ---------------- | -------------- | ------------------------------------------------------------------------------ |
| `read`           | Read           | Grants the ability to read documents in the collection.                        |
| `share`          | Share          | Grants the ability to share the collection with other users or groups.         |
| `delete`         | Delete         | Allows the deletion of the entire collection.                                  |
| `write`          | Write          | Provides write access to the collection, including creating and updating data. |
| `admin`          | Admin          | Grants full administrative control over the collection.                        |
| `create_content` | Create Content | Allows creating new documents in the collection.                               |
| `read_content`   | Read Content   | Enables reading the content of documents in the collection.                    |
| `update_content` | Update Content | Permits updating existing documents in the collection.                         |
| `delete_content` | Delete Content | Authorizes the deletion of documents from the collection.                      |

**HTTP Request**:

```http
PUT /api/datastores/v1/collections/{collectionId}/permission/RYUU_APP/{proxyId}?permissions=read,create_content,read_content,update_content,delete_content
```

**Headers**:

- `X-DOMO-Developer-Token`: `<developer token here>`
- `Accept`: `application/json`
- `Content-Type`: `application/json`

**Response**:

```http
HTTP/1.1 204 No Content
```
