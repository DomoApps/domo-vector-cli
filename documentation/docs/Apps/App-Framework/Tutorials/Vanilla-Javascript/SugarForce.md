---
stoplight-id: a2bd06daaff7e
tags: [app platform]
---

# SugarForce

### Intro

---

This tutorial will walk you through building the “SugarForce” app. <span style="text-decoration: underline;">Before beginning make sure you've completed the [Quick Start](../../Quickstart/Prerequisites.md), which includes setup and installation and the prerequisites for building on the Domo App Platform.</span>

#### What we're building

We will go through how to create an app, get data to power it, visualize that data, use app development tools in the Domo platform, and publish an app. This example will help you understand the core elements of building apps in Domo that you can then take and apply to your own custom apps.

You can check out complete code examples of the SugarForce app **<a href="https://github.com/DomoApps/sugarforce">here**.</a>

<https://player.vimeo.com/video/430153930>

### Step 1: Create the App

---

#### Create a New App

Run the following commands from your command line to set up a new Domo App project.

<pre><code>domo init
</code></pre>

Name your design "SugarForce". You'll then be asked which starter kit to use. Choose `sugarforce`.

When asked to connect a dataset, select yes (`y`) and then paste the dataset ID from the previous step. Use "leads" for the dataset alias.

Finally, open the project directory in your favorite editor. You should now have a project with the following structure.

<pre><code>+ components
    - autocomplete.js
    - floatingactionbutton.js
    - modal.js
    - router.js
    - table.js
+ js
    - app.js
    - domo.js
    - domoPhoenixWithMaps.js
    - helpers.js
    - home.js
    - leads.js
    - opportunities.js
    - reports.js
+ styles
    - app.css
index.html
manifest.json
thumbnail.png
</code></pre>

#### Deploy for Testing

In order to test your app with the sample dataset you just created, you'll need to publish your app to your Domo instance. Publishing does not make your app public, it simply sets up the connections between your app, your Domo instance, and your data.

Publish your app by running the following

<pre><code>domo publish
</code></pre>

Once your app is published, you can run

<pre><code>domo dev
</code></pre>

to launch a hot-reloading preview of your app useful for seeing changes you make as you develop it. Let's use this to see changes we make to the code.

### Step 2: Connect to and Query Data in Domo

---

#### Connect Data in Domo

We’ll be using some sample data provided by Domo’s <a href="https://www.domo.com/appstore/connector/sample-data-connector/overview">Sample Data Connector</a>.

To make the sample data available to your app, you need to create the dataset in Domo using the Sample Data Connector.

<a href="https://www.domo.com/login?utmrefresh=1&amp;utm_source=Sample%20Data%20Connector&amp;utm_medium=domo&amp;utm_campaign=Appstore_domo_com.domo.connector.sampledata_connect&amp;utm_campid=701f2000001BwAIAA0">Click here</a> to create that dataset. You’ll select “SugarForce” as the datasource and “Leads” as the report. Select the default refresh schedule and give it a name.

Once your dataset is created, copy and save the dataset ID displayed in the URL as we’ll need this for the next section.

<img src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-setup-1.png" alt="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-setup-1.png" />

#### Get Data

To use data from Domo in your app, simply call the Domo Data API via the `domo` resource provided.

Open `leads.js` and look at the data query

<pre>
<code>domo.get('/data/v1/leads?limit=10')
    .then(function(leads){
      console.log("leads", leads);
    });
</code>
</pre>

Domo is getting the dataset we've aliased as `leads` in `manifest.json` and returning the last 10 rows. Click the "Leads" tab. You'll see the response output to `console.log` which is viewable by opening your developer console in your browser. If you're not familiar with the developer tools, this is where you can see console logs, errors in your code, and other useful things like network responses, etc. More information about Chrome developer tools <a href="https://developers.google.com/web/tools/chrome-devtools/open">can be found here</a> and Firefox developer tools <a href="https://developer.mozilla.org/en-US/docs/Tools/Web_Console">can be found here.</a>

<img src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-step-2-1.png" alt="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-step-2-1.png" />

#### Select Fields

Modify the data query by adding a `fields` parameter to the URL

<pre>
<code>domo.get('/data/v1/leads?fields=id,name,title,company_name,city,state&amp;limit=10')
    .then(function(leads){
      console.log("leads", leads);
    });
</code>
</pre>

This will limit the result set to the columns specified.

#### Draw a Table

Now that we have the data response the way we'd like from Domo, output the data to a table. For our example, you can just pass the response to `drawTable` and it does the work for you.

`drawTable` expects a data object (the response from the data query) and the ID of a table target to output to. Create the table target by appending the following to `leads.html`

<pre>
<code>&lt;table id="leads-table"&gt;&lt;/table&gt;
</code></pre>

Then update your code in `leads.js`

<pre>
<code>
domo.get('/data/v1/leads?fields=id,name,title,company_name,city,state&amp;limit=10')
    .then(data =&gt; drawTable(data, 'leads-table'));
</code>
</pre>

Now when you go to the "Leads" section, you should see the following

<img src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-step-2-2.png" alt="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-step-2-2.png" />

#### Additional resources

For more examples on how to create complex queries of your data refer to the [Data Queries samples guide](../../Guides/querying-data.md).

### Step 3: Visualize Data

---

To visualize data, you can use Domo’s charting library called Phoenix. Phoenix allows you to leverage all of Domo’s native chart types and add custom styles. If needed, you can check out Phoenix’s full documentation  <a href="https://domoapps.github.io/domo-phoenix/">here.</a>

#### Create a Map

The "Reports" page of SugarForce is where we'll add visualizations of our "Leads" data. This example helps you create a single visualization but you can always add more.

Open `reports.js` and add the following

<pre>
<code>domo.get('/data/v1/leads?filter=state in ["CA","OR","WA"]&amp;groupby=state&amp;unique=company_name')
    .then(resultSet =&gt; {
        const columns = [
          {
            type: DomoPhoenix.DATA_TYPE.STRING,
            name: 'State',
            mapping: DomoPhoenix.MAPPING.ITEM
          },
          {
            type: DomoPhoenix.DATA_TYPE.DOUBLE,
            name: 'Companies',
            mapping: DomoPhoenix.MAPPING.VALUE
          }
        ];

        const data = {
            columns: columns,
            rows: resultSet.map(row =&gt; [row.state, row.company_name])
        }

        const options = {
          width: 650,
          height: 400
        };

        const chart = new DomoPhoenix.Chart(DomoPhoenix.CHART_TYPE.MAP_UNITED_STATES, data, options);

        document.getElementById('map').appendChild(chart.canvas);

        chart.render();
    });
</code>
</pre>

You'll also need to add a target and header to `reports.html`. Append the following

<pre>
<code>&lt;h2&gt;Filtered Map of Pacific Territory&lt;/h2&gt;
&lt;div id="map"&gt;&lt;/div&gt;
</code></pre>

Let's take a moment to explain each part of that code.

<pre>
<code>
domo.get('/data/v1/leads?filter=state in ["CA","OR","WA"]&amp;groupby=state&amp;unique=company_name')
</code></pre>

We're already familiar with Domo's Data API. In the above example, we've added a filter to include only rows where the state is in California, Oregon, or Washington. We've also added a `groupby` to aggregate the data. By default, values that are not part of the grouping are counted. That is, `company_name` is a count of all `company_name`values <em>grouped by</em> `state`. Finally we added a `unique` parameter to make that count distinct.

<pre><code>const columns = [
  {
    type: DomoPhoenix.DATA_TYPE.STRING,
    name: 'State',
    mapping: DomoPhoenix.MAPPING.ITEM
  },
  {
    type: DomoPhoenix.DATA_TYPE.DOUBLE,
    name: 'Companies',
    mapping: DomoPhoenix.MAPPING.VALUE
  }
];
</code></pre>

Domo’s Phoenix charting library expects an explicit definition of columns. The `type` attribute uses one of Phoenix’s pre-defined data types. `name` is the identifier of the charted dimension. `mapping` is specific to the chart type used, and more details can be found in the <a href="https://domoapps.github.io/domo-phoenix/">official Phoenix documentation</a>.

<pre><code>const data = {
  columns: columns,
  rows: resultSet.map(row =&gt; [row.state, row.company_name])
}
</code></pre>

Phoenix expects chart data to be formatted as an object with two attributes, `columns`, and `rows`. `columns` is an array of columns as defined in the previous example. `rows` is an array of arrays, each representing a single row. The code example is simply converting our result set to the expected format.

<pre><code>const options = {
  width: 650,
  height: 400
};

const chart = new DomoPhoenix.Chart(DomoPhoenix.CHART_TYPE.MAP_UNITED_STATES, data, options);

document.getElementById('map').appendChild(chart.canvas);

chart.render();
</code></pre>

Chart options we'll look at a little in more detail in the next section, but can be used to customize the style of a chart. The `chart` variable is assigned a new instance of the Phoenix chart which is then rendered as a child of the element specified.

#### Customize Colors

You can customize chart colors to align with your brand. Let's use a different hue of blue.

In `reports.js`, replace

<pre><code>const options = {
  width: 650,
  height: 400
};
</code></pre>

with

<pre><code>const customColors = [
  '#002159',
  '#03449E',
  '#0967D2',
  '#47A3F3',
  '#BAE3FF'
];

const options = {
  width: 650,
  height: 400,
  colors: customColors
};
</code></pre>

Your final result should look like this:

<img src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-step-3-1.png" alt="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-step-3-1.png" />

### Step 4: Use AppDB for Data Storage

---

No need to stand up a database to store your app’s business logic. AppDB is a nosql database for storing arbitrary JSON documents and creating Domo DataSets from your application.

#### Define a Collection

If you're coming from a SQL background, think of collections like tables and documents like rows. We'll be creating a new collection and then creating documents in that collection.

We'll need to let users create Opportunities that we can associate with the Leads that we're getting from our Domo dataset. We'll start by deciding what attributes an Opportunity object will contain.

For our example, we'll create a very simple Opportunity object which will have an association to a lead, an amount, notes, and an attachment for uploading a sales order.

<pre><code>Company Name
Amount
Notes
Attachment
</code></pre>

Now we need to add a reference to the collection in our `manifest.json`. Add the following

<pre><code>"collections": [{
  "name": "opportunities"
}],
</code></pre>

Your `manifest.json` will look something like the following

<pre><code>{
  "name": "SugarForce",
  "version": "0.1.0",
  "size": {
    "width": 5,
    "height": 3
  },
  "collections": [{
    "name": "opportunities"
  }],
  "mapping": [
    {
      "dataSetId": "d6906ec6-9a23-40d2-b93c-7bb53f231bce",
      "alias": "leads",
      "fields": []
    }
  ],
  "fileName": "manifest.json",
  "id": "15e5a077-22df-4228-b232-d71dd631394c"
}
</code></pre>

#### Set Up Your Proxy

You'll be making advanced requests to use AppDB, so in order to make these requests in your development environment, you'll need to publish your app in your Domo instance and use the published version as a proxy.

Publish your current work by closing your dev server and publishing your app. (Use CTRL+C to stop your dev server).
Use `domo publish`, which returns a URL which is where you can view your design in Domo.

<img src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-step-4-1.png" alt="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-step-4-1.png" />

You can also find these designs by going to the “Asset Library” from your “More” menu

<img src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-step-4-2.png" alt="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-step-4-2.png" />

From your Asset Library, you can now find and instantiate your app design as a card. Click on the “New Card” button for SugarForce.

<img src="https://web-assets.domo.com/blog/wp-content/uploads/2022/06/Sugarforce-New-1.png" alt="https://web-assets.domo.com/blog/wp-content/uploads/2022/06/Sugarforce-New-1.png" />

You’ll be taken to a screen where you can name your card and wire up data. Give your card a new name up top then click on the Collections tab in the bottom left (it’ll have a red dot next to it).

<img src="https://web-assets.domo.com/blog/wp-content/uploads/2022/06/Sugarforce-New-2.png" alt="https://web-assets.domo.com/blog/wp-content/uploads/2022/06/Sugarforce-New-2.png" />

After clicking the Collections tab look for the “Automatically create un-configured collections with app defaults” toggle and click that to enable it.

<img src="https://web-assets.domo.com/blog/wp-content/uploads/2022/06/Sugarforce-New-3.png" alt="https://web-assets.domo.com/blog/wp-content/uploads/2022/06/Sugarforce-New-3.png" />

After enabling that toggle click “SAVE & FINISH” in the top right.

When the page refreshes, you'll see your app displayed on a page. You need to copy the app ID from the iframe source URL. It will be of the form XXXXXXXX-XXXX-4XXX-XXXX-XXXXXXXXXXXX. To find the ID:

<ul>
 	<li>Right-click anywhere in the card and choose "View Frame source"</li>
 	<li>When the frame source opens in a new tab, the URL should be of the form ...//{HASH}.domoapps.prodX.domo.com?userId=...</li>
 	<li>Copy the ID found between // and .domoapps. That is your app's ID.</li>
</ul>
<img src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-step-4-5.png" alt="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-step-4-5.png" />

<!-- theme: warning -->

> #### WARNING!
>
> App IDs are associated to cards. If you delete the card from which you retrieved the appContextId, you will have to get a new one from another card created from your app design.

Now add this to your `manifest.json`

<pre><code>"proxyId": "024071f5-f67e-4e0a-9caa-2b1f5d74da91",
</code></pre>

Your entire manifest file will look like this

<pre><code>{
  "name": "SugarForce",
  "version": "0.1.0",
  "size": {
    "width": 5,
    "height": 3
  },
  "collections": [{
    "name": "opportunities"
  }],
  "mapping": [
    {
      "dataSetId": "d6906ec6-9a23-40d2-b93c-7bb53f231bce",
      "alias": "leads",
      "fields": []
    }
  ],
  "fileName": "manifest.json",
  "proxyId": "426b5c72-4829-4ed6-8d8b-5bbf19d29734",
  "id": "15e5a077-22df-4228-b232-d71dd631394c"
}
</code></pre>

#### Create a Document</h3>

Now we're ready to create a new document.

Open `opportunities.js` and add the following

<pre><code>function getOpportunities() {
  domo.get(`/domo/datastores/v1/collections/opportunities/documents/`)
    .then(opportunities =&gt; {

      const rows = opportunities.map(opportunity =&gt; ({id: opportunity.id, ...opportunity.content}));

      const options = {
        editable: true,
        action: updateOpportunity
      };

      drawTable(rows, 'opportunities-table', options)
    });
}

function updateOpportunity(id, document) {
  domo.put(`/domo/datastores/v1/collections/opportunities/documents/${id}`, { content: document })
    .then(getOpportunities);
}

function createOpportunity(document) {
  domo.post(`/domo/datastores/v1/collections/opportunities/documents/`, { content: document })
    .then(getOpportunities);
}
</code></pre>

These functions get, update, and create opportunities respectively. Each function sends a request to the AppDB API and then uses a callback to handle the response. The `getOpportunities` callback is a function that first transforms the data returned from AppDB into rows we can use to populate our table, and then sets the objects to be editable and defines what function to use to edit an opportunity. Finally it renders the table to a table element with the ID `opportunities-table`. Let's add that to `opportunities.html` now by appending the following

<pre><code>&lt;table id="opportunities-table"&gt;&lt;/table&gt;
</code></pre>

We need to create some content in AppDB and then render it.

We'll be calling `createOpportunity` with data (a document).

To test this, let's add the following to `opportunities.js`

<pre><code>createOpportunity({
  company_name: 'ABC Company',
  amount: 100000,
  notes: "We spoke to the CEO and she's really interested"
})
</code></pre>

Notice that we've excluded an attachment as we'll test that later.

Now load the page on our dev server (run by executing `domo dev` in the command line).

#### Use a Form

Prepare to use a form by thinking about how to simplify user input. Try to minimize manual input. Instead of making users type the company name associated to an opportunity manually, give them a dropdown list of options from the `Leads` dataset already stored in Domo. Add the following to `opportunities.js`

<pre><code>function getLeads() {
  return domo.get(`/data/v1/leads?fields=company_name&amp;groupby=company_name`);
}
</code></pre>

This code should look familiar. We are querying our leads dataset and getting a list of distinct company names from which users can select.

Now let's create our form. We'll use some components included in your template. Replace

<pre><code>createOpportunity({
  company_name: 'ABC Company',
  amount: 100000,
  notes: "We spoke to the CEO and she's really interested"
})
</code></pre>

with the following in `opportunities.js`

<pre><code>(function() {

  const opportunity = {
    company_name: new AutoComplete(getLeads),
    amount: 0,
    notes: ''
  };

  addButton(opportunity, createOpportunity)

  getOpportunities();

})();
</code></pre>

This code defines how the opportunities will be displayed in the form and adds a button to the bottom-right corner which opens the form. Finally it triggers `getOpportunities` when the page loads.

<img src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-Step4-7.png" alt="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-Step4-7.png" />

#### Additional Resources</strong>

For additional information on using AppDB, refer to the [AppDB API Reference Guide](../../../../Domo-App-APIs/AppDB-API.md).

### Step 5: Working with Files

---

#### Leverage Files API

The [Files API](../../../../Domo-App-APIs/Files-API.md) gives you the ability to handle files in a Domo app. Let users upload a file by adding the following to `opportunities.js`

<pre><code>functionuploadFile(file) {
  const formData =new FormData();
  formData.append('file', file);
  const options = { contentType: 'multipart' };
  return domo.post(`/domo/data-files/v1?name=${file.name}`, formData, options);
}
</code></pre>

In this example, the [Files API](../../../../Domo-App-APIs/Files-API.md) is receiving a multipart upload based on the File object passed in as the argument `file`. It will return a promise that yields a file ID which we'll store in AppDB to access these attachments later.

Example response:

<pre><code>HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8

{
    "dataFileId": 1234
}
</code></pre>

Also add this to your form by replacing

<pre><code>const opportunity = {
    company_name:new AutoComplete(getLeads),
    amount: 0,
    notes: ''
  };
</code></pre>

with

<pre><code>const opportunity = {
    company_name:new AutoComplete(getLeads),
    amount: 0,
    notes: '',
    attachment:new FileUpload(uploadFile)
  };
</code></pre>

Your form now allows you to add attachments to Opportunities. Those files will be stored in Domo and can be accessed by your app with a specific URL. This URL is stored in AppDB along with the rest of the Opportunity data.

<img src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-step-5-1.png" alt="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-step-5-1.png" />

<img src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-step-5-2.png" alt="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-step-5-2.png" />

### Publish and Share

---

We publish our final product to Domo using

<pre><code>domo publish
</code></pre>

Once your app is deployed as a card, you can share it like you would any other content in Domo. Congratulations on building your first Domo app! Don't step here! Keep building.
