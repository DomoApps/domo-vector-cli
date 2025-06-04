---
stoplight-id: 3989acf1bafff
---

# Import and Export Data

Leveraging the power of Domo's data pipeline can be achieved extended with the flexibility of the DataSet API import and export capabilities.  The Domo platform allows you to easily store, transform, aggregate, and query data. As a result, your data can then power rich visualizations or just as easily be shared with other external systems by executing an export of your Domo DataSet.

<!-- theme: info -->

> #### Note
> In order to import or export data you must first have a DataSet created. To learn how to create a DataSet, utilize the [DataSet Quickstart](quickstart.md).

The following details are provided to fully understand the capabilities of the DataSet API for importing and exporting data:

### Prepare data for import
---

<!-- theme: info -->

> #### Best Practice
> There are two APIs that can be used to import data into Domo. The DataSet API should be used to create small DataSets that occasionally need their data updated. For creating and updating massive, constantly changing, or rapidly growing DataSets, the Stream API is recommended. Note: Only DataSets created with the API can be updated via APIs. Note: Pushing data to the API is limited to once per hour for Standard and Standard Trial users.

As you begin the process of importing your data we we recommend you first [review Domo's data format specifications](format-data-to-import.md) before you import.

<!-- theme: info -->

> #### Known Limitation
> The DataSet API only supports importing data in CSV format

### Choosing update method
---
Once creating a new DataSet via the API,  store the DataSet's `dataset_id` or simply retrieve preferred `dataset_id` through the [DataSet API](../../API-Reference/Domo-APIs/DataSet-API.yaml).

With the `dataset_id`, it is important to choose the appropriate `updateMethod` when importing data via the API.  The two choices available are either to `APPEND` or `REPLACE` the data that currently exists in the DataSet.  Choosing `APPEND` will incrementally create new rows of data to the dataset as they are imported through the API. `REPLACE` will completely remove the existing data and refresh the DataSet with all data from the last import via the API.

Defining which method to use when importing data with the API is done through the `updateMethod` parameter as shown in the example below:

```HTTP
PUT https://api.domo.com/v1/datasets/{DATASET_ID}/data?updateMethod=APPEND 
```

In the example above, any data will be added to bottom of the DataSet.

### Single part upload
---
Once you've chosen the type of updateMethod for the data you plan to import you will then need to use the `dataset_id` to make the following request:

#### Sample Request

See this sample request in [Java](https://github.com/domoinc/domo-java-sdk/blob/master/domo-java-sdk-all/src/test/java/com/domo/sdk/datasets/ImportDataExample.java), [Python](https://github.com/domoinc/domo-python-sdk/blob/master/examples/dataset.py).

```HTTP
PUT https://api.domo.com/v1/datasets/317970a1-6a6e-4f70-8e09-44cf5f34cf44/data
Content-Type: text/csv
Authorization: bearer <your-valid-oauth-access-token>

1,2,3
4,5,6
7,8,92
```

Domo will return a response of success or error for the outcome of data being imported into DataSet.

#### Sample Response
```HTTP
HTTP/1.1 204 No Content
```

### Multi-part uploads
---
Sending large amounts of data over HTTP can be problematic.  Even the smallest of network disruptions can render your entire upload corrupted.  We designed the Streams API to help alleviate some of these problems and provide you with the ability to consistently and successfully upload data to your Domo instance.

<!-- theme: info -->

> #### Note
> Only DataSets created with the API can be updated via APIs. Pushing data to the API is limited to once per hour for Standard and Standard Trial users.

A DataSet is your data at rest in your Domo instance. A stream is a simple abstraction that describes your data in motion.

In order to leverage the Stream API, a basic understanding is needed of each step shown in the diagram below:
<p style="text-align: center;"><em>Figure: Stream API Flow</em></p>
<a href="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/08181204/StreamsAPIFlow.png"><img class="aligncenter size-large wp-image-2989" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/06/08181204/StreamsAPIFlow-1024x402.png" alt="" width="1024" height="402" /></a>

&nbsp;

Streams in Domo allow you to import data for multiple use cases:
<ul>
 	<li>Constant import of large amounts of data into a DataSet</li>
 	<li>Updates to existing data on a frequent basis</li>
 	<li>Accelerating the time required to import large DataSets</li>
</ul>
### Quickstart:
---
Creating a stream to then upload data to a DataSet only requires these steps:
<ol>
 	<li>Create a stream</li>
 	<li>Create a stream execution</li>
 	<li>Upload your data</li>
 	<li>Finalize your execution</li>
</ol>
After creating a stream, you can create multiple executions to upload batches of data.

<!-- theme: info -->

> #### Note
>In order to utilize this Quickstart you will need to obtain an [access token](../../API-Reference/Embed-APIs/Embed-Token-API.yaml) or you can leverage any of [Domo's SDKs](../../Getting-Started/sdks.md) which will also handle authentication.

### Step 1: Create a stream

The first step required to upload data to your Domo instance is to create a Stream.  Include a DataSet and an update method in your request body.

The supported update methods are "APPEND" and "REPLACE".

#### Sample Request

See this sample request in [Java](https://github.com/domoinc/domo-java-sdk/tree/master/domo-java-sdk-all/src/test/java/com/domo/sdk/streams/CreateExample.java), [Python](https://github.com/domoinc/domo-python-sdk/blob/master/examples/stream.py).

```bash
$ curl 'https://api.domo.com/v1/streams' -i -X POST -H 'Content-Type: application/json' -H 'Accept: application/json' -H 'Authorization: bearer <your-valid-oauth-access-token>' -d '{
  "dataSet" : {
    "name" : "Leonhard Euler Party",
    "description" : "Mathematician Guest List",
    "rows" : 0,
    "schema" : {
      "columns" : [ {
        "type" : "STRING",
        "name" : "Friend"
      }, {
        "type" : "STRING",
        "name" : "Attending"
      } ]
    }
  },
  "updateMethod" : "APPEND"
}'
```

The response contains a Stream ID.  Keep track of this ID as you will use it for all uploads.  If you ever need to find a Stream ID that is associated with a DataSet, there is a search API.  See the detailed Stream API documentation for more details.

#### Sample Response
```HTTP
HTTP/1.1 201 Created
Location: https://api.local.domo.com/v1/streams/42
Content-Type: application/json;charset=UTF-8
Content-Length: 470

{
  "id" : 42,
  "dataSet" : {
    "id" : "0c1e0dbe-9f71-4625-9b50-b79e6e4266f2",
    "name" : "Leonhard Euler Party",
    "description" : "Mathematician Guest List",
    "rows" : 0,
    "columns" : 0,
    "owner" : {
      "id" : 27,
      "name" : "DomoSupport"
    },
    "createdAt" : "2016-05-27T17:53:04Z",
    "updatedAt" : "2016-05-27T17:53:10Z"
  },
  "updateMethod" : "APPEND",
  "createdAt" : "2016-05-27T17:53:05Z",
  "modifiedAt" : "2016-05-27T17:53:05Z"
}
```

### Step 2: Create a stream execution

After creating a Stream, you now need to create an Execution.  An Execution does a few things.  It creates a line item in the DataSet history, it triggers all animations in the product (for example, the data importing arc in the Data Warehouse UI), and it also tells Domo that you're about to start sending data.

The primary reason to tell Domo that you're starting to upload data (and one of the key benefits of Streams) is that it allows you to break up your data into smaller chunks and parallelize those uploads at the same time.  This can result in huge performance increases and protects you from potential HTTP network issues.  For example, if you break a million rows up into one hundred 10,000 chunks, if one upload fails, you only need re-upload that one failed chunk.

#### Sample Request

See this sample request in [Java](https://github.com/domoinc/domo-java-sdk/tree/master/domo-java-sdk-all/src/test/java/com/domo/sdk/streams/ExecutionCreateExample.java), [Python](https://github.com/domoinc/domo-python-sdk/blob/master/examples/stream.py).

```bash
$ curl 'https://api.domo.com/v1/streams/42/executions' -i -X POST -H 'Content-Type: application/json' -H 'Accept: application/json' -H 'Authorization: bearer <your-valid-oauth-access-token>'
```

The response contains the Execution ID.  Each Stream has it's own incrementing Execution sequence.  The Execution ID is important to keep track of as you'll use it as a path parameter with each part (or chunk) upload you perform.

#### Sample Response
```HTTP
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
Content-Length: 227

{
  "id" : 1,
  "startedAt" : "2016-05-26T22:20:21Z",
  "currentState" : "ACTIVE",
  "createdAt" : "2016-05-26T22:20:21Z",
  "modifiedAt" : "2016-05-26T22:20:21Z"
}
```

### Step 3: Upload your data

As previously mentioned, this step can be parallelized.  How small should you make each part?  That depends on a couple factors.  Generally, the smaller the part, the less likely it is to make it to your Domo instance without a network disruption.  However, there is a lot of overhead incurred by creating too many requests.  We've found that for narrow DataSets (those with around 100 columns or less), somewhere between 10,000 and 100,000 rows works well.

The part ID specified on the request is used to track ordering of the parts as they're reassembled on your Domo instance.  The client is responsible for incrementing these IDs with each part.  It's preferable to start with 1 for each Execution and increment with each subsequent part.

Please Note:  it is preferable that these requests be compressed using gzip.

#### Sample Request

See this sample request in [Java](https://github.com/domoinc/domo-java-sdk/tree/master/domo-java-sdk-all/src/test/java/com/domo/sdk/streams/ExecutionUploadDataPartExample.java), [Python](https://github.com/domoinc/domo-python-sdk/blob/master/examples/stream.py).

```bash
$ echo '"Pythagoras","FALSE"
"Alan Turing","TRUE"
"George Boole","TRUE"
' | gzip -c | curl 'https://api.domo.com/v1/streams/42/executions/1/part/1' -i -X PUT -H 'Content-Type: text/csv' -H 'Accept: application/json' -H 'Authorization: bearer <your-valid-oauth-access-token>' -d @-
```

#### Sample Response
```http
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
Content-Length: 227

{
  "id" : 1,
  "startedAt" : "2016-05-27T15:16:01Z",
  "currentState" : "ACTIVE",
  "createdAt" : "2016-05-27T15:15:59Z",
  "modifiedAt" : "2016-05-27T15:15:59Z"
}
```

If you receive a status code of 200, your data has been received and it is stored until you finish the execution where it is then reassembled prior to indexing.  If you receive a non 200 response, something has happened and you'll need to upload that part again.

### Step 4: Finalize your execution

When you are done uploading all your parts (or chunks of data).  Send a final request that tells your Domo instance that you're done.

#### Sample Request

See this sample request in [Java](https://github.com/domoinc/domo-java-sdk/tree/master/domo-java-sdk-all/src/test/java/com/domo/sdk/streams/ExecutionCommitExample.java), [Python](https://github.com/domoinc/domo-python-sdk/blob/master/examples/stream.py).

```bash
$ curl 'https://api.domo.com/v1/streams/42/executions/1/commit' -i -X PUT -H 'Accept: application/json' -H 'Authorization: bearer <your-valid-oauth-access-token>'
```

#### HTTP Response
```http
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
Content-Length: 227

{
  "id" : 1,
  "startedAt" : "2016-05-27T15:16:01Z",
  "currentState" : "ACTIVE",
  "createdAt" : "2016-05-27T15:15:59Z",
  "modifiedAt" : "2016-05-27T15:15:59Z"
}
```

Congrats. you now have a DataSet with data that you've uploaded from a Multi-part upload using Stream API.

### API Recipe: Upload data in parallel
---
&nbsp;

You have a table containing one billion rows, and want to upload it to a Domo DataSet quickly. To do this, we divide the data in ten groups of 100 million rows, and then upload each part in parallel. Let's walk through this process.
<p class="doc-row-title"><strong>For use with Big Data</strong></p>
Parallel uploading is generally used for massive DataSets, and this guide effectively reviews the Stream API. For small DataSets, please use the DataSet API.
<p class="doc-row-title"><strong>Data Division and Part Size</strong></p>
In this example, we divide one billion rows into ten parts of 100 million rows. In reality, data parts should be at least 50mb in size. The row count for each part varies depending on the number of columns in the datasource, as well as the general length of cell contents. Experimentation with row count per part may be required for each datasource.

#### Parallel Upload Overview
<strong>Data Preparation (one billion row example)</strong>
<ol>
 	<li>Query your database or datasource for the desired result set</li>
 	<li>Convert the result set to a column/row format</li>
 	<li>Partition the result set into groups of 100 million rows (or partition via multiple DB queries/offsets)</li>
 	<li>Convert each group into header-less CSV files (In this example, ten CSV files would be generated)</li>
 	<li>Gzip compress each CSV file (this significantly reduces upload time)</li>
</ol>
<strong>Parallel Upload via Stream Pipeline</strong>
<ol>
 	<li>Create a Stream Execution, or upload job, on the desired Domo DataSet</li>
 	<li>Asynchronously upload all ten gzip files (data parts) in parallel, via the Execution</li>
 	<li>Ensure all ten parts have uploaded successfully, retry any failed parts</li>
 	<li>When all parts have been uploaded, commit the Stream Execution to finalize the upload job</li>
</ol>

#### Parallel Upload Tutorial - Java SDK

The following tutorial features code snippets from a fully executable project, which can be downloaded here.

We begin assuming your data has already been divided into parts, into CSV files on disk.

1 - Create a Domo Dataset via the Upload Accelerator/Stream API, or use an existing DataSet that was created using the Upload Accelerator/Stream API. For example:

```Java
// Define a Domo DataSet Schema
CreateDataSetRequest dataSetRequest = new CreateDataSetRequest();
dataSetRequest.setName("Leonhard Euler Party");
dataSetRequest.setDescription("Mathematician Guest List");
List<Column> columns = new ArrayList<>();
columns.add(new Column(STRING, "Friend"));
columns.add(new Column(STRING, "Attending"));
dataSetRequest.setSchema(new Schema(columns));

// Create the Domo DataSet using the Schema, via the Stream Pipeline API
StreamRequest streamRequest = new StreamRequest();
streamRequest.setDataSet(dataSetRequest);
streamRequest.setUpdateMethod(UpdateMethod.REPLACE);
Stream stream = streamClient.create(streamRequest);
System.out.println("Created:" + stream);
```

2 - Retrieve the Stream ID of the newly created DataSet Stream Pipeline, or the ID of an existing DataSet Stream Pipeline

```Java
// From a newly created/returned Stream Pipeline
long streamId = stream.getId();
```

3 - Compress the CSV files within a temp folder, for convenience

```Java
//Compress the incoming csv files in a temp folder
List<File> csvFiles = loadExampleFiles();
File tempFolder = new File(csvFiles.get(0).getParent() + "/temp/");
if (!tempFolder.exists()){
    tempFolder.mkdir();
}
List<File> compressedCsvFiles = toGzipFilesUTF8(csvFiles, tempFolder.getPath() + "/");

// Gzip functions for convenience. UTF-8 encoding is critical.
public List<File> toGzipFilesUTF8( List<File> sourceFiles, String path){
    List<File> files = new ArrayList<>();
    for (File sourceFile : sourceFiles) {
        String zipFileName = sourceFile.getName().replace(".csv", ".zip");
        files.add(toGzipFileUTF8(sourceFile, path + zipFileName));
    }
    return files;
}

public File toGzipFileUTF8( File csvFile, String zipFilePath){
    File outputFile = new File(zipFilePath);
    try {
        GZIPOutputStream gzos = new GZIPOutputStream(new FileOutputStream(outputFile));
        BufferedReader reader = new BufferedReader(new FileReader(csvFile));

        String currentLine;
        while ((currentLine = reader.readLine()) != null){
            currentLine += System.lineSeparator();
            // Specifying UTF-8 encoding is critical; getBytes() uses ISO-8859-1 by default
            gzos.write(currentLine.getBytes("UTF-8")); 
        }

        gzos.flush();
        gzos.finish();
        gzos.close();

    }
    catch(IOException e) {
        logger.error("Error compressing a string to gzip", e);
    }

    return outputFile;
}
```

4 - Create a Stream Pipeline Execution (Upload job declaration)

```Java
// Create an Execution on the given Stream Pipeline
Execution execution = this.streamClient.createExecution(streamId);
```

5 - Encapsulate each part upload in Java Runnable task, for use with a Java ExecutorService

```java
// Create the asynchronous executor service and task collection
ExecutorService executorService = Executors.newCachedThreadPool();
List<Callable<Object>> uploadTasks = Collections.synchronizedList(new ArrayList<>());

// For each data part (csv gzip file), create a runnable upload task
long partNum = 1;
for (File compressedCsvFile : compressedCsvFiles){
    long myPartNum = partNum;
    // "uploadDataPart()" accepts csv strings, csv files, and compressed csv files
    Runnable partUpload = () -> this.streamClient.uploadDataPart(streamId, execution.getId(), myPartNum, compressedCsvFile); 
    uploadTasks.add(Executors.callable(partUpload));
    partNum++;
}
```

6 - Asynchronously execute the uploads via the Java ExecutorService
```Java
// Asynchronously execute all uploading tasks
try {
    executorService.invokeAll(uploadTasks);
}
catch (Exception e){
    logger.error("Error uploading all data parts", e);
}
```

6 - Commit the Stream Pipeline Execution (Finalize the upload job)

```Java
// Commit the Stream Execution to finalize the multi-part upload
this.streamClient.commitExecution(streamId, execution.getId());
```

7 - Delete the gzip temp folder

```Java
// Delete the temp folder
if (tempFolder.exists()) {
    try {
        Files.delete(tempFolder.toPath());
    }
    catch (Exception e){
        logger.error("Error deleting the compressed csv temp folder");
    }
}
```

In summary, divide your data into compressed CSV files, create a Stream Pipeline Execution, upload all parts asynchronously, and then commit the Execution to finalize the upload job.

### Export Data
---
Domo enables you the power to export data that has been prepared and transformed through Domo's data platform.  

When requesting an export of a DataSet, you may choose to include the column headers and the name of the file.  

You will then need to use the `dataset_id` again in your request as seen below.  In this example you will notice the resulting file exported will include column headers and will be named "Q4_Sales_Data".

#### Sample Request

[yourlang]See this sample request in [Java](https://github.com/domoinc/domo-java-sdk/blob/master/domo-java-sdk-all/src/test/java/com/domo/sdk/datasets/ImportDataExample.java), [Python](https://github.com/domoinc/domo-python-sdk/blob/master/examples/dataset.py).

```HTTP
GET https://api.domo.com/v1/datasets/317970a1-6a6e-4f70-8e09-44cf5f34cf44/data?includeHeader=true&fileName=Q4_Sales_Data.csv 
Accept: text/csv
Authorization: bearer <your-valid-oauth-access-token>
```

Domo will return a response of success or error for the outcome of data being imported into DataSet.

#### Sample Response
```http
HTTP/1.1 200 OK
Content-Disposition: attachment; filename=Q4_Sales_Data.csv

first,second,third
1,2,3
4,5,6
7,8,92
```

### Next Steps
---
Explore more about the DataSet API now that you know how to import and export data.

- [DataSet Quickstart](quickstart.md)
- [Manage DataSets](managing-datasets.md)
- [Create Personalized Data Permissions (PDP)](personalized-data-permissions.md)
- [DataSet API Reference](../../API-Reference/Domo-APIs/DataSet-API.yaml)
- [Stream API Reference](../../API-Reference/Domo-APIs/Stream-API.yaml)

### Need additional help?
---
No problem, we'd love to help. Explore our [documentation](https://knowledge.domo.com), answers to [frequently asked questions](https://dojo.domo.com/main), or join other developers in Domo's [Developer Forum](https://dojo.domo.com/main).  For further help, feel free to [email us](mailto:support@domo.com) or [contact our sales team](mailto:sales@domo.com).


