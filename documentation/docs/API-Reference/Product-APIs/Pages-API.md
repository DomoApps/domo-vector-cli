# Pages API

## Create Subpage

**Method:** `POST`  
**Endpoint:** `/api/content/v1/pages`

### Request Parameters

| Property Name | Type   | Required | Description                        |
| --------------|--------|----------|------------------------------------|
| parentPageId  | String | yes      | ID of the parent page              |
| title         | String | yes      | Title of the subpage               |
| hasLayout     | Boolean| no, default is true | Whether the page should have a layout |

### Example

```json
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/content/v1/pages",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": {
    "parentPageId": "12345",
    "title": "New Subpage Title",
    "hasLayout": true
  }
}
```

### Response

**Success (200):** Page created successfully.  
**Forbidden (403):** Operation not permitted.  
**Conflict (409):** Conflict encountered (e.g., duplicate title).

```json
200:
{
  "pageId": 11111111,
  "parentPageId": 2222222,
  "ownerId": 123123123,
  "owners": [
    {
      "id": 123123123,
      "type": "USER",
      "displayName": null
    }
  ],
  "type": "page",
  "title": "Test Subpage",
  "pageName": "Test Subpage",
  "locked": false,
  "mobileEnabled": true,
  "sharedViewPage": true,
  "metadata": "{\"pageTitle\":\"Test Subpage\",\"title\":\"Test Subpage\",\"type\":\"page\"}",
  "virtualPage": false,
  "hasLayout": true
}
```

---

## Bulk Move Pages

**Method:** `PUT`  
**Endpoint:** `/api/content/v1/pages/bulk/move`

### Request Parameters

| Property Name  | Type              | Required | Description              |
|----------------|-------------------|----------|--------------------------|
| pageIds        | Array of Numbers | yes      | IDs of pages to move     |
| parentPageId   | Number            | yes      | ID of the new parent page|
| pagePermission | String            | yes      | Permission for the pages |

**Valid Options for `pagePermission`:**
- `"ORIGINAL"`

### Example

```json
{
  "method": "PUT",
  "url": "https://{instance}.domo.com/api/content/v1/pages/bulk/move",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": {
    "pageIds": [123, 456],
    "parentPageId": 789,
    "pagePermission": "ORIGINAL"
  }
}
```

### Response

**Success (200):** Pages moved successfully.  
**Forbidden (403):** Permission denied.  
**Conflict (409):** Conflict encountered (e.g., permission constraints).

---

## Revoke Page Access

**Method:** `DELETE`  
**Endpoint:** `/api/content/v1/share/page/{pageId}/user/{personId}`

### Path Parameters

| Property Name | Type   | Required | Description                        |
|---------------|--------|----------|------------------------------------|
| pageId        | Number | yes      | ID of the page                    |
| personId      | Number | yes      | ID of the user                    |

### Example

```json
{
  "method": "DELETE",
  "url": "https://{instance}.domo.com/api/content/v1/share/page/12345/user/67890",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  }
}
```

### Response

**Success (200):** Access revoked successfully.  
**Forbidden (403):** Operation not permitted.  
**Conflict (409):** Conflict encountered while attempting to revoke access.

