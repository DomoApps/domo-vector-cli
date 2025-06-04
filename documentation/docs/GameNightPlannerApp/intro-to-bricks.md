---
stoplight-id: ndvsmatbqz5gk
---

# Game Night Planner App - Intro to Domo Bricks

Welcome to part one of a three part series on building introductory custom apps in Domo. In this part, we'll be starting by building our solution as a Domo Brick (the lightest weight way to get into custom app development in Domo). In the next part we'll migrate our solution into a full custom application to give you some intuition on the difference between a Domo Brick and a Custom App.

We're going to be building a powerful custom table application that can help us plan a fun board game night.

![boardgametablebrick.gif](../../assets/images/boardgametablebrick-2.gif)


### Key steps and learning objectives
---
1. Downloading a Domo Brick Template
2. Connecting to Data in a Domo Brick
3. Importing [Tabulator](https://tabulator.info/) (an amazing third party table library)
4. Creating a basic table
5. Customizing our table
6. Review limitations of bricks relative to custom apps

### Downloading a Domo Brick Template
---
To get started let's add a blank Domo Brick template to a Dashboard or App Studio canvas.

1. Edit your Dashboard.
![Screenshot 2024-03-22 at 10.05.58 AM.png](../../assets/images/Screenshot%202024-03-22%20at%2010.05.58%20AM.png)

2. Drag the "App" Icon on to your Dashboard.
![Screenshot 2024-03-22 at 10.08.39 AM.png](../../assets/images/Screenshot%202024-03-22%20at%2010.08.39%20AM.png)

3. Search for the "Blank Brick" template to use and click "GET".
![Screenshot 2024-03-22 at 10.15.40 AM.png](../../assets/images/Screenshot%202024-03-22%20at%2010.15.40%20AM.png)

4. You should now see your blank brick on the Dashboard. Next you'll want to click "Edit Card" to enter the Brick Code Editor.
![Screenshot 2024-03-22 at 10.19.33 AM.png](../../assets/images/Screenshot%202024-03-22%20at%2010.19.33%20AM.png)

5. Explore the Bricks Editor and "Wiring Screen"
![Screenshot 2024-03-22 at 10.23.07 AM.png](../../assets/images/Screenshot%202024-03-22%20at%2010.23.07%20AM.png)


<!-- theme: warning -->
> #### Bricks Limitation
>
> You can only write code in the three provided files: JAVASCRIPT, HTML, CSS. This can be restrictive as the length and complexity of your code grows.

### Connecting to Data in a Domo Brick
---

1. Review provided sample code

In this brick template, you can wire up to three different datasets. However, the sample code provided is only technically reading from `dataset0`.

![Screenshot 2024-03-22 at 10.31.59 AM.png](../../assets/images/Screenshot%202024-03-22%20at%2010.31.59%20AM.png)

The dropdown provides the `alias` used to refer to a particular wired Dataset. This is the name you'll use in your code when connecting to data.

<!-- theme: warning -->
> #### Bricks Limitation
>
> Each brick has its own template that defines how many Datasets you can connect and what the aliases are named. You don't have control over this template for Domo Bricks, but do with Custom Apps.

In the brick code, you will automatically have access to the `domo.js` library via the `domo` global variable as well as a list of the dataset aliases via the `datasets` global variable.

```js
 
//Available globals
var domo = window.domo; // For more on domo.js: https://developer.domo.com/docs/dev-studio-guides/domo-js#domo.get
var datasets = window.datasets;

```

In practice, you can use these two variables to send a request via the Data API. The sample code provided shows how that works.

```js
//Step 2. Query your dataset(s): https://developer.domo.com/docs/dev-studio-references/data-api
var fields = ['state', 'revenue'];
var groupby = ['state'];
var query = `/data/v1/${datasets[0]}?fields=${fields.join()}&groupby=${groupby.join()}`;
domo.get(query).then(handleResult);



//Step 3. Do something with the data from the query result
function handleResult(data){
  console && console.log(data);
}

```

You can define the fields that you need access to, any aggregation logic, as well as the query to send to the Data API itself. Once the data is returned from Domo, the `handleResult` function is run and the data is printed in the console.

If you right-click and open the developer console, you should see the data printed out.

![Screenshot 2024-03-22 at 10.41.34 AM.png](../../assets/images/Screenshot%202024-03-22%20at%2010.41.34%20AM.png)

2. Connect to a new dataset

You can [download the data used in this tutorial at the following GitHub repo here](https://github.com/DomoApps/game-night-planner-walkthrough/blob/main/data/Board_Game_Details_Dataset.csv). Once you've downloaded the data, you can use Domo's csv upload connector to get the data in Domo.

Now lets wire up `dataset0` to a new Dataset. Select the button under "Select Dataset" and search for the name of the Dataset you just uploaded.

You should now see a new Dataset displayed for `dataset0`. Note: you may need to click 
"Save and Finish" and re-enter the Brick wiring screen to persist the new Dataset connection.

![Screenshot 2024-03-22 at 2.41.29 PM.png](../../assets/images/Screenshot%202024-03-22%20at%202.41.29%20PM.png)

But, if you click "Run" you'll notice that the default code in the brick not pulling the data correctly!

![Screenshot 2024-03-22 at 2.43.43 PM.png](../../assets/images/Screenshot%202024-03-22%20at%202.43.43%20PM.png)


There are a few things that we need to fix. First, we're requesting fields (`state` and `revenue`) and an aggregation (groupby `state`) in the Data API query. We can simplify our code to request all fields in the Dataset and remove the aggregation.

Replace everything in `//Step 2.` with the following code:

```js
//Step 2. Query your dataset(s): https://developer.domo.com/docs/dev-studio-references/data-api
var fields = []; // keeping empty requests all fields
var groupby = []; // keeping empty to not use groupby
var query = `/data/v1/${datasets[0]}?fields=${fields.join()}&groupby=${groupby.join()}`;
domo.get(query).then(handleResult);

```

When you click "Run", you should now see ~21.6k records printed in the console.

![Screenshot 2024-03-22 at 2.48.42 PM.png](../../assets/images/Screenshot%202024-03-22%20at%202.48.42%20PM.png)

Congrats! You've successfully connected our brick to a new Dataset.

### Importing Tabulator
---
Next we want to actually display our data in a new table visual. We'll be using an open-source third party library that is designed specifically to create very powerful table applications.

You can check out more about the [Tabulator library in their documentation](https://tabulator.info/).

![Screenshot 2024-03-22 at 2.52.49 PM.png](../../assets/images/Screenshot%202024-03-22%20at%202.52.49%20PM.png)


<!-- theme: warning -->
> #### Bricks Limitation
>
> In order to leverage third party libraries in bricks, since we only have the ability to customize three files, we'll need to import Tabulator via a CDN. This just means that the files that make up the library are hosted elsewhere and we will load them in via a url.
>
> With Custom Apps, you can use package management tools like `yarn` and `npm`, which becomes increasingly important as the number of dependencies in your application grows.


You can find more installation instructions for the Tabulator library in their [Quickstart Guide](https://tabulator.info/docs/6.0/quickstart#sources-cdn). 

To pull the library into our brick, you can add the following lines in the `HTML` file.

```html
<script src="
https://cdn.jsdelivr.net/npm/tabulator-tables@6.0.1/dist/js/tabulator.min.js
"></script>
<link href="
https://cdn.jsdelivr.net/npm/tabulator-tables@6.0.1/dist/css/tabulator.min.css
" rel="stylesheet">

```

### Creating a custom table
---

Now that we have Tabular installed in our brick, let's create our Tabulator table! This will only require two small bits of code.

First, add the following `div` to your `HTML` file, which will be where the table will be rendered.

```html
<div id="tabulator-table"></div>
```

Second, add the following snippet to instantiate the table in the `handleResult` callback function.


```js
  var table = new Tabulator("#tabulator-table", {
      data:data,
      columns:[
          {title:"Ranking", field:"Board Game Rank"},
          {title:"Name", field:"primary", headerFilter:"input"},
          {title:"Description", field:"description", headerFilter:"input"},
      ],
      layout:"fitColumns",
      pagination:"local",
      paginationSize:10,
      paginationSizeSelector:[10, 25, 50, 100],
  });
```

### Customizing our table
---
Now with our basic table setup, we can have a bit of fun using the Tabulator library.

As you can see by our basic setup, customizing our table is as simple as adjusting settings in the object that includes:
```js
{
      data:data,
      columns:[
          {title:"Ranking", field:"Board Game Rank"},
          {title:"Name", field:"primary", headerFilter:"input"},
          {title:"Description", field:"description", headerFilter:"input"},
      ],
      layout:"fitColumns",
      pagination:"local",
      paginationSize:10,
      paginationSizeSelector:[10, 25, 50, 100]
  }
```

If you start to explore the Tabulator library, you can see how much we can start to customize things. To get some practice, let's try to make three updates to our table:

1. Add the image `thumbnail` for each board game and the average star rating `average` that users have rated the game.
2. Update the theming of our table to look a bit cooler.
3. Add a new editable column that lets us track which games we already own so we can plan our game night!

#### Add image and stars

To add our new columns all we need to do is include them in the columns array.

To do this, just replace the `handleResult` function with the following code:

```js
function handleResult(data){
  console && console.log(data);

  var table = new Tabulator("#tabulator-table", {
      data:data,
      columns:[
          {title:"Ranking", field:"Board Game Rank"},
          {title:"Image", field:"thumbnail"},
          {title:"Name", field:"primary", headerFilter:"input"},
          {title:"Description", field:"description", headerFilter:"input"},
          {title:"Stars", field:"average"},

      ],
      layout:"fitColumns",
      pagination:"local",
      paginationSize:10,
      paginationSizeSelector:[10, 25, 50, 100],
  });
}

```

This update added the columns to our table, but we'd like them formatted to look better. That's where we can leverage [Tabulator's formatters](https://tabulator.info/examples/6.0?#formatters).

To turn our thumnail link into an image, let's update the columns configuration object that corresponds to `thumbnail` as follows:

```js
{title:"Image", field:"thumbnail", formatter: "image"}
```

If you click "Save and Finish", your table should now look like this:


![Screenshot 2024-03-22 at 4.36.15 PM.png](../../assets/images/Screenshot%202024-03-22%20at%204.36.15%20PM.png)

Adding start formatting is just as easy. Update the columns configuration object that corresponds to `average` as follows:

```js
{title:"Stars", field:"average", formatter: "star"}
```

Looking much better already!

![Screenshot 2024-03-22 at 4.38.39 PM.png](../../assets/images/Screenshot%202024-03-22%20at%204.38.39%20PM.png)

#### Improve theming

Thanks to [Tabulator's flexible theming options](https://tabulator.info/examples/6.0?#theming)
, we can customize the look and feel of our table even further.


In this case, we'll use CSS to override the default themes and make our table fit Domo's color scheme.

For reference, the color scheme we will use is the follow:
- **Primary Color:** Domo Blue `#99CCEE`
- **Secondary Color:** Light Gray `#888888`
- **Tertiary Color:** Dark Gray `#555555`
- **Accent Color:** Orange `#FF9922` (not using for now)

![Screenshot 2024-03-22 at 4.45.22 PM.png](../../assets/images/Screenshot%202024-03-22%20at%204.45.22%20PM.png)

To apply our new color scheme, all we need to do is add the following CSS to the CSS file:


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
Your "Domo-fied" table should look like the below:

![Screenshot 2024-03-22 at 4.53.57 PM.png](../../assets/images/Screenshot%202024-03-22%20at%204.53.57%20PM.png)

#### Create an editable column to mark ownership

To properly plan my game night, I want to be able to mark which games I already own so I can filter down the list a bit better.

Tabulator makes turning columns `editable` very easy. Just add a new object to the `columns` configuration list.

Your `handleResult` function should now look like below. Note the new column `Own` with an editable property. 

```js
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

Now you should be able to adjust the check mark in the `Own` column but clicking it.

![Screenshot 2024-03-22 at 5.01.27 PM.png](../../assets/images/Screenshot%202024-03-22%20at%205.01.27%20PM.png)

But wait! If we refresh the page, this edit doesn't persist anywhere...that's because we aren't storing the change anywhere in Domo. That's where AppDB will come in.

<!-- theme: warning -->
> #### Bricks Limitation!
>
> Although it is possible to write to AppDB from a brick it is strongly encouraged to move to a full Custom App so you have more control over your AppDB Collections.

In our next part of the training, we'll be converting the brick we just built into a full Custom App and we'll add read/write data capabilities to our application using AppDB.



### Review limitations of bricks relative to custom apps
---

Bricks are great for simple, singular purpose widgets, but as soon as complexity starts to increase, custom apps provide a lot more flexibility.

![bricks-or-app-framework.png](../../assets/images/bricks-or-app-framework.png)






