# Scheduled Reports API

## List Report Schedules

**Method**: `GET`  
**Endpoint**: `/api/content/v1/reportschedules`

**Query Parameters**:

| Name        | Type    | Required | Default     | Description                   | Enum Values                   |
| ----------- | ------- | -------- | ----------- | ----------------------------- | ----------------------------- |
| filter      | string  | false    | "USER"      | Filter type for the schedules | -                             |
| title       | string  | false    | ""          | Filter by title               | -                             |
| limit       | integer | false    | 0           | Number of items to return     | -                             |
| skip        | integer | false    | 0           | Number of items to skip       | -                             |
| orderBy     | string  | false    | "startDate" | Field to sort by              | startDate, nextRunDate, title |
| isAscending | boolean | false    | false       | Sort in ascending order       | -                             |

**Example**:

```json http
{
  "method": "GET",
  "url": "https://{instance}.domo.com/api/content/v1/reportschedules?filter=USER&title=Sales&limit=10&skip=0&orderBy=startDate&isAscending=true",
  "headers": {
    "X-DOMO-Developer-Token": ""
  }
}
```

**Responses**:

`200 OK`

```json
[
  {
    "id": 123456,
    "reportViewId": 789012,
    "pageId": 345678,
    "title": "Monthly Sales Report",
    "viewName": "Sales Dashboard",
    "type": "RECURRING",
    "ownerId": 901234,
    "embedViewId": 567890,
    "owner": true,
    "cardCount": 5,
    "recipientCount": 10,
    "cardId": 234567,
    "schedule": {
      "frequency": "MONTHLY",
      "daysToRun": "1",
      "hourOfDay": 9,
      "minOfHour": 0,
      "timezone": "America/New_York",
      "enabled": true
    }
  }
]
```

`403 Forbidden`

`409 Conflict`

## Create Report Schedule

**Method**: `POST`  
**Endpoint**: `/api/content/v1/reportschedules`

**Request Body**: ReportScheduleInfo object

**Example**:

```json http
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/content/v1/reportschedules",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": {
    "title": "Weekly Performance Report",
    "pageId": 345678,
    "viewId": 789012,
    "schedule": {
      "frequency": "WEEKLY",
      "daysToRun": "MON",
      "hourOfDay": 8,
      "minOfHour": 0,
      "timezone": "America/New_York",
      "enabled": true,
      "additionalRecipients": [
        {
          "type": "EMAIL",
          "value": "user@example.com"
        }
      ]
    },
    "attachmentInclude": true
  }
}
```

**Responses**:

`200 OK`

```json
{
  "id": 123457,
  "reportViewId": 789012,
  "pageId": 345678,
  "title": "Weekly Performance Report",
  "schedule": {
    "frequency": "WEEKLY",
    "daysToRun": "MON",
    "hourOfDay": 8,
    "minOfHour": 0,
    "enabled": true,
    "nextRunDate": 1700481600000
  }
}
```

`403 Forbidden`

`409 Conflict`

## Delete Report Schedule by Page ID

**Method**: `DELETE`  
**Endpoint**: `/api/content/v1/reportschedules`

**Query Parameters**:

| Name   | Type    | Required | Default | Description                           |
| ------ | ------- | -------- | ------- | ------------------------------------- |
| pageId | integer | true     | -       | ID of the page to delete schedule for |

**Example**:

```json http
{
  "method": "DELETE",
  "url": "https://{instance}.domo.com/api/content/v1/reportschedules?pageId=345678",
  "headers": {
    "X-DOMO-Developer-Token": ""
  }
}
```

**Responses**:

`200 OK`

`403 Forbidden`

`409 Conflict`

## Get Report Schedule by ID

**Method**: `GET`  
**Endpoint**: `/api/content/v1/reportschedules/{scheduleId}`

**Path Parameters**:

| Name       | Type    | Required | Description                    |
| ---------- | ------- | -------- | ------------------------------ |
| scheduleId | integer | true     | ID of the schedule to retrieve |

**Example**:

```json http
{
  "method": "GET",
  "url": "https://{instance}.domo.com/api/content/v1/reportschedules/123456",
  "headers": {
    "X-DOMO-Developer-Token": ""
  }
}
```

**Responses**:

`200 OK`

```json
{
  "id": 123456,
  "reportViewId": 789012,
  "pageId": 345678,
  "title": "Monthly Sales Report",
  "schedule": {
    "frequency": "MONTHLY",
    "daysToRun": "1",
    "hourOfDay": 9,
    "minOfHour": 0,
    "timezone": "America/New_York",
    "enabled": true
  }
}
```

`403 Forbidden`

`409 Conflict`

## Update Report Schedule

**Method**: `PUT`  
**Endpoint**: `/api/content/v1/reportschedules/{scheduleId}`

**Path Parameters**:

| Name       | Type    | Required | Description                  |
| ---------- | ------- | -------- | ---------------------------- |
| scheduleId | integer | true     | ID of the schedule to update |

**Request Body**: ReportScheduleInfo object

**Example**:

```json http
{
  "method": "PUT",
  "url": "https://{instance}.domo.com/api/content/v1/reportschedules/123456",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": {
    "title": "Updated Monthly Sales Report",
    "schedule": {
      "frequency": "MONTHLY",
      "daysToRun": "15",
      "hourOfDay": 10,
      "minOfHour": 30,
      "timezone": "America/New_York",
      "enabled": true
    }
  }
}
```

**Responses**:

`200 OK`

```json
{
  "id": 123456,
  "title": "Updated Monthly Sales Report",
  "schedule": {
    "frequency": "MONTHLY",
    "daysToRun": "15",
    "hourOfDay": 10,
    "minOfHour": 30,
    "timezone": "America/New_York",
    "enabled": true,
    "nextRunDate": 1701864600000
  }
}
```

`403 Forbidden`

`409 Conflict`

## Delete Report Schedule

**Method**: `DELETE`  
**Endpoint**: `/api/content/v1/reportschedules/{scheduleId}`

**Path Parameters**:

| Name       | Type    | Required | Description                  |
| ---------- | ------- | -------- | ---------------------------- |
| scheduleId | integer | true     | ID of the schedule to delete |

**Example**:

```json http
{
  "method": "DELETE",
  "url": "https://{instance}.domo.com/api/content/v1/reportschedules/123456",
  "headers": {
    "X-DOMO-Developer-Token": ""
  }
}
```

**Responses**:

`200 OK`

`403 Forbidden`

`409 Conflict`

## Enable/Disable Report Schedule

**Method**: `PUT`  
**Endpoint**: `/api/content/v1/reportschedules/{scheduleId}/enabled`

**Path Parameters**:

| Name       | Type    | Required | Description        |
| ---------- | ------- | -------- | ------------------ |
| scheduleId | integer | true     | ID of the schedule |

**Request Body**: boolean

**Example**:

```json http
{
  "method": "PUT",
  "url": "https://{instance}.domo.com/api/content/v1/reportschedules/123456/enabled",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": true
}
```

**Responses**:

`200 OK`

`403 Forbidden`

`409 Conflict`

## Get Report History by Schedule ID

**Method**: `GET`  
**Endpoint**: `/api/content/v1/reportschedules/{scheduleId}/history`

**Path Parameters**:

| Name       | Type    | Required | Description        |
| ---------- | ------- | -------- | ------------------ |
| scheduleId | integer | true     | ID of the schedule |

**Query Parameters**:

| Name  | Type    | Required | Default | Description               |
| ----- | ------- | -------- | ------- | ------------------------- |
| limit | integer | false    | 100     | Number of items to return |
| skip  | integer | false    | 0       | Number of items to skip   |

**Example**:

```json http
{
  "method": "GET",
  "url": "https://{instance}.domo.com/api/content/v1/reportschedules/123456/history?limit=100&skip=0",
  "headers": {
    "X-DOMO-Developer-Token": ""
  }
}
```

**Responses**:

`200 OK`

```json
[
  {
    "id": 789012,
    "reportId": 123456,
    "reportTitle": "Monthly Sales Report",
    "reportSubject": "Sales Report for November 2024",
    "startTime": "2024-11-01T09:00:00Z",
    "endTime": "2024-11-01T09:05:00Z",
    "automated": true,
    "cardCount": 5,
    "attachmentCount": 2,
    "attachmentSize": 1024000,
    "emailSize": 1536000,
    "status": "success",
    "recipients": [
      {
        "userId": 901234,
        "displayName": "John Doe",
        "emailAddress": "john.doe@example.com"
      }
    ]
  }
]
```

`403 Forbidden`

`409 Conflict`

## Build and Email Report

**Method**: `POST`  
**Endpoint**: `/api/content/v1/reportschedules/{scheduleId}/notifications`

**Path Parameters**:

| Name       | Type    | Required | Description        |
| ---------- | ------- | -------- | ------------------ |
| scheduleId | integer | true     | ID of the schedule |

**Request Body**: Array of ReportRecipient objects

**Example**:

```json http
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/content/v1/reportschedules/123456/notifications",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": [
    {
      "userId": 901234,
      "displayName": "John Doe",
      "emailAddress": "john.doe@example.com"
    }
  ]
}
```

**Responses**:

`202 Accepted`

`403 Forbidden`

`409 Conflict`

## Queue Build and Email Report

**Method**: `POST`  
**Endpoint**: `/api/content/v1/reportschedules/{scheduleId}/notifications/queue`

**Path Parameters**:

| Name       | Type    | Required | Description        |
| ---------- | ------- | -------- | ------------------ |
| scheduleId | integer | true     | ID of the schedule |

**Request Body**: Array of ReportRecipient objects

**Example**:

```json http
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/content/v1/reportschedules/123456/notifications/queue",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": [
    {
      "userId": 901234,
      "displayName": "John Doe",
      "emailAddress": "john.doe@example.com"
    }
  ]
}
```

**Responses**:

`202 Accepted`

`403 Forbidden`

`409 Conflict`

## Queue Report Now

**Method**: `POST`  
**Endpoint**: `/api/content/v1/reportschedules/{scheduleId}/queue`

**Path Parameters**:

| Name       | Type    | Required | Description        |
| ---------- | ------- | -------- | ------------------ |
| scheduleId | integer | true     | ID of the schedule |

**Request Body**: Array of ReportScheduleRecipient objects

**Example**:

```json http
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/content/v1/reportschedules/123456/queue",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": [
    {
      "type": "EMAIL",
      "value": "john.doe@example.com"
    }
  ]
}
```

**Responses**:

`202 Accepted`

`403 Forbidden`

`409 Conflict`

## Resubscribe to Report

**Method**: `POST`  
**Endpoint**: `/api/content/v1/reportschedules/{scheduleId}/resubscribe`

**Path Parameters**:

| Name       | Type    | Required | Description        |
| ---------- | ------- | -------- | ------------------ |
| scheduleId | integer | true     | ID of the schedule |

**Query Parameters**:

| Name    | Type    | Required | Description |
| ------- | ------- | -------- | ----------- |
| userId  | integer | false    | User ID     |
| emailId | string  | false    | Email ID    |

**Example**:

```json http
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/content/v1/reportschedules/123456/resubscribe?userId=901234&emailId=john.doe@example.com",
  "headers": {
    "X-DOMO-Developer-Token": ""
  }
}
```

**Responses**:

`200 OK`

`403 Forbidden`

`409 Conflict`

## Send Report Now

**Method**: `POST`  
**Endpoint**: `/api/content/v1/reportschedules/{scheduleId}/sendnow`

**Path Parameters**:

| Name       | Type    | Required | Description        |
| ---------- | ------- | -------- | ------------------ |
| scheduleId | integer | true     | ID of the schedule |

**Request Body**: Array of ReportScheduleRecipient objects

**Example**:

```json http
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/content/v1/reportschedules/123456/sendnow",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": [
    {
      "type": "EMAIL",
      "value": "john.doe@example.com"
    }
  ]
}
```

**Responses**:

`202 Accepted`

`403 Forbidden`

`409 Conflict`

## Send Resubscribe Email

**Method**: `POST`  
**Endpoint**: `/api/content/v1/reportschedules/{scheduleId}/sendResubscribe`

**Path Parameters**:

| Name       | Type    | Required | Description        |
| ---------- | ------- | -------- | ------------------ |
| scheduleId | integer | true     | ID of the schedule |

**Request Body**: Array of ReportScheduleRecipient objects

**Example**:

```json http
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/content/v1/reportschedules/123456/sendResubscribe",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": [
    {
      "type": "EMAIL",
      "value": "john.doe@example.com"
    }
  ]
}
```

**Responses**:

`202 Accepted`

`403 Forbidden`

`409 Conflict`

## Unsubscribe from Report

**Method**: `POST`  
**Endpoint**: `/api/content/v1/reportschedules/{scheduleId}/unsubscribe`

**Path Parameters**:

| Name       | Type    | Required | Description        |
| ---------- | ------- | -------- | ------------------ |
| scheduleId | integer | true     | ID of the schedule |

**Example**:

```json http
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/content/v1/reportschedules/123456/unsubscribe",
  "headers": {
    "X-DOMO-Developer-Token": ""
  }
}
```

**Responses**:

`200 OK`

`403 Forbidden`

`409 Conflict`

## Delete Unsubscribed Recipient

**Method**: `DELETE`  
**Endpoint**: `/api/content/v1/reportschedules/{scheduleId}/unsubscribe/recipient`

**Path Parameters**:

| Name       | Type    | Required | Description        |
| ---------- | ------- | -------- | ------------------ |
| scheduleId | integer | true     | ID of the schedule |

**Query Parameters**:

| Name    | Type    | Required | Description |
| ------- | ------- | -------- | ----------- |
| userId  | integer | false    | User ID     |
| emailId | string  | false    | Email ID    |

**Example**:

```json http
{
  "method": "DELETE",
  "url": "https://{instance}.domo.com/api/content/v1/reportschedules/123456/unsubscribe/recipient?userId=901234&emailId=john.doe@example.com",
  "headers": {
    "X-DOMO-Developer-Token": ""
  }
}
```

**Responses**:

`200 OK`

`403 Forbidden`

`409 Conflict`

## Render Card for Email

**Method**: `POST`  
**Endpoint**: `/api/content/v1/reportschedules/card-email-data`

**Request Body**: Array of integers (card IDs)

**Example**:

```json http
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/content/v1/reportschedules/card-email-data",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": [123, 456, 789]
}
```

**Responses**:

`200 OK`

```json
{
  "additionalProperties": {
    "title": "Sample Card",
    "encodedImage": "base64string",
    "encodedImageId": "img123",
    "timeframeLabel": "Last 30 Days",
    "summaryNumberValue": "10,000",
    "summaryNumberLabel": "Total Sales",
    "htmlContent": "<div>Card content</div>",
    "cardType": "kpi",
    "cardLink": "https://instance.domo.com/cards/123",
    "pdpEnabled": true,
    "certified": true,
    "companyCertified": false
  }
}
```

`403 Forbidden`

`409 Conflict`

## Get Created Report History

**Method**: `GET`  
**Endpoint**: `/api/content/v1/reportschedules/created`

**Query Parameters**:

| Name        | Type    | Required | Default | Description                 |
| ----------- | ------- | -------- | ------- | --------------------------- |
| filter      | string  | false    | "USER"  | Filter type                 |
| days        | integer | false    | 10      | Number of days to look back |
| isAscending | boolean | false    | false   | Sort order                  |

**Example**:

```json http
{
  "method": "GET",
  "url": "https://{instance}.domo.com/api/content/v1/reportschedules/created?filter=USER&days=10&isAscending=false",
  "headers": {
    "X-DOMO-Developer-Token": ""
  }
}
```

**Responses**:

`200 OK`

```json
[
  {
    "reportId": 123456,
    "reportTitle": "New Report",
    "ownerId": 789,
    "created": "2024-11-14T10:00:00Z",
    "resourceType": "PAGE",
    "resourceId": 456,
    "resourceName": "Dashboard"
  }
]
```

`403 Forbidden`

`409 Conflict`

## Enable/Disable Scheduled Report Emails

**Method**: `PUT`  
**Endpoint**: `/api/content/v1/reportschedules/emails/enabled`

**Request Body**: boolean

**Example**:

```json http
{
  "method": "PUT",
  "url": "https://{instance}.domo.com/api/content/v1/reportschedules/emails/enabled",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": true
}
```

**Responses**:

`200 OK`

`403 Forbidden`

`409 Conflict`

## Get Extended Report History

**Method**: `GET`  
**Endpoint**: `/api/content/v1/reportschedules/extendedHistory`

**Query Parameters**:

| Name        | Type    | Required | Default     | Description                 | Enum Values                                                                                       |
| ----------- | ------- | -------- | ----------- | --------------------------- | ------------------------------------------------------------------------------------------------- |
| filter      | string  | false    | "USER"      | Filter type                 | -                                                                                                 |
| days        | integer | false    | 10          | Number of days to look back | -                                                                                                 |
| orderBy     | string  | false    | "startTime" | Field to sort by            | reportTitle, startTime, endTime, automated, cardCount, attachmentCount, attachmentSize, emailSize |
| isAscending | boolean | false    | false       | Sort order                  | -                                                                                                 |

**Example**:

```json http
{
  "method": "GET",
  "url": "https://{instance}.domo.com/api/content/v1/reportschedules/extendedHistory?filter=USER&days=10&orderBy=startTime&isAscending=false",
  "headers": {
    "X-DOMO-Developer-Token": ""
  }
}
```

**Responses**:

`200 OK`

```json
[
  {
    "id": 123456,
    "reportId": 789012,
    "reportTitle": "Extended Report",
    "reportSubject": "Extended Report Details",
    "startTime": "2024-11-14T10:00:00Z",
    "endTime": "2024-11-14T10:05:00Z",
    "automated": true,
    "cardCount": 5,
    "attachmentCount": 2,
    "attachmentSize": 1024000,
    "emailSize": 1536000,
    "status": "success",
    "ownerId": 901234,
    "recipientCount": 10,
    "resourceType": "PAGE",
    "resourceId": 345678,
    "resourceName": "Sales Dashboard"
  }
]
```

`403 Forbidden`

`409 Conflict`

## Rerun Failed Scheduled Reports

**Method**: `POST`  
**Endpoint**: `/api/content/v1/reportschedules/failures/rerun`

**Query Parameters**:

| Name  | Type    | Required | Description     |
| ----- | ------- | -------- | --------------- |
| start | integer | true     | Start timestamp |
| end   | integer | true     | End timestamp   |

**Example**:

```json http
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/content/v1/reportschedules/failures/rerun?start=1699977600000&end=1700064000000",
  "headers": {
    "X-DOMO-Developer-Token": ""
  }
}
```

**Responses**:

`200 OK`

`403 Forbidden`

`409 Conflict`

## Get Report History

**Method**: `GET`  
**Endpoint**: `/api/content/v1/reportschedules/history`

**Query Parameters**:

| Name                 | Type    | Required | Default     | Description                   | Enum Values                                                                                       |
| -------------------- | ------- | -------- | ----------- | ----------------------------- | ------------------------------------------------------------------------------------------------- |
| filter               | string  | false    | "USER"      | Filter type                   | -                                                                                                 |
| limit                | integer | false    | 100         | Number of items to return     | -                                                                                                 |
| skip                 | integer | false    | 0           | Number of items to skip       | -                                                                                                 |
| orderBy              | string  | false    | "startTime" | Field to sort by              | reportTitle, startTime, endTime, automated, cardCount, attachmentCount, attachmentSize, emailSize |
| isAscending          | boolean | false    | false       | Sort order                    | -                                                                                                 |
| includeRecipientInfo | boolean | false    | false       | Include recipient information | -                                                                                                 |

**Example**:

```json http
{
  "method": "GET",
  "url": "https://{instance}.domo.com/api/content/v1/reportschedules/history?filter=USER&limit=100&skip=0&orderBy=startTime&isAscending=false&includeRecipientInfo=true",
  "headers": {
    "X-DOMO-Developer-Token": ""
  }
}
```

**Responses**:

`200 OK`

```json
[
  {
    "id": 123456,
    "reportId": 789012,
    "reportTitle": "History Report",
    "startTime": "2024-11-14T10:00:00Z",
    "endTime": "2024-11-14T10:05:00Z",
    "automated": true,
    "cardCount": 5,
    "status": "success",
    "recipients": [
      {
        "userId": 901234,
        "displayName": "John Doe",
        "emailAddress": "john.doe@example.com"
      }
    ]
  }
]
```

`403 Forbidden`

`409 Conflict`

## Get Report History by ID

**Method**: `GET`  
**Endpoint**: `/api/content/v1/reportschedules/history/{id}`

**Path Parameters**:

| Name | Type    | Required | Description      |
| ---- | ------- | -------- | ---------------- |
| id   | integer | true     | History entry ID |

**Example**:

```json http
{
  "method": "GET",
  "url": "https://{instance}.domo.com/api/content/v1/reportschedules/history/123456",
  "headers": {
    "X-DOMO-Developer-Token": ""
  }
}
```

**Responses**:

`200 OK`

```json
{
  "id": 123456,
  "reportTitle": "Specific History Report",
  "startTime": "2024-11-14T10:00:00Z",
  "endTime": "2024-11-14T10:05:00Z",
  "status": "success"
}
```

`403 Forbidden`

`409 Conflict`

## Search Report History

**Method**: `POST`  
**Endpoint**: `/api/content/v1/reportschedules/history/search`

**Query Parameters**:

| Name        | Type    | Required | Default     | Description               | Enum Values                                                                                       |
| ----------- | ------- | -------- | ----------- | ------------------------- | ------------------------------------------------------------------------------------------------- |
| filter      | string  | false    | "USER"      | Filter type               | -                                                                                                 |
| limit       | integer | false    | 100         | Number of items to return | -                                                                                                 |
| skip        | integer | false    | 0           | Number of items to skip   | -                                                                                                 |
| orderBy     | string  | false    | "startTime" | Field to sort by          | reportTitle, startTime, endTime, automated, cardCount, attachmentCount, attachmentSize, emailSize |
| isAscending | boolean | false    | false       | Sort order                | -                                                                                                 |

**Request Body**: ReportLogSearchCriteria object

**Example**:

```json http
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/content/v1/reportschedules/history/search?filter=USER&limit=100&skip=0&orderBy=startTime&isAscending=false",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": {
    "includeTitleClause": true,
    "titleSearchText": "Sales",
    "includeStatusClause": true,
    "status": "success",
    "includeTypeClause": true,
    "isAutomated": true,
    "includeScheduleIdClause": false
  }
}
```

**Responses**:

`200 OK`

```json
[
  {
    "id": 123456,
    "reportTitle": "Sales Report",
    "startTime": "2024-11-14T10:00:00Z",
    "endTime": "2024-11-14T10:05:00Z",
    "automated": true,
    "status": "success"
  }
]
```

`403 Forbidden`

`409 Conflict`

## Get Misconfigured Reports

**Method**: `GET`  
**Endpoint**: `/api/content/v1/reportschedules/misconfigured`

**Query Parameters**:

| Name  | Type    | Required | Default | Description               |
| ----- | ------- | -------- | ------- | ------------------------- |
| limit | integer | false    | 100     | Number of items to return |
| skip  | integer | false    | 0       | Number of items to skip   |

**Example**:

```json http
{
  "method": "GET",
  "url": "https://{instance}.domo.com/api/content/v1/reportschedules/misconfigured?limit=100&skip=0",
  "headers": {
    "X-DOMO-Developer-Token": ""
  }
}
```

**Responses**:

`200 OK`

```json
[
  {
    "id": 123456,
    "title": "Misconfigured Report",
    "schedule": {
      "frequency": "MONTHLY",
      "enabled": false
    },
    "active": false
  }
]
```

`403 Forbidden`

`409 Conflict`

## Get Resources with Reports

**Method**: `GET`  
**Endpoint**: `/api/content/v1/reportschedules/resources`

**Query Parameters**:

| Name  | Type    | Required | Default | Description               |
| ----- | ------- | -------- | ------- | ------------------------- |
| limit | integer | false    | 100     | Number of items to return |
| skip  | integer | false    | 0       | Number of items to skip   |
| title | string  | false    | ""      | Filter by title           |

**Example**:

```json http
{
  "method": "GET",
  "url": "https://{instance}.domo.com/api/content/v1/reportschedules/resources?limit=100&skip=0&title=Sales",
  "headers": {
    "X-DOMO-Developer-Token": ""
  }
}
```

**Responses**:

`200 OK`

```json
[
  {
    "resourceId": 123456,
    "title": "Sales Dashboard",
    "type": "PAGE"
  }
]
```

`403 Forbidden`

`409 Conflict`

## Get Report Schedules by Resource ID

**Method**: `GET`  
**Endpoint**: `/api/content/v1/reportschedules/resources/{resourceType}/{resourceId}`

**Path Parameters**:

| Name         | Type    | Required | Description        | Enum Values              |
| ------------ | ------- | -------- | ------------------ | ------------------------ |
| resourceType | string  | true     | Type of resource   | OPEN, PAGE, CARD, REPORT |
| resourceId   | integer | true     | ID of the resource | -                        |

**Query Parameters**:

| Name    | Type    | Required | Default | Description        |
| ------- | ------- | -------- | ------- | ------------------ |
| showAll | boolean | false    | false   | Show all schedules |

**Example**:

```json http
{
  "method": "GET",
  "url": "https://{instance}.domo.com/api/content/v1/reportschedules/resources/PAGE/123456?showAll=true",
  "headers": {
    "X-DOMO-Developer-Token": ""
  }
}
```

**Responses**:

`200 OK`

```json
[
  {
    "id": 123456,
    "title": "Resource Report",
    "schedule": {
      "frequency": "WEEKLY",
      "enabled": true
    }
  }
]
```

`403 Forbidden`

`409 Conflict`

## Get Report Schedules Map

**Method**: `GET`  
**Endpoint**: `/api/content/v1/reportschedules/sortby`

**Query Parameters**:

| Name        | Type    | Required | Default     | Description               | Enum Values                   |
| ----------- | ------- | -------- | ----------- | ------------------------- | ----------------------------- |
| filter      | string  | false    | "USER"      | Filter type               | -                             |
| title       | string  | false    | ""          | Filter by title           | -                             |
| limit       | integer | false    | 0           | Number of items to return | -                             |
| skip        | integer | false    | 0           | Number of items to skip   | -                             |
| orderBy     | string  | false    | "startDate" | Field to sort by          | startDate, nextRunDate, title |
| isAscending | boolean | false    | false       | Sort order                | -                             |

**Example**:

```json http
{
  "method": "GET",
  "url": "https://{instance}.domo.com/api/content/v1/reportschedules/sortby?filter=USER&title=Sales&limit=10&skip=0&orderBy=startDate&isAscending=false",
  "headers": {
    "X-DOMO-Developer-Token": ""
  }
}
```

**Responses**:

`200 OK`

```json
[
  {
    "id": 123456,
    "title": "Sales Report",
    "schedule": {
      "frequency": "WEEKLY",
      "enabled": true
    }
  }
]
```

`403 Forbidden`

`409 Conflict`

## Get Report Schedule by View ID

**Method**: `GET`  
**Endpoint**: `/api/content/v1/reportschedules/views/{viewId}`

**Path Parameters**:

| Name   | Type    | Required | Description    |
| ------ | ------- | -------- | -------------- |
| viewId | integer | true     | ID of the view |

**Example**:

```json http
{
  "method": "GET",
  "url": "https://{instance}.domo.com/api/content/v1/reportschedules/views/123456",
  "headers": {
    "X-DOMO-Developer-Token": ""
  }
}
```

**Responses**:

`200 OK`

```json
{
  "id": 123456,
  "title": "View Report",
  "schedule": {
    "frequency": "WEEKLY",
    "enabled": true
  }
}
```

`403 Forbidden`

`409 Conflict`

## Send Report Now by View ID

**Method**: `POST`  
**Endpoint**: `/api/content/v1/reportschedules/views/{viewId}/sendNow`

**Path Parameters**:

| Name   | Type    | Required | Description    |
| ------ | ------- | -------- | -------------- |
| viewId | integer | true     | ID of the view |

**Query Parameters**:

| Name              | Type    | Required | Description         |
| ----------------- | ------- | -------- | ------------------- |
| attachmentInclude | boolean | false    | Include attachments |

**Request Body**: Array of ReportScheduleRecipient objects

**Example**:

```json http
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/content/v1/reportschedules/views/123456/sendNow?attachmentInclude=true",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": [
    {
      "type": "EMAIL",
      "value": "user@example.com"
    }
  ]
}
```

**Responses**:

`202 Accepted`

`403 Forbidden`

`409 Conflict`

## Send Report Now with Parameters by View ID

**Method**: `POST`  
**Endpoint**: `/api/content/v1/reportschedules/views/{viewId}/sendNowWithParams`

**Path Parameters**:

| Name   | Type    | Required | Description    |
| ------ | ------- | -------- | -------------- |
| viewId | integer | true     | ID of the view |

**Query Parameters**:

| Name              | Type    | Required | Description         |
| ----------------- | ------- | -------- | ------------------- |
| attachmentInclude | boolean | false    | Include attachments |

**Request Body**: ResourceSendNowInfo object

**Example**:

```json http
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/content/v1/reportschedules/views/123456/sendNowWithParams?attachmentInclude=true",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": {
    "recipients": [
      {
        "type": "EMAIL",
        "value": "user@example.com"
      }
    ],
    "alertActionId": 789012,
    "emailParams": {
      "param1": "value1"
    }
  }
}
```

**Responses**:

`202 Accepted`

`403 Forbidden`

`409 Conflict`
