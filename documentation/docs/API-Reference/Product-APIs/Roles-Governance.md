# Roles Governance API

This API reference is useful if you are trying to manage Domo Roles from anywhere 'outside' of your Domo instance such as:

1. Jupyter scripts
1. Code Engine Functions
1. Custom Java/Node/Python scripts

## Create Role

### Overview

Create a Role based on an existing role's authorities

### Endpoint

**POST** `/api/authorization/v1/roles`

### Body Parameters

| Parameter     | Type    | Required | Description                                     |
| ------------- | ------- | -------- | ----------------------------------------------- |
| `name`        | String  | Yes      | The name that will be displayed for the role    |
| `description` | String  | Yes      | Description that will be displayed for the role |
| `fromRoleId`  | Integer | Yes      | The ID of the role to fetch                     |

### Example

```json
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/authorization/v1/roles",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": {
    "name": string,
    "description": string,
    "fromRoleId": number
  }
}
```

### Response

```json
  HTTP/1.1 200 OK
  Content-Type: application/json;charset=UTF-8
  {
    "id": 1234567,
    "name": "",
    "description": ""
  }
```

---

## Get Role By Id

### Overview

Fetch a single Role by role id

### Endpoint

**GET** `/api/authorization/v1/roles/{roleId}`

### Path Parameters

| Parameter | Type    | Required | Description                 |
| --------- | ------- | -------- | --------------------------- |
| `roleId`  | Integer | Yes      | The ID of the role to fetch |

### Example

```json
{
  "method": "GET",
  "url": "https://{instance}.domo.com/api/authorization/v1/roles/{roleId}",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  }
}
```

### Response

```json
  HTTP/1.1 200 OK
  Content-Type: application/json;charset=UTF-8
  {
    "id": 1,
    "name": "Admin",
    "description": "Full access to everything",
    "authorityCount": 94,
    "userCount": 358,
    "created": 1550093701000,
    "modified": 1550093701000
  }
```

---

## Get All Roles

### Overview

Fetch a all Roles in an instance

### Endpoint

**GET** `/api/authorization/v1/roles`

### Example

```json
{
  "method": "GET",
  "url": "https://{instance}.domo.com/api/authorization/v1/roles",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  }
}
```

### Response

```json
  HTTP/1.1 200 OK
  Content-Type: application/json;charset=UTF-8
  [
    {
      "id": 1,
      "name": "Admin",
      "description": "Full access to everything",
      "authorityCount": 94,
      "userCount": 358,
      "created": 1550093701000,
      "modified": 1550093701000
    },
    ...
  ]
```

---

## Update Role Authorities

### Overview

Updates the authorities or grants which a role is capable of utilizing

### Endpoint

**PATCH** `/api/authorization/v1/roles/{roleId}/authorities`

### Path Parameters

| Parameter | Type    | Required | Description                   |
| --------- | ------- | -------- | ----------------------------- |
| `roleId`  | Integer | Yes      | The ID of the role to updated |

### Body

The body for this query is a string array containing the complete list of authorities the role should have after the update

### Example

```json
{
  "method": "PATCH",
  "url": "https://{instance}.domo.com/api/authorization/v1/roles/{roleId}/authorities",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json",
    "body": ["dataset.manage", "dataset.export"]
  }
}
```

### Response

```json
  HTTP/1.1 200 OK
  Content-Type: application/json;charset=UTF-8
  {
    "status": "SUCCESS",
    "message": ""
  }
```

---

## Delete Role

### Overview

Delete a Role

### Endpoint

**DELETE** `/api/authorization/v1/roles/{roleId}`

### Path Parameters

| Parameter | Type    | Required | Description                   |
| --------- | ------- | -------- | ----------------------------- |
| `roleId`  | Integer | Yes      | The ID of the role to updated |

### Example

```json
{
  "method": "DELETE",
  "url": "https://{instance}.domo.com/api/authorization/v1/roles/{roleId}",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  }
}
```

### Response

```json
  HTTP/1.1 204 No Content
  1
```
