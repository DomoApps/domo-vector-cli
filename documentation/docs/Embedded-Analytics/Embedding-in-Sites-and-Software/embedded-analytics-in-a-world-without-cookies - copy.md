---
stoplight-id: nldrdylitc11u
---

# Embedded Analytics in a World Without Cookies

Keep your external data experiences future-proof with Domo Everywhere

## What is changing with cookies?

---

Cookies are small text files stored by your web browser when you visit websites. Visitors can control how websites use cookies by configuring browser's privacy settings. Cookie blocks are becoming much more common to protect privacy.

Some browsers like Safari already block third-party cookies that do not come from the main site. This can complicate authentication when you want to mix content from multiple systems with embedded analytics.

![EmbedwithoutCookies1](https://web-assets.domo.com/blog/wp-content/uploads/2022/08/EmbedwithoutCookies1.png)

## Why are these changes being made by the browsers?

---

These privacy changes help visitors understand how they are tracked throughout the web. To maintain trust, we all must align with governmental regulations like GDPR. Experimental APIs like the Storage Access API allow users to give intentional consent when websites need to store tracking data on their browser.

With these policies having already rolled out or rolling out soon, the message is clear: **don’t rely completely on cookies and other web storage to authenticate or track users.**

## How should embedded data experiences be protected now?

---

Domo has a way to balance privacy with authentication in embedded analytics: tokens and headers. By shifting to header-based authentication, embedded analytics can stay future-proof while avoiding entanglement in policy changes with cookies. Shifting to these types of tokens even simplifies distributing private data experiences to huge audiences.

**Best of all, you do not even need to lift a finger to keep embedded experiences safe**, secure, and reliable in every browser. All changes are being made by our engineering team in the Domo backend.

You can confidently continue to embed dashboards in the view experience or create dedicated environments for each customer in the edit experience. All backend changes will be complete before leading browsers block cookies. If you want to accelerate support for these new authentication methods in the view experience, the final section below shows how this can be done immediately by migrating from PDP to programmatic filters.

## When do I need to shift to this new authentication method?

---

Domo recommends starting this migration right away since Safari already blocks third-party cookies. Firefox is following close behind with a strict set of default privacy settings. Chrome and Edge will follow later

Every browser will eventually need to conform to Intelligent Tracking Prevention policies that have been emphasized for the past few years: [Intelligent Tracking Prevention 2.3](https://webkit.org/blog/9521/intelligent-tracking-prevention-2-3/)

![EmbedwithoutCookies4](https://web-assets.domo.com/blog/wp-content/uploads/2022/08/EmbedwithoutCookies4.png)

![EmbedwithoutCookies5](https://web-assets.domo.com/blog/wp-content/uploads/2022/08/EmbedwithoutCookies5.png)

Currently, all Domo requests are still authenticated by a cookie. Domo is finishing the process of upgrading all endpoints to authenticate with tokens in the header instead of cookies. Engineering will then update Domo front-end code to reference that header in every request.

Once that migration is completed in 2023, we will store that token locally in memory so it will not persist across sessions. This will give all customers plenty of protection before other browsers expand third party cookie blocks. For example, Google recently announced that change is not targeted until late 2024: [Update on Testing Privacy Sandbox Web](https://blog.google/products/chrome/update-testing-privacy-sandbox-web)

![NoCookiesEmbed4](https://web-assets.domo.com/blog/wp-content/uploads/2022/08/NoCookiesEmbed4.png)

## How will this change impact the embedded edit experience?

---

When users of the edit experience refresh their browser, that will impact the outer page that hosts the embedded experience. Therefore, it will not be an interruption to go through the authentication flow and get a new token each time.

This change from cookies to tokens will not impact the normal login experience when accessing instances directly. This will only apply to embedded experiences that rely on Domo Everywhere and the Domo Identity Broker. Here is how the authentication process will flow:

![EmbedwithoutCookies6](https://web-assets.domo.com/blog/wp-content/uploads/2022/08/EmbedwithoutCookies6.png)

## How will this change impact the embedded view experience?

---

If external viewers have an active session, everything in embedded cards and dashboards will load correctly. If they do not have an active session, external viewers will see a login screen in most browsers but are blocked completely in Safari.

To avoid seeing the Domo login screen in the private embed iframe, SSO integrations were formerly configured in very old deployments of Domo Everywhere that started way back in 2017.

&nbsp;
![EmbedwithoutCookies7](https://web-assets.domo.com/blog/wp-content/uploads/2022/08/EmbedwithoutCookies7.png)
&nbsp;

Those SSO configurations are blocked in Safari today because of their reliance on cookies. After Domo releases this new header authentication flow, SSO will work seamlessly even in an iframe.

In the meantime, the majority of Domo Everywhere customers focused on distributing the view experience have already migrated to the modern token-based approach. This is done by replacing PDP policies for each external user with programmatic filters in secure server-side code. This is documented in detail [here](1yafxad1u8azv-programmatic-filtering).

Here is how the authentication process flows:

![EmbedwithoutCookies8](https://web-assets.domo.com/blog/wp-content/uploads/2022/08/EmbedwithoutCookies8.png)

Migrating from PDP to programmatic filters delivers numerous other benefits beyond cookies. Filtering is now done according to the user profiles already in your host system. You no longer need to rebuild access policies in PDP. Nor do you need to create individual user accounts in Domo for each external viewer. You can show the approved content and rows for each user all through a service account that acts as a proxy for every other viewer.

![EmbedwithoutCookies2](https://web-assets.domo.com/blog/wp-content/uploads/2022/08/EmbedwithoutCookies2.png)

Even though the changes for the edit experience will apply in 2023, all these benefits are ready for you today in the view experience. We encourage you to try these new authentication options today whether you are an existing customer or a prospect interested in a free trial: [https://www.domo.com/embedded-analytics](https://www.domo.com/embedded-analytics).
