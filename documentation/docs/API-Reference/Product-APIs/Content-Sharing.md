# Content Sharing

The following endpoints can be used to share a variety of Domo content with other Domo users or Domo groups.

## Share Resource

Share Pages, Cards or Datasets with Users and Groups.

#### Query Parameters

| Property Name | Type    | Required | Description                                                                            |
| ------------- | ------- | -------- | -------------------------------------------------------------------------------------- |
| sendEmail     | Boolean | Optional | `true` if user or group should get an email when content is shared. `false` otherwise. |

#### HTTP Request

```text
POST https://{instance}.domo.com/api/content/v1/share)

HTTP/1.1
Accept: application/json

{
    "resources": [
        {
            "type": "page",
            "id": 830800298
        }
    ],
    "recipients": [
        {
            "type": "user",
            "id": 1129696109
        }
    ],
    "message": "I thought you might find this page interesting."
}

```

#### Request Body

| Property Name | Type             | Required | Description                                                                                                            |
| ------------- | ---------------- | -------- | ---------------------------------------------------------------------------------------------------------------------- |
| resources     | Array of objects | Required | Each resource object takes two properties `type` and `id`. Valid types are `"page"`, `"badge"` ( Card), `"dataset"`, . |
| recipients    | Array of objects | Required | Each recipient object takes two properties `type` and `id`. Valid types are `"group"` or `"user"`.                     |
| message       | String           | Optional | The message that gets included in the email when the content is shared with the recipient.                             |

#### HTTP Response

Returns status of 200 if successful.

```json
HTTP/1.1 200 OK
```

## Share App Studio App

Share one or many App Studio Apps with Users and Groups.

#### Query Parameters

| Property Name | Type    | Required | Description                                                                            |
| ------------- | ------- | -------- | -------------------------------------------------------------------------------------- |
| sendEmail     | Boolean | Optional | `true` if user or group should get an email when content is shared. `false` otherwise. |

#### HTTP Request

```text
POST https://{instance}.domo.com/api/content/v1/dataapps/share?sendEmail=true)

HTTP/1.1
Accept: application/json

{
    "message": "I thought you might find this app interesting.",
    "dataAppIds": [
        "1666052780"
    ],
    "recipients": [
        {
            "id": 1129696109,
            "type": "user"
        }
    ]
}

```

#### Request Body

| Property Name | Type             | Required | Description                                                                                        |
| ------------- | ---------------- | -------- | -------------------------------------------------------------------------------------------------- |
| dataAppIds    | Array of strings | Required | A list of all App Studio App ids to share.                                                         |
| recipients    | Array of objects | Required | Each recipient object takes two properties `type` and `id`. Valid types are `"group"` or `"user"`. |
| message       | String           | Optional | The message that gets included in the email when the content is shared with the recipient.         |

#### HTTP Response

Returns status of 200 if successful.

```json
HTTP/1.1 200 OK
```
