---
stoplight-id: e0a20a74a7754
---

# Data Connection via API Overview
<img class="aligncenter size-full wp-image-3176" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2017/08/04100006/DataSetView.png" alt="" />

DataSets represent the data extracted from a <em>data source</em>; the extracted data is used as the foundation to create visualizations within Domo. The DataSet API enables you to import data from <em>any</em> source as well as export data to <em>any </em>destination.  Leveraging the API allows you to not only import your data into Domo, but enables you to automate creating Personalized Data Permission (PDP) policies to restrict access to users or groups within Domo to only view specific data within a DataSet.

### DataSet use cases
---
The DataSet API allows you to extend Domo's data platform to support multiple use cases:
<ul>
 	<li>Automate external processes to push smaller sets data that occasionally need to be updated into Domo data pipeline</li>
 	<li>Export aggregated and transformed Domo data for statistical analysis or any need</li>
 	<li>Create user and group access to data within a DataSet through API's Personalized Data Permission (PDP) policies</li>
 	<li>Automate external processes to manage DataSets and update intervals based on retrieving DataSets update information</li>
 	<li>Utilize Upsert operations to insert or update an existing record in a single call</li>
</ul>


<!-- theme: info -->

> #### Best Practice
>There are two APIs that can be used to import data into Domo. The DataSet API should be used to create small DataSets that occasionally need their data updated. For creating and updating massive, constantly changing, or rapidly growing DataSets, the Stream API is recommended. Note: Only DataSets created with the API can be updated via APIs. Note: Pushing data to the API is limited to once per hour for Standard and Standard Trial users.

### Next Steps
---
Read on to get started with the DataSet API

- [DataSet Quickstart](quickstart.md)
- [Import and Export Data](import-and-export-data.md)
- [Manage DataSets](managing-datasets.md)
- [Create Personalized Data Permissions (PDP)](personalized-data-permissions.md)
- [DataSet API Reference](../../API-Reference/Domo-APIs/DataSet-API.yaml)

### Need Additional Help?
---

No problem, we'd love to help. Explore our [documentation](https://knowledge.domo.com), answers to [frequently asked questions](https://dojo.domo.com/main), or join other developers in Domo's [Developer Forum](https://dojo.domo.com/main).  For further help, feel free to [email us](mailto:support@domo.com) or [contact our sales team](mailto:sales@domo.com).

