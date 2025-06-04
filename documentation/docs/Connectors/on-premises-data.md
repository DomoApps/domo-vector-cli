# On-Premises Data

### Workbench Add-ons
---

Workbench is a tool that allows you to upload data to Domo from your on-premises systems, and is frequently used to upload data that exists behind your firewall. You can use Domo Workbench to routinely upload data from Excel, CSV, ODBC, QuickBooks, and other data sources to Domo. Workbench can be downloaded from the On Premise section of the Data Center or the admin page in your Domo instance.

### Overview
---
In Workbench 5, Domo has a developer platform that enables you to build your own custom Domo plugins. In this release of the platform we enable you to build your own:
<ul>
 	<li>Data Transport Methods</li>
 	<li>Data Sources</li>
 	<li>Data Transforms</li>
</ul>
The Workbench Developer Platform uses Dynamic-Link Library (DLL) that can be built in your .NET Framework language and IDE of choice and then installed into Workbench through the Plugin Manager.

This platform provides complete flexibility giving you control over creating the connection to your data source, defining how the data will be read and parsed, enabling you to run custom transforms on your data. All this flexibility is managed and maintained within Workbench giving you the benefit of having these custom plugins run in your own data center.

The process is simple:
<ol>
 	<li>Decide what you want to create</li>
 	<li>Determine how you want to build it</li>
 	<li>Leverage our Domo Workbench SDK</li>
 	<li>Install your plugin into Workbench</li>
</ol>

### Deciding what to build
---
Domo allows you to connect to your data no matter where it resides. The Workbench Developer Platform gives you control to determine all aspects of your data acquisition, ingestion, and normalization.

#### Data Transport Methods

The first question is what will you connect to. Using a Data Transport Method plugin you will be able to explicitly define how you will connect to your Data Source. Regardless of whether you are connecting to a database, a file system or a service you will need to define how you will connect Workbench to the system that has the data. This may include URLs, authentication information, or proxy settings. The Data Transport Methods plugin is where you define your connection information.

Workbench provides basic database, local file, remote file, and SFTP/FTP connections out of the box. In most cases one of these existing transport methods will work for your needs, but if other connections are needed you will likely be able to simply customize one of these existing transport methods for your own unique needs. For example maybe you are connecting to a different flavor of database than what Workbench provides support to out of the box. If this is the case you can leverage an existing transport method as a starting point rather than creating your connection from scratch.

Once you have gathered the information you need to make your connection you are ready to move onto the plugin creation step.


#### Data Source Connection

All data is unique and you need to be able to read and understand the data before it can be sent to Domo. The Data Source Connection plugin allows you to create a custom reader that can pull the data into Workbench in a readable manner. For example it may not be enough to pull all the data from an Excel workbook, maybe you need to be more specific and pull only a single sheet or even a specific set of cells from a specific sheet.

With data source connection plugins you can take the raw data source and pick out the specific data points that you need to run your business.


#### Data Transforms

Data never comes quite the way that you want it. Maybe a column name from the report is incorrect, or maybe you need to run some specific algorithm to prepare the data for use by your end customer. The Workbench Developer Platform allows you to build these custom transforms to ensure your data are normalized and ready for use as soon as it gets to Domo.

To build your transforms you will need to know what actions must be taken each time you import your data. Define which columns are needed for the transformation and what the expected outcome will be.

### Deciding how you want to build
---
We understand that developers have a preference before starting to work with Domo. We are using DLLs as the delivery vehicle for the three plugin types we support. This allows you to select from a wide range of base languages to write your plugin. It also means that your plugin will be supported on all the platforms supported by Workbench, meaning your plugin will be useful well beyond your own use.

#### The Workbench SDK

The Workbench SDK is a library that helps you build your Workbench Plugin. This robust set of programming classes provides everything you need from how to work with accounts and authenticate to your data source to logging the execution steps that your plugin takes when executed.

After installing Workbench, the directory <code>C:\Program Files\Domo\Workbench\SDK</code> will contain the SDK documentation along with a Visual Studio plugin and sample project.

The best way to get started though is following the example that we have included with this getting started document.

#### Install your Plugin

Once you have built your plugin and produced a DLL file you simply need to install it into the Workbench environment.

After installing Workbench 5, simply go to the Workbench Plugin Manager by clicking on the more menu and selecting Plugins.

<img class="aligncenter wp-image-115" src="https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-wokbench5-ui.png" alt="plugin manager screen" />

Since we want to add a new plugin, we want to click on the ellipses (…) next to the Search Path field and select Add after you have chosen your directory. The directory you choose should contain another directory containing your plugin.

Once you have installed your plugin it will appear when you work with your DataSet Job. If you created a Transport Method or Data Source Connection you will be able to select your new option when creating or editing a DataSet Job. If you created a new Transform then you will be able to select your Transform as an option when you create a new transform for your DataSet Job.

### Additional Resources
---
For additional help using Workbench refer to the following guides and articles:
- [Connecting to Data Using Workbench 5](https://knowledge.domo.com/Connect/Connecting_to_Data_Using_Workbench_5)
- [Workbench 5 FAQs](https://knowledge.domo.com/Connect/Connecting_to_Data_Using_Workbench_5/13Workbench_5_FAQs)
- [Common Workbench errors](https://knowledge.domo.com/Connect/Connecting_to_Data_Using_Workbench_5/Common_Workbench_Errors)
