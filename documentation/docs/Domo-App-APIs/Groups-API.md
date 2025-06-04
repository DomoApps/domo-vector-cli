---
stoplight-id: 2hwa98wx7kdm4
---

# Groups API

The Groups API is a Read Only set of endpoints available to retrieve information about the various groups that belong to the instance in which a Custom App is published. This enables your application to take advantage of knowing the groups that individual users could potentially belong to and alter their user experience accordingly.

### All Groups
---
Retrieve a list of details for all groups of an instance.

#### Code Example

```text
domo.get(`/domo/groups/v1`)
   .then(data => console.log(data))
```

#### HTTP Request

```text
GET /domo/groups/v1
Content-Type: application/json
Accept: application/json
```

#### HTTP Response

```json
HTTP/1.1 200 OK
[
    {
        "id": 1051417,
        "name": "New Users",
        "type": "adHoc",
        "userIds": [],
        "created": "2018-10-03T23:26:04.000+0000",
        "memberCount": 15210,
        "active": true,
        "default": true
    },
    {
        "id": 1085275,
        "name": "Power Users",
        "type": "directory",
        "userIds": [],
        "created": "2018-11-15T15:21:27.000+0000",
        "memberCount": 2265,
        "active": true,
        "default": false
    }
]
```

### Group by Id
---
Retrieve the details for an individual group given its Id.

#### Code Example

```text
domo.get(`/domo/groups/v1/1051417`)
    .then(data => console.log(data))
```

#### HTTP Request

```text
GET /domo/groups/v1/{groupId}
Content-Type: application/json
Accept: application/json
```

#### Arguments

| Property Name| Type | Required | Description |
| --- | --- | --- | --- |
| groupId | Long | Required | The ID of the desired group |

#### HTTP Response

```json
HTTP/1.1 200 OK
{
    "id": 1051417,
    "name": "New Users",
    "type": "adHoc",
    "userIds": [],
    "created": "2018-10-03T23:26:04.000+0000",
    "memberCount": 15210,
    "active": true,
    "default": true
}
```

### Group by Name
---
Retrieve the details for an individual group given its name.

#### Code Example

```text
domo.get(`/domo/groups/v1/name?groupName=New Users`)
    .then(data => console.log(data))
```

#### HTTP Request

```text
GET /domo/groups/v1/name?groupName={groupName}
Content-Type: application/json
Accept: application/json
```

#### Arguments

| Property Name| Type | Required | Description |
| --- | --- | --- | --- |
| groupName | String | Required | The name of the desired group |

#### HTTP Response

```json
HTTP/1.1 200 OK
{
    "id": 1051417,
    "name": "New Users",
    "type": "adHoc",
    "userIds": [],
    "created": "2018-10-03T23:26:04.000+0000",
    "memberCount": 15210,
    "active": true,
    "default": true
}
```

### Groups by User
---
Retrieve the details for an all groups that an individual user belongs to, given a user Id. You can obtain the user Id of the current user using the `domo` object (provided via the `domo.js` javascript file that is included with all apps initialized by the Domo Apps CLI) as demonstrated in the code example below.

#### Code Example

```text
domo.get(`/domo/groups/v1/user/${domo.env.userId}`)
    .then(data => console.log(data))
```

#### HTTP Request

```text
GET /domo/groups/v1/user/{userId}
Content-Type: application/json
Accept: application/json
```

#### Arguments

| Property Name| Type | Required | Description |
| --- | --- | --- | --- |
| userId | Long | Required | The id of the desired user |

#### HTTP Response

```json
HTTP/1.1 200 OK
[
    {
        "id": 1051417,
        "name": "New Users",
        "type": "adHoc",
        "userIds": [],
        "created": "2018-10-03T23:26:04.000+0000",
        "memberCount": 15210,
        "active": true,
        "default": true
    },
    {
        "id": 1085275,
        "name": "Power Users",
        "type": "directory",
        "userIds": [],
        "created": "2018-11-15T15:21:27.000+0000",
        "memberCount": 2265,
        "active": true,
        "default": false
    }
]
```
