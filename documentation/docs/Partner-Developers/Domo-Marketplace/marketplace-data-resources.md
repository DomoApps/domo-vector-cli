---
stoplight-id: 6ea9fcd9e478c
---

# Appstore Data Resources

App visualizations are powered by DataSets that reside in Domo. The architecture of app DataSets is a critical part of building a valuable app and warrants careful consideration. For example, creating DataSets that can be easily reproduced by Domo customers simplifies app installation and results in an improved customer experience. This page introduces you to data resources and information that will help you create apps with optimal data architectures.

## Sample Data Engine

If you don’t have credentials to all the Connectors available on Domo (don’t worry, we don’t expect you to), then you’ll want to utilize our Sample Data Engine to power your budding app.

The Sample Data Engine is a powerful tool to give you the data you need from the most widely used Connectors so you can focus on building your app rather than producing compatible, fictitious data.

Modocorp, the fictitious company on which the Sample Data Engine reports are based, is a large, technical company with an affinity for using as many applications as possible--and for maintaining relationships between those applications. For example, you’ll see the same employees in their HR system, as well as in their recruiting and hiring systems; likewise, you’ll see the same customer base in their PM and CRM systems.

When you use the Sample Data Engine to power your visualizations, there are no surprises between you and your customers. Though fictitious, the DataSets you’ll find in the Sample Data Engine maintain compatibility with the real Connectors, so your customers will see the same data you submit to the Domo Appstore when initially installed, simplifying their data connection experience by removing the guesswork of data provenance.

Overall benefits to powering your development with Sample Data Engine reports:

1. Compatible with the most widely used Connectors
2. Provides real-to-life fictitious data
3. Complies with sensitive data requirements
4. Bridges the gap between the one-source requirement and your multiple connector apps

## Data Architecture

Data is the lifeblood of your app. It shapes your design, powers your visualizations, and provides the valuable insights your customers are seeking in Domo. As a publisher, you will have access to powerful tools which you can use to manipulate your data to provide enriched insights for your customers. The way you choose to architect your data has a significant impact on the usability and value proposition of your app.

One of the most important architectural considerations you will need to make as a publisher is which data sources your app will support. The Domo Sample Data Engine provides data from the most popular systems in use today, but it is up to you to decide which sources you want to support. The more data sources you support, the more potential customers you will have. To support more than one data source (or a combination of data sources), you will need to choose from two high-level architectures, each with its own pros and cons. In this section, we will review each architecture and its corresponding powerup experience from both the publisher and customer perspectives.

### Architecture 1 - System-Specific Data

The first architectural model for supporting multiple data sources involves building and publishing a separate version of your app for each system (or combination of systems) you want to support. The benefit of this model is that your customer's data is more likely to match the sample data grids powering your app, thus making powerup a snap. However, it requires that you, the publisher, build and maintain multiple versions of your app.

#### Publisher Experience

![dev_how_to copy-01](https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/02/17003807/dev_how_to-copy-01.jpg)

![dev_how_to copy-02](https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/02/17003807/dev_how_to-copy-02.jpg)

![dev_how_to copy-03](https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/02/17003807/dev_how_to-copy-03.jpg)

![dev_how_to copy-04](https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/02/17003807/dev_how_to-copy-04.jpg)

![PublisherExperience1[5]](https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/03/08173205/PublisherExperience15.png)

#### Customer Experience

![dev_how_to copy-07](https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/02/17003807/dev_how_to-copy-07.jpg)

![dev_how_to copy-08](https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/02/17003807/dev_how_to-copy-08.jpg)

### Architecture 2 - System-Agnostic Data

The second architectural model for supporting multiple data sources involves authoring generic sample data grids for your customers to map onto from the system of their choice. The benefit of this model is that you only need to maintain a single listing for your app. However, your customers must do a little more technical lifting on their side to power it up.

#### Publisher Experience

![PublisherExperience2[0]](https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/03/08173205/PublisherExperience20.jpeg)

![PublisherExperience2[1]](https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/03/08173205/PublisherExperience21.jpeg)

![PublisherExperience2[2]](https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/03/08173205/PublisherExperience22.jpeg)

![PublisherExperience2[3]](https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/03/08173205/PublisherExperience23.jpeg)

![PublisherExperience2[4]](https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/03/08173205/PublisherExperience24.jpeg)

![PublisherExperience2[5]](https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/03/08173205/PublisherExperience25.jpeg)

#### Customer Experience

![dev_how_to copy-15](https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/02/17003807/dev_how_to-copy-15.jpg)

![dev_how_to copy-16](https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/02/17003807/dev_how_to-copy-16.jpg)

![dev_how_to copy-17](https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/02/17003807/dev_how_to-copy-17.jpg)

## Other Resources

For information about other data topics--such as the Data Center, data transforms, or Connectors--follow the links below:

- [No Code Story Apps](https://domo-support.domo.com/s/article/360043428433?language=en_US)
- [App Developer Framework Getting Data Guide](../../Apps/App-Framework/Guides/getting-data.md)
