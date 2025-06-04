---
stoplight-id: u3ejmw0namdxf
---

# Federated V1 to V2 Migration APIs

These APIs leverage a Domo access token that you can generate in the admin panel from within your Domo instance. [Instructions on generating your access token can be found here](https://domo-support.domo.com/s/article/360042934494?language=en_US).

## Prerequisites

### Federated Architecture: Standard vs. Agent

Please go through the Federated V2 setup instructions found at https://domo-support.domo.com/s/article/360042932974?language=en_US and decide whether you will be utilizing a Standard Federated Architecture, or a Federated Agent Architecture.

### Create Federated V2 Accounts

Migrating Federated V1 datasources to V2 requires that Federated V2 accounts of the matching integration type (MySQL, Snowflake, Postgres, etc.) be created in the Domo platform prior to attempting migration. To create these Federated V2 accounts, first please contact your Domo account representative to ensure that Federated V2 has been enabled in your Domo instance.

Once Federated V2 has been enabled, create the necessary Federated V2 account(s) by repeating the following steps as many times as needed:

1. Navigate to the Domo Datacenter page, then the DataSets view on that page.
   ![Dataset navigation example](../../../assets/images/image-2024-4-25_8-21-5.png)

2. Click on the Federated button to open the Federated / Cloud Amplifier start screen.
   ![Federated integration example](../../../assets/images/image-2024-4-25_8-23-51.png)

3. Select the Federated integration type matching the V1 datasource(s) to migrate. If you do not see a matching integration type, click on the 'See More' option.
   ![Federated see more example](../../../assets/images/image-2024-4-25_8-26-24.png)

4. In the opened 'Connect a Federated DataSet' dialog, click the 'Add New Account' button.
   ![add new account example](../../../assets/images/image-2024-4-25_8-28-9.png)

5. Complete the displayed form and click the now enabled 'Connect' button to finish creating the account.

### List Federated Integration Types

Retrieves a list of the Federated integration types matching integrations that exist in the Domo instance.

**URL**: `https://{domo-domain}/api/query/migration/federated/v1/to/v2/types`

**URL Parameters**:

- `domo-domain`: The fully qualified domain of the Domo instance housing the Federated integrations.

**HTTP Method**: GET

**Response Content-Type**: JSON

**Response Sample**

```json
["mysql-federated", "snowflake-federated"]
```

**Sample cURL Command**

```curl
curl 'https://{domo-domain}/api/query/migration/federated/v1/to/v2/types' \
  -H 'accept: application/json,*/*;q=0.8' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'cache-control: max-age=0' \
  -H 'X-DOMO-Developer-Token: {developer-token}'
```

### List Federated V2 Accounts by Integration Type

Retrieves a list of Federated V2 accounts matching the provided Federated integration type. The accounts returned are ones accessible to the calling user, and my change depending on that user's permissions.

**URL**: `https://{domo-domain}/api/query/migration/federated/v1/to/v2/accounts/{integration-type}`

**URL Parameters**:

- `domo-domain`: The fully qualified domain of the Domo instance housing the Federated integrations.
- `integration-type`: One of the in-use federated integration types returned from the List Federated Integration Types API.

**HTTP Method:** GET

**Response Content-Type**: JSON

**Response Sample**

```json
[
  {
    "id": "2",
    "type": "mysql-federated",
    "name": "mysql v2 agent"
  },
  {
    "id": "1",
    "type": "mysql-federated",
    "name": "mysql v2"
  }
]
```

**Sample cURL Command**

```curl
curl 'https://{domo-domain}/api/query/migration/federated/v1/to/v2/accounts/{integration-type}' \
  -H 'accept: application/json,*/*;q=0.8' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'cache-control: max-age=0' \
  -H 'X-DOMO-Developer-Token: {developer-token}'
```

### List Federated V1 Migration Candidate Datasources by Account

Retrieves a list of migration candidate datasources matching the provided Federated V2 account.

**URL**: `https://{domo-domain}/api/query/migration/federated/v1/to/v2/candidates/{account-id}`

**URL Parameters**:

- `domo-domain`: The fully qualified domain of the Domo instance housing the Federated integrations.
- `account-id`: The unique ID of one of the Federated V2 accounts returned from the List Federated V2 Accounts by Integration Type API.

**HTTP Method**: GET

**Response Content-Type**: JSON

**Response Sample**

```json
[
  {
    "id": "495e28ec-6c07-41fc-99ed-b2dce9a5f569",
    "name": "MySQL Table 1",
    "migrated": false,
    "migrationDate": null
  },

  {
    "id": "F495e28ec-6c07-41fc-99ed-b2dce9a5f569",
    "name": "MySQL Table 2",
    "migrated": false,
    "migrationDate": null
  }
]
```

**Sample cURL Command**

```curl
curl 'https://{domo-domain}/api/query/migration/federated/v1/to/v2/candidates/{account-id}' \
  -H 'accept: application/json,*/*;q=0.8' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'cache-control: max-age=0' \
  -H 'X-DOMO-Developer-Token: {developer-token}'
```

### Migrate Federated V1 Datasource to V2

Migrates the provided Federated V1 datasource to V2, associating it with the provided Federated V2 account.

**URL**: `https://{domo-domain}/api/query/migration/federated/v1/to/v2/{datasource-id}/accounts/{account-id}`

**URL Parameters**:

- `domo-domain`: The fully qualified domain of the Domo instance housing the Federated integrations.
- `datasource-id`: The unique ID of one of the Federated V1 datasources returned from the List Federated V1 Migration CandidateDatasources by Account API.
- `account-id`: The unique ID of one of the Federated V2 accounts returned from the List Federated V2 Accounts by Integration Type API.

**Request Body Properties:**

- `catalog`: Case-sensitive name of the catalog/database of the database table the Federated V1 datasource is referencing.
- `schema`: Case-sensitive name of the schema of the database table the Federated V1 datasource is referencing. May be the literal 'NULL' if the database does not utilize schemas.
- `table`: Case-sensitive name of the database table the Federated V1 datasource is referencing.

**Request Body Sample**

```json
{
  "catalog": "MyCatalogName",
  "schema": "MySchemaName",
  "table": "MyTableName"
}
```

**HTTP Method**: POST

**Response Content-Type**: JSON

**Response Properties**:

- `toe`: Unique identifier of the migration request.
- `datasourceId`: Unique identifier of the datasource migration was requested for.
- `direction`: Direction of the migration. Will be 'V1_TO_V2'.
- `startTime`: Starting date and time of the migration.
- `state`: Final state of the migration, one of `["COMPLETE", "INCOMPLETE", "ABORTED"]`.
  - COMPLETE: Migration has completed successfully.
  - INCOMPLETE: Migration failed after some changes to the datasource were made. Domo content powered by the datasource may remain unavailable and/or non-functional until the migration is re-attempted and completes successfully. More information can be found in the 'errorMessage' property.
  - ABORTED: Migration was aborted prior to any changes being made to the datasource. More information can be found in the 'errorMessage' property.
- `errorMessage`: Message populated with additional details when a migration fails to complete normally or is aborted prior to starting.
- `endTime`: Timestamp indicating the end time of the migration.
  Response Sample

```json
{
  "toe": "DM4X9GT6H5-5ERQX-MPDO6",
  "datasourceId": "495e28ec-6c07-41fc-99ed-b2dce9a5f569",
  "direction": "V1_TO_V2",
  "startTime": "2024-04-15T19:48:00.073+00:00",
  "state": "COMPLETE",
  "errorMessage": null,
  "endTime": "2024-04-15T19:48:02.410+00:00"
}
```

**Sample cURL Command**

```curl
curl 'https://{domo-domain}/api/query/migration/federated/v1/to/v2/{datasource-id}/accounts/{account-id}' \
  -X POST \
  -H 'content-type: application/json' \
  -H 'accept: application/json,*/*;q=0.8' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'cache-control: max-age=0' \
  -H 'X-DOMO-Developer-Token: {developer-token}' \
  -d '{"catalog":"{catalog-name}","schema":"{schema-name}","table":"{table-name}"}'
```

### Reverse Federated V1 to V2 Datasource Migration

Reverses the migration of the provided Federated V1 datasource to V2.

**URL**: `https://{domo-domain}/api/query/migration/federated/v1/to/v2/{datasource-id}/reverse`

**URL Parameters**:

- `domo-domain`: The fully qualified domain of the Domo instance housing the Federated integrations.
- `datasource-id`: The unique ID of one of the Federated V1 datasources returned from the List Federated V1 Migration CandidateDatasources by Account API.

**HTTP Method**: POST

**Response Content-Type**: JSON

**Response Properties**:

- `toe`: Unique identifier of the migration reversal request.
- `datasourceId`: Unique identifier of the datasource migration reversal was requested for.
- `direction`: Direction of the migration reversal. Will be 'V2_TO_V1'.
- `startTime`: Starting date and time of the migration reversal.
- `state`: Final state of the migration reversal, one of `["COMPLETE", "INCOMPLETE", "ABORTED"]`
  - COMPLETE: Migration reversal has completed successfully.
  - INCOMPLETE: Migration reversal failed after some changes to the datasource were made. Domo content powered by the datasource may remain unavailable and/or non-functional until the migration reversal is re-attempted and completes successfully. More information can be found in the 'errorMessage' property.
  - ABORTED: Migration reversal was aborted prior to any changes being made to the datasource. More information can be found in the 'errorMessage' property.
- `errorMessage`: Message populated with additional details when a migration reversal fails to complete normally or is aborted prior to starting.
- `endTime`: Timestamp indicating the end time of the migration reversal.

**Response Sample**

```json
{
  "toe": "DM4X9GT6H5-5ERQX-MPDO6",
  "datasourceId": "495e28ec-6c07-41fc-99ed-b2dce9a5f569",
  "direction": "V2_TO_V1",
  "startTime": "2024-04-15T19:48:00.073+00:00",
  "state": "COMPLETE",
  "errorMessage": null,
  "endTime": "2024-04-15T19:48:02.410+00:00"
}
```

**Sample cURL Command**

```curl
curl 'https://{domo-domain}/api/query/migration/federated/v1/to/v2/{datasource-id}/reverse' \
  -X POST \
  -H 'content-type: application/json' \
  -H 'accept: application/json,*/*;q=0.8' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'cache-control: max-age=0' \
  -H 'X-DOMO-Developer-Token: {developer-token}'
```
