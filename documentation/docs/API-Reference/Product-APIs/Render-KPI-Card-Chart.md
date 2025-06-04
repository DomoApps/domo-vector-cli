Render KPI Card Chart or Table
===========================

### Authentication

Requests to this endpoint require authentication using an access token. The token must be included in the request header as `X-DOMO-Developer-Token`. For more information on generating an access token, refer to the [Domo Support Documentation](https://domo-support.domo.com/s/article/360042934494?language=en_US).

### HTTP Method: `PUT`

### URL

`/api/content/v1/cards/kpi/{urn}/render`

### Tags

*   `card-kpi-resource`

### Summary

This endpoint renders a KPI card chart or table based on the specified `urn`. It supports various parameters, including locale and specific parts of the chart to be rendered. The response contains an array of base64 encoded images corresponding to the requested parts of the KPI card. These base64 strings can then be decoded and compiled into a PDF.

### Parameters

#### Path Parameters

*   **`urn`** (required):  
    The unique resource name (URN) of the KPI card to be rendered.
    *   **Schema:** `$ref: '#/components/schemas/CardURNParam'`

#### Query Parameters

*   **`locale`** (optional):  
    Specifies the locale in which to render the KPI card.
    
    *   **Type:** `string`
*   **`parts`** (required):  
    A list of specific parts of the chart to be rendered. This allows for a customized response that includes only the necessary components.
    
    *   **Type:** `array` (unique items)
    *   **Items:** `string`
    *   **Enum:**
        *   `title`
        *   `chartType`
        *   `queryResult`
        *   `data`
        *   `image`
        *   `imagePDF`
        *   `graph`
        *   `dynamic`
        *   `summary`
        *   `summaryImage`
        *   `dataSource`
        *   `pdp`
        *   `annotations`
        *   `extendedDateInfo`
        *   `table`

### Request Body

The request body must be in JSON format and should adhere to the `ChartRequest` schema.

*   **Content-Type:** `application/json`
*   **Schema:** `$ref: '#/components/schemas/ChartRequest'`

### Responses

#### 200 OK

The request was successful, and the KPI card chart or table has been rendered according to the specified parameters. The response will include an array of base64 encoded images.

*   **Content-Type:** `application/json`
*   **Schema:** `$ref: '#/components/schemas/ChartResponse'`

#### 403 Forbidden

The request was not authorized. The client lacks the necessary permissions to access this resource.

#### 409 Conflict

The request could not be completed due to a conflict with the current state of the target resource.

### Example Code

Here’s an example of how to use the API to render a KPI card chart or table:

```javascript

async function getPDF(cardID) {
  try {
    const body = {
  queryOverrides: {},
  treatLongsAsStrings: true,
  cardLoadContext: {}
};;

    return await Helpers.handleRequest('put', '/api/content/v1/cards/kpi/'+cardID+'/render?parts=title,imagePDF,', body);
  } catch (error) {
    throw new Error('getPDF: ', error);
  }
}
```

### Example Response

The response will contain an array of base64 encoded strings representing the images of the requested KPI card parts. Below is a truncated example of what the response might look like:

`
{
  "data": [
    "JVBERi0xLjQKJeLjz9MKMyAwIG9iaiA8PC9GaWx0ZXIvRmxhdGVEZWNvZGUvTGVuZ3RoIDExOTg+PnN0cmVhbQp4nO1XS28kNRBuiVtfuISVQBx8QiCEY5df7SuCZHlIwCZoEdeRWLSaHIADf5+vqmy3JxJiIs2eSEbJVLnL9frqczvOJkO14u/DGpwf2rFpX3hR3C7+jo83/PnzzfobxLdrwYNNfVBNXTni2d/YuVGJyczfIQXz6na9W31gYy87RS7VbtF4sj6bsmHBc2SRDuvGz0Quw7R0BwfNIvBOMdxi3y7SYVWvuhyG7Z7CQUpzNiZXN+SZqyNONwYftVZnA9XosRhikq8EnZ/9yxMU+eX9en3jTTX33CuHjzdUgtmcuX9YP12ulveXj/jz2f3b9ev7y8VII8Tny/fLt8t3LUAHrMQJMFHOBSznHbAcd8By6B0XqQEmchmmpTtQwPI2AMt1bK8TYLochu2eQgcs9zwFKQD4bhDLaUbsg+XF5RHrIa6XV8uvj/BKM8HSUwiWJoLFiWBxECxOBIudYHEQLO0ESzvB0iBYmgmWBsHSTrA0EyzwDxPM18xdIfm+OF5pYtiHQOzjy+PVQ3jg9Xp5b8nL3fJyuQHfvsHvy+X2EYZx5lx8CufCxLkwcS4MzoWJc6FzLgzOhZ1zYedcGJwLM+fC4FzYORdmzlUmG2NYIHCnQkE/Lo5hSDOGL97FKdlDOMYLqP2y/PgINZqZR09hHk3M8xPz/GCen5jnO/P8YB7tzKOdeTSYRzPzaDCPdubRzLwNnaGBlrNeWnXyHvfziPwOTQxNSAwMDAwMCBuIAowMDAwMDAwMDE1IDAwMDAwIG4gCjAwMDAwMDk0NDUgMDAwMDAgbiAKMDAwMDAwMTI4MSAwMDAwMCBuIAowMDAwMDAxNDYxIDAwMDAwIG4gCjAwMDAwMDgyODUgMDAwMDAgbiAKMDAwMDAw"
  ] 
}
`