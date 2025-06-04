---
stoplight-id: 66b06bf6ac52d
---

# IDE Limitations

### Variables/parameters set in the account section are not accessible in the process data section
---
In the IDE, the authentication and process data scripts run independently through your local browser. Hence, the values assigned in the account section are not accessible in the process data section.
Example: When you are assigning a token value to an account section parameter in the authentication script i.e. 'metadata.account.token = response.access_token;' and if you try to access the same field in the process data section then it is not accessible.
Please note that the values defined in the text boxes from the account section will be available in the authentication and process data section. However, anything that is set explicitly in the authentication script will not be reflected in process data

### Show when conditions do not work
---
The showwhen conditions do not work in IDE.


### Limitation on response size/request timeout
---
In the IDE, if the response size exceeds 7MB, it throws an error saying- 'Domo encountered an error proxying your request: 500.'

We would suggest to use pagination for such cases and bring data in smaller chunks.
Also, if the API takes longer than seconds to respond to the request, you will see the same error.


### Streaming is not available
---
To handle large API responses, streaming is for now not supported in the IDE.

### Limit on console logs
---
Using DOMO.log() function, you can see logs in the IDE console. However, it has a limitation. So, you can use console.log() function to see complete logs in your browser console.

> Note: 
> All these limitations are with IDE only and not with published or self-published versions.

