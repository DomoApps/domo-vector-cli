# Hello World Tutorial

This tutorial walks through how to build a configurable accordion widget into Domo. It will demonstrate:

- how to build and deploy a simple vanilla Javascript application to Domo
- how to leverage 3rd party libraries via CDN
- and how to power your application with Domo DataSets in a highly configurable and modular way.

### Step 1: Setup and Installation

---

Before beginning, please make sure you’ve successfully installed the Domo Apps CLI and followed the basic setup and installation instructions found [here](https://developer.domo.com/docs/dev-studio-quick-start/set-up).

### Step 2: Initialize the App

---

Next, we’ll initialize our application using the Domo Apps CLI with the command `domo init`. We’ll give our app design a descriptive name and select the `hello world` base app templates that `domo init` provides. For now, we won’t connect any DataSets since I’d like to demonstrate what this looks like iteratively in our code. You can see that now `domo init` has generated a new project directory for us, where all of our app code will live.

### Step 3: Explore Basic File Structure

---

Let’s briefly explore these files. Once you `cd` into the `hello-world-tutorial-accordion-widget` project directory, you can see five files. The first of which is an `index.html` file and like any web application, this will be the primary file that Domo uses to render your app.

In the `index.html` file, you can see a few linked files that Domo created for you, including:

1.  `app.css`, where you can define the style of your application; 
2.  `app.js` where you can define your Javascript; and crucially 
3. `manifest.json`, which is where you’ll configure the key Domo-specific parameters of your app.

### Step 4: Launch a Local Development Environment

---

Before we do any development, let’s take a quick look at the local development environment Domo provides. `domo dev` will launch a hot-reloading [localhost](http://localhost) browser window where you can see what your app will look like as you develop. In this case, it just has the `h1` element we can see in our template code.

Note a few warnings here.

1. We haven’t published our App design to Domo yet, which we’ll need to do in order to connect data.
2. All apps require a `thumbnail.png` file to serve as the app’s icon in Domo.

Just to prove our app will hot reload when we change code in our project directory, let’s adjust the size of our app in the `manifest.json` file.

### Step 5: Add Required Thumbnail to the Base Directory

---

Before deploying our app to Domo, we need to add a `thumbnail.png` file. For the sake of this tutorial, I’ll just add a blank one using the `touch thumbnail.png` command, but for your app it’s best practice to choose a thumbnail that is specific to your app.

### Quick Recap

---

So far we’ve completed the basic local setup by:

- Installing the Domo CLI
- Initializing a basic app template using `domo init`
- Launching a local developer server with the `domo dev` command
- Giving our app design an icon

### Step 6: Publish Initial App Design to Your Domo Instance

---

Now, we’re ready to publish our initial app design to Domo. First, make sure you’re logged in to the instance that you’d like to deploy to. You can use the `domo login` command to authenticate from the CLI.

Next, deploying your app to Domo is as simple as using the `domo publish` command.

You can see that Domo has now created a new App Design in your instance, successfully uploaded all the files in your project directory, and added your App Design’s id to your `manifest.json` file.

### Step 7: Explore Initial App Design

---

Let’s check out what our very basic App Design now looks like in Domo.

In addition to the Overview tab, you can see sections for Cards, Data, and Versions.

Since we haven’t created any instances (or “Cards” in Domo) of this app design and we haven’t connected any data, there’s not much to see here yet.

We can create an instance of our app, by clicking the “Create New Card” button and you can see we now have a very basic app that reflects our starter code. 

Domo’s App Framework is extremely flexible in part because a single App Design, can now spawn many different App Instances all powered by different data. But, we haven’t connected any DataSets or AppDB collections to this App Instance yet. We’ll cover DataSets in this tutorial and AppDB collections in a future one.

### Step 8: Define Connection to DataSet in `manifest.json`

---

To power our accordion widget, I’ve put together some sample Domo App FAQs in a Domo Webform DataSet. We’ll be developing against this DataSet. However, as long as we configure our connection this DataSet correct in the `manifest.json` file, we can use any DataSet with the same schema to power our app in Production.

Configuring a connection is relatively simple. Just add an object to the `mapping` array with three properties:

1. an `alias`, which will be the name you can use to reference the DataSet in your code.
2. the `dataSetId`, which should correspond to the DataSet you’d like to develop against.
3. a `fields` array, which we’ll leave empty for now to allow access all DataSet columns by default.

Ok, let’s check out how this update to the `manifest.json` file impacts our App Instances in Domo. But looks like I have a typo so let’s fix that and `domo publish` once again.

Since our App Design `mapping` has changed, the CLI is telling us that we should check our cards (also known as our App Instances) for potential mis-mappings. So let’s check out the card we’ve already deployed. It looks there isn’t a DataSet connection in our Instance yet. That’s because the mapping changed and we need to go and resave our card to update it.

When we edit our existing app instance, we can see that the edit screen has changed in a pretty significant way. We can now see the DataSet that we defined in our app manifest as well as the option to select other DataSets from our Domo Instance to power this particular App Instance.

At Domo, this edit screen that gives us the ability to wire our App Instance to different DataSets is appropriately called the “wiring screen”. Once we’re happy with how we’ve wired up our App Instance, let’s save and finish. And we can now see the DataSet connection reflected in the Data Tab.

### Step 9: Define Expected DataSet Fields

---

Let’s say we want to build an App that will work across multiple DataSets even when those DataSets have different column names. That’s where defining what fields your app should expect in the `manifest.json` file is critical.

The `fields` array takes an object for each column that contains an `alias` property and a `columnName` property. The `alias` will be the name we use to refer to the column in our code and the `columnName` will map to the name of the column in the DataSet that we’re developing against. To update our App Design with the new DataSet mapping, `domo publish` again.

Note: I’m actually using the wrong columnName here as the two columns in our FAQ dataset are actually Question and Answer. I can fix this in our App Instance, by using the column mapping now accessible to me via the wiring screen. To develop locally, I’ll still need to go back and fix this.

### Step 10: Setup Proxy to Domo App Instance to Connect to Data Locally

---

Let’s see what developing locally against a Domo DataSet looks like.

First, because we’re developing on our local machine, we’ll need a way to tell Domo how to securely make requests to get data from our DataSet. To do that, we need to define a `proxyId` which corresponds to the App Instance that we want to make requests against. If you click on the Iframe source of our app instance,  you can see that it’s actually deployed to its own url. We can get the `proxyId` from this url or from the previous screen. 

Once you’ve copied the proxyId, go ahead and add it to your `manifest.json` file. To complete the `proxyId` configuration, we just need to `domo publish` again.

It’s time to prove to ourselves that the data connection works locally. Spin up your development server again using `domo dev.`

In the `app.js` file, the following code leverages the built-in `domo.js` utility to request data from our `faqdata` DataSet and logs the result in the console. Even though our DataSet is small, it’s best practice to include a `limit` in the query to prevent requesting the entire DataSet.

```jsx
domo.get('/data/v2/faqdata?limit=100')
    .then(function(faqdata){
      console.log("faqdata", faqdata);
    });
```

If we inspect our [localhost](http://localhost) window and take a look at the console output, we can see that we’ve successfully pulled data from the DataSet into our app even though it’s running on a development server on our local machine.

### Step 11: Build the Static Accordion Widget

---

Now that we have everything connected, we can start writing the code for our accordion widget.

We’ll be leveraging the Bootstrap CSS Library and more specifically, its accordion widget component.

- Accordion Widget - [https://getbootstrap.com/docs/5.0/components/accordion/](https://getbootstrap.com/docs/5.0/components/accordion/)
- Installation Page - [https://getbootstrap.com/docs/5.0/getting-started/download/#cdn-via-jsdelivr](https://getbootstrap.com/docs/5.0/getting-started/download/#cdn-via-jsdelivr)

To load the Bootstrap library into our app, we’ll use the CDN links found on the Download page. However, future tutorials will demonstrate how to load 3rd party resources via package managers like `yarn` and `npm`.

Go ahead and copy the code found here and paste it into the `index.html` page.

```jsx
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
```

We can now copy the sample accordion widget code from the Bootstrap documentation as a starting point for our own widget. Let’s replace our h1 tag with this sample code and check out what it looks like in our [localhost](http://localhost) environment.

```jsx
<div class="accordion" id="accordionExample">
      <div class="accordion-item">
        <h2 class="accordion-header" id="headingOne">
          <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
            Accordion Item #1
          </button>
        </h2>
        <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne" data-bs-parent="#accordionExample">
          <div class="accordion-body">
            <strong>This is the first item's accordion body.</strong> It is shown by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
          </div>
        </div>
      </div>
      <div class="accordion-item">
        <h2 class="accordion-header" id="headingTwo">
          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
            Accordion Item #2
          </button>
        </h2>
        <div id="collapseTwo" class="accordion-collapse collapse" aria-labelledby="headingTwo" data-bs-parent="#accordionExample">
          <div class="accordion-body">
            <strong>This is the second item's accordion body.</strong> It is hidden by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
          </div>
        </div>
      </div>
      <div class="accordion-item">
        <h2 class="accordion-header" id="headingThree">
          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
            Accordion Item #3
          </button>
        </h2>
        <div id="collapseThree" class="accordion-collapse collapse" aria-labelledby="headingThree" data-bs-parent="#accordionExample">
          <div class="accordion-body">
            <strong>This is the third item's accordion body.</strong> It is hidden by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
          </div>
        </div>
      </div>
    </div>
```

Looks pretty good, but this is of course hard coded data so in the next step we’ll need to do a bit of work to hook it up to our FAQ dataset.

Before we do that, lets `domo publish` just to see what this static accordion widget looks like in production.

### Step 12: Power the Accordion Widget with FAQ Data

---

Make sure your development server is running with the `domo dev` command and double check that we’re still successfully logging data from the dataset in our console.

I’m going to paste the following Javascript code in `app.js` that does basically three things:

1. It fetches data from our dataset
2. Loops through each row in our dataset
3. For each row, it constructs a Bootstrap Accordion Widget Item and adds it to the widget.

```jsx
// load accordion widget on successful return of data from Domo
const fetchData = () => {
    domo.get('/data/v2/faqdata?limit=100')
        .then(function(faqdata) {
            console.log("faqdata", faqdata);
            loadAccordion(faqdata);
    });
}

// loop through each row of data and create an accordion card for it
const loadAccordion = (data) => {
    console.log("load accordion");
    const accordion = document.getElementById("accordion");
    console.log(accordion);
  
    for (let i = 0; i < data.length; i++) {
      const element = data[i];
      const name = element["name"];
      const description = element["description"];
      console.log(name);
      console.log(description);
      createAccordionItem(accordion, String(i), name, description);
    }  
  }

  const createAccordionItem = (parentElement, itemId, itemHeaderTitle, itemDescription) => {
    const item = parentElement.appendChild(document.createElement('div'));
    item.classList.add('accordion-item');
  
    const itemHeader = item.appendChild(document.createElement('h2'));
    itemHeader.setAttribute("id", "heading" + itemId);
    itemHeader.classList.add('accordion-header');
    
    const button = itemHeader.appendChild(document.createElement('button'));
    button.classList.add("accordion-button");
    button.setAttribute('type', "button");
    button.setAttribute('data-bs-toggle', "collapse");
    button.setAttribute('data-bs-target', "#collapse-" + itemId);
    button.setAttribute('aria-expanded', "true");
    button.setAttribute('aria-controls', "#collapse-" + itemId);
    button.textContent = itemHeaderTitle;
    
  
    const itemCollapse = item.appendChild(document.createElement('div'));
    itemCollapse.setAttribute("id", "collapse-" + itemId);
    itemCollapse.classList.add("accordion-collapse", "collapse", "hide");
    itemCollapse.setAttribute("data-bs-parent","#accordion");
    itemCollapse.setAttribute("aria-labelledby", "heading" + itemId);
    const itemBody = itemCollapse.appendChild(document.createElement('div'));
    itemBody.classList.add("accordion-body");
    itemBody.textContent = itemDescription;
  }
```

Finally, we just need to get rid of the static widget elements in our code and tell our Javascript `fetchData()` function to fire when the body of our app loads - `<body onload="fetchData()">`.

Our final `index.html` file should look like the following:

```html
<html>
  <head>
    <link rel="stylesheet" href="app.css" />
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
  </head>
  <body onload="fetchData();">
    <div class="accordion" id="accordion">
    </div>

    <!-- domo.js optional utils -->
    <script src="domo.js"></script>
    <script src="app.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

  </body>
</html>
```

Once the development server reloads, we can see that our accordion widget is now powered by our sample FAQ DataSet.

Lets `domo publish` one last time to get our app in production.

And to drive home the point that this App is now highly configurable, we can jump into the wiring screen and pick a new DataSet to power our widget. All we need to do is map the column names, save our app instance, and boom we’re done.