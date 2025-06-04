# Security and Governance

## Overview

Groups are useful inside Domo because you can grant access to specified content or conversations to all members of a group. It also adds quick access for users inside Domo's chat tool, Buzz, to mention a group of users which can then trigger notifications to each member.

<img class="aligncenter size-full wp-image-3179" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2017/06/07120326/GroupImage.png" alt=""  />

For example, you might create a "Marketing" group whose members have access to marketing-related dashboards. Or, you could create a "Solutions Consulting" group with access to specific message conversation inside Domo's Buzz tool.
<a href="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2017/06/07120326/GroupImage.png">
</a> <a href="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2017/06/07120327/GroupMessage.png"><img class="aligncenter size-large wp-image-3180" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2017/06/07120327/GroupMessage.png" alt="" /></a>

### Group use cases
---
Groups in Domo allow you to scale and extend Domo's user management to support multiple use cases:

- Grant personalized data permissions to an entire set of related users based on similar attributes (e.g. department, team, locale)
- Share subscriptions and access to dashboards and metrics to a group without needing to enroll individuals one at a time
- Easily draw attention to a larger audience by sending a message to an entire group while in Domo's collaboration tool.


## Quickstart
---

Creating a group with users inside Domo is easy to do and only requires two steps
<ol>
  <li>Create a group</li>
  <li>Add a user to a group</li>
 	<li>Remove a user from a group</li>
</ol>
After creating a group, you will need to execute the second step and third steps as more users need to be added or removed from a group.


<!-- theme: info -->

> #### Note
> In order to utilize this Quickstart you will need to obtain an [access token](../API-Reference/Embed-APIs/Embed-Token-API.yaml#quickstart) or you can leverage any of [Domo's SDKs](../Getting-Started/sdks.md) which will also handle authentication.

### Step 1: Create a group
---
Groups are collections of users. Group APIs makes it easy to manage a large number of users that are related in some way. Groups allow you to set access rights to data that stays consistent even when the group members may change. Groups are also a convenient way to communicate with a group of related users inside Domo's collaboration tool, Buzz.

This code creates a group via the [Group](../API-Reference/Domo-APIs/Group-API.yaml) API:

#### Sample Request


See this sample request in [Java](https://github.com/domoinc/domo-java-sdk/tree/master/domo-java-sdk-all/src/test/java/com/domo/sdk/groups/CreateExample.java), [Python](https://github.com/domoinc/domo-python-sdk/blob/master/examples/group.py).


```HTTP
POST https://api.domo.com/v1/groups HTTP/1.1
Content-Type: application/json
Accept: application/json
Authorization: bearer <your-valid-oauth-access-token>

{
  "name": "Groupy Group"
}
```

Domo returns a new `Group` object with all the relevant details:

#### Sample Response

```HTTP
HTTP/1.1 201 Created
Content-Type: application/json;charset=UTF-8

{
  "id": 876655018,
  "name": "Groupy Group",
  "active": true,
  "creatorId": "87659738",
  "default": false
}
```

Once you create the group, store the id value to group name in your own database to utilize when adding users with the [User](../API-Reference/Domo-APIs/User-API.yaml) API or applying data permissions inside with the [Personalized Data Permission Policy (PDP)](pdp.md) API.


### Step 2: Add user(s) to a group
---
With a new `group_id`, add an existing `user_id` (from [User](../API-Reference/Domo-APIs/User-API.yaml) API) to the group:

#### Sample Request

See this sample request in [Java](https://github.com/domoinc/domo-java-sdk/tree/master/domo-java-sdk-all/src/test/java/com/domo/sdk/groups/CreateExample.java), [Python](https://github.com/domoinc/domo-python-sdk/blob/master/examples/group.py).

```HTTP
PUT https://api.domo.com/v1/groups/876655018/users/27
Content-Type: application/json
Accept: application/json
Authorization: bearer <your-valid-oauth-access-token>
```

Domo will return a parameter of success or error based on the group ID being valid.

#### Sample Response

```http
HTTP/1.1 204 No Content
```

### Step 3: Remove user(s)
---
Similar to adding a user to a group, you will need both the `group_id` and `user_id` in order to remove a user from a group:

#### Sample Request

See this sample request in [Java](https://github.com/domoinc/domo-java-sdk/tree/master/domo-java-sdk-all/src/test/java/com/domo/sdk/groups/CreateExample.java), [Python](https://github.com/domoinc/domo-python-sdk/blob/master/examples/group.py).

```HTTP
DELETE https://api.domo.com/v1/groups/876655018/users/27 HTTP/1.1
Content-Type: application/json
Accept: application/json
Authorization: bearer <your-valid-oauth-access-token>
```

Domo will return a parameter of success or error based on the group ID being valid.

#### Sample Response
```HTTP
HTTP/1.1 204 No Content
```