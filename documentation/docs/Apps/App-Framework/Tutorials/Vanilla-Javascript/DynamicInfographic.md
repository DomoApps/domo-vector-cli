---
stoplight-id: atp50e7pzs4yd
---

# Creating Dynamic Infographics

This tutorial walks through the steps required to convert a static infographic into a dynamic one.

The power of bringing our infographic into Domo is all about the functionality that Domo's data and apps layer gives us out of the box. With relatively little code and setup, our infographic can be:
- Connected to live data
- Combined with other compelling visualizations and filtering components for a dynamic experience
- Distributable as an application you can share or embed anywhere

To do this only requires three steps:

1. Create your infographic and export it as a `.png` image
2. Get your data in Domo
3. Create a Domo App that dynamically inserts the data on top of your `.png` infographic image

https://youtu.be/ETGmHX-N9dw


### Step 1: Create your Infographic Template
---

For this example, lets say you're in real estate and want to regularly share key insights on the housing market in your area. You could create an infographic in a great tool like [Canva](https://www.canva.com/), duplicate it for each zip code, and manually update the data for each as it changes as shown below.

![canva-infographics-duplication.gif](../../../../../assets/images/canva-infographics-duplication.gif)

However, by combining the power of Domo and Canva in a Domo App, you can create one infographic and tie it to data in Domo for a dynamic experience.

#### Prepare infographic template

To prepare your infographic template, you'll want to delete all the pieces of the infographic that you want to be dynamic, but before you do that it's important to note the unique styles associated with those components.

For example, we'll want to replicate the font and text alignment properties set in Canva for the title as well as the description components of our initial infographic. Let's note these down.


![Screenshot 2024-04-19 at 12.35.51 PM.png](<../../../../../assets/images/Screenshot 2024-04-19 at 12.35.51 PM.png>)
![Screenshot 2024-04-19 at 12.35.13 PM.png](<../../../../../assets/images/Screenshot 2024-04-19 at 12.35.13 PM.png>)

![Screenshot 2024-04-19 at 12.39.12 PM.png](<../../../../../assets/images/Screenshot 2024-04-19 at 12.39.12 PM.png>)
![Screenshot 2024-04-19 at 12.38.49 PM.png](<../../../../../assets/images/Screenshot 2024-04-19 at 12.38.49 PM.png>)

- **Title**: 
  - Font: Moontime
  - Alignment: Center
  - Color: #000000
- **Description**:
  - Font: Raleway
  - Alignment: Center
  - Color: #000000



Now I can delete the parts of the infographic that I want to make dynamic.

![Screenshot 2024-04-19 at 12.40.29 PM.png](<../../../../../assets/images/Screenshot 2024-04-19 at 12.40.29 PM.png>)

Finally, export this template infographic as a `.png` file. If you'd like to follow along for the next steps, [you can download this infographic template here](https://github.com/DomoApps/canva-infographic-walkthrough/blob/step-03/make-dynamic-data/infographic.png).


### Step 2: Setup Data in Domo
---

In this example, we will setup data in a Domo Webform that we can edit whenever we would like. However, Domo has a vast array of tools for integrating many different sources of data. A subsequent step in this project -- but not covered in this tutorial -- would be to setup an automatically refreshable data pipeline for the real estate data. 


To add data to a Domo Webform, just navigate to "Data" > "Connectors" > Search "Webform".

![Screenshot 2024-04-19 at 1.00.35 PM.png](<../../../../../assets/images/Screenshot 2024-04-19 at 1.00.35 PM.png>)

You can then paste the following data in your Webform. NOTE: to match the code below, you will want all your column names to be lower-case.

city | zip | num_homes_listed | avg_dom | median_list_price | price_change_pct | market_type
---------|----------|---------|---------|----------|---------|---------|
Bend |	97701	| 73 |	127	| 725000	| 48	| 36 |
Bend | 97702 |	114 |	96| 	842000 |	45|	38
Bend |	97703|	105 |	129|	1500000 |	46	|36
Bend | 97707 |	42 |	109 |	914000 |	38 |	31
La Pine	| 97739	| 68 |	130	| 492000	| 26 |	36
Prineville |	97754 |	82|	127|	471000	|39	|30
Powell Butte |	97753|	24|	91|	1525000	|33 |	27
Redmond	| 97756	| 159 |	114 |	599000 |	39 |	35
Sisters	| 97759	| 40	| 164 |	1225000 |	38 |	35
Madras |	97741 |	41 |	128 |	470000 |	32	| 33


![Screenshot 2024-04-19 at 1.08.12 PM.png](<../../../../../assets/images/Screenshot 2024-04-19 at 1.08.12 PM.png>)

Once, you've added this data to Domo, click "Save & Continue".

Now we have the data we need to power our dynamic infographic App!

### Step 3: Build Domo App 

Complete [code for this walkthrough can be found on GitHub here](https://github.com/DomoApps/canva-infographic-walkthrough).

#### Initialize App

Before beginning, please be sure you have the Domo App CLI installed sucessfully. See the [Quickstart instructions here](../../Quickstart/Setup-and-Installation.md).

To generate an initial app template, use the `domo init` command from your command line in the directory where you want your app files to live.

You'll be prompted to:

1. Give your app a name
2. Select a starter template
3. Connect a DataSet

Please use the same configuration as the image below, replacing the `dataset id` with the `id` of your DataSet. You can find the `dataset id` by navigating to your Dataset in Domo and copying it from the url.

![Screenshot 2024-04-19 at 1.18.39 PM.png](<../../../../../assets/images/Screenshot 2024-04-19 at 1.18.39 PM.png>)


![image (1).png](<../../../../../assets/images/image (1)-3.png>)

Once the files have been initialized in a new directory, you can navigate to that directory with the `cd` command and explore the basic file structure of your App. It should look like the following:

![files.png](../../../../../assets/images/files-2.png)


If you open up the `manifest.json` file you can see that we have some default configuration set for our app.

```json
{
  "name": "canva infographic walkthrough",
  "version": "1.0.0",
  "size": {
    "width": 1,
    "height": 1
  },
  "mapping": [
    {
      "dataSetId": "53f5ad94-9e04-485b-b885-fb89cac64b14",
      "alias": "infographicData",
      "fields": []
    }
  ]
}

```

In order to create an App Design in our Domo instance, the last thing we need is a `thumbnail.png` file to use for the App's icon image in Domo. You may use the [image found here](https://github.com/DomoApps/canva-infographic-walkthrough/blob/step-01/init-app/thumbnail.png) or any thumbnail image of your choice as long as you name the file `thumbnail.png`.

Once, you've added the `thumbnail.png` file, go ahead and run the `domo publish` command (after running `domo login`). This should automatically add the `id` of the App Design in Domo to your `manifest.json` file as well as a `fileName` property.

Make sure your `manifest.json` file now looks something like this:

```json
{
  "name": "canva infographic walkthrough",
  "version": "1.0.0",
  "size": {
    "width": 1,
    "height": 1
  },
  "mapping": [
    {
      "dataSetId": "53f5ad94-9e04-485b-b885-fb89cac64b14",
      "alias": "infographicData",
      "fields": []
    }
  ],
  "fileName": "manifest.json",
  "id": "c86f6e58-2060-4273-9906-13a8ff2da14e"
}

```

You can find a link to your new App Design in the terminal output.

![publish.png](../../../../../assets/images/publish.png)


Go ahead and click on that link and then create a new Card.

![design.png](../../../../../assets/images/design.png)


When you create a new Card (also known as an "App Instance"), you should see the App Wiring Screen that looks like the below. Our app has a simple `h1` element and is successfully wired up to a DataSet with the alias `infographicData`, which we've set by default to the sample DataSet we setup in Step 1.

![card.png](../../../../../assets/images/card.png)


Click 'Save and Finish' and we're ready to start writing the code to build our App.

Let's have a look at some of the default files generated by our starter template. 

The `index.html` file contains the basic structure of our page and loads our JavaScript and CSS assets.

```html
<html>
  <head>
    <link rel="stylesheet" href="app.css" />
  </head>
  <body>
    <h1>canva infographic walkthrough</h1>
    <!-- domo.js optional utils -->
    <script src="domo.js"></script>
    <script src="app.js"></script>
  </body>
</html>

```

The [`domo.js` utility library](../../Tools/domo.js.md) provides a number of useful functions for interfacing with Domo, including the `domo.get` call that is included in our `app.js` file by default.

```js
domo.get('/data/v2/infographicData?limit=100')
    .then(function(infographicData){
      console.log("infographicData", infographicData);
    });
```
This starter code uses Domo's [Data API](../../../../Domo-App-APIs/Data-API.md) to get the first 100 records from our DataSet with the alias `infographicData`.

Let's confirm that this is working by running the `domo dev` command to launch a hot-reloading local server. You should see a window open in your browser at `localhost:3000`.

![running.png](../../../../../assets/images/running.png)


Next, right-click in your browser and click "Inspect", the navigate to the console to see if the `domo.get` request is logging data from your DataSet.

![show-data.png](../../../../../assets/images/show-data-2.png)



Great! We have a nice development environment ready to go and it's connected directy to data in Domo.

#### Add Infographic Template

First of all, let's add to our project the infographic `.png` image that we created in the step 1. Name this file `infographic.png` and place it in the same directory as the rest of your app files.

![add-png.png](../../../../../assets/images/add-png-2.png)


The next step is to work on the infographic template by editing the HTML code in the `index.html` file; let's create a simple structure that we can use to display the infographic information.

Note: we are loading in fonts from Google Fonts to match the look and feel of the original infographic template. You can get the fonts you need by searching the [Google Fonts library](https://fonts.google.com/) and copying the `link` tags it generates for you.


```html
<html>
  <head>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Moon+Dance&family=Raleway:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="app.css" />
  </head>
  <body>
    <img class="background" src="infographic.png" alt="" />

    <span id="title" class="title">Bend 97701</span>
    <span id="homes-listed" class="description">73 <br> homes</span>
    <span id="avg-dom" class="description">Average DOM <br> 127</span>
    <span id="median-list-price" class="description">Median list price <br> $725,000</span>
    <span id="price-change" class="description">48% of sellers reduced price</span>
    <span id="market-type" class="description">36 (Seller's Market)</span>

    <!-- domo.js optional utils -->
    <script src="domo.js"></script>
    <script src="app.js"></script>
  </body>
</html>
```
Make sure to include `id` properties like `title` or `homes-listed` and the classes like `description` that we added to the HTML tags above. These will help us replace the data dynamically and style the elements later.

Please note that we set the `img` tag to use our infographic as the App's background by using the `src="infographic.png"` attribute.

**Add Item CSS**

The next step is adding some CSS rules to help the elements position in our layout, and includes the infographic background correctly, for this, let's update the `app.css` file by adding the next snippet.


```css

/* Set the body to display the infographic as a background */
body {
  width: 100%;
  height: 100%; /* Full height */
  margin: 0; /* Remove default margin */
}

.background {
  width: 100%;
  height: 100%;
  position: absolute;
}

.title {
  font-family: "Moon Dance", cursive;
  font-weight: 400;
  font-style: normal;
  font-size: 10vh; /* Sets the font size to 10vh */
  color: #000000; /* Sets the text color to black */
  position: fixed;
  top: 6%;
  text-align: center;
  width: 100%;
}

.description {
  font-family: 'Raleway', sans-serif; /* Uses Raleway, with sans-serif as a fallback */
  font-size: 4vh; /* Sets the font size to 4vh */
  color: #000000; /* Sets the color to black */
  position: fixed;
  text-align: center;
}

#homes-listed {
  top: 55%;
  left: 6%;
  width: 25%;
}

#avg-dom {
  top: 55%;
  left: 42%;
  width: 16%;
}

#median-list-price {
  top: 55%;
  left: 72%;
  width: 20%;
}

#price-change {
  top: 85%;
  left: 15%;
  width: 32%;
}
#market-type {
  top: 85%;
  left: 53%;
  width: 30%;
}
```

After styling the application, Let's confirm that this is working by running the `domo dev` command again, please remember to open a window in your browser at `localhost:3000`.

![look&feel.png](../../../../../assets/images/look&feel.png)


Great! Our application looks much better and reflects all the work we did on the HTML and CSS files.

#### Make Our Infographic Dynamic

Once we have our static infographic template looking good and displaying our information, we need to make it dynamic. For this, we will pull some data from our dataset and inject this data to our HTML code by using Javascript and adding it to the `app.js` file.

First of all, we will add a data structure to link the HTML IDs we added before to the respective column in our dataset; this will allow us to identify the correct element and add the data quickly.

```Javascript
// map structure to link DOM item to dataset column
const mapDomColumns = [
    { id: 'title', key: 'city', column: 'city' },
    { id: 'title', key: 'zip', column: 'zip' },
    { id: 'homes-listed', key: 'num_homes_listed', column: 'num_homes_listed' },
    { id: 'avg-dom', key: 'avg_dom', column: 'avg_dom' },
    { id: 'median-list-price', key: 'median_list_price', column: 'median_list_price', price: true },
    { id: 'price-change', key: 'price_change_pct', column: 'price_change_pct' },
    { id: 'market-type', key: 'market_type', column: 'market_type', market_type: true },
];
```

After defining our structure, we need to set these variables into our HTML code by using the respective element ID and the key we will replace dynamically.

```html
<html>
  <head>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Moon+Dance&family=Raleway:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="app.css" />
  </head>
  <body onload="init();">
    <img class="background" src="infographic.png" alt="" />
    <span id="title" class="title">{city} {zip}</span>

    <span id="homes-listed" class="description">{num_homes_listed} listed <br> homes</span>
    <span id="avg-dom" class="description">Average DOM <br> {avg_dom}</span>
    <span id="median-list-price" class="description">Median list price <br> ${median_list_price}</span>
    <span id="price-change" class="description">{price_change_pct}% of sellers reduced price</span>
    <span id="market-type" class="description">{market_type}</span>

    <!-- domo.js optional utils -->
    <script src="domo.js"></script>
    <script src="app.js"></script>
  </body>
</html>
```

Notice how we replaced the static values in our HTML file with the keys we defined in our structure following the format `{key}`; this will help us to replace them later by using our Javascript code.

Then, our title tag will go from this:

```html
<span id="title" class="title">Bend 97701</span>
```

To this:

```html
<span id="title" class="title">{city} {zip}</span>
```

Then, we will add some Javascript functions to fetch the Domo dataset data, format the numeric values, and interpolate the data from the dataset into our HTML template.

```Javascript
// function to fetch the dataset
const fetchData = async () => domo.get('/data/v2/infographicData?limit=100&useBeastMode=true');

// formatting price number
const formatPrice = (price) => {
    return isNaN(Number(price)) ? price : new Intl.NumberFormat('en-US', {
        minimumFractionDigits: 0,
        maximumFractionDigits: 0,
    }).format(Number(price));
}

// formatting market type string
const formatMarketType = (marketType) => {
  console.log("formatting market type");
  if (Number(marketType) >= 30) {
    return `${marketType} (Seller's Market)`
  } else {
    return `${marketType} (Buyers's Market)`
  }
} 


// function to interpolate the data into the HTML template
const interpolateData = (data) => {
  const row = data[0];
  console.log("interpolating data");
  console.log(row);

  mapDomColumns.forEach(value => {
    let columnValue = "";
    const defaultValue = document.getElementById(value.id).innerHTML.toString();
    
    if (value.price) {
      columnValue = formatPrice(row[value.column]);
    } else if (value.market_type) {
      columnValue = formatMarketType(row[value.column]);
    } else {
      columnValue = row[value.column];
    }

    const newValue = defaultValue.replaceAll(`{${value.key}}`, columnValue);
    document.getElementById(value.id).innerHTML = newValue;
  });
}
```

Finally, we will add an init function, which will be our point of entry for the Javascript code.

```Javascript
const init = async () => {
    const data = await fetchData();
    console.log("data: ", data);
    interpolateData(data);
}
```

After adding our Javascript code into the `app.js` file, our file should look similar to this.

```Javascript
// map structure to link DOM item to dataset column
const mapDomColumns = [
  { id: 'title', key: 'city', column: 'city' },
  { id: 'title', key: 'zip', column: 'zip' },
  { id: 'homes-listed', key: 'num_homes_listed', column: 'num_homes_listed' },
  { id: 'avg-dom', key: 'avg_dom', column: 'avg_dom' },
  { id: 'median-list-price', key: 'median_list_price', column: 'median_list_price', price: true },
  { id: 'price-change', key: 'price_change_pct', column: 'price_change_pct' },
  { id: 'market-type', key: 'market_type', column: 'market_type', market_type: true },
];

// function to fetch the dataset
const fetchData = async () => domo.get('/data/v2/infographicData?limit=100&useBeastMode=true');

// formatting price number
const formatPrice = (price) => {
  return isNaN(Number(price)) ? price : new Intl.NumberFormat('en-US', {
    minimumFractionDigits: 0,
    maximumFractionDigits: 0,
  }).format(Number(price));
}

const formatMarketType = (marketType) => {
  console.log("formatting market type");
  if (Number(marketType) >= 30) {
    return `${marketType} (Seller's Market)`
  } else {
    return `${marketType} (Buyers's Market)`
  }
} 

// function to interpolate the data into the HTML template
const interpolateData = (data) => {
  const row = data[0];
  console.log("interpolating data");
  console.log(row);

  mapDomColumns.forEach(value => {
    let columnValue = "";
    const defaultValue = document.getElementById(value.id).innerHTML.toString();
    
    if (value.price) {
      columnValue = formatPrice(row[value.column]);
    } else if (value.market_type) {
      columnValue = formatMarketType(row[value.column]);
    } else {
      columnValue = row[value.column];
    }

    const newValue = defaultValue.replaceAll(`{${value.key}}`, columnValue);
    document.getElementById(value.id).innerHTML = newValue;
  });
}

const init = async () => {
  const data = await fetchData();
  console.log("data: ", data);
  interpolateData(data);
}

```
To see these functions being called by your app, you will need to add the `init()` function call to the body onload event in your `app.html` file like so:

```html
<body onload="init();">
```

Great! We have our Javascript code ready to fetch data from the dataset and add it to our infographic template dynamically.

Now, let's run our application again using the `domo dev` command to see if is working well and including our dataset data in the HTML code:

![Screenshot 2024-04-19 at 1.56.05 PM.png](<../../../../../assets/images/Screenshot 2024-04-19 at 1.56.05 PM.png>)

Congrats! The application is working well and adding the data from our infographic dataset dynamically.


To complete your App, run the `domo publish` command to deploy the updated code to Domo.


### Step 4: Finalize App and Benefits of Building on Domo
---
Now that we have our App deployed to Domo, we can display it in an App Studio canvas.

This will make it so we can add:
- easy filtering capabilities to switch between different locations
- other visualizations that live alongside our infographic
- a way to share our dynamic embed our infographic with others.


#### Create App Studio Canvas

Let's start by creating an App Studio canvas in Domo, which will provide a place for our new dynamic infographic to live alongside out-of-the-box Domo components like charts and filters.

You can create an App Studio canvas by navigating to "Apps" > "Create App" > Select Theme > "Apply" as shown below.

![create app studio gif.gif](<../../../../../assets/images/create app studio gif.gif>)

Once you are in the edit view of your new App Studio canvas, you can add our custom dynamic infographic component.

Click the "+" button on the left navigation menu and drag the "Card" icon to your canvas. Search for your dynamic infographic component. Select it and size the component to your liking.


![add component to app studio.gif](<../../../../../assets/images/add component to app studio.gif>)

#### Pro-code and No-code Components

One of the great things about both Domo Dashboards and App Studio is that "pro-code" components like our dynamic infographic can easily live along-side out of the box components.

**Adding a filter component**

The first out-of-the-box components we'll want to add to make our infographic truly dynamic is a filter card component. This will allow users of our App to toggle between locations to update what data is displayed on the infographic.

To create a filter card, we'll:
- drag a new card on to our App Studio canvas
- choose to create a new visualization from existing data
- select the filter card visual
- make sure it's hooked up to the same dataset that is powered our dynamic infographic
- create a Beast Mode (`city_zip`) that we can use to display both city and zip in our filter
- Size our filter component on the App Studio canvas

![adding filter to app.gif](<../../../../../assets/images/adding filter to app.gif>)


**Adding a bar chart**

For my app I'd also like to provide additional context around the infographic so people can see what the overall distribution of home prices looks like. For that I'll add a bar chart component.

You can follow a similar pattern to add the bar chart:
- drag a new card on to our App Studio canvas
- choose to create a new visualization from existing data
- select the bar chart card visual
- adjust the y and x axes as well as the sorting settings


![adding chart to app.gif](<../../../../../assets/images/adding chart to app.gif>)

You can see that both our bar chart and dynamic infographic inherit the filter on our App. However, since we'd like the chart to provide more global context, we can disable filtering for that component.

![adjust filter exceptions.gif](<../../../../../assets/images/adjust filter exceptions.gif>)

Great! Before sharing our app with the world, we can make some small quality of life improvements.
- rename the App
- rename the App page
- adjust the styles of different components for consistency

After those small tweaks, the final app looks like the following:

![Screenshot 2024-04-24 at 10.52.29 AM.png](<../../../../../assets/images/Screenshot 2024-04-24 at 10.52.29 AM.png>)


#### Sharing our App

One of the major benefits of building our solution on Domo is that we can now easily share our app via an embed or a link.

- click the share icon
- select "Embed Domo App"
- configure the embed settings
- copy the Iframe (for embedding in other places) or just the link to your app

![public embedding app.gif](<../../../../../assets/images/public embedding app.gif>)


If you'd like to see [the final solution live, you can do so here](https://public.domo.com/embed/pages/rRvmp)!




