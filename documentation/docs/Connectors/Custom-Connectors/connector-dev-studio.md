---
stoplight-id: 3cfe84d925633
---

# Custom Connectors

With pre-built connectors covering most popular data sources, Domo helps you get the data you need to drive your business. However, if you need a unique cloud connection that is not currently available, with a little JavaScript knowledge, the Connector Dev Studio enables you to create your own Connector. Whether you want the Connector for exclusive use within your own company, or you want to add it to the community of all available Connectors, our Connector Dev Studio guide will walk you through building your own custom Connector.

## Connector Dev Studio

### Before You Start
---
Before building a new Connector, make sure the Connector doesn’t already exist. Domo has over 1,000 pre-built Connectors, with more continually being added. You can see existing Connectors by navigating to the Connectors page in the Domo Appstore **[here](https://www.domo.com/appstore/apps?appType=Connector)**.

You can then search and filter to find if the Connector you need has already been built.

<img class="alignnone size-full wp-image-3731" src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-connectors-list-misc.png" alt="" width="1083" height="&quot;1008" />

### Let's Build!
---

To build a custom connector, the API you wish to connect to must meet a few requirements. It must:

- Use https
- Use a REST API
- Either require no authentication, or authenticate using
   - OAuth 2.0
   - An API Key
   - A username and password

<button class="domo-cta-button">
  <a href="https://api.domo.com/builder/index.html">Build a Custom Connector</a>
</button>

<!-- theme: info -->

> #### Note
>Because the IDE is built using the [Java 17 Graavl engine], you need to write your code using JavaScript compatible with [ECMAScript 5 (ES5)](https://www.w3schools.com/js/js_es5.asp). For example, Xmlhttprequest is not supported. Use httprequest in its place:

```
httprequest.get('https://samplecrm.domo.com/samplecrm');
```

