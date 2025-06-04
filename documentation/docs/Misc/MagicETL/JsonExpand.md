## JSON Expand Action

### Overview

This action takes as an input a column of JSON data and returns tabular data. The action config provides tools to construct a JSON operation tree customized to the shape of any JSON data and provides controls on formatting/outputting data in a tabular format.

### Configuring the JSON Expand Action

#### Select a source column

The source column specifies where the JSON data will be pulled from on each run on the dataflow

#### JSON Operations

Within the JSON Expand action, there are 3 major types of operations:

- Expand into **columns**
- Expand into **rows**
- Create **column**

#### JSON Operations fundamentals

1. The source column can have 1 nested JSON operation. _(A column operation will be selected by default)_
2. **Expand** operations can have other **Expand** operations or **Column** operations nested on them.
3. **Column** operations represent the leaf nodes of the JSON operation tree. These cannot have any other operations nested on them.
4. There can only exist 1 **Exapnd into rows** operation at each level of the tree.

##### Expand into columns

> _This type of operation can operate on either JSON objects or JSON arrays._

###### JSON Object

"Expand **object** into columns" takes in a JSON object and allows a new JSON operation to be configured for each key of the object.

###### JSON Array

"Expand **array** into columns" takes in a JSON array and allows a new JSON operation to be configured for each index of the array.

##### Expand into rows

> _This type of operation can operate on either JSON objects or JSON arrays._

Any nested operations of an "Expand into rows" operation will be applied to all elements of the JSON object or JSON array.

###### JSON Object

"Expand **object** into rows" takes in a JSON object and creates a new row per value/key pair on the object. A key column and a value column will also be created.

###### JSON Array

"Expand **array** into rows: takes in a JSON array and creates a new row per index of the array.

##### Create column

> _This type of operation can operation on any JSON data_

This type of operation allows a name and type to be specified for the data that goes into this column. This operation can be attached at any point to the output of an Expand operation or to the source column itself.

#### The JSON Operation Graph

In the JSON Expand action, the operation graph provides an easy way to navigate and configure different sections of the JSON data. The first node of the graph represents the selected source column and each subsequent node of this graph represents a configurable JSON operation that will act on that data.

##### Navigating the graph

The graph can be navigated horizontally or vertically. Each node lists it's nested operations. Clicking on one of these children from the list will open that operation to the right of the current node.

#### Additional Tools

Configuring a tree of nested JSON operations can quickly become complex. While configuring a JSON Expand action it may also be difficult to do so without a sample of the JSON data expected to come into the tile during the execution of the dataflow. To help improve the authoring experience 2 tools are provided in the configuration window.

##### Sample JSON Editor

The Sample JSON Editor provides a space to mock the JSON data expected to come into the action during the execution of the dataflow. This editor provides quick formatting tools to edit and view JSON data. If there is valid JSON present in this editor, the operation graph will draw from the data to populate different branches of the operation tree when possible.

Rather than inputting JSON data manually, clicking the "Populate from preview" will run a preview of the execution and provide a sample of that data for use while configuring the action.

> Using a combination of the "Populate from preview" and "Auto-Configure" tools can be a powerful combination for turning JSON data into tabular data in a matter of seconds.

##### Auto-Configuration

When the "Auto-Configure" button is clicked, it will draw from the sample JSON provided and create a tree of JSON operations to turn the data into tabular format according to DOMO's predetermined JSON parsing algorithm.

This tool provides a great way to get a jump start on configuring the action, allowing for modification wherever different output is desired.

##### JSON to Table Preview

Perhaps the most powerful tool provided in the configuration window is the ability to view a live preview of the sample output of the action. By navigating to the table preview tab, columns and rows will be added to the table as they are configured in the configuration graph above it.

When used in conjunction with Sample JSON, this tool provides a very quick way to recieve feedback on what the output of the action will look like.

Clicking on any of the column headers in the table will navigate to the operation in the graph above that configured it. This provides a very easy way to navigate a complex tree of JSON operations.

#### Configuring a JSON Operation

##### Selecting a different JSON operation

Each node of the graph represents a JSON operation. Each node provides the option to switch to a different type of JSON operation.

##### Custom JSON keys & indices

This configuration tool provides an alternative route to configuring the JSON operation tree. Rather than including all expected keys and indices in the sample JSON, these keys and indices can be provided directly to each **Expand** operation node on the graph. When adding a custom key, this will result in the default creation of a Column Operation that can then be switched to the desired operation type.

##### Ignore JSON

There may be part of the data that should be ignored and not output. By clicking the checkbox next to each key or index of an **Expand** operation, that entire section of the tree will be ignored. This is helpful for focusing on the most important JSON data.

The "add all" and "ignore all" buttons provide a quick way to ignore or show all the data in a JSON operation.
