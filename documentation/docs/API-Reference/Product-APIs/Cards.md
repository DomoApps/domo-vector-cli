## Update Card Title

**Method**: `PUT`  
**Endpoint**: `/api/content/v1/cards/<CARD_ID>/title`

**Example**:

```json
{
  "method": "PUT",
  "url": "https://{instance}.domo.com/api/content/v1/cards/<CARD_ID>/title",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": {
   "dynamicTitle":{
      "text":[
         {
            "type":"TEXT",
            "text":"Pivot Table - Change 22 the quick brown fox jumped over the lazy dog"
         }
      ]
   },
   "dynamicDescription":{
      "text":[
          {
            "type":"TEXT",
            "text":"Pivot Table - Change 22 the quick brown fox jumped over the lazy dog"
          }
      ]
   }
}
```

**Response**:

```json
200:
{}

```
