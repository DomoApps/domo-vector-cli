# Activity Log

## Overview

The Activity Log API provides programmatic access to users’ actions in Domo. For example, programs can discover the most active users or show trending cards based on page views. The information provided through this API is same data as provided in the Activity Log in the Admin Settings page of Domo.

<img class="size-full wp-image-3271 aligncenter" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2018/01/08164723/ActivityLog1.png" alt=""  />

Note that the API currently supports lookups for activity by specified users.

### Use cases
---
Using the Activity Log API, your program can:
- Create a list of most active users in the instance
- Discover trends in your Domo instance, such the most popular cards of the week based on card views
- Surface suspicious activities, such as logins from unexpected locations or at unusual times
- Identify certain problems in your Domo instance, such as failed login attempts and user lockouts


## Quickstart

Accessing your Activity Log entry data is simple and can be done in just one request.

<strong>NOTE:</strong> In order to utilize this Quickstart you will need to obtain an [access token](../API-Reference/Embed-APIs/Embed-Token-API.yaml#quickstart).

### Retrieving Activity Log Entries
---
This code retrieves a list of Activity Log entries via the Audit API:

<!-- [Audit](https://developer.domo.com/docs/domo-apis/audit) -->


#### Sample Request

```HTTP
GET https://api.domo.com/v1/audit
Content-Type: application/json
Accept: application/json
Authorization: bearer <your-valid-oauth-access-token>
```
#### Returns

Returns a list of Activity Log entries. You can provide query parameters to narrow your results based on time and user id. To see an example of please look at the Activity Log API Reference.


#### Sample Response
```HTTP
HTTP/1.1 200 OK
Content-Type: application/json

    {
        "actionType": "VIEWED",
        "actorId": 0,
        "actorName": "",
        "additionalComment": "Leonard Euler viewed page Intro to Domo.",
        "browserDetails": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "device": "desktop",
        "eventText": "Viewed page",
        "ipAddress": "50.207.241.61",
        "objectId": "663909457",
        "objectName": "Intro to Domo",
        "objectType": "PAGE",
        "time": "2017-12-13 10:57:35 PM",
        "userId": "1619916076",
        "userName": "Leonard Euler",
        "userType": "USER"
    }
```