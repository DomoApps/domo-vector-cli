---
stoplight-id: 3c6pp23q82y90
---

# Programmatically Create a Client

Creating a Client ID and Secret using developer.domo.com in the browser is outlined in the [API Overview](../../../docs/API-Reference/Domo-APIs/API-Authentication.yaml).

For scenarios that require programmatic creation of Clients, the following guide may be used.

### Obtain a Customer Instance Session Identifier

Using the [authenticate](Instance-Authentication.json/paths/~1api~1content~1v2~1authentication/post) customer instance API, you are able to obtain a session identifier using multiple methods of authentication based upon the instance's sign on options.

#### Password Authentication

Customer instances with direct sign on are able to use the `password` method to create a session token.

Call the [authenticate](Instance-Authentication.json/paths/~1api~1content~1v2~1authentication/post) endpoint using `"method": "password"` and including the appropriate `"emailAddress"` and `"password"`

```bash
curl --request POST \
  --header "Origin: https://${customer}.domo.com" \
  --header "Content-Type: application/json" \
  --data '{"method": "password", "emailAddress": "user@customer.example", "password": "hunter2"}' \
  https://${customer}.domo.com/api/content/v2/authentication'

```

#### Cookie Authentication (SSO)

For instances that don't use direct sign on cookie authentication may be used with the `exptoken` method.

To obtain the necessary cookie value, you may extract it using browser Developer Tools after logging into your instance.
Locate and copy the `_dsidv1` cookie value

![image.png](../../../assets/images/image-98.png)

Call the [authenticate](Instance-Authentication.json/paths/~1api~1content~1v2~1authentication/post) endpoint with the matching `_dsidv1` cookie set and `"method": "exptoken"` in the request body.

```bash
curl --request POST \
  --header "Origin: https://${customer}.domo.com" \
  --header "Content-Type: application/json" \
  --header "Cookie: _dsidv1=${dsidFromBrowser}" \
  --data '{"method": "exptoken"}' \
  https://${customer}.domo.com/api/content/v2/authentication'
```

#### Session Identifier

Both methods will respond with a `sessionToken` needed for the next steps.

```json
{
	"userId": 123456,
	"success": true,
	"sessionToken": "eyJhbGwiOiAiYmFzZSIsICJiZWxvbmciOiAidXMifQo="
}
```

## Create a Client

A Client for `api.domo.com` can be created using the `sessionToken`.

Call the [clients](Client-API.yaml/paths/~1clients/post) endpoint using `sessionToken` as the value of `X-DOMO-Authentication`

```bash
curl --request POST \
  --header "X-DOMO-Authentication: ${sessionToken}" \
  --header "X-DOMO-CustomerDomain: ${customer}.domo.com" \
  --header 'Content-Type: application/json' \
  --data '{"name": "Automation Client", "scope": ["data"]}' \
  https://api.domo.com/clients
```

In response, a client will have been created. Use the `client_id` and `client_secret` for any future Platform APIs

```json
{
	"name": "Automation Client",
	"scope": ["data"],
	"user": 123456,
	"client_id": "4e21cf44-b616-48c5-bba7-0ab9c0d8ca77",
	"client_secret": "abc123def456",
	"authorized_grant_types": ["client_credentials"]
}
```
