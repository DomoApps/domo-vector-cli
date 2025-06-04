# Group Documentation

## Fetch Group

### Overview
Retrieve details of a specific group by its ID.

### Endpoint
**GET** `/api/content/v2/groups/{group}`

### Path Parameters
| Parameter | Type   | Required | Description               |
|-----------|--------|----------|---------------------------|
| `group`   | String | Yes      | The ID of the group to fetch |

### Request Example
```http
GET https://{instance}.domo.com/api/content/v2/groups/{group}
Headers:
  X-DOMO-Developer-Token: <token>
  Content-Type: application/json
```

### Response Example
**Status Code**: 200
```json
{
  "id": 6789456782,
  "name": "Group Name",
  "type": "closed",
  "userIds": [
    123123123,
    342342344,
    555543423,
    432423423
  ],
  "creatorId": 4421231232,
  "memberCount": 4,
  "guid": "guid-goes-here",
  "description": "",
  "hidden": false,
  "default": false,
  "active": true
}
```

---

## Fetch User Details

### Overview
Fetch detailed information for a specific user by their ID.

### Endpoint
**GET** `/api/identity/v1/users/{userId}`

### Path Parameters
| Parameter | Type   | Required | Description        |
|-----------|--------|----------|--------------------|
| `userId`  | String | Yes      | The ID of the user |

### Query Parameters
| Parameter | Type   | Required | Description               |
|-----------|--------|----------|---------------------------|
| `parts`   | String | No       | Specifies the detail level, e.g., `detailed` |

### Request Example
```http
GET https://{instance}.domo.com/api/identity/v1/users/{userId}?parts=detailed
Headers:
  X-DOMO-Developer-Token: <token>
  Content-Type: application/json
```

### Response Example
**Status Code**: 200
```json
[
  {
    "name": "Domo User",
    "id": 3817263817,
    "location": "",
    "manager": "",
    "phoneNumber": "+phone number",
    "title": "Software Engineer"
  }
]
```

---

## Create a Group

### Overview
Create a new group with the specified details.

### Endpoint
**POST** `/api/content/v2/groups`

### Body Parameters
| Parameter     | Type   | Required | Description                       |
|---------------|--------|----------|-----------------------------------|
| `name`        | String | Yes      | Name of the group                 |
| `description` | String | No       | Description of the group          |
| `type`        | String | Yes      | Group type: `closed`, `open`, or `dynamic` |

### Request Example
```http
POST https://{instance}.domo.com/api/content/v2/groups
Headers:
  X-DOMO-Developer-Token: <token>
  Content-Type: application/json
body:
{
  "name": "New Group",
  "description": "This is a new group",
  "type": "closed"
}
```

### Response Example
**Status Code**: 200
```json
{
  "id": "123123123"
}
```

---

## Add People to a Group

### Overview
Add a user to a specific group.

### Endpoint
**PUT** `/api/content/v2/groups/{group}/user/{userId}`

### Path Parameters
| Parameter | Type   | Required | Description                            |
|-----------|--------|----------|----------------------------------------|
| `group`   | String | Yes      | The ID of the group                   |
| `userId`  | String | Yes      | The ID of the user to add to the group |

### Request Example
```http
PUT https://{instance}.domo.com/api/content/v2/groups/{group}/user/{userId}
Headers:
  X-DOMO-Developer-Token: <token>
  Content-Type: application/json
```

### Response Example
**Status Code**: 200
```json
true
```

---

## Remove a Person from a Group

### Overview
Remove a user from a specific group.

### Endpoint
**DELETE** `/api/content/v2/groups/{group}/removeuser/{userId}`

### Path Parameters
| Parameter | Type   | Required | Description                            |
|-----------|--------|----------|----------------------------------------|
| `group`   | String | Yes      | The ID of the group                   |
| `userId`  | String | Yes      | The ID of the user to remove           |

### Request Example
```http
DELETE https://{instance}.domo.com/api/content/v2/groups/{group}/removeuser/{userId}
Headers:
  X-DOMO-Developer-Token: <token>
  Content-Type: application/json
```

### Response Example
**Status Code**: 200
```json
true
```

---

## Remove Multiple People from a Group

### Overview
Remove multiple users from a specific group.

### Endpoint
**PUT** `/api/content/v2/groups/access`

### Body Parameters
| Parameter         | Type    | Required | Description                                    |
|-------------------|---------|----------|------------------------------------------------|
| `groupId`         | String  | Yes      | The ID of the group                          |
| `removeMembers`   | Array   | Yes      | List of members to remove, with `type` and `id` |

### Request Example
```http
PUT https://{instance}.domo.com/api/content/v2/groups/access
Headers:
  X-DOMO-Developer-Token: <token>
  Content-Type: application/json
body:
[
  {
    "groupId": "1231231232",
    "removeMembers": [
      {
        "type": "USER",
        "id": "112321221"
      }
    ]
  }
]
```

### Response Example
**Status Code**: 200
```json
true
```

