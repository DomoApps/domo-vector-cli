# Federated V2 to Amplifier Migration APIs

These APIs leverage a Domo access token that you can generate in the admin panel from within your Domo instance. [Instructions on generating your access token can be found here](https://domo-support.domo.com/s/article/360042934494?language=en_US).

### List Cloud Amplifier Integration Types

Retrieves a list of the Cloud Amplifier integration types matching integrations that exist in the Domo instance.

**URL**:

`https://{domo-domain}/api/query/migration/integrations/types`

**URL Parameters**:

`domo-domain`: The fully qualified domain of the Domo instance housing the Cloud Amplifier Integrations.

**HTTP Method**: GET

**Response Content-Type**: JSON

**Response Sample**
```json
[
    "BIGQUERY",
    "SNOWFLAKE"
]
```

**Sample cURL Command**

```curl
curl 'https://{domo-domain}/api/query/migration/integrations/types' \
  -H 'accept: application/json,*/*;q=0.8' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'cache-control: max-age=0' \
  -H 'X-DOMO-Developer-Token: {developer-token}'
```

### List Cloud Amplifier Integrations by Type
Retrieves a list of Cloud Amplifier integrations matching the provided integration type.

**URL**:

`https://{domo-domain}/api/query/migration/integrations/{integration-type}`

**URL Parameters:**

- `domo-domain`: The fully qualified domain of the Domo instance housing the Cloud Amplifier Integrations.
- `integration-type`: One of the integration types returned by the 'List Cloud Amplifier Integration Types' API (case-insensitive).

**HTTP Method:** GET

**Response Content-Type:** JSON

**Response Properties:**
- `id`: Unique identifier of the Cloud Amplifier integration.
- `name`: Readable name of the Cloud Amplifier integration.
- `type`: Type of the Cloud Amplifier integration.
- `authMethod`: Authentication method of the Cloud Amplifier integration, one of `[ "OAUTH", "SERVICE_ACCOUNT" ]`.

**Response Sample**

```json
[
    {
        "id": "31e0307a-cb31-4018-b824-eb04b15827e1",
        "name": "My BigQuery Amplifier Integration",
        "type": "BIGQUERY",
        "authMethod": "SERVICE_ACCOUNT"
    }
]
```
**Sample cURL Command**
```curl
curl 'https://{domo-domain}/api/query/migration/integrations/{integration-type}' \
  -H 'accept: application/json,*/*;q=0.8' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'cache-control: max-age=0' \
  -H 'X-DOMO-Developer-Token: {developer-token}'
```

### List Datasource Migration Candidates by Amplifier Integration
Retrieves a list of datasources eligible as candidates for migration from Federated to the provided Cloud Amplifier integration.

**URL**: `https://{domo-domain}/api/query/migration/candidates/federated/to/amplifier/integrations/{integration-id}`

**URL Parameters**:

- `domo-domain`: The fully qualified domain of the Domo instance housing the Cloud Amplifier Integrations.
- `integration-id`: The unique ID of the Cloud Amplifier integration to list migration candidates for.

**HTTP Method**: GET

**Response Content-Type**: JSON

**Response Properties:**

- `id`: Unique identifier of the datasource.
- `name`: Readable name of the datasource.
- `type`: Type of the datasource.
- `catalogName`: Name of the catalog (or equivalent) of the datasource in the system external to Domo.
- `schemaName`: Name of the schema (or equivalent) of the datasource in the system external to Domo.
- `tableName`: Name of the table (or equivalent) of the datasource in the system external to Domo.
- `collision`: Boolean indicating whether a different datasource matching this candidate's catalog/schema/table name combination already exists in the destination Cloud Amplifier integration. If true, this indicates that attempting to migrate the candidate datasource will fail and that Domo content associated with the candidate datasource need to be migrated to the colliding datasource.
- `collidingDatasourceId`: Unique identifier of the datasource colliding with this candidate datasource. Usually null.
- `collidingDatasourceName`: Readable name of the datasource colliding with this candidate datasource. Usually null.
- `migrated`: Boolean indicating whether the datasource has been previously migrated to the Cloud Amplifier integration.
- `migrationDate`: Date indicating when the datasource was previously migrated to the Cloud Amplifier integration.


**Response Sample**

```json
[
    {
        "id": "8c487fef-b62d-486f-af7a-90c7d6ee0347",
        "name": "Federated BigQuery fifty_row_table",
        "type": "bigquery-federated",
        "catalogName": "my-project",
        "schemaName": "my-schema",
        "tableName": "fifty_row_table",
        "collision": false,
        "collidingDatasourceId": null,
        "collidingDatasourceName": null,
        "migrated": false,
        "migrationDate": null
    }
]
```

**Sample cURL Command**
```curl
curl 'https://{domo-domain}/api/query/migration/candidates/federated/to/amplifier/integrations/{integration-id}' \
  -H 'accept: application/json,*/*;q=0.8' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'cache-control: max-age=0' \
  -H 'X-DOMO-Developer-Token: {developer-token}'
  ```

### Migrate Datasource to Amplifier Integration
Migrates a candidate Federated datasource to the provided Cloud Amplifier integration. NOTE: Domo content powered by the datasource will be unavailable and/or non-functional while the migration is ongoing.

**URL**: `https://{domo-domain}/api/query/migration/federated/to/amplifier/{datasource-id}/integrations/{integration-id}`

**URL Parameters**:

- `domo-domain`: The fully qualified domain of the Domo instance housing the Cloud Amplifier Integrations.
- `datasource-id`: The unique ID of the federated datasource to migrate.
- `integration-id`: The unique ID of the Cloud Amplifier integration that the federated datasource should be migrated to.

**HTTP Method**: POST

**Response Content-Type**: JSON

**Response Properties**:

- `toe`: Unique request identifier. Used by Domo support to retrieve additional information for failed migration attempts.
- `datasourceId`: Unique identifier of the datasource the migration occurred for.
- `direction`: Direction of the migration. Will be "FEDERATED_TO_CLOUD_AMPLIFIER".
- `startTime`: Timestamp indicating the start time of the migration.
- `state`: Final state of the migration, one of [ "COMPLETE", "INCOMPLETE", "ABORTED" ]. 
  - COMPLETE: Migration has completed successfully. 
  - INCOMPLETE: Migration failed after some changes to the datasource were made. Domo content powered by the datasource may remain unavailable and/or non-functional until the migration is re-attempted and completes successfully. More information can be found in the 'errorMessage' property.
  - ABORTED: Migration was aborted prior to any changes being made to the datasource. More information can be found in the 'errorMessage' property.
- `errorMessage`: Message populated with additional details when a migration fails to complete normally or is aborted prior to starting.
- `endTime`: Timestamp indicating the end time of the migration.

**Response Sample**

```json
{
    "toe": "UCIIAGMUEF-G4XS4-9G8UP",
    "datasourceId": "8c487fef-b62d-486f-af7a-90c7d6ee0347",
    "direction": "FEDERATED_TO_CLOUD_AMPLIFIER",
    "startTime": "2024-03-26T14:55:40.496+00:00",
    "state": "COMPLETE",
    "endTime": "2024-03-26T14:55:48.476+00:00"
}
```

**Sample cURL Command**
```curl
curl 'https://{domo-domain}/api/query/migration/federated/to/amplifier/{datasource-id}/integrations/{integration-id}' \
  -X POST \
  -H 'content-type: application/json' \
  -H 'accept: application/json,*/*;q=0.8' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'cache-control: max-age=0' \
  -H 'X-DOMO-Developer-Token: {developer-token}'
```

### List Datasource Reverse Migration Candidates by Amplifier Integration
Retrieves a list of datasources previously migrated from Federated to the provided Cloud Amplifier integration.

**URL**: `https://{domo-domain}/api/query/migration/candidates/amplifier/to/federated/integrations/{integration-id}`

**URL Parameters:**

- `domo-domain`: The fully qualified domain of the Domo instance housing the Cloud Amplifier Integrations.
- `integration-id`: The unique ID of the Cloud Amplifier integration to list reverse migration candidates for.

**HTTP Method**: GET

**Response Content-Type**: JSON

**Response Properties**:

- `id`: Unique identifier of the datasource.
- `name`: Readable name of the datasource.
- `type`: Type of the datasource.
- `catalogName`: Name of the catalog (or equivalent) of the datasource in the system external to Domo.
- `schemaName`: Name of the schema (or equivalent) of the datasource in the system external to Domo.
- `tableName`: Name of the table (or equivalent) of the datasource in the system external to Domo.
- `collision`: Boolean indicating whether a different datasource matching this candidate's catalog/schema/table name combination already exists in the destination Cloud Amplifier integration. If true, this indicates that attempting to migrate the candidate datasource will fail and that Domo content associated with the candidate datasource need to be migrated to the colliding datasource.
- `collidingDatasourceId`: Unique identifier of the datasource colliding with this candidate datasource. Usually null.
- `collidingDatasourceName`: Readable name of the datasource colliding with this candidate datasource. Usually null.
- `migrated`: Boolean indicating whether the datasource has been previously migrated to the Cloud Amplifier integration.
- `migrationDate`: Date indicating when the datasource was previously migrated to the Cloud Amplifier integration.


**Response Sample**
```json
[
    {
        "id": "8c487fef-b62d-486f-af7a-90c7d6ee0347",
        "name": "Federated BigQuery fifty_row_table",
        "type": "bigquery-federated",
        "catalogName": "my-project",
        "schemaName": "my-schema",
        "tableName": "fifty_row_table",
        "collision": false,
        "collidingDatasourceId": null,
        "collidingDatasourceName": null,
        "migrated": true,
        "migrationDate": "2024-03-26T16:08:27.000+00:00"
    }
]
```

**Sample cURL Command**
```curl
curl 'https://{domo-domain}/api/query/migration/candidates/amplifier/to/federated/integrations/{integration-id}' \
  -H 'accept: application/json,*/*;q=0.8' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'cache-control: max-age=0' \
  -H 'X-DOMO-Developer-Token: {developer-token}'
```

**Reverse Datasource Migration**

Reverses the migration of a Federated datasource previously migrated to a Cloud Amplifier integration. 

**URL**: `https://{domo-domain}/api/query/migration/amplifier/to/federated/{datasource-id}`

**URL Parameters**:

- `domo-domain`: The fully qualified domain of the Domo instance housing the Cloud Amplifier Integrations.
- `datasource-id`: The unique ID of a datasource previously migrated from federated to a Cloud Amplifier integration.

**HTTP Method**: POST

**Response Content-Type**: JSON

**Response Properties**:

- `toe`: Unique request identifier. Used by Domo support to retrieve additional information for failed migration reversal attempts.
- `datasourceId`: Unique identifier of the datasource the migration reversal occurred for.
- `direction`: Direction of the migration. Will be "CLOUD_AMPLIFIER_TO_FEDERATED".
- `startTime`: Timestamp indicating the start time of the migration reversal.
- `state`: Final state of the migration reversal, one of `["COMPLETE", "INCOMPLETE", "ABORTED"]`.
  - COMPLETE: Migration reversal has completed successfully.
  - INCOMPLETE: Migration reversal failed after some changes to the datasource were made. Domo content powered by the datasource may remain unavailable and/or non-functional until the migration reversal is re-attempted and completes successfully. More information can be found in the 'errorMessage' property.
  - ABORTED: Migration reversal was aborted prior to any changes being made to the datasource. More information can be found in the 'errorMessage' property.
- `errorMessage`: Message populated with additional details when a migration reversal fails to complete normally or is aborted prior to starting.
- `endTime`: Timestamp indicating the end time of the migration reversal.

**Response Sample**
```json
{
    "toe": "VG586G9YQ3-XERVQ-4J7VA",
    "datasourceId": "8c487fef-b62d-486f-af7a-90c7d6ee0347",
    "direction": "CLOUD_AMPLIFIER_TO_FEDERATED",
    "startTime": "2024-03-26T14:57:19.085+00:00",
    "state": "COMPLETE",
    "endTime": "2024-03-26T14:57:26.287+00:00"
}
```

**Sample cURL Command**
```curl
curl 'https://{domo-domain}/api/query/migration/amplifier/to/federated/{datasource-id}' \
  -X POST \
  -H 'content-type: application/json' \
  -H 'accept: application/json,*/*;q=0.8' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'cache-control: max-age=0' \
  -H 'X-DOMO-Developer-Token: {developer-token}'
  ```
