---
stoplight-id: 9k5nqhgffv7wq
---

# URL Parameters in Embedded Content

Domo Everywhere supports three main types of URL parameters in embedded content: 

- Transparent Backgrounds
- Pfilters
- AppData
- Locale

## Transparent Backgrounds
---
Many embed customers customize the dashboard background color or image to make embedded content feel native. 

https://www.youtube.com/watch?v=plqweXEX6u0


<img src="https://web-assets.domo.com/blog/wp-content/uploads/2022/08/URLParameters1-1.png" />

With this URL parameter, making the background totally transparent can make embedded content seem even more native to the host page. 

Here is how an embedded dashboard looks when the background is the host page is black and the URL parameter is set to true (?transparentBackground=true) 

<img src="https://web-assets.domo.com/blog/wp-content/uploads/2022/08/URLParameters2.png" />


Here is how that same embedded dashboard looks when the background transparency is set to false (?transparentBackground=false)

<img src="https://web-assets.domo.com/blog/wp-content/uploads/2022/08/URLParameters3.png" />

## PFilters
---

You can use Pfilters (Python particle filters) to apply filters from URL query parameters to embedded Domo Dashboards as a layer after SSO or programmatic filtering. 

The Pfilter acts as an array of page filter objects. Any matching column names will be filtered upon page load even if they are based on different DataSets. Results can be validated in POST requests on the network tab.  

Review how to link from one embedded dashboard to another while maintaining secure programmatic filters [here](1yafxad1u8azv-programmatic-filtering#linking-across-embedded-dashboards-while-persisting-programmatic-filters).

### Example

The following multi-line example shows Pfilters being used to apply filters to an embedded Domo Dashboard. Note, this example is broken up into multiple lines: 

```url
example.domo.com/embed/pages/private/ABCDE 

?pfilters=[{ 
  "column":"Pos", 
  "operand":"IN", 
  "values":["TE","WR"], 
}, 
{ 
  "column":"Location", 
  "operand":"IN", 
  "values":["Amsterdam","Anchorage"], 
}] 
```

### Operands

The operands you can use when writing code with Pfilters are as follows. Note that the values always need square brackets for the array, even when only a single value is included.   
- IN 
- CONTAINS 
- EQUALS 
- NOT_EQUALS 
- GREATER_THAN 
- LESS_THAN 
- GREAT_THAN_EQUALS_TO 
- LESS_THAN_EQUALS_TO 
- BETWEEN 


### Persistence of Pfilters across Pages 

Domo automatically creates Pfilters when you check Persist Filters in the embed dialog, as shown here:

![Screenshot 2023-11-09 at 12.02.05 PM.png](<../../../assets/images/Screenshot 2023-11-09 at 12.02.05 PM.png>)

You can then view the parameters by hovering over the content. (Card interactions must be turned on and set to External link for this to work). This is shown for the "QA pass rate by model" Card in the following example:


![Screenshot 2023-11-09 at 12.03.02 PM.png](<../../../assets/images/Screenshot 2023-11-09 at 12.03.02 PM.png>)

When viewers click those links, any parts of the story they had previously clicked will be passed along as Pfilters to the next Page. These filters can either be applied to single Cards or complete Pages (even if the Pages contain many Cards based on various DataSets). 

![Screenshot 2023-11-09 at 12.04.56 PM.png](<../../../assets/images/Screenshot 2023-11-09 at 12.04.56 PM.png>)

### Persistence of Pfilters across sessions 

If you want Pfilters to expand beyond pages to also persist across sessions and refreshes, you'll need to store and load the last known state of the Pfilters. One way to do this is through AppDB.  

### Malformed criteria 

If a Pfilter is written incorrectly, the unfiltered version renders and a black error bar appears. 

![Screenshot 2023-11-09 at 12.06.54 PM.png](<../../../assets/images/Screenshot 2023-11-09 at 12.06.54 PM.png>)



## AppData
---
The appData parameter supports passing in general types of inputs to the app. The app developer needs to watch for the parameter, parse the value, and inject it into the most relevant part of the app. 
 
For example, the value of the parameter could then auto-populate a drop-down menu in an app that selects the location. This way, the host page can avoid the delay of waiting for manual inputs. They can now deep-link to a version of the app that already has specific values filled in. Spaces should be encoded as “+” :

```html
public.domo.com/embed/pages/abcde?appData=Salt+Lake+City
```
The query parameters on the embed URL will then be automatically passed down into the apps (e.g. xyz.domoapps.prod4.domo.com) contained by the embedded cards or dashboards. 


## Locale
---

Here are a list of the supported options for the localization parameter `?locale=`:

```text
"de-AT",
"de-CH",
"de-DE",
"de-LI",
"de-LU",
"en-AU",
"en-BZ",
"en-CA",
"en-CB",
"en-GB",
"en-IE",
"en-JM",
"en-NZ",
"en-PH",
"en-TT",
"en-US",
"en-ZA",
"en-ZW",
"es-AR",
"es-BO",
"es-CL",
"es-CO",
"es-CR",
"es-DO",
"es-EC",
"es-ES",
"es-GT",
"es-HN",
"es-MX",
"es-NI",
"es-PA",
"es-PE",
"es-PR",
"es-PY",
"es-SV",
"es-UY",
"es-VE",
"fr-BE",
"fr-CA",
"fr-CH",
"fr-FR",
"fr-LU",
"fr-MC",
"ja-JP",
"sw-KE"
```


