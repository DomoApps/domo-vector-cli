---
stoplight-id: n4pswi7dd2azo
---

# Moving from Brick to App

We're going to be migrating the Domo Brick that [we built in part one](intro-to-bricks.md) into a full custom application. In particular, this part will highlight some of the capabilities that moving from bricks to apps will unlock, especially around leveraging AppDB and handling CRUD functionality.

### Key steps and learning objectives
---
1. Initializing a Domo App
2. Configuring the `manifest.json` file and publishing Domo Apps (`domo publish`)
3. Developing Apps Locally (`domo dev`)
4. Migrating our Domo Brick Code
5. Configuring our AppDB collection
6. Writing data to AppDB
7. Displaying data from AppDB


### Initializing a Domo App
---

You should already have the `Domo Apps CLI` and a VS Code editor installed on your machine. To verify that you have it installed, please:

1. open VS Code
2. open a Terminal window (`Command-J` on Mac)
3. type the command `domo` in the Terminal and press Enter

You should see a list of all the available commands in the Domo Apps CLI.

![Screenshot 2024-03-22 at 5.52.48 PM.png](../../assets/images/Screenshot%202024-03-22%20at%205.52.48%20PM.png)

To initialize a new Domo App, you can use the `domo init` command. A wizard should walk you through the following steps. Please:

1. Give your App Design a unique name - mine is `GameNightPlannerNF`
2. Select the `hello world` starter template
3. Don't connect any datasets for now (type `n`)


![Screenshot 2024-03-22 at 5.57.51 PM.png](../../assets/images/Screenshot%202024-03-22%20at%205.57.51%20PM.png)

You should see that the `domo init` command has successfully created the initial app files you'll need.

Next, you'll want to navigate to the directory where these new app files live. You can navigate to "Open Folder" in VS Code and find the directory where the App was newly created. For me it is the `GameNightPlannerNF` directory.

![Screenshot 2024-03-22 at 6.00.22 PM.png](../../assets/images/Screenshot%202024-03-22%20at%206.00.22%20PM.png)

You should see 5 files now in VS Code. They should look very familiar to the files you start with in a Domo Brick.

![Screenshot 2024-03-22 at 6.01.37 PM.png](../../assets/images/Screenshot%202024-03-22%20at%206.01.37%20PM.png)

Let's explore these files briefly.

- `index.html`: this is the main file in your app - comparable to the HTML file in the Domo Bricks Editor. Notice the starter code in this file includes links to the `app.css`, `domo.js`, and `app.js` files.

```html
<html>
  <head>
    <link rel="stylesheet" href="app.css" />
  </head>
  <body>
    <h1>GameNightPlannerNF</h1>
    <!-- domo.js optional utils -->
    <script src="domo.js"></script>
    <script src="app.js"></script>
  </body>
</html>

```

Bricks handle this file linkage in the background so this is one of the first big differences. Exposing this flexibility to you means that you can add more files in your directory and load them into `index.html`

- `domo.js` - this is the preloaded `domo.js` library, which is analogous to the `var domo = window.domo;` global variable found in Domo Bricks. You don't need to worry about the contents of this file - just know you can use the same `domo` global variable without pulling it off the `window`.
- `app.css` - analogous to the CSS file in bricks
- `app.js`- analogous to the JS file in bricks
- `manifest.json` - the key configuration file that give you control over the "Brick Template" and resources in Domo you want your App to leverage. (More on this in a minute).

Now that we have our bearings, we can see that there isn't that much of a difference between the hello world starter app template and our Bricks files.

The major difference is that we have access to the `manifest.json` file that defines all the configuration options for our Domo App.


### Configuring the `manifest.json` file and publishing Domo Apps (`domo publish`)
---

Open up the `manifest.json` file and have a quick look at what we're starting with.

```json
{
  "name": "[YOUR_APP_DESIGN_NAME]",
  "version": "1.0.0",
  "size": {
    "width": 1,
    "height": 1
  },
  "mapping": [
    
  ]
}
```

It's pretty bare bones initially. We have the `name` of our App Design (think Brick Template), the `version` number of our App Design, the default size of cards built from our App Design, and an empty `mapping` array. This `mapping` object will let us define which Datasets we want to connect to our app as well as what  `alias` they use.

Let's leave this blank for now and just publish the very bare-bones version of our Hello World app.

#### Domo Login

First, make sure you are authenticated against the Domo instance. To do this open up your Terminal in VS Code again and type the command `domo login`

Select `new instance` and type in the url of the Domo instance you are developing against. In my case, it's `domo-training-apps.domo.com`.

![Screenshot 2024-03-22 at 7.03.11 PM.png](../../assets/images/Screenshot%202024-03-22%20at%207.03.11%20PM.png)

This command should launch a window in your browser to authenticate against our training Domo instance.

![Screenshot 2024-03-22 at 7.04.25 PM.png](../../assets/images/Screenshot%202024-03-22%20at%207.04.25%20PM.png)

Your terminal should include this welcome message: 

![Screenshot 2024-03-22 at 7.05.07 PM.png](../../assets/images/Screenshot%202024-03-22%20at%207.05.07%20PM.png)

Now that we've made the connection between our command line and our Domo instance, we can publish the first version of our App.

#### Domo Publish

Type the command `domo publish` in your Terminal. You should see an `id` property get automatically added in your `manifest.json` file. This `id` corresponds to the App Design now published in your Domo instance.

```json
{
  "name": "[YOUR_APP_DESIGN_NAME]",
  "version": "1.0.0",
  "size": {
    "width": 1,
    "height": 1
  },
  "mapping": [],
  "fileName": "manifest.json",
  "id": "[YOUR_APP_DESIGN_ID]"
}
```

In our Terminal output we should see that our App Design has been successfully published to Domo, but there is a warning message about a missing `thumbnail.png` file.

![Screenshot 2024-03-22 at 7.08.51 PM.png](../../assets/images/Screenshot%202024-03-22%20at%207.08.51%20PM.png)

Domo requires a `thumbnail.png` file to display as an icon for your App. Go ahead and take a moment to pick any image you'd like to use as an icon and drag it into your App directory and name it `thumbnail.png`. I'll be using this chatGPT generated image - feel free to use it as well if you'd like.

![thumbnail.png](../../assets/images/thumbnail.png)

Now go ahead and run the `domo publish` command one more time.

![Screenshot 2024-03-22 at 7.14.03 PM.png](../../assets/images/Screenshot%202024-03-22%20at%207.14.03%20PM.png)

Click on the link in the Terminal output to locate your App Design in Domo. You should be taken to a page like this one:

![Screenshot 2024-03-22 at 7.14.44 PM.png](../../assets/images/Screenshot%202024-03-22%20at%207.14.44%20PM.png)

App Designs are really just the template for an App Instance (or "Card" in Domo terminology). Let's go ahead a click "Create New Card" to create our first App Instance.

![Screenshot 2024-03-22 at 7.16.10 PM.png](../../assets/images/Screenshot%202024-03-22%20at%207.16.10%20PM.png)

Notice, this looks a lot like the Brick Editor screen, but much more bare-bones. With custom Apps, we have control over the options displayed on this screen.

Click "Save and Finish" and move the new card to your Dashboard.

#### Configuring `manifest.json` to wire up Datasets

Let's setup our App to connect to our Board Games Dataset by default.

Update your `manifest.json` so that the `mapping` list looks like the following.

```json
{
  "name": "[YOUR_APP_DESIGN_NAME]",
  "version": "1.0.0",
  "size": {
    "width": 1,
    "height": 1
  },
  "mapping": [
    {
      "alias": "boardgames",
      "dataSetId": "0e0c22d9-72f9-4115-81cf-a090b9645e65",
      "fields": []
    }
  ],
  "fileName": "manifest.json",
  "id": "[YOUR_APP_DESIGN_ID]"
}

```

Run `domo publish` again and you should see a big difference on the Wiring Screen of your App. Click "Edit Card" for the "App Instance" (aka card) you created a moment ago.

![Screenshot 2024-03-22 at 7.27.05 PM.png](../../assets/images/Screenshot%202024-03-22%20at%207.27.05%20PM.png)

Notice, you now have a single Dataset connected to your App with the alias `boardgames` and the default Dataset for your card is tied to the Dataset we would expect. You can swap this Dataset out just like you would in a Brick if you want to power this App Instance with different data.

![Screenshot 2024-03-22 at 7.28.47 PM.png](../../assets/images/Screenshot%202024-03-22%20at%207.28.47%20PM.png)

### Developing Apps Locally (`domo dev`)
---

Now that we have the minimum setup required to recreate our brick, let's start developing!

Back in your Terminal, go ahead and type the `domo dev` command. This will launch a hot-reloading local server so you can develop your App locally and only publish to Domo when you're ready to either overwrite the existing version of an App or publish to a new version.

![Screenshot 2024-03-22 at 7.31.42 PM.png](../../assets/images/Screenshot%202024-03-22%20at%207.31.42%20PM.png)

Your App is now running locally!

![Screenshot 2024-03-22 at 7.32.21 PM.png](../../assets/images/Screenshot%202024-03-22%20at%207.32.21%20PM.png)

Let's change the title of the App so you can see what happens in your local server.
Update your `index.html` file with a new title.

```html
<html>
  <head>
    <link rel="stylesheet" href="app.css" />
  </head>
  <body>
    <h1>Game Night Planner</h1>
    <!-- domo.js optional utils -->
    <script src="domo.js"></script>
    <script src="app.js"></script>
  </body>
</html>

```

Save the file -- and look at localhost:3000 in your browser.

![Screenshot 2024-03-22 at 7.34.32 PM.png](../../assets/images/Screenshot%202024-03-22%20at%207.34.32%20PM.png)

Your title should have changed.

### Migrating our Domo Brick Code
---

Our App is still pretty boring. Just a lonely `<h1>`. Let's copy the code that we had in our brick from earlier with only very minor changes.

Our HTML code, can be copied in our `index.html` file. Your updated `index.html` file should look like this:

```html
<html>
  <head>
    <link href="https://cdn.jsdelivr.net/npm/tabulator-tables@6.0.1/dist/css/tabulator.min.css" rel="stylesheet">
    <link rel="stylesheet" href="app.css" />
  </head>
  <body>
    <h1>Game Night Planner</h1>
    <div id="tabulator-table"></div>
    

    <!-- domo.js optional utils -->
    <script src="domo.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/tabulator-tables@6.0.1/dist/js/tabulator.min.js"></script>
    <script src="app.js"></script>
  </body>
</html>

```

Next, replace the entire `app.css` file with the CSS from your brick code.

```css
/*Theme the Tabulator element*/
#tabulator-table{
  background-color:#888888;
  border: 1px solid #333;
  border-radius: 10px;
}

/*Theme the header*/
#tabulator-table .tabulator-header {
  background-color:#99CCEE;
  color:#555555;
}

#tabulator-table .tabulator-col {
  background-color:#99CCEE;
}


/*Allow column header names to wrap lines*/
#etabulator-table .tabulator-header .tabulator-col,
#tabulator-table .tabulator-header .tabulator-col-row-handle {
  white-space: normal;
}

/*Color the table rows*/
#tabulator-table .tabulator-tableholder .tabulator-table .tabulator-row{
  color:#fff;
  background-color: #666;
}

/*Color even rows*/
#tabulator-table .tabulator-tableholder .tabulator-table .tabulator-row:nth-child(even) {
  background-color: #555555;
}

```

You can also copy your JS code into `app.js` however a couple minor changes are required.

- You no longer need to load in the `domo.js` library since that's covered by the script tag in the `index.html` file.
- The `datasets` alias array is now based on what you defined in your manifest. So I've set `var datasets = ['boardgames']` to match the alias we gave our dataset.


Everything else can remain the same.

```js 
var datasets = ['boardgames'];

// Query your dataset(s): https://developer.domo.com/docs/dev-studio-references/data-api
var fields = [];
var groupby = [];
var query = `/data/v1/${datasets[0]}?fields=${fields.join()}&groupby=${groupby.join()}`;
domo.get(query).then(handleResult);



//Step 3. Do something with the data from the query result
function handleResult(data){
  console && console.log(data);

  var table = new Tabulator("#tabulator-table", {
      data:data,
      columns:[
          {title:"Ranking", field:"Board Game Rank"},
          {title:"Image", field:"thumbnail", formatter: "image"},
          {title:"Name", field:"primary", headerFilter:"input"},
          {title:"Description", field:"description", headerFilter:"input"},
          {title:"Stars", field:"average", formatter: "star"},
          {title:"Own", field:"owned", hozAlign:"center", editor:true, formatter:"tickCross"},

      ],
      layout:"fitColumns",
      pagination:"local",
      paginationSize:10,
      paginationSizeSelector:[10, 25, 50, 100],
  });
}

```

Now check out localhost again.

![Screenshot 2024-03-22 at 7.47.25 PM.png](../../assets/images/Screenshot%202024-03-22%20at%207.47.25%20PM.png)

Only thing is that it looks a bit too small. Adjust the size property in your `manifest.json` file to be 6x6 instead of 1x1.

```json
"size": {
    "width": 6,
    "height": 6
  },
```

Quit your local server and restart it to apply the changes from the `manifest.json` file. 
- `ctrl-C` in your Terminal
- `domo dev` again.

![Screenshot 2024-03-22 at 7.49.42 PM.png](../../assets/images/Screenshot%202024-03-22%20at%207.49.42%20PM.png)

There we go! Much nicer. `domo publish` again -- and we've successfully converted our brick to an App. Now the fun can begin!

### Configuring our new AppDB collection
---

Configuring a new AppDB collection is just like configuring a Dataset in an App. For our AppDB collection, we just want to be able to track whether the currently signed-in user has marked a given row as "Owned" or not. 

This will allow our users to track which games they currently own, which will help them plan a successful game night. Can't plan a game night if you don't know which games you can play!

We'll define a new `ownership` AppDB collection so that each document in the collection has a property for `boardGameId` and `owned`. 

To do that, we add a `collections` list to the `manifest.json` file.

```json
{
  "name": "[YOUR_APP_DESIGN_NAME]",
  "version": "1.0.0",
  "size": {
    "width": 6,
    "height": 6
  },
  "mapping": [
    {
      "alias": "boardgames",
      "dataSetId": "0e0c22d9-72f9-4115-81cf-a090b9645e65",
      "fields": []
    }
  ],
  "collections": [
    {
      "name": "ownership",
      "schema": {"columns": 
            [{"name": "boardGameId", "type": "LONG"}, 
              {"name": "owned", "type": "STRING"}]
        },
      "syncEnabled": true
    }
  ],
  "fileName": "manifest.json",
  "id": "[YOUR_APP_DESIGN_ID]"
}
```

The `syncEnabled` property tells Domo that we want the data in our AppDB collection automatically synced to a new Domo Dataset.

Once you've updated your `manifest.json` file, run the `domo publish` command again.

Open up your App's card to see the updated Wiring Screen. Notice a new tab on the left

![Screenshot 2024-03-22 at 8.02.59 PM.png](../../assets/images/Screenshot%202024-03-22%20at%208.02.59%20PM.png)

Click on it and you should see an empty array and some additional information about your new AppDB collection in the wiring screen.

![Screenshot 2024-03-22 at 8.03.54 PM.png](../../assets/images/Screenshot%202024-03-22%20at%208.03.54%20PM.png)

One last thing we need to do so that we can develop against our new collection locally is to add a `proxyId` to our `manifest.json` file. This `proxyId` corresponds to the App Card and can be found by:

- Go to the "Asset Library" under the "More" menu in Domo.
![Screenshot 2024-03-22 at 8.17.05 PM.png](../../assets/images/Screenshot%202024-03-22%20at%208.17.05%20PM.png)

- Click on the App Design for your App
 ![Screenshot 2024-03-22 at 8.17.35 PM.png](../../assets/images/Screenshot%202024-03-22%20at%208.17.35%20PM.png)

- Navigate to "Cards"
![Screenshot 2024-03-22 at 8.18.20 PM.png](../../assets/images/Screenshot%202024-03-22%20at%208.18.20%20PM.png)
- Copy the "Proxy Id" listed for you card.

- Add it to your `manifest.json` file.


```json
{
  ...
  "fileName": "manifest.json",
  "id": "[YOUR_APP_DESIGN_ID]",
  "proxyId": "[YOUR_PROXY_ID]"
}
```

We're now ready to actually write data to our collection.


### Writing data to AppDB
---

Remember when we click the editable field in our Tabulator table, nothing persists. We'll now just need to hook up that click action to write a new document in our AppDB collection if one doesn't exist for that board game yet, or update a document if one does.

To do that, we'll leverage Tabulator callback functions in conjunction with the [AppDB API](https://developer.domo.com/portal/1l1fm2g0sfm69-app-db-api).

In the [documentation for Editable Data](https://tabulator.info/examples/6.0#editable), Tabulator notes that any time a cell is edited the `cellEdited` callback function is called. We'll want to sync this up with AppDB.

#### Create new AppDB Document

First lets just get something to print in the console to verify that the callback is triggering as expected.

Update the table configuration to add the `cellEdited` callback function for the `own` column. 

```js
var table = new Tabulator("#tabulator-table", {
      data:data,
      columns:[
          {title:"Ranking", field:"Board Game Rank"},
          {title:"Image", field:"thumbnail", formatter: "image"},
          {title:"Name", field:"primary", headerFilter:"input"},
          {title:"Description", field:"description", headerFilter:"input"},
          {title:"Stars", field:"average", formatter: "star"},
          {title:"Own", field:"owned", hozAlign:"center", editor: true, cellEdited: handleCellEdited, formatter:"tickCross"},

      ],
      layout:"fitColumns",
      pagination:"local",
      paginationSize:10,
      paginationSizeSelector:[10, 25, 50, 100],
  });
  ```
Then just define the callback function - in this case I've called it `handleCellEdited`.

```js
const handleCellEdited = (cell) => {

    const rowData = cell._cell.row.data;
    const boardGameId = rowData.id;
    const ownedValue = rowData.owned;
    console.log("cell edited")
    console.log(rowData);
    debugger;
}
```
I've added a debugger statement to make it easier to see exactly what data we have access to when the handleCellEdited callback function runs.

In localhost, you should see something like this when you try to edit the `own` field now.

![Screenshot 2024-03-22 at 8.34.31 PM.png](../../assets/images/Screenshot%202024-03-22%20at%208.34.31%20PM.png)

We now have access to the `boardGameId` for the row we clicked on and the value for game ownership.

Next we want to write this data to AppDB.

Update the `handleCellEdited` callback to create a new AppDB document on edit.

```js
const handleCellEdited = (cell) => {

    const rowData = cell._cell.row.data;
    const boardGameId = rowData.id;
    const ownedValue = rowData.owned;

    const document = {
        "content": {
            "boardGameId": boardGameId,
            "owned": ownedValue
        }
    }

    domo.post(`/domo/datastores/v1/collections/ownership/documents/`, document)
    .then(data => console.log(data));
}
```

This code is creating a new document with the properties we defined in our `manifest.json` file and making a POST request to the `ownership` collection.

Now try editing a record in your localhost environment. If successful, you'll see the AppDB document that you just created print to the console.


![Screenshot 2024-03-22 at 9.03.43 PM.png](../../assets/images/Screenshot%202024-03-22%20at%209.03.43%20PM.png)

Even better, if you go check the Wiring Screen of your App in Domo you should be able to see the data in the AppDB collection.

![Screenshot 2024-03-22 at 9.05.01 PM.png](../../assets/images/Screenshot%202024-03-22%20at%209.05.01%20PM.png)

Note that AppDB tracks metadata on every request including the users Domo id (`owner`), which we'll be able to use to personalize our table based on who is looking at it.

#### Implement Update or Create Logic

While we now have a way to store whether a user owns a particular board game, we still need to handle the case where a document in AppDB for a given user and board game already exist. If it does, we just want to update the record rather than create a new one...otherwise we could end up with a lot of duplicate AppDB documents.

Update your `handleCellEdited` callback function to handle this case.


```js
const handleCellEdited = async (cell) => {
    const collectionAlias = 'ownership';

    const rowData = cell._cell.row.data;
    const boardGameId = rowData.id;
    const ownedValue = rowData.owned;
    const userId = domo.env.userId;

    // check if a document already exists in AppDB for the current user and board game.

    const appDBQuery = `{
        "owner": {
            "$eq": ${userId}
        },
        "content.boardGameId": {
            "$eq": ${boardGameId}
        }
    }`


    const existingAppDBDocument = await domo.post(`/domo/datastores/v1/collections/${collectionAlias}/documents/query`, appDBQuery)

    const document = {
        "content": {
            "boardGameId": boardGameId,
            "owned": ownedValue
        }
    }
    
    if (existingAppDBDocument.length > 0) {
        // update existing document
        const existingDocumentId = existingAppDBDocument[0].id;
        const updatedDocument = await domo.put(`/domo/datastores/v1/collections/${collectionAlias}/documents/${existingDocumentId}`, document)
        console.log("updatedDocument", updatedDocument);
        

    } else {
        // create new document
        const newDocument = await domo.post(`/domo/datastores/v1/collections/${collectionAlias}/documents/`, document);
        console.log("newDocument", newDocument);
    }
}
```

Now as you start to check the owned field in the table for each row, it should create a new document only when one doesn't already exist.

There is still some best practice clean up to do to handle error cases (when any request to AppDB fails, but we'll leave that as a challenge).

You can `domo publish` to push your most recent changes to Domo.

Go ahead and click a few. You can even share your App card with your neighbor to confirm that new documents get created on a per-user basis.

I can see in AppDB Admin, that I've successfully tracked ownership for 5 of my favorite games.

![Screenshot 2024-03-22 at 9.31.26 PM.png](../../assets/images/Screenshot%202024-03-22%20at%209.31.26%20PM.png)


### Displaying data from AppDB
---

There's at least one thing still missing from our App to complete the data collection functionality. We aren't displaying the stored values in our Tabulator table.

To do that, we'll need to fetch all the AppDB documents for the current user and join them by boardGameId on the client-side before rendering the table.

Here's how we can do that. Let's refactor our code a bit to be more reusable.
- Create a new function`fetchData` where we'll fetch data from both the Dataset and our AppDB collection. 
- Before handling results and rendering the table, merge AppDB collection data with Dataset on `boardGameId`
- Call the `fetchData` function when the `<body>` of our app loads.

Your `app.js` file should now look like this:

```js
var datasets = ['boardgames'];
const collectionAlias = 'ownership';
const userId = domo.env.userId;

async function fetchData() {
    console.log("fetching data");
    // Query your dataset(s): https://developer.domo.com/docs/dev-studio-references/data-api
    const boardGameDataQuery = `/data/v1/${datasets[0]}`;
    const boardGameOwnershipDataQuery = {
        "owner": {
            "$eq": userId
        }
    }

    const boardGameData = await domo.get(boardGameDataQuery);
    const boardGameOwnershipData = await domo.post(`/domo/datastores/v1/collections/${collectionAlias}/documents/query`, boardGameOwnershipDataQuery)

    const data = mergeGameData(boardGameData, boardGameOwnershipData);

    handleResult(data);

}

function mergeGameData(inputData, mergeList) {
    // Step 1: Add an 'owner' field to every item in inputData, defaulting to false
    inputData.forEach(item => {
        item.owned = false;
    });

    // Step 2: Create a mapping from boardGameId to 'owned' status from the mergeList
    const ownershipMap = mergeList.reduce((acc, cur) => {
        const boardGameId = cur.content.boardGameId;
        const ownedStatus = cur.content.owned;
        acc[boardGameId] = ownedStatus;
        return acc;
    }, {});

    // Step 3: Update the 'owner' field in inputData based on the mergeList 'owned' status
    inputData.forEach(item => {
        if (ownershipMap.hasOwnProperty(item.id)) {
            item.owned = ownershipMap[item.id];
        }
    });

    return inputData;
}


const handleCellEdited = async (cell) => {
    const rowData = cell._cell.row.data;
    const boardGameId = rowData.id;
    const ownedValue = rowData.owned;

    // check if a document already exists in AppDB for the current user and board game.
    const appDBQuery = `{
        "owner": {
            "$eq": ${userId}
        },
        "content.boardGameId": {
            "$eq": ${boardGameId}
        }
    }`


    const existingAppDBDocument = await domo.post(`/domo/datastores/v1/collections/${collectionAlias}/documents/query`, appDBQuery)

    const document = {
        "content": {
            "boardGameId": boardGameId,
            "owned": ownedValue
        }
    }
    
    if (existingAppDBDocument.length > 0) {
        // update existing document
        const existingDocumentId = existingAppDBDocument[0].id;
        const updatedDocument = await domo.put(`/domo/datastores/v1/collections/${collectionAlias}/documents/${existingDocumentId}`, document)
        console.log("updatedDocument", updatedDocument);
        

    } else {
        // create new document
        const newDocument = await domo.post(`/domo/datastores/v1/collections/${collectionAlias}/documents/`, document);
        console.log("newDocument", newDocument);
    }
}



function handleResult(data){
  console && console.log(data);

  var table = new Tabulator("#tabulator-table", {
      data:data,
      columns:[
          {title:"Ranking", field:"Board Game Rank"},
          {title:"Image", field:"thumbnail", formatter: "image"},
          {title:"Name", field:"primary", headerFilter:"input"},
          {title:"Description", field:"description", headerFilter:"input"},
          {title:"Stars", field:"average", formatter: "star"},
          {title:"Own", field:"owned", hozAlign:"center", editor: true, cellEdited: handleCellEdited, formatter:"tickCross", headerFilter:"tickCross"},

      ],
      layout:"fitColumns",
      pagination:"local",
      paginationSize:10,
      paginationSizeSelector:[10, 25, 50, 100],
  });
}

```

And just a minor addition to `index.html` to update the body tag:

```html
<body onload="fetchData()">
```

Go ahead and `domo publish` and we should have a fairly functional app that lets us track which games we own so we can better plan a game night.



Next up: Getting even more advanced. In part 3, we'll have AI write a game night agenda based on the games we own.








