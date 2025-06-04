## Schedule Report and Send Now

**Method**: `POST`  
**Endpoint**: `api/content/v1/reportschedules/<REPORT_ID>/sendnow`

**Example**:

```json
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/content/v1/reportschedules/<REPORT_ID>/sendnow",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": [{ "type": "USER", "value": "<USER_ID>", "email": null }]
}
```

**Response**:

```json
200:
{}

```
