---
stoplight-id: wbwvwmq9rd714
---

# Filtering Options

All these filter types are layered in the sequence below:

![Filtering Options 1](https://web-assets.domo.com/blog/wp-content/uploads/2022/08/FilteringOptions1.png)

## SECURE POLICIES

### Personalized Data Permissions (PDP)

**Documentation:** [Creating and Deleting PDP Policies](https://domohelp.domo.com/hc/en-us/articles/360042934614-Creating-and-Deleting-PDP-Policies)

**Definition:** Outdated SSO integration reliant upon cookies for individual accounts for each viewer

**Use case:** Forced row-level security defined in the Domo interface that cannot be seen nor edited by viewers

**Warning:** Browsers are expanding their 3rd party cookie blocks. The best practice is to use Programmatic Filters instead of PDP to [stay future-proof](52ozpgfra3lsd-embedded-analytics-in-a-world-without-cookies).

**Note:** If this older method must absolutely be used for personalization, protect yourself from embed viewers tracing the iframe back to the instance and seeing extra cards and pages beyond the embedded content. This is done by creating a dedicated instance for external use cases, applying the Whitelabel V1 template of feature switches, and embedding from there instead of your main internal instance.

![Filtering Options 2](https://web-assets.domo.com/blog/wp-content/uploads/2022/08/FilteringOptions2.png)

### Server-side Programmatic Filters

**Documentation:** [Programmatic Filtering](1yafxad1u8azv-programmatic-filtering)

**Definition:** Newer SSO integration with cookie-less auth through a single service account for all viewers

**Use case:** Forced row-level security defined in server side code that cannot be seen nor edited by viewers

**Warning:** This will shift contracts from user/viewer pricing to impression/view pricing since a single service account acts as proxy for all viewers.

**Note:** No dedicated external instance is required for this approach since the viewers will not have access to the client ID and secret of the service account. Therefore, they cannot trace the iframe and gain access to the Domo instance.

![Filtering Options 3](https://web-assets.domo.com/blog/wp-content/uploads/2022/08/FilteringOptions3.png)

## CLIENT-SIDE PARAMS

### JS API Filters

**Documentation:** [JS API Sample Code Repo](https://github.com/domoinc/domo-node-embed-filters/blob/master/public/jsapi.js)

- Outputs: The JS API listens for click events on the embedded content and passes them back up to the host page for cross-system links and interaction analytics.
- Inputs: The JS API also completes the bidirectional passing of context by letting the host page push filters down into the embedded content
- Controls: The code above can be triggered by any external menu in the host page

**Events:** currently the following events are supported.

| Event                 | Type   | Description                                                                                                                                                  | Message                                                                                                                                                                  | Support                     |
| --------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------- |
| /v1/onFrameSizeChange | Output | Event communicating the content size of the embed asset. Use when wanting to make sure the iframe is the exact size of the content so no scroll bars appear. |                                                                                                                                                                          | App Studio, Dashboard, Card |
| /v1/onFiltersChange   | Output | Event communicating filter changes                                                                                                                           |                                                                                                                                                                          | App Studio, Dashboard, Card |
| /v1/onAppData         | Output | Event communicating "appData" between an app in an embedded asset and the embedding website                                                                  |                                                                                                                                                                          | App Studio, Dashboard, Card |
| /v1/onAppReady        | Output | Event communicated by App Studio app to indicate the app finished loading                                                                                    |                                                                                                                                                                          | App Studio                  |
| /v1/filters/apply     | Input  | Event to communicate filters for an asset to apply                                                                                                           | {<br>id: 'setFilters123',<br>jsonrpc: '2.0',<br>method: '/v1/filters/apply',<br>params: {<br>filters: [{'column': 'name', 'operand': 'IN', 'values': ['ABC']}]<br>}<br>} | App Studio, Dashboard, Card |
| /v1/appData/apply     | Input  | Event to communicate "appData" to an app within the embed asset                                                                                              | { <br>id: 'appData',<br>jsonrpc: '2.0',<br>method: '/v1/appData/apply',<br>params: {<br>appData: appData <br>}<br>}                                                      | App Studio                  |

**Example:**

Here are some [examples](https://github.com/STEEZENS/domo-pfilters) of external drop-down filter controls we used while building [Domo’s COVID-19 Tracker](https://www.domo.com/covid19/daily-pulse/):

![Filtering Options 4](https://web-assets.domo.com/blog/wp-content/uploads/2022/08/FilteringOptions4.png)

**Definition:** Client-side approach here contrasts from server-side approach above because these are meant to be visible and editable for viewers. The filters applied via the embed API through event ports and listeners.

**Use case:** Newer approach to applying external filter controls from the host page (like drop down menus outside of the iframe). Changes can be applied faster to multiple pieces of embedded content **without forcing iframe refresh**. Also supports bidirectional context passing (where click events on the embedded content can also be passed back to the home page for cross-iframe or cross-page drills, links, and interactions.)

**Warning:** JS API (here) and Pfilters (below) are not a secure replacement for Programmatic Filters because the client-side parameters can be seen and changed by viewers by either glancing at the URL or inspecting the content. These should only be used for filters that aid exploration.

**Note:** The **main pre-requisite** is population of the “Embed Authorized Domains” whitelist. This whitelist drives a CSP (content security policy) which ensures these bidirectional signals are only sent in ports for sites you approve:

![Filtering Options 5](https://web-assets.domo.com/blog/wp-content/uploads/2022/08/FilteringOptions5.png)

The demo video below shows how the events are displayed with specific references even if multiple iframes are included in the same page:

[Demo Video](https://player.vimeo.com/video/515861680)

### Pfilter URL parameters

[Using Pfilters to Apply Filters from URL Query Parameters to Embedded Dashboards](url-parameters-in-embedded-content.md#pfilters)

**Definition:** Simpler setup in URL params instead of client side code like JS API filters. However, pfilters are slightly **slower because they force an iframe** refresh to apply the filter logic. They use the same filter pattern (column, operand, value) as client-side JS API and server-side Programmatic Filters.

**Use Case:** Older approach to applying external filter controls.

**Warning:** Pfilters and the JS API are not a secure replacement for Programmatic Filters because the client-side parameters can be seen and changed by viewers by either glancing at the URL or inspecting the content. These should only be used for filters that aid exploration.

![Filtering Options 7](https://web-assets.domo.com/blog/wp-content/uploads/2022/08/FilteringOptions7.png)

### Additional App Studio URL parameter

**Definition:** For additional control over an embedded App Studio app, the URL param **overrideFilters** can be added to provide more control over whether an app should load up its saved default filters. When **overrideFilters=true**, the App Studio app will not load up any filters, instead, it will wait for a filter event from the parent before loading filters. When **overrideFilters=false** or when not provided, the filters saved to the default filter view of an App Studio app will load.

**Use Case:** If you are actively applying filters to an embedded App Studio app, this parameter will help prevent getting in a mixed filtered state where the nested app may load up its own and get out of sync with the parent OR change the intended filters meant to be passed to the app.

**Warning:** If setting **overrideFilters=true**, filters will not load up **UNTIL** the parent communicates a filter state using the **/v1/filters/apply** event. Even if it is an empty filter state, the parent must communicate it to the embedded App Studio App.

## DOMO INTERACTIONS

### Page filters

(and named filter views)

**Documentation:** [Applying Page-Level Filters (with_Filter_Views)](https://domohelp.domo.com/hc/en-us/articles/360042923914-Applying-Page-Level-Filters-with-Filter-Views-BETA-)

**Definition:** Top filter bar of embedded cards and dashboards similar to what is available in the full Domo instance

**Use Case:** Ad hoc filter creation by the user when the creator does not know all the slices the viewer might want to explore

**Note:** As emphasized in the layer sequence above, these lower priority filters can only return results within the subset of rows made available by PDP or Programmatic Filters.

![Filtering Options 8](https://web-assets.domo.com/blog/wp-content/uploads/2022/08/FilteringOptions8.png)

### Interaction filters across cards

**Documentation:** [Applying Card-to-Card Filters](https://domohelp.domo.com/hc/en-us/articles/360042923914-Applying-Page-Level-Filters-with-Filter-Views-BETA-#Applying_Card-to-Card_Filters)

**Definition:** Slicer cards similar to the cross-card interactions available in the full Domo instance

**Use Case:** These are the simplest filter interaction for viewers. They are ideal when the content creator already knows the filters will want

**Note:** As emphasized in the layer sequence above, these lower priority filters can only return results within the subset of rows made available by PDP or Programmatic Filters

![Filtering Options 9](https://web-assets.domo.com/blog/wp-content/uploads/2022/08/FilteringOptions9.png)
