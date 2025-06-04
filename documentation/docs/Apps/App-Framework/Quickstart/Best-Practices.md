---
stoplight-id: 9l1mzcir4ht5h
---

# Best Practices

#### Use Only the Data You Need
---
Some DataSets are massive and will bring any web browser to its knees if you try to load the entire thing. To keep your app performing optimally, take advantage of limits, aggregations, and row filtering to bring down just the data your app needs. Do not include all columns in your data mapping file, just the ones you need.

#### Make Your App Responsive
---
You want your app to look great no matter where it is rendered. Use the principles of responsive design so that your app displays perfectly whether it is rendered small on a mobile device, large on a details page, etc.

#### Be a Good Citizen
---
Because you are creating a custom app from web tech, you need to ensure that your users have a quality user experience. Consider the following during development to optimize that experience:

* Test for browser compatibility.
* Consider how the app will appear on mobile devices, and design accordingly.
* Only request the data you want to visualize. Remember your code is being run in a browser, so if you request a significant amount of data, your app will be slow and could freeze the browser. Be sure to aggregate and filter the data so you only get what you need. For example, you don’t need to visualize millions of points of data as individual elements; instead, you should aggregate it.
* Similarly, perform as much logic as possible on the server via queries (and ETL). There is no reason to calculate a sum or average client-side.
* Test your app’s performance. Be aware of code load times, memory requirements, and the performance of your code.
* Only pull in the assets your app absolutely needs.

#### Use a Bundler Tool
---
Your app size can be significantly reduced if you use a bundler tool like Webpack. Webpack is ideal because of its small runtime and developer productivity.

