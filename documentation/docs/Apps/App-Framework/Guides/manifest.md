---
stoplight-id: af407395c766b
---

# The Manifest File

The manifest file is the configuration file used to provide meta-data about an App Design and the resources that it needs access to in Domo. The manifest file should be placed in the base directory of the App Design and should be named <strong>manifest.json</strong>.


Property | Type  | Description | Notes | Required | Guide
---------|----------|--------- | ---------- | ----------- | -------
 `name` | String | The name of App Design | An App Design can have many App Instances (Cards in Domo) - each App Instance has its own name. | Required |
 `version` | String | The version of your App Design. | | Required |
 `size` | Object | The size of your App.  | Object with `width` and `height` properties defined on a scale of 1-6 | Required |
 `fullpage` | Boolean | Allows the app to be viewed in full page mode.  |  | Optional | 
 `datasetsMapping` | List of Objects | A list of Datasets that the App Design uses. | Each object corresponds to one Dataset and should include an `alias`, `dataSetId`, and `fields` property. If the App Design doesn't use Datasets, `datasetsMapping` can be an empty list `[]`| Required |
 `collections` | List of Objects | A list of AppDB collections that the App Design uses  | Each object corresponds to one AppDB collection and should include a `name`, `schema` (optional), and `syncEnabled` property. If your App Design leverages AppDB collections, you'll also need to setup a `proxyId` property in the manifest file. | Optional | [AppDB API](../../../Domo-App-APIs/AppDB-API.md)
 `workflowMapping` | List of Objects | A list of Workflows that the App Design uses.  | Each object corresponds to one Workflow and should include an `alias` and `parameters` property. If your App Design leverages Workflows, you'll also need to setup a `proxyId` property in the manifest file.| Optional | [Hitting a Workflow from an App](hitting-a-workflow.md)
  `packageMapping` | List of Objects | A list of Code Engine packages that the App Design uses.  | Each object corresponds to one Code Engine package and should include an `alias`,  `parameters` (if applicable), and `output` property. If your App Design leverages Code Engine packages, you'll also need to setup a `proxyId` property in the manifest file.| Optional | [Hitting Code Engine from an App](hitting-code-engine-from-an-app.md)
`ignore` | List | Instructs the CLI to ignore certain files when publishing.  | Accepts an array of glob patterns. | Optional |
  `id` | String | This is a unique identifier for your App Design.  | It is added to the manifest automatically by the command line tool the first time you publish your design via `domo publish`. | Required |
  `proxyId` | String | This is an id of a card you want to impersonate.  | It is required if you want to be able to develop locally against Domo Workflows, Code Engine, or AppDB. | Optional | [Getting a proxyId](https://developer.domo.com/portal/af407395c766b-the-manifest-file#getting-a-proxyid-advanced)


### Example Manifest
---
Here is an example demonstrating a complete manifest file.

```json
{
    "name": "My App Design",
    "version": "0.0.1",
    "fullpage": true,
    "size": {
        "width": 4,
        "height": 3
    },
    "datasetsMapping": [
        {
        "alias": "sales",
        "dataSetId": "5168da8d-1c72-4e31-ba74-f609f73071dd",
        "fields": [
            {
                "alias": "amount",
                "columnName": "Sales Amount"
            },
            {
                "alias": "name",
                "columnName": "Client Name"
            },
            {
                "alias": "startDate",
                "columnName": "Contract Initiation Date"
            }
        ]
        }
    ],
    "collections": [
      {
        "name": "CommentsTable",
        "schema": {"columns": 
              [{"name": "user", "type": "STRING"}, 
                {"name": "comment", "type": "STRING"}]
          },
        "syncEnabled": true
      },
      {
        "name": "Users"
      }
    ],
    "workflowMapping": [
      {
        "alias": "workflow1",
        "parameters": [
          {
            "aliasedName": "num1",
            "type": "number",
            "list": false,
            "children": null
          },
          {
            "aliasedName": "num2",
            "type": "number",
            "list": false,
            "children": null
          }
        ]
      },
      {
        "alias": "workflow2",
        "parameters": [
          {
            "aliasedName": "thing1",
            "type": "number",
            "list": false,
            "value": 2,
            "children": null
          },
          {
            "aliasedName": "thing2",
            "type": "number",
            "list": false,
            "children": null
          }
        ]
      }
    ],
    "packageMapping": [
      {
        "alias": "awesomeFunction",
        "parameters": [
          {
            "alias": "number1AppInput",
            "type": "number",
            "nullable": false,
            "isList": false,
            "children": null
          },
          {
            "alias": "number2AppInput",
            "type": "number",
            "nullable": false,
            "isList": false,
            "children": null
          }
        ],
        "output": {
          "alias": "sumAppOutput",
          "type": "number",
          "children": null
        }
      }
    ]
}
```

*Note*: The `id` field is automatically added to the manifest by the `domo` command line tool the first time it is published via `domo publish`.


### name
---
This is the name of the design as it will appear in Domo. This is the name that users will look for when creating a card that is based off of your design.


### version
---
This is the current version of your design, and should follow [semantic versioning](http://semver.org/) guidelines.

> MAJOR version when you make incompatible API changes,
>
> MINOR version when you add functionality in a backwards-compatible manner, and
>
> PATCH version when you make backwards-compatible bug fixes.

Sometimes it can be helpful to display what version the app is running on. Since the version can be changed between building and deploying it's better to get the version this way:

```js
const version = await fetch('./manifest.json').then(res => res.json()).then(manifest => manifest.version)
```


### size
---
The size of the app cannot be defined in pixels. It can only be defined in Domo card sizes. To better understand how card sizing relates to pixels, see the chart below:
<table class="t1" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td class="td1" valign="middle">
<p class="p1"><span class="s1"><b>Card Size</b></span></p>
</td>
<td class="td2" valign="middle">
<p class="p1"><span class="s1"><b>Width (px)</b></span></p>
</td>
<td class="td3" valign="middle">
<p class="p1"><span class="s1"><b>Height (px)</b></span></p>
</td>
</tr>
<tr>
<td class="td1" valign="middle">
<p class="p1"><span class="s1">6</span></p>
</td>
<td class="td2" valign="middle">
<p class="p1"><span class="s1">1400</span></p>
</td>
<td class="td3" valign="middle">
<p class="p1"><span class="s1">1700</span></p>
</td>
</tr>
<tr>
<td class="td4" valign="middle">
<p class="p1"><span class="s1">5</span></p>
</td>
<td class="td5" valign="middle">
<p class="p1"><span class="s1">1165</span></p>
</td>
<td class="td6" valign="middle">
<p class="p1"><span class="s1">1410</span></p>
</td>
</tr>
<tr>
<td class="td1" valign="middle">
<p class="p1"><span class="s1">4</span></p>
</td>
<td class="td2" valign="middle">
<p class="p1"><span class="s1">930</span></p>
</td>
<td class="td3" valign="middle">
<p class="p1"><span class="s1">1120</span></p>
</td>
</tr>
<tr>
<td class="td4" valign="middle">
<p class="p1"><span class="s1">3</span></p>
</td>
<td class="td5" valign="middle">
<p class="p1"><span class="s1">695</span></p>
</td>
<td class="td6" valign="middle">
<p class="p1"><span class="s1">830</span></p>
</td>
</tr>
<tr>
<td class="td1" valign="middle">
<p class="p1"><span class="s1">2</span></p>
</td>
<td class="td2" valign="middle">
<p class="p1"><span class="s1">460</span></p>
</td>
<td class="td3" valign="middle">
<p class="p1"><span class="s1">540</span></p>
</td>
</tr>
<tr>
<td class="td4" valign="middle">
<p class="p1"><span class="s1">1</span></p>
</td>
<td class="td5" valign="middle">
<p class="p1"><span class="s1">225</span></p>
</td>
<td class="td6" valign="middle">
<p class="p1"><span class="s1">250</span></p>
</td>
</tr>
<tr>
<td class="td1" valign="middle">
<p class="p1"><span class="s1">0.5</span></p>
</td>
<td class="td2" valign="middle">
<p class="p1"><span class="s1">NA</span></p>
</td>
<td class="td3" valign="middle">
<p class="p1"><span class="s1">105</span></p>
</td>
</tr>
</tbody>
</table>

<!-- theme: warning -->
> #### Warning
>
> If height and width is unspecified, the card will default to 1x1 Domo card sizing.

Card size is measured by the number of medium cards that would fit along a dimension. For example, an app with the size 4x3 will be 4 medium cards wide and 3 medium cards tall. This allows an app to maintain consistent sizing when being viewed alongside other cards within Domo.

```json
{
    "name": "My Design",
    "size": {
        "width": 4,
        "height": 3
    }
}
```

### fullpage
---
The `fullpage` property consists of a boolean value that can allow the app to be viewed in full page mode.

If you want you to build your app so that it is responsive, you can enable the `fullpage` property in your manifest file. When this property is enabled the iFrame that contains the Custom App will resize as the browser window size changes. This resizing is for the card Details view. You as a developer will need to respond to the resizing events and adjust your app’s presentation accordingly. Custom Apps that do not have the `fullpage` property set to ‘true’ will have the iFrame size remain constant. The `fullpage` property retains the Domo header, navigation, and card action options.  In addition, any information displayed in the footer is available by scrolling to the bottom of the Custom App.  

The `fullpage` property consists of a boolean value.
 
```
{
  "name": "My fullpage app",
  "fullpage": true
}
```

### id
---
This is a unique identifier for your design. It is added to the manifest automatically by the command line tool the first time you publish your design via `domo publish`.

### ignore
---
This optional property instructs the CLI to ignore certain files when publishing. It accepts an array of glob patterns.
Examples:

`["*.css"]` would ignore all CSS files.

`["src/**/*", "sample/**/*"]` would ignore everything in `src/` and `sample/` directories.

If your app contains a `node_modules` directory that will be ignored as well.

### datasetsMapping
---
The `datasetsMapping` property consists of a list of DataSet mappings that the design uses. Each DataSet mapping object has the following format.

```json
{
    "name": "My Design",
    "datasetsMapping": [
        {
        "alias": "sales",
        "dataSetId": "5168da8d-1c72-4e31-ba74-f609f73071dd",
        "fields": [
            {
                "alias": "amount",
                "columnName": "Sales Amount"
            },
            {
                "alias": "name",
                "columnName": "Client Name"
            },
            {
                "alias": "startDate",
                "columnName": "Contract Initiation Date"
            }
        ]
        }
    ]
}
```

As seen above, the properties in the datasetsMapping object are as follows.

* alias
* dataSetId
* fields

#### alias

The DataSet alias is the name that is used to refer to this DataSet. Since users can wire up their app to any DataSet they choose, an alias is needed for the design to refer to the DataSet.

This alias is used by the design to request data using HTTP GET requests.

```javascript
data/v1/[DataSet Alias]
```

For example, if a design were requesting the data in the DataSet aliased as `sales`, it may make a request like this.

```javascript
var xhr = new XMLHttpRequest();
xhr.open('GET', 'data/v1/sales', true);

xhr.onload = function (e) {
    var json;

    if (this.status == 200) {
        json = JSON.parse(xhr.response);
        // process data here
    }
};

xhr.send();
```

Or using jQuery like this.

```javascript
$.get( 'data/v1/sales', function (json) {
    // process data here
});
```

#### dataSetId

This is the unique id representing the DataSet that is used to provide data to this alias. This id can be obtained by viewing the DataSet in Domo and looking at the url.

```
https://company.domo.com/datasources/f3bd3e25-b686-401d-ad2f-a414f4ea61f4
```

#### fields

This property contains information about what fields are included in responses when a DataSet is requested. More specific information about the `fields` property is contained in the Field Mapping section below.

### Field Mapping

The `fields` property of a DataSet mapping may contain a list of fields, or columns, from the DataSet that the app uses.

A `field` object looks like this.

```json
{
    "alias": "amount",
    "columnName": "Sales Amount"
}
```

A field object has the following properties.

* alias
* columnName

*Note*: If the `field` property is empty and does not contain any `field` objects, then all columns from the DataSet will be returned when the DataSet requests data. Since no field aliases are defined in this case, the original column names are used to index the data.

#### alias

This is the name used to refer to a specific column in a DataSet. When data is requested, it is returned in the following array-of-objects format.

```json
[
    {"first": "Joe", "last": "Jacobs", "age": 39},
    {"first": "Henry", "last": "Woolington", "age": 23}
]
```

In this example, `first`, `last`, and `age` are the aliases that were defined in the manifest for the design that requested this data.

This allows the design to easily access the data by name like this.

```javascript
function printData(json) {
    var obj = json[0];
    console.log(obj.first, obj.last, obj.age);
}
```

*Note*: If the `fields` property in a DataSet mapping is left empty (i.e. no field objects are defined), then the original column names from the DataSet will be used in place of the field alias.

#### columnName

This is the actual name of the column in the DataSet that the field alias gets mapped to.


### Getting a proxyId (Advanced)
---
Apps using DQL, writeback, or oAuth features are required to supply an proxyId as part of the proxy configuration. This includes use of AppDB, Workflows, and Code Engine. The `proxyId` allows the proxy to know how to properly route requests. The `proxyId` can be found as part of the URL for the iframe in which your app is displayed. It will be of the form XXXXXXXX-XXXX-4XXX-XXXX-XXXXXXXXXXXX. To find the ID:
<ol>
 	<li>Make sure the app has been published at least once with Domo Publish</li>
 	<li>Publish a new card based on your app design, or navigate to an existing card made from your app design</li>
 	<li>Right-click anywhere in the card and choose "Inspect element"</li>
 	<li>Find the &lt;iframe&gt;that contains your app's code. The URL should be of the form //{HASH}.domoapps.prodX.domo.com?userId=...</li>
 	<li>Copy the ID found between //and .domoapps. That is your app's proxyId
proxyIds tie apps to cards. If you delete the card from which you retrieved the proxyId, you will have to get a new one from another card created from your app design.</li>
 	<li>Add proxyId=”XXXXXXXX-XXXX-4XXX-XXXX-XXXXXXXXXXXX” to your manifest after your designId.</li>
</ol>
&nbsp;
