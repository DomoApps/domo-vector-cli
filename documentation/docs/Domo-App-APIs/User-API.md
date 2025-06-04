---
stoplight-id: n7f7swo7h29wg
---

# User API

### All Users

---

Information for all users can be retrieved using the following endpoint:

```text
GET /domo/users/v1?includeDetails={true|false}&limit={int}&offset={int}
```

#### Details

- includeDetails: Include all user information
- limit: The number of user records to return
- offset: Get users starting with this offset in the list of users
- returns (includeDetails=false)

```json
[
 {
     "id": 1,
     "displayName": "User One",
     "avatarKey": "/domo/avatars/v1/avatars/dev/86/420BB31EE19FDDBA8096F19ACD4C4D.jpg",
     "role": "Admin"
 },
 {
     "id": 3,
     "displayName": "User Two",
     "avatarKey": "/domo/avatars/v1/avatars/dev/86/510BB31EE19FDDBA8046F18ACD3C5D.jpg",
     "role": "Privileged"
 },
...
]
```

- returns (includeDetails=true)

```json
[
 {
     "id": 1,
     "displayName": "User One",
     "avatarKey": "/domo/avatars/v1/avatars/dev/86/420BB31EE19FDDBA8096F19ACD4C4D.jpg",
     "role": "Admin",
     "detail": {
        "title": "",
        "email": "userone@domo.com",
        "phoneNumber": "",
        "employeeNumber": 1,
        "pending": false
    }
 },
 {
     "id": 2,
     "displayName": "User Two",
     "avatarKey": "/domo/avatars/v1/avatars/dev/86/510BB31EE19FDDBA8046F18ACD3C5D.jpg",
     "role": "Privileged",
     "detail": {
        "title": "",
        "email": "usertwo@domo.com",
        "phoneNumber": "",
        "employeeNumber": 2,
        "pending": false
    }
 },
...
]
```

### Single User

---

Information for a single user can be retrieved using the following endpoint:

```text
GET /domo/users/v1/:userId?includeDetails={true|false}
```

#### Details

- userId: The id (long) of the desired user. Note: The current user Id is supplied via by the domo.js library as part of the domo.env object
- includeDetails: Include all user information
- returns (includeDetails=false)

```json
{
  "id": 1,
  "displayName": "User One",
  "avatarKey": "/domo/avatars/v1/avatars/dev/86/420BB31EE19FDDBA8096F19ACD4C4D.jpg",
  "role": "Admin"
}
```

- returns (includeDetails=true)

```json
{
  "id": 1,
  "displayName": "User One",
  "avatarKey": "/domo/avatars/v1/avatars/dev/86/420BB31EE19FDDBA8096F19ACD4C4D.jpg",
  "role": "Admin",
  "detail": {
    "title": "",
    "email": "userone@domo.com",
    "phoneNumber": "",
    "employeeNumber": 1,
    "pending": false
  }
}
```

### User Avatar

---

User avatars are available at the avatars endpoint

```text
GET /domo/avatars/v2/{entityType}/{entityId}?size={size}&defaultForeground={color}&defaultBackground={color}&defaultText={text}
```

Valid sizes (pixels)

- 100: 100 X 100
- 300: 300 X 300

#### HTTP Request

```text
GET /domo/avatars/v2/USER/846578099?size=300&defaultForeground=fff&defaultBackground=000&defaultText=D
```

#### Code Example

```html
<img
  src="/domo/avatars/v2/USER/846578099?size=300&defaultForeground=fff&defaultBackground=000&defaultText=D"
  alt="User Avatar"
/>
```
