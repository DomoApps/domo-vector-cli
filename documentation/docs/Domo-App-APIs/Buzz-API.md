---
stoplight-id: 0rss4j81nqj1a
---

# Buzz API

The Buzz Integration API, allows configuring two-way communication between Buzz and a service outside of Domo.

A Buzz integration is a service hosted outside of Domo’s infrastructure that can receive events from Buzz, and can post messages to Buzz. To use this feature, invoke this API to register an integration, then create one or more event subscriptions for the integration. When a corresponding event occur, Buzz will POST an HTTP request using the configured URL and headers.

Each integration is configured to be active on one or more channels, based on the `scope` field described below. An integration is also configured with headers to be included with each HTTP POST that Buzz sends to the integration, for authentication or other purposes.

Event subscriptions specify the type of event, along with a URL that will be used to POST the event. The URL must start with `https://`, no other protocol is supported.

Events are sent as a JSON payload. The payload includes details about the event as documented below, including a `callback` field with a URL and headers that can be used to post a message back to the originating Buzz channel. Such messages will appear with the name of the integration.

### Create Integration

#### Definition

```
POST https://api.domo.com/v1/buzz/integrations
```

#### Create Integration Object


Property Name | Type | Description
---------|----------|---------
 name | String | The name of the integration, shown whenever it posts a message to Buzz
description	| String |	Description of the integration
scope	| String	|`PUBLIC_CHANNELS`	All public channels, `OWNER_ACCESS`	All channels accessible by the user that creates the integration, `CHANNEL_LIST`	All channels specified in the channelIds list
channelIds |	List of Strings |	Must be provided if and only if scope is CHANNEL_LIST
headers |	List|	Every event that Buzz sends to the integration will be sent as an HTTP POST with these headers. Headers may be used for authentication or other purposes.


#### Sample request

```json
POST https://api.domo.com/v1/buzz/integrations
Content-Type: application/json
Accept: application/json
Authorization: bearer <your-valid-oauth-access-token>

{
  "name": "Sentiment Analyzer",
  "description": "Natural language processor that determines user sentiment",
  "scope": "CHANNEL_LIST",
  "channelIds": [
    "4af927ea-ec3b-4a56-9acc-6a3d3d36a475",
    "73f4bf8b-445a-438b-be83-6e640e32c607"
  ],
  "headers": [
    {
      "name": "x-my-api-secret",
      "value": "b5d25c5b-e38f-495e-9e16-40973be50c3a"
    }
  ]
}
```

#### Sample response

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8

{
  "id": "ccb48dd0-bd80-4a99-a7ea-9b4f002bb373",
  "ownerId": 39485,
  "name": "Sentiment Analyzer",
  "description": "Natural language processor that determines user sentiment",
  "scope": "CHANNEL_LIST"
  "channelIds": [
    "4af927ea-ec3b-4a56-9acc-6a3d3d36a475",
    "73f4bf8b-445a-438b-be83-6e640e32c607"
  ],
  "headers": [
    {
      "name": "x-my-api-secret",
      "value": "b5d25c5b-e38f-495e-9e16-40973be50c3a"
    }
  ],
}
```

### Get integration

#### Definition

```
GET https://api.domo.com/v1/buzz/integrations/{INTEGRATION_ID}
```

#### Sample response

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8

{
  "id": "ccb48dd0-bd80-4a99-a7ea-9b4f002bb373",
  "ownerId": 39485,
  "name": "Sentiment Analyzer",
  "description": "Natural language processor that determines user sentiment",
  "scope": "CHANNEL_LIST"
  "channelIds": [
    "4af927ea-ec3b-4a56-9acc-6a3d3d36a475",
    "73f4bf8b-445a-438b-be83-6e640e32c607"
  ],
  "headers": [
    {
      "name": "x-my-api-secret",
      "value": "b5d25c5b-e38f-495e-9e16-40973be50c3a"
    }
  ],
}
```
### Get all Integrations

This endpoint returns all integrations that are active on any channel that the current user has access to.

#### Definition

```
GET https://api.domo.com/v1/buzz/integrations
```

#### Sample response

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8

{
  "integrations": [
    {
      "id": "ccb48dd0-bd80-4a99-a7ea-9b4f002bb373",
      "ownerId": 39485,
      "name": "Sentiment Analyzer",
      "description": "Natural language processor that determines user sentiment",
      "scope": "CHANNEL_LIST"
      "channelIds": [
        "4af927ea-ec3b-4a56-9acc-6a3d3d36a475",
        "73f4bf8b-445a-438b-be83-6e640e32c607"
      ],
      "headers": [
        {
          "name": "x-my-api-secret",
          "value": "b5d25c5b-e38f-495e-9e16-40973be50c3a"
        }
      ],
    },
    {
      "id": "0594c31b-0e6b-45ed-80c8-f6de7048d45d",
      "ownerId": 39485,
      "name": "Weather",
      "description": "Current and forecasted weather report",
      "scope": "PUBLIC_CHANNELS",
      "headers": [
        {
          "name": "x-weather-api-key",
          "value": "e745c28b-3468-4f3b-960b-6110d2feb9c7"
        }
      ],
    }
  ]
}
```

### Delete integration

Permanently deletes a Buzz integration.

<!-- theme: danger -->
> #### Warning
> This is destructive and cannot be reversed.

#### Definition

```
DELETE https://api.domo.com/v1/buzz/integrations/{INTEGRATION_ID}
```

#### Sample response

```
HTTP/1.1 204 No Content
```

### Subscribe to Buzz events

An event subscription enables a Buzz integration to receive events from Buzz. Event types include the following:

- `MESSAGE_POSTED`: A user posted a message
- `SLASH_COMMAND`: A user invoked a specific slash command
- `THREAD_CREATED`: A thread was created on the parent channel
- `USERS_JOINED_CHANNEL`: One or more users joined the channel
- `USERS_LEFT_CHANNEL`: One or more users left the channel


#### Definition
```
POST https://api.domo.com/v1/buzz/integrations/{INTEGRATION_ID}/subscriptions
```

#### Create Event Subscription Object

Property Name | Type | Description
---------|----------|---------
 eventType | String | One of: `MESSAGE_POSTED`, `SLASH_COMMAND`, `THREAD_CREATED`, `USERS_JOINED_CHANNEL`, `USERS_LEFT_CHANNEL`
 url | String | The integration will post to this URL when an event occurs
 slashCommand | String | Required if and only if eventType is `SLASH_COMMAND`



#### Sample request

```json
POST https://api.domo.com/v1/buzz/integrations/ccb48dd0-bd80-4a99-a7ea-9b4f002bb373
Content-Type: application/json
Accept: application/json
Authorization: bearer <your-valid-oauth-access-token>

{
  "eventType":"SLASH_COMMAND",
  "url":"http:my.domain.com/buzz-integration/close-deal",
  "slashCommand": "close"
}
```

#### Sample response

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8

{
  "id":"18019b09-428a-45ae-a9ff-5fc0730ac9bd"
  "eventType":"SLASH_COMMAND",
  "url":"http:my.domain.com/buzz-integration/close-deal",
  "slashCommand": "close"
}
```

### Get event subscriptions

#### Definition

```
GET https://api.domo.com/v1/buzz/integrations{INTEGRATION_ID}/subscriptions
```

#### Sample response

``` json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8

{
  "subscriptions": [
    {
      "id":"18019b09-428a-45ae-a9ff-5fc0730ac9bd"
      "eventType":"SLASH_COMMAND",
      "url":"http:my.domain.com/buzz-integration/close-deal",
      "slashCommand": "close"
    }
  ]
}
```

### Delete Subscription

Deletes an existing event subscription from a Buzz integration. The integration will no longer receive events for the given subscription.

<!-- theme: danger -->
> #### Warning
> This is destructive and cannot be reversed.

#### Definition

```
DELETE https://api.domo.com/v1/buzz/integrations/{INTEGRATION_ID}/subscriptions/{SUBSCRIPTION_ID}
```

#### Sample response
```
HTTP/1.1 204 No Content
```
### Sample event payloads

The following are examples of event payloads to be sent to Buzz integrations.

#### Fields

Each field in the event payload is a JSON object.


Name | Description 
---------|----------
 author | Included in events associated with a specific message, this object contains information about the author of the message.
 message | Also included in events associated with a specific message, this object contains information about the message itself.
 users | A list of objects representing users. Only included in USERS_JOINED_CHANNEL and USERS_LEFT_CHANNEL events.
event |	Details about the event itself.
owner |	The user that created the integration.
channel	| The channel in which the event occurred.
callback	| URL and headers that the integration may use to post a message back to Buzz. Expires one hour after the event occurred.


### Message posted

```json
{
  "author": {
    "id": 67392,
    "displayName": "Adam Craven",
    "email": "adam@acme.com"
  },
  "message": {
    "text": "Good morning"
  },
  "event": {
    "type": "MESSAGE_POSTED"
  },
  "owner": {
    "id": 39485,
    "displayName": "Jamis Maxwell",
    "email": "jamis@acme.com"
  },
  "organization": {
    "domain": "acme.domo.com"
  },
  "channel": {
    "id": "4af927ea-ec3b-4a56-9acc-6a3d3d36a475",
    "parentId": "4af927ea-ec3b-4a56-9acc-6a3d3d36a475",
    "title": "General"
  },
  "callback": {
    "url": "https://acme.domo.com/api/buzz/v1/bots/message/4af927ea-ec3b-4a56-9acc-6a3d3d36a475",
    "headers": {
      "x-buzz-bot-token": "691575144a28497b9247e471cba9bf8ead2e5a7a20ee4d04b13e1a317260d0fc"
    }
  }
}
```

### Slash command

```json
{
  "author": {
    "id": 67392,
    "displayName": "Adam Craven",
    "email": "adam@acme.com"
  },
  "message": {
    "text": "/close deal 73964"
  },
  "event": {
    "type": "SLASH_COMMAND"
  },
  "owner": {
    "id": 39485,
    "displayName": "Jamis Maxwell",
    "email": "jamis@acme.com"
  },
  "organization": {
    "domain": "acme.domo.com"
  },
  "channel": {
    "id": "4af927ea-ec3b-4a56-9acc-6a3d3d36a475",
    "parentId": "4af927ea-ec3b-4a56-9acc-6a3d3d36a475",
    "title": "General"
  },
  "callback": {
    "url": "https://acme.domo.com/api/buzz/v1/bots/message/4af927ea-ec3b-4a56-9acc-6a3d3d36a475",
    "headers": {
      "x-buzz-bot-token": "691575144a28497b9247e471cba9bf8ead2e5a7a20ee4d04b13e1a317260d0fc"
    }
  }
}
```

### Thread created

```json
{
  "thread": {
    "id": "6b740b3f-717d-466c-9639-e7ec25a66554",
    "parentId": "4af927ea-ec3b-4a56-9acc-6a3d3d36a475",
    "title": "This is the thread title"
  }
  "event": {
    "type": "THREAD_CREATED"
  },
  "owner": {
    "id": 39485,
    "displayName": "Jamis Maxwell",
    "email": "jamis@acme.com"
  },
  "organization": {
    "domain": "acme.domo.com"
  },
  "channel": {
    "id": "4af927ea-ec3b-4a56-9acc-6a3d3d36a475",
    "parentId": "4af927ea-ec3b-4a56-9acc-6a3d3d36a475",
    "title": "General"
  },
  "callback": {
    "url": "https://acme.domo.com/api/buzz/v1/bots/message/4af927ea-ec3b-4a56-9acc-6a3d3d36a475",
    "headers": {
      "x-buzz-bot-token": "691575144a28497b9247e471cba9bf8ead2e5a7a20ee4d04b13e1a317260d0fc"
    }
  }
}
```

### Users joined channel
```json
{
  "users": [
    {
      "displayName": "Adam Craven",
      "email": "adam@acme.com"
    }
  ],
  "event": {
    "type": "USERS_JOINED_CHANNEL"
  },
  "owner": {
    "id": 39485,
    "displayName": "Jamis Maxwell",
    "email": "jamis@acme.com"
  },
  "organization": {
    "domain": "acme.domo.com"
  },
  "channel": {
    "id": "4af927ea-ec3b-4a56-9acc-6a3d3d36a475",
    "parentId": "4af927ea-ec3b-4a56-9acc-6a3d3d36a475",
    "title": "General"
  },
  "callback": {
    "url": "https://acme.domo.com/api/buzz/v1/bots/message/4af927ea-ec3b-4a56-9acc-6a3d3d36a475",
    "headers": {
      "x-buzz-bot-token": "691575144a28497b9247e471cba9bf8ead2e5a7a20ee4d04b13e1a317260d0fc"
    }
  }
}
```

### Users left channel

```json
{
  "users": [
    {
      "displayName": "Adam Craven",
      "email": "adam@acme.com"
    }
  ],
  "event": {
    "type": "USERS_LEFT_CHANNEL"
  },
  "owner": {
    "id": 39485,
    "displayName": "Jamis Maxwell",
    "email": "jamis@acme.com"
  },
  "organization": {
    "domain": "acme.domo.com"
  },
  "channel": {
    "id": "4af927ea-ec3b-4a56-9acc-6a3d3d36a475",
    "parentId": "4af927ea-ec3b-4a56-9acc-6a3d3d36a475",
    "title": "General"
  },
  "callback": {
    "url": "https://acme.domo.com/api/buzz/v1/bots/message/4af927ea-ec3b-4a56-9acc-6a3d3d36a475",
    "headers": {
      "x-buzz-bot-token": "691575144a28497b9247e471cba9bf8ead2e5a7a20ee4d04b13e1a317260d0fc"
    }
  }
}
```
