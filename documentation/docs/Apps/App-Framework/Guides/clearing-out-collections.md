

# Deleting all documents from a collection

Use the following script to delete all the documents from a collection.

<!-- theme: warning -->
> #### Danger!
> **Note**: This action is destructive and is not reversible.<br/>
> **Note**: If you ***really*** need to reverse this action please contact Domo Support. However, please be careful - we may not be able to restore this action and in cases where we can, there are costs associated with it.

Just copy this code to your browser console, set up your `collectionId` and press enter.

---
```js
const collectionToDeleteId = {{collectionId}};

// accepts a collectionId and purges all records with no conditions
// must be used from the top level of an instance as it consumes /api
const SLICE_SIZE = 15
const purgeRecords = async(collectionId)=>{
    const data = await getCollectionContent(collectionId)
    if (!data || !data.length) {
        return console.log(`No data to delete in collectionId: ${collectionId}`)
    }

    const ids = data.map(e=>e.id);
    console.log(`ids to delete, ${ids}`);
    for (let i = 0; i < ids.length; i += SLICE_SIZE) {
        await fetch(`/api/datastores/v1/collections/${collectionId}/documents/bulk?ids=${ids.slice(i, i + SLICE_SIZE)}`, {
            method: 'DELETE'
        });
    }

    if (data.length === 10000) { 
      purgeRecords(collectionId);
    }
}

const getCollectionContent = async(collectionId)=>{
    const result = await fetch(`/api/datastores/v1/collections/${collectionId}/documents/query`, {
        method: 'POST',
        body: "{}"
    });
    const data = await result.json();

    return data;
}

purgeRecords(collectionToDeleteId);
}
```

