---
stoplight-id: 2a14dd34496e7
---

# Handling Data Updates

This is an example of a simple app that leverages the `domo.onDataUpdate` function to manage how the app responds to updates made to the underlying dataset. Without this function, the app would be reloaded each time that underlying data was updated, which could lead to a bad user experience if the app refreshed in the middle of a user interaction. This is particularly painful with SPA apps where the user may have navigated to a sub route in the app and then get kicked back to the main route because the data refreshed.

### Getting Started
---
#### **Sample Data**

Load the contents of this [sample data](https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2017/06/27151228/galatic-sales-sample.csv) into a new Domo Webform and note the new ID.
 
#### **domo init**

Run the `domo init` command.

* design name: onDataUpdate
* select a starter: hello world
* would you like to connect to any datasets?: Yes
* dataset id: the Id of the dataset you just created
* dataset alias: sales
* add another dataset? No
 
#### **Update field mapping in manifest.json**

```json
{
  ...
  "fields": [
    { "alias": "name", "columnName": "Name" },
    { "alias": "email", "columnName": "Email" },
    { "alias": "total", "columnName": "Total" }
  ]
  ...
}
```
 
#### **index.html**

Replace the `index.html` content with the following:

```html
<html>
  <head>
    <link rel="stylesheet" href="app.css" />
  </head>
  <body>
    <h1>Handling Data</h1>

    <h2>Total Sales</h2>
    <div>$ <span id="total">0</span></div>

    <h4># Data Fetches</h4>
    <div id="updateCount">0</div>

    <!-- domo.js optional utils -->
    <script src="domo.js"></script>
    <script src="app.js"></script>
  </body>
</html>
```
 
#### **Publish**

Add a `thumbnail.png` and then publish your design.


### Development
---
Start the local development server: `domo dev`. We'll be making a few changes to the `app.js` file. Replace the current contents with the following:

```js
(function(domo){
  var COUNTER = 0;
  var TOTAL = 0;

  // main function to fetch data from domo
  function getData(alias) {
    COUNTER += 1;
    domo.get('/data/v1/' + alias + '?sum=total')
      .then(function(data) {
        TOTAL = data[0].total;
        updateUI();
      });
  }

  // add variables to UI
  function updateUI(){
    var totalEl = document.getElementById('total');
    var counterEl = document.getElementById('updateCount');

    totalEl.innerHTML = TOTAL.toString();
    counterEl.innerHTML = COUNTER.toString();
  }

  // initial fetch
  console.info('App Ready...');
  getData('sales');
})(domo);
```

In its current state, the `COUNTER` variable would never increment. It would always show as `1` because the app would always do a full refresh each time the data updated. Go ahead and try it. Publish the design in its current state, deploy a new app, and then in a new tab update a row in the Webform dataset.
 
#### Adding `domo.onDataUpdate()`

See how the app did a full page reload after the dataset was updated and the counter remained at `1`? Now we'll add an event listener to add more control over how our app behaves on data updates. Add the following function inside your script.

```js
domo.onDataUpdate(function(alias) {
  console.info('domo.onDataUpdate: ', new Date().getTime());
  getData(alias);
});
```

Publish again and now this time, each time you update the dataset your app should update the counter.