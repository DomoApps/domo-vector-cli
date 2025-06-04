
# Sync AppDB Only Once a Day

Since Domo doesn't currently allow you to specify sync intervals, AppDB can **only** be set to either 1) not sync at all or 2) sync every 15 minutes. If you would like to **conserve credits** on syncs, you can create a Workflow to **sync on your schedule**.

This guide leverages Workflows. Please make sure you are familiar with [Workflows](https://domo-support.domo.com/s/article/000005108?language=en_US) and [Code Engine](https://domo-support.domo.com/s/article/000005173?language=en_US) first. 

<!-- theme: info -->
> #### Links to documentation
> - Workflow Documentation (https://domo-support.domo.com/s/article/000005108?language=en_US) 
> - Code Engine Documentation (https://domo-support.domo.com/s/article/000005173?language=en_US)


1. [Create a Workflow](https://domo-support.domo.com/s/article/000005331?language=en_US) that runs at the time you want to sync the collection
2. Specify which collection you want to sync
    - You can [specify it as a variable](https://domo-support.domo.com/s/article/000005331?language=en_US#add_a_variable) in the Workflow
3. [Create a Code Engine function](https://domo-support.domo.com/s/article/000005173?language=en_US#create_custom_package) to execute a sync, which could be written like this:
```js
const codeengine = require("codeengine");

async function syncCollection(collectionId) {
  // gets the collection
  const collection = await codeengine.sendRequest(
    "get",
    `/api/datastores/v1/collections/${collectionId}`
  );

  // enables collection sync
  const putBody = { id: collectionId, syncEnabled: true };
  await codeengine.sendRequest(
    "put",
    `/api/datastores/v1/collections/${collectionId}`,
    JSON.stringify(putBody)
  );

  // forces collection sync
  await codeengine.sendRequest(
    "post",
    `/api/datastores/v1/export/${collection.datastoreId}`,
    ""
  );

  // turns off collection sync
  await codeengine.sendRequest(
    "put",
    `/api/datastores/v1/collections/${collectionId}`,
    JSON.stringify({ ...putBody, syncEnabled: false })
  );
}
```
4. Call the new Code Engine function in the Workflow with the collection id
