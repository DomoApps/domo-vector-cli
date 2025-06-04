# App Studio API

## Admin Summary

**Method**: `POST`  
**Endpoint**: `/api/content/v1/dataapps/adminsummary`

**Query Parameters**:

- limit - (Integer) Limits how many apps will be returned
- skip - (Integer) Skips the first n results

**Example**:

```json
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/content/v1/dataapps/adminsummary",
  "headers": {
    "X-DOMO-Developer-Token": "{access_token}",
    "Content-Type": "application/json"
  },
  "body": {
    "includeOwnerClause": "true",
    "includeTitleClause": "true",
    "orderBy": "title",
    "titleSearchText": "example title"
  }
}
```

**Response**:  
Returns a list of app summaries that you have access to

```json
200:
{
    "dataAppAdminSummaries": [
        {
            "dataAppId": 123456789,
            "title": "App title",
            "locked": false,
            "viewCount": 1,
            "owners": [
                {
                    "id": 1234567890,
                    "type": "USER",
                    "displayName": "Pranit Gurav"
                }
            ],
            "lastUpdated": 1234567890
        },
        ...
    ]
}

```

---

## Get Data Apps

**Method**: `GET`  
**Endpoint**: `/api/content/v1/dataapps/`

**Example**:

```json
{
  "method": "GET",
  "url": "https://{instance}.domo.com/api/content/v1/dataapps/",
  "headers": {
    "X-DOMO-Developer-Token": "{access_token}",
    "Content-Type": "application/json"
  }
}
```

**Response**:  
Returns a list of all of the data apps associated with your user

```json
200:
[
    {
        "dataAppId": 123456789,
        "title": "Test App",
        "description": null,
        "iconDataFileId": 0,
        "navIconDataFileId": null,
        "landingViewId": 123456789,
        "enabled": true,
        "isVirtualized": false,
        "locked": false,
        "lastUpdated": 123456789,
        "owners": null,
        "isOwner": true,
        "isFavorite": false,
        "canEdit": true,
        "showNavigation": true,
        "showTitle": true,
        "showLogo": false,
        "navOrientation": "TOP",
        "views": [],
        "userAccess": null,
        "theme": {
            "name": "Saturated Brand",
            "chartColorPalette": {
                "id": "Brand-Blue",
                "type": "APP_STUDIO"
            },
            ...
        },
        "themeMetrics": null,
        "navigations": [],
        "persistSettings": null
    },
    ...
]

```

---

## Get Data Apps by ID

**Method**: `GET`  
**Endpoint**: `/api/content/v1/dataapps/{dataAppId}`  
**Path Parameters**:

- `dataAppId` - (Integer, Required) - The id of the data app you are requesting

**Query Parameters**:

- includeHiddenViews - (Boolean) - Determines whether to include any hidden views

**Example**:

```json
{
  "method": "GET",
  "url": "https://{instance}.domo.com/api/content/v1/dataapps/{dataAppId}",
  "headers": {
    "X-DOMO-Developer-Token": "{access_token}",
    "Content-Type": "application/json"
  }
}
```

**Response**:  
Returns the data app associated with the given id

```json
200:
"dataAppId": 123456789,
    "title": "App title",
    "description": null,
    "iconDataFileId": 0,
    "navIconDataFileId": null,
    "landingViewId": 123456789,
    "enabled": true,
    "isVirtualized": false,
    "locked": false,
    "lastUpdated": 123456789,
    "owners": [
        {
            "id": 123456789,
            "type": "USER",
            "displayName": "Michael Scott"
        }
    ],
    "isOwner": true,
    "isFavorite": false,
    "canEdit": true,
    "showNavigation": true,
    "showTitle": true,
    "showLogo": false,
    "navOrientation": "TOP",
    "views": [
        {
            "viewId": 123456789,
            "title": "App Page 1",
            "parentViewId": 0,
            "viewOrder": 1,
            "visible": true,
            "view": null,
            "layout": null,
            "children": []
        }
    ],
    "userAccess": {
        "users": [
            {
                "id": 123456789,
                "displayName": "Michael Scott",
                "avatarKey": null,
                "role": "Admin"
            }
        ],
        "totalCount": 1
    },
    "theme": {
        "name": "Clarion",
        "chartColorPalette": {
            "id": "Domo Default Palette",
            "type": "DOMO"
        },
        ...
    },
    "themeMetrics": [
        {
            "dataAppId": 123456789,
            "viewId": 123456789,
            "styleCount": {
                "ca2": 2
            },
            "overriddenStyles": []
        }
    ],
    "navigations": [
        {
            "dataAppId": 123456789,
            "entity": "HOME",
            "entityId": "home",
            "title": "Home",
            "description": "All Domo apps",
            "navOrder": 1,
            "visible": true,
            "interaction": null,
            "icon": {
                "value": "home",
                "size": "DEFAULT"
            },
            "iconPosition": "LEFT",
            "style": null
        },
        ...
    ],
    "persistSettings": {
        "dataAppId": 123456789,
        "persistFiltersEnabled": false,
        "persistInteractionsEnabled": false,
        "persistDateEnabled": false,
        "persistVariablesEnabled": false,
        "persistedColumns": []
    }

```

---

## Get Data Apps Access List

**Method**: `GET`  
**Endpoint**: `/api/content/v1/dataapps/{dataAppId}/access`  
**Path Parameters**:

- `dataAppId` - (Integer, Required) The id of the data app you are requesting

**Query Parameters**:

- `expandUsers` - (Boolean, Optional) Determines whether to return the full user object

**Example**:

```json
{
  "method": "GET",
  "url": "https://{instance}.domo.com/api/content/v1/dataapps/{dataAppId}/access",
  "headers": {
    "X-DOMO-Developer-Token": "{access_token}",
    "Content-Type": "application/json"
  }
}
```

**Response**:  
Returns a list of users with access to the given data app

```json
200:
{
    "users": [
        {
            "id": 123456789,
            "invitorUserId": 123456789,
            "displayName": "Jon Hamm",
            "userName": "jon.hamm@example.com",
            "emailAddress": "jon.hamm@example.com",
            "accepted": true,
            "userType": "USER",
            "modified": 123456789,
            "created": 123456789,
            "role": "Admin",
            "roleId": 1,
            "rights": 63,
            "anonymous": false,
            "systemUser": false,
            "pending": false,
            "active": true
        }
    ],
    "totalUserCount": 1
}

```

## Share Data Apps

**Method**: `POST`  
**Endpoint**: `/api/content/v1/dataapps/share`

**Path Parameters**:

- `sendEmail` - (Boolean, Optional) Determines whether to send an email to the recipients

**Example**:

```json
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/content/v1/dataapps/share",
  "headers": {
    "X-DOMO-Developer-Token": "{access_token}",
    "Content-Type": "application/json"
  },
  "body": {
    "dataAppIds": ["{{data_app_id}}"],
    "recipients": [
      {
        "type": "group",
        "id": "{{group_id}}"
      },
      {
        "type": "user",
        "id": "{{user_id}}"
      }
    ],
    "message": "I thought you might find this page interesting."
  }
}
```

**Response**:  
Returns a status indicating whether the share operation was successful

```json
200:
undefined

```
