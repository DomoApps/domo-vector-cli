---
stoplight-id:
---

# Alerts API

Domo Alerts allow users to subscribe to various events and receive timely notifications as changes occur. Find out more about Alerts by reading [this article](https://domo-support.domo.com/s/article/360043430373?language=en_US). The Alerts API can be used to manage alerts in your Domo instance.

## Get alerts

Query alerts from your Domo instance.

**Method:** `GET`  
**Endpoint:** `/api/social/v4/alerts?all=true&limit=5`

#### Code Example

```js
async function getAlerts() {
  const url = `/api/social/v4/alerts`;
  const response = await fetch(url);
  return await response.json();
}
```

#### Query Parameters

| Property Name            | Type    | Required | Default                                                                                                       | Description                                                                             |
| ------------------------ | ------- | -------- | ------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| all                      | Boolean | Optional |                                                                                                               | Whether to fetch all alerts at once                                                     |
| cardId                   | Integer | Optional |                                                                                                               | A specific card id to fetch alerts for                                                  |
| currentUserSubscriptions | Boolean | Optional | false                                                                                                         | Whether to fetch the alerts subscribed to by the current user                           |
| dataSetId                | String  | Optional |                                                                                                               | A specific dataset id to fetch alerts for                                               |
| disabled                 | Boolean | Optional |                                                                                                               | Whether to fetch only disabled alerts                                                   |
| fields                   | String  | Optional | id, category, type, name, description, resourceType, resourceId, createdAt, createdBy, modifiedAt, modifiedBy | Which alert fields to include in the response (can be set to 'all' to fetch all fields) |
| limit                    | Integer | Optional | 100                                                                                                           | The query limit                                                                         |
| offset                   | Integer | Optional | 0                                                                                                             | The query offset (for pagination)                                                       |
| ownerId                  | Integer | Optional |                                                                                                               | A specific user id to fetch owned alerts for                                            |
| pageId                   | Integer | Optional |                                                                                                               | A specific page id to fetch alerts for                                                  |
| sort                     | String  | Optional | createdAt                                                                                                     | The field to sort by                                                                    |
| subscriberId             | Integer | Optional |                                                                                                               | A specific user id to fetch subscribed alerts for                                       |
| subscriptionTypes        | String  | Optional |                                                                                                               | A list of subscription types to filter the alerts by                                    |
| suggested                | Boolean | Optional |                                                                                                               | Whether to fetch only alerts that are suggested for you                                 |
| triggered                | String  | Optional |                                                                                                               | Whether to fetch only alerts that have been triggered                                   |

#### Response

Returns the alerts based on the included query params.

```json
HTTP/1.1 200 OK
Content-Type: application/json
{
  [
    {
        "id": 358,
        "name": "Any row has changes for column(s): 'embedURL, metric, src, filesAPINum, docId, userName, title'",
        "type": "ANY_ROW",
        "resourceType": "DATASET",
        "resourceId": "58b3775b-ab03-4f54-9052-a3c5f7cbf426",
        "createdAt": "2024-12-12 23:37:32",
        "createdBy": 1341393147,
        "modifiedAt": "2024-12-13 18:55:17",
        "modifiedBy": 1341393147,
        "category": "DATA"
    }, ...
  ]
}
```

## Get an alert

Gets an existing alert by id.

**Method:** `GET`  
**Endpoint:** `/api/social/v4/alerts/{alertId}`

#### Code Example

```js
async function getAlert(alertId) {
  const url = `/api/social/v4/alerts/${alertId}`;
  const response = await fetch(url);
  return await response.json();
}
```

#### Path Parameters

| Property Name | Type    | Description                         |
| ------------- | ------- | ----------------------------------- |
| alertId       | Integer | The id of the alert you want to get |

#### Query Parameters

| Property Name | Type   | Required | Description                                   |
| ------------- | ------ | -------- | --------------------------------------------- |
| fields        | String | Optional | Which alert fields to include in the response |

#### Response

Returns the alert.

```json
HTTP/1.1 200 OK
{
  "actions": [],
  "active": true,
  "category": "DATA",
  "configurations": [],
  "contextual": true,
  "createdAt": "2024-01-01 00:00:00",
  "createdBy": 123456789,
  "currentUserSubscribed": false,
  "enabled": true,
  "error": {},
  "filterGroups": [],
  "id": 123,
  "modifiedAt": "2024-01-01 00:00:00",
  "modifiedBy": 123456789,
  "name": "My Favorite Alert",
  "owner": 123456789,
  "resourceId": "58b3775b-ab03-4f54-9052-a3c5f7cbf426",
  "resourceName": "Test Dataset",
  "resourceType": "DATASET",
  "rule": "Any row has changes for column(s): 'test'",
  "subscriptions": [],
  "triggerFrequency": "Rarely",
  "triggered": false,
  "type": "ANY_ROW"
}
```

## Delete an alert

Deletes an existing alert by id.

**Method:** `DELETE`  
**Endpoint:** `/api/social/v4/alerts/{alertId}`

#### Code Example

```js
async function deleteAlert(alertId) {
  const url = `/api/social/v4/alerts/${alertId}`;
  const response = await fetch(url, {
    method: 'DELETE',
  });
  return await response.json();
}
```

#### Arguments

| Property Name | Type    | Required | Description                            |
| ------------- | ------- | -------- | -------------------------------------- |
| alertId       | Integer | Required | The id of the alert you want to delete |

#### Response

Returns the parameter of success or error based on the alert id being valid.

```text
HTTP/1.1 200 OK
```

## Subscribe user to an alert

This endpoint subscribes a Domo user to an existing alert.

**Method:** `POST`  
**Endpoint:** `/api/social/v4/alerts/{alertId}/subscriptions`

#### Code Example

```js
async function subscribeToAlert(alertId, userId) {
  const url = `/api/social/v4/alerts/${alertId}/subscriptions`;
  const response = await fetch(url, {
    body: JSON.stringify({ subscriberId: userId, type: 'USER' }),
  });
  return await response.json();
}
```

#### Arguments

| Property Name | Type    | Required | Description                                           |
| ------------- | ------- | -------- | ----------------------------------------------------- |
| alertId       | Integer | Required | The id of the alert you want to subscribe the user to |

#### Response

Returns the parameter of success or error based on the alert id being valid.

```text
HTTP/1.1 200 OK
```

## Unsubscribe user from an alert

This endpoint unsubscribes a Domo user from an existing alert.

**Method:** `POST`  
**Endpoint:** `/api/social/v4/alerts/{alertId}/subscriptions?subscriberId={subscriberId}&type={type}`

#### Code Example

```js
async function unsubscribeFromAlert(alertId, userId) {
  const url = `/api/social/v4/alerts/${alertId}/subscriptions?subscriberId=${userId}&type=USER`;
  const response = await fetch(url, {
    method: 'DELETE',
  });
  return await response.json();
}
```

#### Arguments

| Property Name | Type    | Required | Description                                           |
| ------------- | ------- | -------- | ----------------------------------------------------- |
| alertId       | Integer | Required | The id of the alert you want to subscribe the user to |

#### Query Parameters

| Property Name | Type    | Required | Description                                                       |
| ------------- | ------- | -------- | ----------------------------------------------------------------- |
| subscriberId  | Integer | Required | The id of the entity unsubscribing from the alert                 |
| type          | String  | Required | The entity type, can be USER, GROUP, BUZZ, DAILY, WEEKLY, or AUTO |

#### Response

Returns the parameter of success or error based on the alert id being valid.

```text
HTTP/1.1 200 OK
```

## Share an alert

This endpoint shares an existing alert with a Domo user.

**Method:** `POST`  
**Endpoint:** `/api/social/v4/alerts/{alertId}/share`

#### Code Example

```js
async function shareAlert(alertId, userId, message, email) {
  const url = `/api/social/v4/alerts/${alertId}/share`;
  const payload = {
    userMessage: message,
    alertSubscriptions: [{ subscriberId: userId, type: 'USER' }],
    sendEmail,
    metaData: {},
  };
  const response = await fetch(url, {
    body: JSON.stringify(payload),
  });
  return await response.json();
}
```

#### Arguments

| Property Name | Type    | Required | Description                                           |
| ------------- | ------- | -------- | ----------------------------------------------------- |
| alertId       | Integer | Required | The id of the alert you want to subscribe the user to |

#### Request Body

| Property Name      | Type     | Required | Description                                                                 |
| ------------------ | -------- | -------- | --------------------------------------------------------------------------- |
| userMessage        | String   | Required | The message you want to send to the person                                  |
| alertSubscriptions | Object[] | Required | The entities you want to share the alert with. See above for entity params. |
| sendEmail          | Boolean  |          | Whether or not to send an email to the person once the alert is shared      |
| metaData           | Object   |          |                                                                             |

```json
{
  "userMessage": "I think you'll find this alert useful",
  "alertSubscriptions": [{ "subscriberId": 12345, "type": "USER" }],
  "sendEmail": true,
  "metaData": {}
}
```

#### Response

Returns the parameter of success or error based on the alert id being valid.

```text
HTTP/1.1 200 OK
```
