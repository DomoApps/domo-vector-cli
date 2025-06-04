---
stoplight-id: 28v6sqz9eslb9
---

# Overview

Create an app on the Domo Platform for maximum flexibility in design, data collection, and distribution.

- **Pre-built apps**: [Domo’s Appstore](https://www.domo.com/intelligent-apps/about-appstore) provides a collection of apps built by Domo and our community that you can leverage for fast insights.
- **[Domo Bricks](../Apps/DDX-Bricks/Quickstart/overview.md) (previously DDX Bricks)**: Domo Bricks are pre-built objects that allow you to create advanced visualizations and apps that can be customized in a simple browser-based code editor.
- **[App Framework](../Apps/App-Framework/Welcome.md)**: The Domo App Framework provides a set of APIs for building custom JavaScript-based front-ends on Domo and a transactional database called AppDB, which is a wrapper on top of MongoDB.

## Domo Bricks or the App Framework?

In general, the more complex your app solution, the more you'll want to lean on the full tooling available in the App Framework.

![bricks-or-app-framework.png](../../assets/images/bricks-or-app-framework.png)

**[Domo Bricks](../Apps/DDX-Bricks/Quickstart/overview.md) (previously DDX Bricks)** are a great tool for quickly customizing Domo if your use-case can be achieved by:

- Tweaking the HTML, CSS, and JavaScript of pre-built Domo Brick in the [Domo Appstore](https://www.domo.com/intelligent-apps/about-appstore).
- Building your application from scratch in the three files of the Domo Bricks browser-based editor: HTML, CSS, and JS.
- Leveraging external libraries via [CDN](https://developer.mozilla.org/en-US/docs/Glossary/CDN) (e.g. without the need of a package management tool like [npm](https://www.npmjs.com/) or [yarn](https://yarnpkg.com/)).

As the complexity of your app grows, the full **[App Framework](../Apps/App-Framework/Welcome.md)** tooling is the way to go. This may be because:

- Your app requires more than just three files.
- Your app has many dependencies and is using package management tools (like [npm](https://www.npmjs.com/) or [yarn](https://yarnpkg.com/)).
- You prefer developing in the text editor or IDE of your choice (e.g. VSCode, Sublime Text, Atom, etc.).
- Your app involves data collection via [CRUD](https://developer.mozilla.org/en-US/docs/Glossary/CRUD) operations (Create, Read, Update, Delete), which requires Domo's built-in transactional datastore called [AppDB](../Domo-App-APIs/AppDB-API.md).
  - Note: it is possible to leverage AppDB in a Domo Brick (e.g. [DDX Form and Dataset](https://www.domo.com/appstore/app/ddx-form-and-dataset/overview)), but the App Framework is the preferred approach.
- Your app requires the ability to interface with the [Files API](../Domo-App-APIs/Files-API.md).
- You'd like greater control over the number of DataSets connected to your App (max: 100) and how a user can configure column mappings to those DataSets on the Wiring Screen.
- You'd like to leverage JavaScript frameworks like [React, Angular, or Vue](App-Framework/Quickstart/Starter-Kits.md).
- You'd like to follow standard development lifecycle practices (e.g. version control, CI/CD pipelines, etc.).

## App Showcase

The Domo platform provides tools to build custom solutions that digitize and augment common business processes, create unique visualizations to guide analysis for users, and support data collection—on both desktop and mobile. See for yourself how others have leveraged Domo to build their apps and solutions.

### Utah Jazz

---

<img class="alignleft" src="https://web-assets.domo.com/miyagi/images/product/product-customer-utah-jazz-custom-app-anon.gif" />

#### How an NBA team visualizes their stadium to drive revenue

The Utah Jazz partnered with Domo to develop a custom seat-by-seat visualization of their stadium, enabling them to track key metrics like revenue, sales, and attendance — and to analyze how different conditions impact these values across all 19,000+ seats in the arena.

The app has allowed analysts and non-analysts alike to explore data, drive insights, and increase ticket sales for the organization.

### ESPN

---

<img class="alignleft " src="https://web-assets.domo.com/miyagi/images/product/product-customer-espn-app-anon-2x.png" />

#### Keeping a pulse on fan engagement

ESPN’s Nielsen Social Program App allows ESPN’s team to track daily Nielsen social content ratings and fan sentiment for all their TV and streaming content, then compare the data to interactions with fans in the contact center.

The app provides ESPN with a comprehensive picture of fan sentiment and helps the team ensure that their messaging stays on-brand and consistent.

### Telus

---

<img class="alignright" src="https://web-assets.domo.com/miyagi/images/product/product-customer-telus-custom-app-anon-2.gif" />

#### Real-time store performance KPIs

The Telus Store Manager Dashboard App empowers retail store managers with information on store performance. The app provides a clear view of how each store is performing against goals, as well as how other stores are performing in comparison.

This app provides store managers with a real-time view of their most important KPIs, any time, from any device. Managers have instant access to mission-critical metrics to help drive performance, as well as insight to how their stores stack up against others.

### Retail Store Performance App

<img class="alignleft " src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-customer-app-retail-performance.jpg" />

#### Giving store leaders the data they need to run their business — on their phone

The Retail Store Performance App puts all the data a store leader needs to run their business right on their phone. The app features current sales performance metrics, real-time feedback capture and incident reporting, and push communications to keep the entire store team on the same page.

### Blue Moon

---

<img class="alignright " src="https://web-assets.domo.com/appstore/api/library/v1/images/33137" />

#### Capturing how digital marketing efforts translate into revenue

Blue Moon’s E-commerce Revenue Equation App allows marketers to view and analyze the performance of their digital marketing by channel, device type, and visitor type to see how traffic, AOV, and CVR affect revenue.

<a class="btn btn-primary" style="float: left;" href="https://www.domo.com/appstore/app/ecommerce-revenue-equation/overview" target="_blank" rel="noopener">See it in the Domo Appstore</a>

### Google Maps Pinboard

---

<img class="alignleft " src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-app-custom-google-maps-pinboard.jpg" />

#### Using location metrics to improve business performance

The Google Maps Pinboard uses the power of Google Maps to help you visualize all your locations and drill down to metrics for each one. Simply click on the map to open up details for your selected location. Filter by business category, region, and owner, or search for specific items. See operational data for each location in table format, and even see the value distribution for each of your defined metrics, such as traffic and gross sales.

<a class="btn btn-primary" style="float: left;" href="https://www.domo.com/appstore/app/google-maps-pinboard-app/overview" target="_blank" rel="noopener">See it in the Appstore</a>

### Keypoint Intelligence

---

https://player.vimeo.com/video/329688570

#### Driving better decisions with geospatial visualizations

Keypoint Intelligence worked with Domo to create a custom geospatial visualization application. Their Flex Map app allows users to easily search simple parameters, save their work, and build complex queries. Keypoint’s app provides further functionality by letting users build shapes by zip codes or custom areas to refine their data further. Keypoint can bring all their different areas of data together to drive better decisions.

### Travel Leakage Analyzer App

---

<img class="alignleft" src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-app-custom-christopherson-travel-leakage-analyzer.jpg" />

#### Ensuring travel policy compliance

Christopherson built their Travel Leakage Analyzer App to help businesses understand where travel spend is out of policy. By combining feeds from Christopherson’s robust software platform, AirPortal®, and financial systems such as Concur, NetSuite, and QuickBooks, the Travel Leakage App visualizes where travel spend is compliant, and more importantly, where it is not.

<a class="btn btn-primary" style="float: left;" href="https://www.domo.com/appstore/app/travel-leakage-analyzer-app/overview" target="_blank" rel="noopener">See it in the Domo Appstore</a>

### Sales Leaderboard

---

<img class="alignright " src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-customer-app-sales-leaderboard.jpg" />

#### Motivating sales with real data

With Sales Leaderboard, you can track top performers, predict future leaders, and plan training and incentives accordingly. This app provides sales leadership with a current and forecasted end-of period ranking for all sales reps. Sales leadership can share this app within sales teams or with the broader organization to motivate reps and promote healthy competition.

<a class="btn btn-primary" style="float: left;" href="https://www.domo.com/appstore/app/sales-leaderboard-app/overview" target="_blank" rel="noopener">See it in the Domo Appstore</a>
