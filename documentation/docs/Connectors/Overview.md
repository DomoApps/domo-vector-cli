---
stoplight-id: wiemes1rk6atz
---

# Overview

Get data into and out of Domo. Whether data is stored in excel files, databases, cloud tools, on-prem systems, cloud warehouses, or even IoT devices, there are a wide-variety of ways to securely multiply the value of data in Domo.

- **Pre-built connectors**: [Connectors](https://www.domo.com/appstore/apps?appType=Connector) covering the most common data sources and systems.
- **Build your own connector**: Use Domo's [Connector Dev Studio IDE](../Connectors/Custom-Connectors/overview.md) if a pre-built one doesn't exist yet.
- **[Connect via API](../Connectors/API-Data-Connection/overview.md)**: Leverage the DataSet or Streams APIs.
- **[Cloud Amplifier](https://domo-support.domo.com/s/article/4412849158167?language=en_US)**: Native integrations with cross-cloud systems like Snowflake and Databricks.
- **[Federated data queries](../Connectors/federated-queries.md)**: Use federated adapters to query data directly from where you've already hosted it.
- **[Connect to on-prem data](../Connectors/on-premises-data.md)**: Securely upload your on-prem data to Domo using Workbench.
- **[Jupyter Workspaces](https://domo-support.domo.com/s/article/36004740075?language=en_US)**: Domo offers Jupyter Workspaces with both Python and R kernels, which can be used to move data in and out of Domo.
- **[Domo CLI](https://domo-support.domo.com/s/article/360043437733?language=en_US)**: Often useful to ingest massive DataSets.


### Pre-built connectors
---
You can see existing Connectors by navigating to the Connectors page in the [Domo Appstore](https://www.domo.com/appstore/apps?appType=Connector).

<img loading="lazy" src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-connectors-list-misc.png">


### Custom Connectors
---

If an existing Connector doesn't fit your needs, Domo provides the ability to build Custom Connectors through the [Connector Dev Studio IDE](../Connectors/Custom-Connectors/overview.md). There are two kinds of connectors you can build:

1. **[Standard Custom Connector](Custom-Connectors/overview.md)**: Pull data from an external cloud system into a Domo DataSet
2. **[Writeback Connector](Writeback-Connectors/writeback-connectors.md)**: Push DataSets to third-party file storage applications instead of pulling data from those applications into Domo.


### Connect via API
---

You can programmatically interact with Domo DataSets through the DataSet API or the Streams API (for larger DataSets).

Common use-cases:
- [**Import and Export Data**](API-Data-Connection/import-and-export-data.md) into DataSets
- [**Manage DataSets**](../Governance/data-management.md)
  - Change DataSet Owner
  - Update DataSet Schema
- [**Apply Personalized Data Permissions (PDP)**](../Governance/pdp.md) to DataSets

Looking to get started connecting to DataSets via API? Check out the DataSet API [**Quickstart**](API-Data-Connection/quickstart.md).

<!-- theme: info -->

> #### Note
>
> To import data in CSV format, please follow the [**Domo specification for representing data grids in CSV format**](API-Data-Connection/format-data-to-import.md).





