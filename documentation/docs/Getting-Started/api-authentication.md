---
stoplight-id: 8ba9aedad3679
---

# APIs

Domo's APIs provide programmatic access to the powerful features of the Domo platform, enabling developers and data professionals to automate workflows, integrate external systems, and build custom data applications. Depending on the specific API and the tools you're using, authentication methods may vary — but in every case, your data's security is our top priority. Whether you're pulling data, pushing updates, or managing Users and DataSets, Domo’s APIs offer the flexibility and control you need to extend the value of your data.

## Which APIs should I use?

---

Domo offers several authentication methods, and the APIs available to you will vary based on the context in which you're developing.

1. **App Framework APIs:** APIs available within the Domo App context.
2. **Platform APIs:** APIs that use an OAuth 2.0 authorization and authentication pattern which allows you to define clients with a variety of scopes.
3. **Product APIs:** APIs that allow you to do anything you can do in the Domo UI. Tokens generated for these APIs provide access to all resources the user has in Domo.

| API           | Auth Approach     | Auth Instructions                                                                                                | Endpoint Coverage                                                               |
| ------------- | ----------------- | ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| App Framework | App Session Token | [App Sessions Guide](../Apps/App-Framework/Guides/app-sessions.md)                                               | Limited to endpoints explicitly allowed by the App Framework.                   |
| Platform      | API Client        | [Creating a Developer Client and Auth Token](https://developer.domo.com/portal/1845fc11bbe5d-api-authentication) | Limited to a subset of all Product endpoints that can be given scopes.          |
| Product       | Access Token      | [Managing Access Tokens](https://domo-support.domo.com/s/article/360042934494?language=en_US)                    | Access to all APIs corresponding to an action that can be taken in the Domo UI. |

If you're developing in the context of the [Domo App Framework](../Apps/App-Framework/Welcome.md), then you should use the App Framework APIs. This use-case includes both:

- [Building a Domo Brick](../Apps/DDX-Bricks/Quickstart/overview.md)
- [Building a Custom App on Domo](../Apps/App-Framework/Welcome.md)

If you're developing against Domo outside of the Domo App context, you'll want to use either the Platform (OAuth) APIs or the Product APIs. This use-case may include:

- [Writing Code Engine Functions](https://domo-support.domo.com/s/article/000005173?language=en_US)
- [Scripting in Jupyter Workspaces](../Data-Science/jupyter.md)
- Scripting from outside of Domo

The Platform APIs require using a client to regularly generate a refreshed access token, while the Product APIs only require a single access token. In general, Platform APIs are preferred because they allow for scoping clients to particular resources (e.g. Data, User, Dashboard, etc.) and their access tokens regularly expire and refresh. This reduces risk if you mistakenly leak your token.

The Product APIs are much more expansive in what they enable you to do, but you'll need to be more careful managing access to them.

In either case, admins have the ability to [revoke clients for the Platform APIs](https://domo-support.domo.com/s/article/000005240?language=en_US) or [tokens for the Product APIs](https://domo-support.domo.com/s/article/360042934494?language=en_US) at any time.

## App Framework APIs

---

Typically, authentication for the [App Framework APIs](../Domo-App-APIs/AppDB-API.md) is handled automatically when developing with the [Domo Apps CLI](../Apps/App-Framework/Tools/domo-CLI.md) through the `domo login` command or is inherited by virtue of developing from within your Domo Instance (e.g. building [Domo Bricks](../Apps/DDX-Bricks/Quickstart/overview.md)).

Please note that some of the App Framework APIs share (or have a similar) name as related Platform (OAuth) APIs. This can cause confusion, so it's worth clarifying that the App Framework APIs are for use within the Domo App context and the Platform (OAuth) APIs are more generally accessible.

- [AI Service Layer API](../Domo-App-APIs/AI-Service-Layer-API.md)
- [AppDB API](../Domo-App-APIs/AppDB-API.md)
- [Code Engine API](../Domo-App-APIs/Code-Engine-API.md)
- [Data API](../Domo-App-APIs/Data-API.md)
- [Files API](../Domo-App-APIs/Files-API.md)
- [Groups API](../Domo-App-APIs/Groups-API.md)
- [Task Center API](../Domo-App-APIs/Queues-and-Tasks-API.md)
- [User API](../Domo-App-APIs/User-API.md)
- [Workflows API](../Domo-App-APIs/Workflows-API.md)

## Platform (OAuth) APIs

---

The Domo Platform APIs leverage the OAuth 2.0 authorization and authentication pattern. This means
these APIs require creating and managing clients (which include a `client id`, `client secret`, and `scopes` to limit access). These clients can then be used to generate the `access token` passed in each subsequent API call. See the [OAuth API Authentication Quickstart](../API-Reference/Domo-APIs/API-Authentication.yaml) below for a walkthrough on how to generate clients.

- [Account API](../API-Reference/Domo-APIs/Account-API.yaml)
- [Activity Log API](../API-Reference/Domo-APIs/Activity-Log-API.yaml)
- [Cards API](../API-Reference/Domo-APIs/Card-API.yaml)
- [DataSet API](../API-Reference/Domo-APIs/DataSet-API.yaml)
- [Embed Token API](../API-Reference/Embed-APIs/Embed-Token-API.yaml)
- [Group API](../API-Reference/Domo-APIs/Group-API.yaml)
- [Page API](../API-Reference/Domo-APIs/Page-API.yaml)
- [Projects and Tasks API](../API-Reference/Domo-APIs/Projects-And-Tasks-API.yaml)
- [Simple API](../API-Reference/Domo-APIs/Simple-API.yaml)
- [Stream API](../API-Reference/Domo-APIs/Stream-API.yaml)
- [User API](../API-Reference/Domo-APIs/User-API.yaml)

## Product APIs

---

Product APIs allow you to programmatically do anything you could do as your user in the Domo UI. It requires [generating an access token in Domo](https://domo-support.domo.com/s/article/360042934494?language=en_US) that you pass to each request via the `X-DOMO-Developer-Token` header, which simulates the same request that the Domo product makes.

<!-- theme: warning -->

> #### Server-side only
>
> These APIs are CORS restricted, so they should only be called server-side when scripting against Domo. Due to this restriction, the "Try It" functionality in this documentation will not work, but the code snippet it generates (e.g. the curl request) should, provided that you replace `YOUR_INSTANCE` and `YOUR_TOKEN` with the appropriate values.

Documentation of many of the Product endpoints is underway. If you'd like to request documentation for a particular piece of functionality, please reach out to your CSM.

- [Activity Log API](../API-Reference/Product-APIs/Activity-Log.md)
- [AI Services API](../API-Reference/Product-APIs/AI-Services.md)
- [Alerts API](../API-Reference/Product-APIs/Alerts.md)
- [Beast Modes API](../API-Reference/Product-APIs/Beast-Modes.md)
- [Cards API](../API-Reference/Product-APIs/Cards.md)
- [Certified Content API](../API-Reference/Product-APIs/Certified-Content.md)
- [Connectors API](../API-Reference/Product-APIs/Connectors.md)
- [Data Accounts API](../API-Reference/Product-APIs/Data-Accounts.md)
- [DataSets API](../API-Reference/Product-APIs/Datasets.md)
- [Files API](../API-Reference/Product-APIs/Files.md)
- [Groups API](../API-Reference/Product-APIs/Groups.md)
- [Pages API](../API-Reference/Product-APIs/Pages.md)
- [Roles Governance API](../API-Reference/Product-APIs/Roles-Governance.md)
- [Search API](../API-Reference/Product-APIs/Search.md)
- [Task Center API](../API-Reference/Product-APIs/Task-Center.md)
- [Users API](../API-Reference/Product-APIs/Users.md)
- [Workflows API](../API-Reference/Product-APIs/Workflows.md)
