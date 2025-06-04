---
stoplight-id: pff92wc4t7vgw
---

# Adding Advanced Capabilities to Your App

You've now seen that migrating your Domo Brick to a full Custom App unlocks a lot of flexibility, especially when it comes to managing the resources connected to your App (e.g. Datasets, AppDB collections). Having access to the app manifest file gives your control over the Workflows and Code Engine functions connected to you App too!

In part 3 of the Intro to Custom App Development training, we'll highlight some more advanced functionality that Apps can unlock.

1. Building generative AI features into your App
2. Treating your App as a custom component in App Studio
3. Next step ideas


### Building generative AI features into your App
---

For our game night planning app, we'd like to be able to take a list of all the games that we own and ask an LLM to write a game night plan for us.

To do that we'll:

- Construct a prompt based on the games we own and send it to Domo's Text Generation Service
- Add a new button that triggers a call to our plan generation function
- Display the response in our app

#### Generate a plan

First, we need to write a function that will take a list of games we already own, constructs a prompt, and sends that prompt to Domo's AI Service Layer.

Add this function to your `app.js` file:

```js
const generatePlan = async (gamesOwned) => {
    const prompt = `Please write me an agenda for a fun and engaging game night that lasts between 3 and 4 hours and includes some of the following games: ${JSON.stringify(gamesOwned)}. Please use plenty of puns.`;

    const body = {
        "input": prompt
    }

    const plan = await domo.post(`/domo/ai/v1/text/generation`, body)
    return plan;
}
```

This function will return our AI generated, game night plan.



#### Create a button

Add a container in our HTML where we can create our button.

```html
...
<h1>Game Night Planner</h1>
<span id="generate-plan-button-container"></span>
<div id="tabulator-table"></div>
...
```

Create a reference to this button container element in `app.js` under our other global variables.

```js
var generatePlanButtonContainer = document.getElementById("generate-plan-button-container");

```

Now create a function `createGenerateActionPlanButton` we can use to dynamically insert our button element in the DOM.


```js
const createGenerateActionPlanButton = () => {
    const planButton = document.createElement("button");
    planButton.id = "generate-plan-button";
    planButton.textContent = "Generate Game Night Plan";
    generatePlanButtonContainer.innerHTML = "";
    // Insert the button into the container
    generatePlanButtonContainer.appendChild(planButton);
}
```

#### Connect our button to `generatePlan`

This step will involve a few sub-steps.

1. Create two new global variables we can reference to hold the games we own and the game night plan. Place `var gamesOwned = []` and `var gameNightPlan = "";` below our other global variables at the top of the `app.js` file.
    ```js
    var datasets = ['boardgames'];
    const collectionAlias = 'ownership';
    const userId = domo.env.userId;
    var gamesOwned = [];
    var gameNightPlan = "";
    ...
    ```

2. Update our `fetchData` function to filter our data downed to just the games we own, store that in the `gamesOwned` variable, and call the `createGenerateActionPlanButton` function.
    ```js
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
    
        gamesOwned = data.filter(game => game.owned === true);
    
        gamesOwned = gamesOwned.map(game => ({
            primary: game.primary,
            description: game.description,
            boardgamecategory: game.boardgamecategory,
            minplaytime: game.minplaytime,
            playingtime: game.playingtime
        }));
    
        createGenerateActionPlanButton();
        handleResult(data);
    
    }
    ```

3. Update our `createGenerateActionPlanButton` function to set up a callback to generate the plan when the user clicks the button.

    ```js
    const createGenerateActionPlanButton = () => {
        const planButton = document.createElement("button");
        planButton.id = "generate-plan-button";
        planButton.textContent = "Generate Game Night Plan";
        generatePlanButtonContainer.innerHTML = "";
        // Insert the button into the container
        generatePlanButtonContainer.appendChild(planButton);
    
        planButton.addEventListener("click", async function() {
            console.log("clicked button");
            try {
                gameNightPlan = await generatePlan(gamesOwned);
                gameNightPlan = gameNightPlan.choices[0]["output"];
    
            } catch {
                console.log("Error generating plan");
            }
            
            console.log("games night plan after click", gameNightPlan);
        });
    
    }
    ```

Now when we reload our app, we should be able to see a button appear after the data has been loaded and when we click the button we should see our AI generated plan in the console output.


![Screenshot 2024-03-25 at 6.56.15 AM.png](../../assets/images/Screenshot%202024-03-25%20at%206.56.15%20AM.png)


**Bonus challenge**: add some css to our button to make it look a bit nicer.

![Screenshot 2024-03-25 at 7.03.38 AM.png](../../assets/images/Screenshot%202024-03-25%20at%207.03.38%20AM.png)

We should also implement one more small change to account for the case where we've recently made an update to the list of games we own. Currently, what is stored in `gamesOwned` won't update when we edit our table. 

One way to handle this is to fetch our data again on edit. You can add a call to `fetchData` at the bottom of your  `handleCellEdited` callback function.

```js
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

    fetchData(); // Added 
}
```

There are other, more efficient ways to handle the state of data in your application like using `localStorage` or frameworks like React that have tooling to efficiently handle updates to your app on state change. However, that is beyond the scope of this course, so we'll just refetch all the data each time you make an update to ownership state.



#### Display the response from text generation service

The last thing we want to do is actually show the response after we click the button.


Add a new div where we can display the `gameNightPlan`.

```html
...
<span id="generate-plan-button-container"></span>
<span id="game-night-plan-results-container"></span>
<div id="tabulator-table"></div>
...
```

In our javascript, add a reference to this element we can use:

```js
...
var generatePlanButtonContainer = document.getElementById("generate-plan-button-container");
var gameNightPlanContainer = document.getElementById("game-night-plan-results-container");
...
```

Finally, update the callback inside of the `createGenerateActionPlanButton` to add the `gameNightPlan` to our container:

```js
const createGenerateActionPlanButton = () => {
    const planButton = document.createElement("button");
    planButton.id = "generate-plan-button";
    planButton.textContent = "Generate Game Night Plan";
    generatePlanButtonContainer.innerHTML = "";
    // Insert the button into the container
    generatePlanButtonContainer.appendChild(planButton);

    planButton.addEventListener("click", async function() {
        console.log("clicked button");
        try {
            gameNightPlan = await generatePlan(gamesOwned);
            gameNightPlan = gameNightPlan.choices[0]["output"];

            gameNightPlanContainer.innerHTML = gameNightPlan;

        } catch {
            console.log("Error generating plan");
        }
        
        console.log("games night plan after click", gameNightPlan);
    });

}
```


**Bonus challenge**: Implement a loading state for your button so users can't click it twice while making our `generatePlan` request.


![Screenshot 2024-03-25 at 7.19.11 AM.png](../../assets/images/Screenshot%202024-03-25%20at%207.19.11%20AM.png)


**Bonus challenge #2**: Add some css to make our game night plan container display better.

![Screenshot 2024-03-25 at 7.25.51 AM.png](../../assets/images/Screenshot%202024-03-25%20at%207.25.51%20AM.png)


### Treating your App as a custom component in App Studio
---

One of the most powerful things about building Apps on the Domo platform is that you get to inherit all the great out-of-the-box functionality of Domo like filtering, standard Domo cards, PDP, etc.

With App Studio, you can now build most of your App solution without any code and just focus your development time on the custom components.

Let's `domo publish` our final app and then add it to an App Studio canvas.

Run `domo publish` for the final time today!

Next, navigate to App Studio - "Apps" in the top navbar.

![Screenshot 2024-03-25 at 7.41.16 AM.png](../../assets/images/Screenshot%202024-03-25%20at%207.41.16%20AM.png)

Click "Create App" and pick your theme:

![Screenshot 2024-03-25 at 7.42.02 AM.png](../../assets/images/Screenshot%202024-03-25%20at%207.42.02%20AM.png)

I'm going to go with "Domo Classic".

Next, I'll give my app a name, add an icon, and rename "App Page 1" to "Game Night Explorer".

![Screenshot 2024-03-25 at 7.43.58 AM.png](../../assets/images/Screenshot%202024-03-25%20at%207.43.58%20AM.png)

Let's drop our Custom app on this page. Click the + button and drag the Card icon into the canvas.

![Screenshot 2024-03-25 at 7.44.36 AM.png](../../assets/images/Screenshot%202024-03-25%20at%207.44.36%20AM.png)

Click "Add Existing Card" and search for the App Instance ("Card") you've been building.

![Screenshot 2024-03-25 at 7.47.00 AM.png](../../assets/images/Screenshot%202024-03-25%20at%207.47.00%20AM.png)


Now let's add a filter component to help us explore our games table a bit better.

Drag another Card onto the canvas and this time select "Create new Card" > "Visualization" > "Existing Data".

![Screenshot 2024-03-25 at 7.49.18 AM.png](../../assets/images/Screenshot%202024-03-25%20at%207.49.18%20AM.png)


Select the same Dataset powering our App.

![Screenshot 2024-03-25 at 7.50.05 AM.png](../../assets/images/Screenshot%202024-03-25%20at%207.50.05%20AM.png)


Select a filter card:

![Screenshot 2024-03-25 at 7.50.37 AM.png](../../assets/images/Screenshot%202024-03-25%20at%207.50.37%20AM.png)

I'm going to create a playing time filter so I can more easily narrow games down by playing time.

![Screenshot 2024-03-25 at 7.51.56 AM.png](../../assets/images/Screenshot%202024-03-25%20at%207.51.56%20AM.png)

Click "Save".

Now if I'm looking for a short game, I can easily filter my App.

![Screenshot 2024-03-25 at 7.58.59 AM.png](../../assets/images/Screenshot%202024-03-25%20at%207.58.59%20AM.png)


**Bonus Challenges**: 
- Add more filters to the current page.
- Create a new page or tabs on the current page to use more out-of-the-box charts for additional analytics on games
- Leverage game category or game designer data (may need to create Beast Modes or derivative DataSets to parse out individual values)


### Next steps
---

Want to go beyond this training? Here are some ideas for expanding your App Development skills:

- Try adding integration with Workflows to send an email invitation to your friends. See our [Guide on Hitting a Workflow from an App](../Apps/App-Framework/Guides/hitting-a-workflow.md)
- Try taking an action in a third party system. Refactor your app into a "Game Recommendation Application" and write a Code Engine function that add a Board Game you don't already own to a shopping cart in an ecommerce site. See our Guide on [Hitting Code Engine from an App](../Apps/App-Framework/Guides/hitting-code-engine-from-an-app.md)
- Try building your application with more advanced tooling like our [React Starter Kit](../Apps/App-Framework/Quickstart/Starter-Kits.md).




