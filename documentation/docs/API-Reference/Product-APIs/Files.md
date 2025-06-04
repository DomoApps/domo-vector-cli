---
stoplight-id:
---

# Files API

The Domo Data File Service is a centralized point in your Domo instance to manage, secure, share, and govern all of your files. This enables your applications the ability to upload documents, images, spreadsheets, and many other supported media types for re-use at a later time. The service also provides a version history chain that you can use to track your changes over time.

Domo supports nearly 100 different file types across over 300 file extensions. Please reach out to Domo Support if you have a question about supported file types, as the list changes often.

## Upload a File

Uploading a new file can be accomplished through the following request. You will pass in the file to upload, and Domo will store it and generate a unique identifier for the file, which is returned to you.

**Method:** `POST`  
**Endpoint:** `/api/data/v1/data-files?name={name}&description={description}&public={public}`

<!-- theme: info -->

> #### Security Consideration for Default Permissions
>
> By default, the `public` param is set to `true`, granting all users in the Domo instance access to the file. Remember to set `public` to `false` if you want to restrict access to the user who originally uploaded the file. File permissions can be updated to give access to specific users and groups, if needed. You can find out how to do that by reviewing the [`Update file permissions`](#update-file-permissions) API.

#### Code Example

```js
async function uploadFile(name, description = '', public = false, file) {
  const url = `/api/data/v1/data-files?name=${name}&description=${description}&public=${public}`;
  const response = await fetch(url, file);
  const { dataFileId } = await response.json();
}
```

#### Query Parameters

| Property Name | Type    | Required | Description                                           |
| ------------- | ------- | -------- | ----------------------------------------------------- |
| name          | String  | Required | The name to be given to the file in Domo              |
| description   | String  | Optional | A description of the file                             |
| public        | Boolean | Optional | Whether the permissions of the file are set to public |

#### Request Body

The file to upload.

#### Response

Returns the id of the created file.

```json
HTTP/1.1 200 OK
Content-Type: application/json

{
    "dataFileId": 401
}
```

## Upload a File Revision

The Files API provides versioning support for files that have been uploaded. You may add another version of a file by sending a `PUT` request to the files endpoint referencing the `fileId` of the file you wish to revise.

**Method:** `PUT`  
**Endpoint:** `/api/data/v1/data-files/{dataFileId}`

#### Code Example

```js
async function uploadRevision(dataFileId, file) {
  const url = `/api/data/v1/data-files/${dataFileId}`;
  const response = await fetch(url, file);
  const { revisionId } = await response.json();
}
```

#### Path Parameters

| Property Name | Type    | Required | Description                                                |
| ------------- | ------- | -------- | ---------------------------------------------------------- |
| dataFileId    | Integer | Required | The id of the file for which you wish to upload a revision |

#### Request Body

The file to upload as a revision.

#### Response

Returns the current revision id of the file.

```json
HTTP/1.1 200 OK
Content-Type: application/json

{
    "revisionId": 430
}
```

## Get All Files Metadata

Each file that you upload has corresponding metadata. This endpoint allows you to list all the metadata for each file you have access to. If you want to limit the files returned, you can include query parameters that filter the response.

**Method:** `GET`  
**Endpoint:** `/api/data/v1/data-files/details?userId={userId}&expand={expand}&dataFileIds={dataFileIds}`

#### Code Example

```js
async function getFileDetailsList(
  userId = null,
  expand = null,
  dataFileIds = null,
) {
  const params = new URLSearchParams();
  if (userId !== null) params.append('userId', userId);
  if (expand !== null) params.append('expand', expand);
  if (dataFileIds !== null) params.append('dataFileIds', dataFileIds);

  const queryString = params.toString();
  const url = `/api/data/v1/data-files/details${
    queryString !== '' ? `?${queryString}` : ''
  }`;
  const response = await fetch(url);
  const fileDetailsList = await response.json();
}
```

#### Path Parameters

| Property Name | Type    | Required | Description                                                                                                                    |
| ------------- | ------- | -------- | ------------------------------------------------------------------------------------------------------------------------------ |
| userId        | Integer | Optional | A Domo User Id if you want to limit the files returned by a specific owner                                                     |
| expand        | String  | Optional | An array of string properties specifying the additional details you want to retrieve (either `revisions`, `metadata`, or both) |

#### Query Parameters

| Property Name | Type   | Required | Description                                                                          |
| ------------- | ------ | -------- | ------------------------------------------------------------------------------------ |
| dataFileIds   | String | Optional | An array of File Ids that you wish to be returned if you only want a subset of files |

#### Response

Returns an array of file objects.

```json
HTTP/1.1 200 OK
Content-Type: application/json

[
    {
        "dataFileId": 401,
        "name": "\"SampleFile\"",
        "responsibleUserId": 1089963280,
        "currentRevision": {
            "dataFileRevisionId": 430,
            "dataFileId": 401,
            "contentType": "application/pdf",
            "uploadUserId": 1089963280,
            "sizeBytes": 142783,
            "uploadTimeMillis": 199,
            "md5Hash": "B6C962A9288F132762051A6A33708B90",
            "datetimeUploaded": 1731613990000,
            "scanState": "SAFE",
            "sha256HashValue": "5E3EF0EF4CFAD65A1831D866DEEBD932C5A0AA3484A558FD0D1CA3EB852AE1BF"
        },
        "datetimeCreated": 1731611168000,
        "revisions": [],
        "existing": false
    }
]
```

## Get File Metadata by ID

Given a known file ID, this endpoint allows you to list the metadata for that specific file.

**Method:** `GET`  
**Endpoint:** `/api/data/v1/data-files/{dataFileId}/details?expand={expand}`

#### Code Example

```js
async function getFileDetails(dataFileId, expand = null) {
  let url = `/api/data/v1/data-files/${dataFileId}/details`;
  if (expand !== null) {
    url += `?expand=${expand.join()}`;
  }
  const response = await fetch(url);
  return await response.json();
}
```

#### Path Parameters

| Property Name | Type    | Required | Description        |
| ------------- | ------- | -------- | ------------------ |
| dataFileId    | Integer | Required | The id of the file |

#### Query Parameters

| Property Name | Type         | Required | Description                                                                                                                    |
| ------------- | ------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------ |
| expand        | String Array | Optional | An array of string properties specifying the additional details you want to retrieve (either `revisions`, `metadata`, or both) |

#### Response

Returns the file details object.

```json
HTTP/1.1 200 OK
Content-Type: application/json

{
    "dataFileId": 90361,
    "name": "Sample",
    "responsibleUserId": 1249569521,
    "datetimeCreated": 1731613890000,
    "revisions": [],
    "existing": false
}
```

## Get Revision Metadata by ID

Given a known file revision ID, this endpoint allows you to list the metadata for that specific revision.

**Method:** `GET`  
**Endpoint:** `/api/data/v1/data-files/{dataFileId}/revisions/{revisionId}/details?expand={expand}`

#### Code Example

```js
async function getFileDetails(dataFileId, revisionId, expand = null) {
  let url = `/api/data/v1/data-files/${dataFileId}/revisions/${revisionId}/details`;
  if (expand !== null) {
    url += `?expand=${expand.join()}`;
  }
  const response = await fetch(url);
  return await response.json();
}
```

#### Path Parameters

| Property Name | Type    | Required | Description                 |
| ------------- | ------- | -------- | --------------------------- |
| dataFileId    | Integer | Required | The id of the file          |
| revisionId    | Integer | Required | The id of the file revision |

#### Query Parameters

| Property Name | Type         | Required | Description                                                                                                                    |
| ------------- | ------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------ |
| expand        | String Array | Optional | An array of string properties specifying the additional details you want to retrieve (either `revisions`, `metadata`, or both) |

#### Response

Returns the file revision details object.

```json
HTTP/1.1 200 OK
Content-Type: application/json

{
    "dataFileRevisionId": 92251,
    "dataFileId": 90356,
    "contentType": "image/jpeg",
    "uploadUserId": 1249569521,
    "sizeBytes": 182457,
    "uploadTimeMillis": 216,
    "md5Hash": "CB3BEFA1DC2A5840E5DD61E81ACA1472",
    "datetimeUploaded": 1731620674000,
    "scanState": "SAFE",
    "sha256HashValue": "0E807933F5F0CD4F082784F243F78B1C56C16EF86C427796D52C64C2CFE4EDA9"
}
```

## Get All File Revisions by ID

Given a known file ID, this endpoint fetches the existing revisions of the file.

**Method:** `GET`  
**Endpoint:** `/api/data/v1/data-files/${dataFileId}/revisions/details`

#### Code Example

```js
async function getFileRevisions(dataFileId, expand) {
  let url = `/api/data/v1/data-files/${dataFileId}/revisions/details`;
  if (expand !== null) {
    url += `?expand=${expand.join()}`;
  }
  const response = await fetch(url);
  return await response.json();
}
```

#### Path Parameters

| Property Name | Type    | Required | Description        |
| ------------- | ------- | -------- | ------------------ |
| dataFileId    | Integer | Required | The id of the file |

#### Query Parameters

| Property Name | Type         | Required | Description                                                                                                                    |
| ------------- | ------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------ |
| expand        | String Array | Optional | An array of string properties specifying the additional details you want to retrieve (either `revisions`, `metadata`, or both) |

#### Response

Returns a list of all revisions of the file.

```json
HTTP/1.1 200 OK
Content-Type: application/json

[
    {
        "dataFileRevisionId": 92239,
        "dataFileId": 90356,
        "contentType": "image/jpeg",
        "uploadUserId": 1249569521,
        "sizeBytes": 182457,
        "uploadTimeMillis": 297,
        "md5Hash": "CB3BEFA1DC2A5840E5DD61E81ACA1472",
        "datetimeUploaded": 1731611168000,
        "scanState": "SAFE",
        "sha256HashValue": "0E807933F5F0CD4F082784F243F78B1C56C16EF86C427796D52C64C2CFE4EDA9"
    },
    ...
]
```

## Download a File

This endpoint fetches the file contents of a previously uploaded file, which can then be downloaded to the user's machine. You can optionally include a revisionId as a path parameter to fetch a specific revision of the file.

**Method:** `GET`  
**Endpoint:** `/api/data/v1/data-files/{fileId}/revision/{revisionId}?filename={fileName}`

#### Code Example

```js
async function downloadFile(dataFileId, revisionId = null, fileName = null) {
  let url = `/api/data/v1/data-files/${dataFileId}${
    revisionId !== null ? `/revision/${revisionId}` : ''
  }`;
  if (fileName !== null) {
    url += `?fileName=${fileName}`;
  }
  const response = await fetch(url);
  const { revisionId } = await response.json();
}
```

#### Path Parameters

| Property Name | Type    | Required | Description                                                                 |
| ------------- | ------- | -------- | --------------------------------------------------------------------------- |
| fileId        | Integer | Required | The id of the file you wish to download                                     |
| revisionId    | Integer | optional | The id of the version you wish to download (remove `/revision` if not used) |

#### Query Parameters

| Property Name | Type   | Required | Description                        |
| ------------- | ------ | -------- | ---------------------------------- |
| fileName      | String | Optional | The name you want to give the file |

#### Response

Returns the File to be downloaded.

```text
HTTP/1.1 200 OK
Content-Type: {mime-type of the file}
```

### Copy/Move a File

This endpoint allows you to copy the current revision of a file to another target file. This essentially replaces the target file and leaves the source file intact.

**Method:** `POST`  
**Endpoint:** `/api/data/v1/data-files/copy/{sourceDataFileId}/revisions/current/{targetDataFileId}`

#### Code Example

```js
async function copyFile(sourceDataFileId, targetDataFileId) {
  const url = `/api/data/v1/data-files/copy/${sourceDataFileId}/revisions/current/${targetDataFileId}`;
  const response = await fetch(url);
  const { revisionId } = await response.json();
}
```

#### Path Parameters

| Property Name    | Type    | Required | Description                         |
| ---------------- | ------- | -------- | ----------------------------------- |
| sourceDataFileId | Integer | Required | The file id to move (source)        |
| targetDataFileId | Integer | Required | The file id to be replaced (target) |

#### Response

Returns the current revision id for the target file.

```json
HTTP/1.1 200 OK
Content-Type: application/json

{
    "revisionId": 401
}
```

## Duplicate a File

This endpoint will create a new file object in Domo from an existing one.

**Method:** `POST`  
**Endpoint:** `/api/data/v1/data-files/{dataFileId}/duplicate`

#### Code Example

```js
async function duplicateFile(dataFileId) {
  const url = `/api/data/v1/data-files/${dataFileId}/duplicate`;
  const response = await fetch(url);
  return await response.json();
}
```

#### Path Parameters

| Property Name | Type    | Required | Description              |
| ------------- | ------- | -------- | ------------------------ |
| dataFileId    | Integer | Required | The file id to duplicate |

#### Response

Returns the file metadata for the newly created duplicate.

```json
HTTP/1.1 200 OK
Content-Type: application/json

{
    "dataFileId": 90370,
    "name": "Sample",
    "responsibleUserId": 1249569521,
    "currentRevision": {
        "dataFileRevisionId": 92257,
        "dataFileId": 90370,
        "contentType": "image/jpeg",
        "uploadUserId": 1249569521,
        "sizeBytes": 182457,
        "uploadTimeMillis": 290,
        "md5Hash": "CB3BEFA1DC2A5840E5DD61E81ACA1472",
        "datetimeUploaded": 1731622004000,
        "scanState": "SAFE",
        "sha256HashValue": "0E807933F5F0CD4F082784F243F78B1C56C16EF86C427796D52C64C2CFE4EDA9"
    },
    "datetimeCreated": 1731622002000,
    "revisions": [],
    "existing": false
}
```

## Delete a File

Permanently deletes a File from your instance by ID.

**Method:** `DELETE`  
**Endpoint:** `/api/data/v1/data-files/{dataFileId}`

#### Code Example

```js
async function deleteFile(dataFileId) {
  const url = `/api/data/v1/data-files/${dataFileId}`;
  const response = await fetch(url, {
    method: 'DELETE',
  });
  return await response.json();
}
```

#### Path Parameters

| Property Name | Type    | Required | Description                           |
| ------------- | ------- | -------- | ------------------------------------- |
| dataFileId    | Integer | Required | The id of the file you wish to delete |

#### Response

Returns the parameter of success or error based on the file id being valid.

```text
HTTP/1.1 200 OK
```

## Delete a File Revision

Deletes a specific revision of a file by ID.

**Method:** `DELETE`  
**Endpoint:** `/api/data/v1/data-files/{dataFileId}/revisions/{revisionId}`

#### Code Example

```js
async function deleteFileRevision(dataFileId, revisionId) {
  const url = `/api/data/v1/data-files/${dataFileId}/revisions/${revisionId}`;
  const response = await fetch(url, {
    method: 'DELETE',
  });
  return await response.json();
}
```

#### Path Parameters

| Property Name | Type    | Required | Description                               |
| ------------- | ------- | -------- | ----------------------------------------- |
| dataFileId    | Integer | Required | The id of the file                        |
| revisionId    | Integer | Required | The id of the revision you wish to delete |

#### Response

Returns the parameter of success or error based on the file Id being valid.

```text
HTTP/1.1 200 OK
```

## Get File Permissions

Retrieve existing file permissions for a specific file by ID

**Method:** `GET`  
**Endpoint:** `/domo/data-files/v1/{fileId}/permissions`

#### Code Example

```js
async function getFilePermissions(dataFileId) {
  const url = `/api/data/v1/data-files/${dataFileId}/permissions`;
  const response = await fetch(url);
  return await response.json();
}
```

#### Path Parameters

| Property Name | Type    | Required | Description                                               |
| ------------- | ------- | -------- | --------------------------------------------------------- |
| dataFileId    | Integer | Required | The id of the file you wish to get permission details for |

#### Response

```json
HTTP/1.1 200 OK
Content-Type: application/json
{
    "publicAccess": false,
    "entries": [
        {
            "entityType": "USER",
            "entityId": "1089963280",
            "grant": "READ_WRITE_DELETE_SHARE_ADMIN",
            "pass": "NONE"
        }
    ]
}
```

## Update file permissions

Updates permissions for a specified file. Useful if needing to provide or expand access to a restricted/non-public file

**Method:** `PUT`  
**Endpoint:** `/api/data/v1/data-files/{dataFileId}/permissions`

#### Code Example

```js
async function upadateFilePermissions(dataFileId, permissionData) {
  const url = `/api/data/v1/data-files/${dataFileId}/permissions`;
  const response = await fetch(url, permissionData);
  return await response.json();
}
```

#### Path Parameters

| Property Name | Type    | Required | Description                                                  |
| ------------- | ------- | -------- | ------------------------------------------------------------ |
| dataFileId    | Integer | Required | The id of the file you wish to update permission details for |

#### Request Body

The request body accepts a permissions object.

```json
{
  "publicAccess": true,
  "entries": [
    {
      "entityType": "USER",
      "entityId": "1089963280",
      "grant": "READ_WRITE_DELETE_SHARE_ADMIN",
      "pass": "NONE"
    }
  ]
}
```

#### Response

Returns the parameter of success or error based on a valid permission object for the given file Id.

```text
HTTP/1.1 200 OK
```
