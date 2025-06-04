# Analytics API

The following instructions will enable you to track user interactions and application events within a Domo app or brick. These functions send HTTP requests to a predefined analytics endpoint (/domo/analytics/v1), logging events such as filter changes, application loads, page views, or any user interaction. This enables real-time tracking of user behavior and app usage, which can help enhance the user experience and provide valuable data insights.

Each function makes use of the fetch API to send asynchronous POST requests, passing an authentication token (__RYUU_AUTHENTICATION_TOKEN__) in the headers to authorize each request. The functions are designed to be easily integrated into the application’s codebase, with simple, clearly defined parameters for each type of event.
<!-- theme: info -->


#### Authentication
To authenticate to this service you will need to include the token in your request as follows
```js
const token = window.__RYUU_AUTHENTICATION_TOKEN__;
```
Note: Authentication is handled automatically from within the context of a Domo Custom App when you use the `domo.post()` call.

Here are three common examples of events to track in your application.


<!-- theme: info -->
> #### One Analytics Dataset Per Domo Instance
>
> It's important to note that the analytics service only creates one Dataset (accessible by admins) for all Custom Apps across instances. To avoid hitting the column limit (1500) for this Dataset, it is best practice to **define your properties generically** and then use a DataFlow or Dataset View to isolate just the rows relevant to a particular app id.
> 
> Use property names: "Property 1", "Property 2", etc." to save any related metadata around an analytics call. See the examples defined below.


#### Report an App Load Code Example
```js
/**
 * Sends a request to log when the app is loaded.
 * 
 * This function should be called once each time the application starts up.
 * 
 * @param {string} locale - The location or language setting (e.g., "en-US") for the app load.
 * @returns {Promise<void>} Resolves when the request completes. Errors if the network request fails.
 *
 * @example
 * // Report that the app has loaded in the US English locale
 * reportAppLoad("en-US");
 */
export const reportAppLoad = function(locale) {
  const platform = window.navigator.platform;
  return fetch(`/domo/analytics/v1`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-DOMO-Ryuu-Token': token,
    },
    body: JSON.stringify({
      type: 'LOAD',
      properties: {
        'Property 1': 1,
        'Property 2': platform,
        'Property 3': locale,
      },
    }),
  })
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
  })
  .catch(error => {
    console.error('Failed to report app load:', error);
  });
};
```


#### Report a Page View Code Example
```js
/**
 * Sends a request to log a page view event.
 * 
 * Use this function to report each time a user views a new page within the app.
 * 
 * @param {string} page - The identifier or name of the page that was viewed.
 * @returns {Promise<void>} Resolves when the request completes. Errors if the network request fails.
 *
 * @example
 * // Report that the "Home" page was viewed
 * reportPageView("Home");
 */
export const reportPageView = function(page) {
  return fetch(`/domo/analytics/v1`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-DOMO-Ryuu-Token': token,
    },
    body: JSON.stringify({
      type: 'NAVIGATION',
      properties: {
        'Property 1': page,
      },
    }),
  })
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
  })
  .catch(error => {
    console.error('Failed to report page view:', error);
  });
};
```


#### Report an App Filter Change
```js
/**
 * Sends a request to log a filter change event.
 * 
 * Use this function to report when a filter in the application is modified.
 * 
 * @param {string} type - The type of filter that changed, e.g., "category" or "date".
 * @param {string|string[]} value - The new value(s) of the filter, as a single string or an array of strings.
 * @returns {Promise<void>} Resolves when the request completes. Errors if the network request fails.
 *
 * @example
 * // Report a single filter change
 * reportFilterChange("category", "Electronics");
 * 
 * // Report multiple filter changes
 * reportFilterChange("tags", ["sale", "new arrivals"]);
 */
export const reportFilterChange = function(filterType, filterValue) {
  return fetch(`/domo/analytics/v1`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-DOMO-Ryuu-Token': token,
    },
    body: JSON.stringify({
      type: 'ACTION',
      properties: {
        'Property 1': filterType,
        'Property 2': filterValue,
      },
    }),
  })
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
  })
  .catch(error => {
    console.error('Failed to report filter change:', error);
  });
};
```


### Customization
The examples above show how you can track predefined metrics, but if there is something custom you would like to track that can be done by modifying the `type` and `properties` values in the body of the request.

For example if I wanted to change an event type from `NAVIGATION` and `{pageViewed: page}` to something custom like `ACTION` and `{actionType: buttonClicked}` you would modify the body like this:
```
  body: JSON.stringify({
    type: 'ACTION',
    properties: {
      'Property 1': "buttonClicked",
      'Property 2': "custom value",
    },
  }),
```

### The Output Dataset

The output of these tracking events in your app will create a dataset in your Domo instance that you can then use for down stream reporting. This dataset will appear in your Domo datacenter and look something like the following:

<img width="925" alt="Screenshot 2024-11-14 at 1 12 14 PM" src="https://github.com/user-attachments/assets/dd7c6e61-4119-4fc1-a5b9-7159baab7514">


With this dataset you can build cards, alerts or ETL's like you can with with any other dataset in Domo.


### Conclusion
By integrating this module, teams can easily extend and customize event tracking as needed to capture additional insights or refine data collection, making this a versatile tool for Domo-based applications.
