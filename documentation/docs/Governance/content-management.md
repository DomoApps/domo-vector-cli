# Organize, manage, and share content to other users in Domo using the Page API

## Overview
A page in Domo is a screen where you can view a "collection" of data, which is typically displayed in cards. You use a page to organize, manage, and share content to other users in Domo.

<a href="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2017/08/09100910/PageVisuals.png"><img class="aligncenter size-full wp-image-3185" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2017/08/09100910/PageVisuals.png" alt="" /></a>

Pages allow you to send external reports, create holistic filters across all metrics within the page, or have conversations in Domo's Buzz tool about the data associated to the entire page.  The Page API allows you to create, delete,  retrieve a page or a list of pages, and update page information and content within a page.

### Page use cases
---
The Page API allows you to extend Domo's platform to support multiple use cases:
<ul>
 	<li>Automate external processes to administer and manage content within Domo</li>
 	<li>Easily copy pages, page collections, or cards within an instance</li>
 	<li>Grant access to groups or users to a page</li>
 	<li>Lock or unlock the capability to edit a page's information or content.</li>
</ul>


You can also refer to the following guides and articles for additional help on content and page administration:
<ul>
 	<li><a href="https://knowledge.domo.com/Administer/Controlling_Access_in_Domo" target="_blank" rel="noopener">Controlling Access in Domo</a></li>
 	<li><a href="https://domohelp.domo.com/hc/en-us/articles/360043439153-Specifying-Default-Overview-Content-for-Users" target="_blank" rel="noopener">Specifying Default Overview Content for Users</a></li>
 	<li><a href="https://knowledge.domo.com/Optimize/Filtering_Data/02Applying_Page-Level_Filters" target="_blank" rel="noopener">Applying Page Level Filters</a></li>
</ul>

## Quickstart
Creating a new page in Domo, updating the page layout by adding collections for cards, and then sharing the new page with users and groups requires three steps.
<ol>
 	<li>Create a page</li>
 	<li>Create page collections</li>
 	<li>Share a page with users or groups</li>
</ol>
Once a page is created, you can continue to programmatically update it's content and access.

> **NOTE:** 
> In order to utilize this Quickstart you will need to obtain an [access token](../API-Reference/Embed-APIs/Embed-Token-API.yaml#quickstart) or you can leverage any of [Domo's SDKs](../Getting-Started/sdks.md) which will also handle authentication.

### Step 1: Create a page
---
The first step to managing content in Domo is to create a page. When initially creating a new page, you can automatically add existing cards and grant access to users and groups within the initial request.  

This code creates a page via the [Page](../API-Reference/Domo-APIs/Page-API.yaml) API:

#### Sample Request
See this sample request in <a href="https://github.com/domoinc/domo-java-sdk/blob/master/domo-java-sdk-all/src/test/java/com/domo/sdk/pages/CreateExample.java" target="_blank" rel="noopener">Java</a>, <a href="https://github.com/domoinc/domo-python-sdk/blob/master/examples/page.py" target="_blank" rel="noopener">Python</a>.

```HTTP
POST https://api.domo.com/v1/pages 
Content-Type: application/json
Accept: application/json
Authorization: bearer <your-valid-oauth-access-token>

{
  "name": "Supply Chain",
   "parentId": 23,
   "locked": "TRUE",
   "cardIds": [12,2535,233,694], 
   "visibility": {
        "userIds": [793,20,993,19234],
        "groupIds": [32,25,17,74]
    }
}
```

Domo will then return a page object when successful. 

#### Sample Response
```HTTP
HTTP/1.1 201 Created
Content-Type: application/json;charset=UTF-8

{
   "id": 3242,
   "parentId": 23,
   "ownerId": 88,
   "name": "Supply Chain",
   "locked": TRUE,
   "cardIds": [12,2535,233,694], 
   "visibility": {
        "userIds": [793,20,993,19234],
        "groupIds": [32,25,17,74]
    }
}
```

Once you create the page, store the `page_id` value to page name in your own database to utilize when creating page collections or making updates to the page's content.

### Step 2: Create a page collection
---
Now that you've created a page and added cards, you can now organize the page's content into page collections.  

NOTE: In order to add cards to a page collection,  the cards must already exist on the page. To add a card to the page, you may either add cards when you create or update the Page via the API.

#### Sample Request

See this sample request in <a href="https://github.com/domoinc/domo-java-sdk/blob/master/domo-java-sdk-all/src/test/java/com/domo/sdk/pages/CollectionCreateExample.java" target="_blank" rel="noopener">Java</a>, <a href="https://github.com/domoinc/domo-python-sdk/blob/master/examples/page.py" target="_blank" rel="noopener">Python</a>.

```HTTP
POST https://api.domo.com/v1/pages/3242/collections
Content-Type: application/json
Accept: application/json
Authorization: bearer <your-valid-oauth-access-token>

{
  "title": "East Sales",
  "description": "East Region team  includes all Eastern states.",
   "cardIds": [2535,233,694], 
}
```

#### Returns

Returns the parameter of success or error based on the page ID being valid.

#### Sample Response
```HTTP
HTTP/1.1 200 OK
```

### Step 3: Share page with users or groups
---
When you share a page with a user, the page itself is added to the page tab row in the user's personalized Domo view, and the name of the page is added to the user's Pages listing in the People tab. 

When you share a page with a group, the page is added to the Domo view of every member of that group, and the name of the page is added to the group's Content Accessible by this Group listing in the Groups tab. Users you've shared with have access to the page and all the cards in it (unless you restrict access to specific cards in the page using the Share dialog).

In order to share a page with either a group or user, the `visibility` object needs to be added as a parameter with either an array of  `group_ids` or `user_ids` you wish to grant access.

#### Sample Request

See this sample request in <a href="https://github.com/domoinc/domo-java-sdk/blob/master/domo-java-sdk-all/src/test/java/com/domo/sdk/pages/UpdateExample.java" target="_blank" rel="noopener">Java</a>, <a href="https://github.com/domoinc/domo-python-sdk/blob/master/examples/page.py" target="_blank" rel="noopener">Python</a>.

```HTTP
PUT https://api.domo.com/v1/pages/3242
Content-Type: application/json
Accept: application/json
Authorization: bearer <your-valid-oauth-access-token>

{
  "name": "Supply Chain Management",
   "parentId": 84,
   "locked": FALSE,
   "collectionIds": [2,4,3,1],
   "cardIds": [2535,233,12,9932,694], 
   "visibility": {
        "userIds": [993,19234],
        "groupIds": [2,28,17,24]
    }
}
```
Domo will then return a parameter of success or error based on the page ID being valid.

#### Sample Response
```HTTP
HTTP/1.1 200 OK
```


