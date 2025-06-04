---
stoplight-id: b836f5593ab26
---

# Getting Data

App visualizations are powered by datasets that reside in Domo.  One of the first steps to building an app is getting data.  This section will walk you through some of the fundamental tools and features to acquire and transform data.

## Data Center

The Data Center is where you and your app's users create, view, and manage the data sources that will power your app. You can use Data Center to view and manage existing DataSets, track the performance and status of your existing data, combine DataSets into DataFlows, and add connections to new services.

Building your app around easily reproduced and implemented data sources will have a significant impact on customer experience. Unnecessarily complex implementations will reduce the success rate of your users and result in fewer Domo customers using your app.

The Data Center provides four interfaces for Domo customers to interact with their data: DataSets, Data Warehouse, DataFlows, and Accounts:

<strong>DataSets</strong>

You can view and manage existing DataSets and add new datasets for use in Domo. Search for DataSets by name, DataFlow, or user, and review individual datasets for proper structure and content. Use this view to identify out-of-date or malfunctioning DataSets. For any DataSet, you can access a View Details page that provides additional options.

<strong>Data Warehouse</strong>

Data Warehouse is a 3D management console for data discovery, visibility, and administrative control. Use Data Warehouse to monitor data sources and data flows in real time, identify potential issues, and drill down into DataSets and DataFlows to maximize the value you and your users receive from Domo.

<strong>DataFlows</strong>

You can create and manage DataFlows, DataSets created by combining and transforming two or more input DataSets. DataFlows provide a mechanism for automatically transforming data within Domo, leveraging the power of SQL.

<strong>Accounts</strong>

Use the Accounts interface to connect existing DataSets to Domo, such as SalesForce, Qualtrics, or Google Analytics. Domo provides the Sample Data Engine (see below) so that you will not need credentialed access to every Domo connector, however you should be aware of how your app's users will connect with live data through Domo Connectors.

## Connectors

Domo has developed proprietary Connectors that connect your app directly with hundreds of data sources. Building your app to take advantage of pre-existing Connectors gives you an easy way to improve your users' customer experience - simplifying app setup and data integration while enabling more meaningful analysis and visualizations.

For more information about Connectors, including a sampling of Domo's most popular Connectors, go to <a href="https://www.domo.com/connectors" target="_blank" rel="noopener">Domo Connectors</a>

## Data Transforms

Domo DataFlows are built around data transforms, which allow users to manipulate and combine datasets using our Magic ETL tool, MySql, or Amazon's Redshift SQL. Magic ETL (Extract, Transform, and Load) provides a drag-and-drop interface for cleansing, combining, and transforming data without requiring specialized SQL knowledge. You cal also use MySQL or Redshift SQL to create complex transforms to drive better analysis in your apps.

## Domo Appstore Data Resources

The architecture of app datasets is a critical part of building a great app and warrants careful consideration.  For example, creating datasets that can be easily reproduced by Domo's customers will simplify app installation and result in a much better experience for customers.

Some Domo Appstore data resources are available if you're planning to submit your app to the Domo Appstore.  These resources include:

- [Sample Data Engine](../Domo-Marketplace/marketplace-data-resources.md#sample-data-engine)
- [Data Architecture](../Domo-Marketplace/marketplace-data-resources.md#data-architecture)


