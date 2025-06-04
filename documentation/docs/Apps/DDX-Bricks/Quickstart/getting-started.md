---
stoplight-id: ec60c4980e1b5
---

# Getting Started Using Domo Bricks

### Install a Domo Brick app
---
Go to the Domo Appstore and search for “ddx”

<img class="alignnone size-full" src="https://web-assets.domo.com/blog/wp-content/uploads/2021/07/DDX-AppstoreGallery.png" />
Click the app you like, then click “GET”

<img class="alignnone size-full" src="https://web-assets.domo.com/blog/wp-content/uploads/2021/07/DDX-AppstoreDetail.png" />
Choose the Dashboard you would like to install the app on from the drop down menu and click “Save”

<img class="alignnone size-full" src="https://web-assets.domo.com/blog/wp-content/uploads/2021/07/DDX-Appstore-AddTo.png" />
The Domo Brick app is now installed and ready for you to customize as needed.

### Edit and customize your app
---
After selecting “Edit Card” from the wrench menu, you can:
<ul>
 	<li>Change the datasets or columns the app is using</li>
 	<li>Change the style or colors through the CSS tab</li>
 	<li>Add a link or import your favorite JS framework on the HTML tab</li>
 	<li>Write your custom code on the JavaScript tab</li>
</ul>


### Things to remember
---
<ul>
 	<li>Only the person that installed the app is able to edit the app. You can use “Save as” to make your own copy.</li>
 	<li>You will need a token to use Google Maps or Mapbox.</li>
 	<li>Always be cautious when displaying user supplied or dataset data in HTML. See tips on sanitizing below.</li>
</ul>

### Import Libraries
---
#### Using a CDN (Content Delivery Network)
Use a CDN to pull in your favorite libraries and frameworks (jQuery, d3, Vega, Phoenix, etc.)
- <a href="https://cdnjs.com/" target="_blank" rel="noopener">https://cdnjs.com/</a>
- <a href="https://www.jsdelivr.com/" target="_blank" rel="noopener">https://www.jsdelivr.com/</a>

#### Using fonts
Using custom fonts in your app, by loading them in the HTML tab:

<img class="alignnone size-full" src="https://web-assets.domo.com/blog/wp-content/uploads/2021/07/DDXBricks-Install1.png" width="913" height="71" />

More info about using fonts from Google: <a href="https://developers.google.com/fonts/docs/getting_started" target="_blank" rel="noopener">https://developers.google.com/fonts/docs/getting_started</a>

#### Charting examples
<ul>
 	<li>Easy to use d3 examples can be found <a href="https://www.d3-graph-gallery.com/" target="_blank" rel="noopener">here</a>.</li>
 	<li>Vega chart examples can be found <a href="https://vega.github.io/vega/examples/" target="_blank" rel="noopener">here</a>.</li>
</ul>

### Sanitize Your Data
---
When you cannot 100% guarantee that the data you are working with is safe and that it will always be non-malicious in the future, you should take steps to first sanitize the data before you place it into HTML. You may consider doing something similar to the following to ensure the text you are displaying is safe to use:

```js
// Create a safe version of an input value before it is displated in HTML or stored to the database
// Transforms: "<h1>salt & pepper</h1>" => "&lt;h1&gt;salt &amp; pepper&lt/h1&gt;"
function makeSafeText (text){
   var element = document.createElement('div');
   element.innerText = text;
   return element.innerHTML;
}
```
Read more about sanitizing data here:
<ul>
 	<li><a href="https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Safely_inserting_external_content_into_a_page" target="_blank" rel="noopener">https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Safely_inserting_external_content_into_a_page</a></li>
 	<li><a href="https://owasp.org/www-community/xss-filter-evasion-cheatsheet" target="_blank" rel="noopener">https://owasp.org/www-community/xss-filter-evasion-cheatsheet</a></li>
</ul>


### Debug Your App
---
<ul>
 	<li>You can place a “debugger” line in your code to tell the browser “stop here”, when it gets to executing that line. See line 42 below for an example. This allows you to see what the variables have stored in them at that point in time.</li>
 	<li>You can also use a “console.log” to print out something to the console when it gets to executing the code at that line. An example is shown on line 44 below.</li>
</ul>

```js
41 domo.post('/sql/v1/dataset0' query, {contentType: 'text/plain'}).then(function(result) {
42   debugger;
43   var dataGrid = getDataGridFromQueryResult (result);
44   console.log(dataGrid);
45   chartIt (dataGrid);
46 });
```

### Get the Data
---
#### Method 1 – Using the SQL Endpoint
This method allows you to use traditional SQL to query. This method currently only returns an “array-of-arrays” (see output formats below):

``` text
var query = 'SELECT SUM(amount) as Sales FROM dataset0';
domo.post('/sql/v1/myDatasetAlias', query, {contentType: 'text/plain'}).then(function(result) { … });
```

To use a column name with spaces in your query, wrap the column name with back-ticks, for example:

``` text
var query = 'SELECT SUM(`Store Sales`) as Sales FROM dataset0';
```

#### Method 2 – Using the Data Endpoint

This is the traditional method for getting data out of Domo:

``` text
var query = `fields=amount&sum=amount`;
domo.get('/data/v1/myDatasetAlias?' + query).then(function(result) { … });
```

Here are some references and examples to get you started:

- [Data Queries example code](../../App-Framework/Guides/querying-data.md)
- [Data API deep dive](../../../Domo-App-APIs/Data-API.md)

#### Output formats
The default data endpoint output format may not always be the format you need. Supported formats are:
``` text
array-of-objects (default)
array-of-arrays
excel
csv
```

You can specify the format like this:

```text
domo.get('/data/v1/dataset?' + query, {format: 'csv'}).then(function(result) { … });
```


