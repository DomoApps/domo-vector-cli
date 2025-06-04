---
stoplight-id: 1cleirjemoy6i
---

# App Embed Authentication

Safari has decided to block third party cookies:

- https://webkit.org/blog/9661/preventing-tracking-prevention-tracking/
- https://webkit.org/blog/9521/intelligent-tracking-prevention-2-3/

Since embed authentication is meant to avoid any workflow interruptions, cookies are no longer a viable option in Safari. Any call made from an embedded app must be authenticated in a new way because other browsers will eventually also block cookies from facilitating these types of interactions across domains.

The way to stay future proof with embedded apps is by making an additional reference to a new token in the app’s JavaScript code. Authenticated access for apps in private embed should use a the combination of these three methods that best fit your use case:

## Header-based authentication

- **Use case:** Authenticating any HTTP call through code to get data from the instance
- **Benefit:** The header can then access the tokens required to make the programmatic filter options for private embed effective even as other browsers eventually follow Safari’s example.
- **Best practice:** For consistency, please ensure to maintain double underscores before and after the RYUU token as shown in the code below.
- **Example:** The app.js file that stores this code must be hosted in a folder called “public-assets” to be accessible by Domo.

```js

document.body.onload = () => {
  const token = window.__RYUU_AUTHENTICATION_TOKEN__;

  fetch(`/domo/environment/v1`, {
      method: 'GET',
      headers: {
        'X-DOMO-Ryuu-Token': token,
        'content-type': 'application/json'
      }
    })
    .then(res => res.json())
    .then(console.log)
}

```

## “Public Assets” folder

- **Use case**: Referencing static images and documents like calls to a non-sensitive JavaScript file
- **Benefit:** Simplify access to resources that populate the embedded experience
- **Best practice:** Move files and references to a “public-assets” path. Avoid any sensitive business logic in this folder.
- **Example:** [Public Assets](df8b045188694-public-assets)

## Query parameters in the URL

- **Use case:** Filtering non-sensitive data in apps
- **Benefit:** Provide users with a head start in focusing on the most relevant data. Ensure the host page and embedded content can share context with each other.
- **Example:** `?rpt` param applies not on the iframe but actually inside the app code

```html

<img id="exampleImg" src="example.jpg" />

<script>
    const token = window.__RYUU_AUTHENTICATION_TOKEN__;
    const img = document.getElementById('exampleImg');
    const url = new URL(img.src);
    url.searchParams.append('rpt', token);
    img.src = url.toString();
</script>
```
<!-- theme: info -->

> #### Whitelisting cross-origin access in Identity Providers
>
> When apps are embedded, the IDP (Identity Provider) of the host site will often need to whitelist the Domo domain that serves the apps as a trusted web origin. Since app hosting has a more complex subdomain structure than common cards and pages in your instance, the pattern of `{appId}.domoapps.{environment}.domo.com` results in the ideal whitelist value of: '*.domoapps.​*.domo.com'
>
> Cross-origin access grants can be applied in the application settings of IDPs like Okta, Microsoft Azure Active Directory, Ping Identity, SailPoint, OneLogin, ForgeRock, Centrify, and more.








