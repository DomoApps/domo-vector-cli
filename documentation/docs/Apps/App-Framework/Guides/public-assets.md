---
stoplight-id: df8b045188694
---

# Public Assets

Public assets is a feature developed for custom Domo apps that allows developers to host static assets in an unauthenticated way. This may be useful if you need to share assets like pictures or javascript code between your custom Domo app and your public website. You might also want to build your public website directly on Domo instead of having to find another hosting provider. In that case, you could simply publish an index.html file as a public asset and you would have a public facing website for your Domo app.

Because public assets do not render in an authenticated context, public javascript files will not have access to any of the Domo APIs that you are used to using in a custom Domo app. If a user of your public asset requires access to the APIs you will need to direct them to an authenticated context where they can login and use non-public assets.

<img class="aligncenter" src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-public-assets-flow.png" width="499" height="545" />

### Creating Public Assets
---
Creating public assets is as simple as adding a new folder to your custom Domo app project called "public-assets". Any file that exists within the "public-assets" folder, when published up to your Domo instance and instantiated as a card, will now be available to the public. The URL for your public asset will be the same URL that you find as the `src` for the iframe that hosts your Domo app as a card in your instance.

Example of a public index.html file:
```bash
https://{appID}.domoapps.{environment}.domo.com/public-assets/index.html
```

*Note:* Any assets that were added to a "public-assets" folder in an instantiated app before August 2020 will remain private and require authentication. Only apps created after this time with public asset folders will contain publicly accessible assets.