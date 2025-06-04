# Users API

This API reference is useful if you are trying to manage Domo Users from anywhere 'outside' of your Domo instance such as:

1. Jupyter scripts
1. Code Engine Functions
1. Custom Java/Node/Python scripts

## Create User

**Method**: `POST`  
**Endpoint**: `/api/identity/v1/users`

**Example**:

```json
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/identity/v1/users",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": {
    "displayName": string,
    "emailAddress": string,
    "roleId": number
  }
}
```

**Response**:

```json
  HTTP/1.1 200 OK
  Content-Type: application/json;charset=UTF-8
  {
    "attributes": [
      {
        "key": string,
        "values": number|string[]
      },
    ],
    "id": number,
    "displayName": string,
    "userName": string,
    "roleId": number,
    "emailAddress": string
  }
```

---

## Get User By Id

**Method**: `GET`  
**Endpoint**: `/api/identity/v1/users/{id}`  
**Path Parameters**:

- `id`- Id of the user requested.
  - Integer
  - Required

**Optional Query Parameters**:

- `parts`
  - Options
    - MINIMAL
    - SIMPLE
    - DETAILED
    - GROUPS
    - ROLE
  - Example
    - `/api/identity/v1/users/{id}?parts=DETAILED`

**Example**

```json
{
  "method": "GET",
  "url": "https://{instance}.domo.com/api/identity/v1/users/{id}",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  }
}
```

**Response**:

```json
  HTTP/1.1 200 OK
  Content-Type: application/json;charset=UTF-8
  {
    "users": [
      {
        "attributes": [
          {
            "key": string,
            "values": number|string[]
          },
        ],
        "id": number,
        "displayName": string,
        "userName": string,
        "roleId": number,
        "emailAddress": string
      }
    ]
  }
```

---

## Get All Users

**Method**: `GET`  
**Endpoint**: `/api/identity/v1/users`  
**Optional Query Parameters**:

- `parts`
  - Options
    - MINIMAL
    - SIMPLE
    - DETAILED
    - GROUPS
    - ROLE
  - Example
    - `/api/identity/v1/users?parts=DETAILED`

**Example**

```json
{
  "method": "GET",
  "url": "https://{instance}.domo.com/api/identity/v1/users",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  }
}
```

**Response**:

```json
  HTTP/1.1 200 OK
  Content-Type: application/json;charset=UTF-8
  {
    "users": [
      {
        "attributes": [
          {
            "key": string,
            "values": number|string[]
          },
        ],
        "id": number,
        "displayName": string,
        "userName": string,
        "roleId": number,
        "emailAddress": string
      }
    ]
  }
```

---

## Update User

**Method**: `PATCH`  
**Endpoint**: `/api/identity/v1/users/{id}`  
**Path Parameters**:

- `id` - Id of the user requested.
  - Integer
  - Required

**Example**:

```json
{
  "method": "PATCH",
  "url": "https://{instance}.domo.com/api/identity/v1/users/{id}",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json",
    "body": {
      "roleId": 5
    }
  }
}
```

**Response**:

```json
  HTTP/1.1 200 OK
  Content-Type: application/json;charset=UTF-8
  {
    "attributes": [
      {
        "key": string,
        "values": number|string[]
      },
    ],
    "id": number,
    "displayName": string,
    "userName": string,
    "roleId": number,
    "emailAddress": string
  }
```

---

## Delete User

**Method**: `DELETE`  
**Endpoint**: `/api/identity/v1/users/{id}`  
**Path Parameters**:

- `id` - Id of the user requested.
  - Integer
  - Required

**Example**:

```json
{
  "method": "DELETE",
  "url": "https://{instance}.domo.com/api/identity/v1/users/{id}",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json",
    "body": {
      "roleId": 5
    }
  }
}
```

**Response**:

```json
  HTTP/1.1 200 OK
  Content-Type: application/json;charset=UTF-8
  1
```

