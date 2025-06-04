---
stoplight-id: 71ec34a2958fe
---

# Configure Authentication

To build your own connector you will need to know how to authenticate to your target data system. The Connector Dev Studio supports four different authentication schemes:

<ul class="ul1">
 	<li class="li1">No authentication</li>
 	<li class="li1">Username and password</li>
 	<li class="li1">API Key</li>
 	<li class="li1">OAuth 2.0</li>
 	<li>Custom Account</li>
</ul>

You will need to investigate if your API endpoint requires authentication and what kind of authentication it uses.

**What if I need a different type of authentication?**

The Dev Studio does not support any other authentication methods at this time. However, you can use Domo APIs to write your own program. Click here to learn more about building your own program using [Domo APIs](../../Getting-Started/api-authentication.md).

### No Authentication
---

<p class="p1">If your REST API endpoint does not require any authentication, select <b>None</b>.</p>
<img class="alignnone size-full wp-image-3957" src="https://web-assets.domo.com/blog/wp-content/uploads/2022/02/AuthNone.png" alt="" width="1138" />

````js
auth.authenticationSuccess();
````

<p class="p1">It is not required, but if you would like to check your connection with your API endpoint before you run your report, you can write an authentication script. If you choose to do this, set <i>auth.authenticationSuccess()</i> and <i>auth.authenticationFailed('&lt;&lt;Insert your message&gt;&gt;')</i> appropriately.</p>

```js
var res = httprequest.get('http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson');  

DOMO.log('res: ' + res);

if (httprequest.getStatusCode() == 200) {
  auth.authenticationSuccess();
} else {
  auth.authenticationFailed('Error connecting to earthquake.usgs.gov');
}
```

### Username and Password
---
<ol>
 	<li class="p1">Select <strong>Username and Password</strong>.</li>
 	<li class="p1">Enter your username and password into the <strong>Username</strong> and <strong>Password</strong> fields. These will be securely stored. You can access them in your authentication script by calling <em>metadata.account.username</em> and <em>metadata.account.password</em>.</li>
 	<li class="p1">Write your authentication script as required by your API endpoint.</li>
 	<li>Click <strong>Run Script</strong> to run your authentication script.</li>
</ol>

Although you will need to determine how the API endpoint you want to use authenticates, most endpoints that use username and password will use the [Basic Authentication](https://en.wikipedia.org/wiki/Basic_access_authentication) standard. When making an http request, the request header will usually be:

<table>
<tbody>
<tr>
<td>Key</td>
<td>Value</td>
</tr>
<tr>
<td>Authorization</td>
<td>Basic Base64Encoded(&lt;username&gt;:&lt;password&gt;)</td>
</tr>
</tbody>
</table>
&nbsp;

The Connector Dev Studio provides a built-in function if you need to base-64 encode a string: <em>DOMO.b64EncodeUnicode(&lt;string&gt;)</em>.

<!-- theme: info -->

> #### Note
> The code block needs to determine and set the authentication to either <em>auth.authenticationSuccess()</em> or <em>auth.authenticationFailed('&lt;&lt;Insert your message&gt;&gt;')</em>.

<img class="alignnone size-full wp-image-3976" src="https://web-assets.domo.com/blog/wp-content/uploads/2022/02/Auth-NamePass.png" alt="" />

```js
//This logging is here for testing! Remove before publishing your connector
DOMO.log('metadata.account.username: ' + metadata.account.username);
DOMO.log('metadata.account.password: ' + metadata.account.password); 

var encodedData = DOMO.b64EncodeUnicode(metadata.account.username + ':' + metadata.account.password);

httprequest.addHeader('Authorization', 'Basic ' + encodedData);

var res = httprequest.get('https://developer.domo.com/samplecrm');  

if (httprequest.getStatusCode() == 200) {
  auth.authenticationSuccess();
} else {
  auth.authenticationFailed('Your username and password are incorrect');
}
```

### API Key
---
<ol>
 	<li>Select <strong>API Key</strong>.</li>
 	<li>Enter your API key into the <strong>API Key</strong> field. It will be securely stored. You can access it in your authentication script by calling <em>metadata.account.apikey</em>.</li>
 	<li>Write your authentication script as required by your API endpoint.</li>
 	<li>Click <strong>Run Script</strong> to run your authentication script.</li>
</ol>

An **[API key](https://en.wikipedia.org/wiki/Application_programming_interface_key)** is a token passed in as a header or a query parameter in an http request. It uniquely identifies who is making the call and is often non-expiring. You will need to determine how the REST API you wish to call needs to send the API key.

Use the API key as a query parameter (using the "httprequest.addParameter()" method)

<img class="alignnone size-full wp-image-3961" src="https://web-assets.domo.com/blog/wp-content/uploads/2022/02/AuthAPIKey.png" alt="" />

````js
//This logging is here for testing! Remove before publishing your connector
DOMO.log('metadata.account.apiKey: ' + metadata.account.apikey);

// Adding the api key in the query parameter
httprequest.addParameter('apikey',metadata.account.apikey);

// Making the call to the api endpoint
var res = httprequest.get('https://samplecrm.domo.com/samplecrm');

// Make sure to determine and set the authentication status to either success or failure.
if (httprequest.getStatusCode() == 200) {
  auth.authenticationSuccess();
} else {
  auth.authenticationFailed('The api key you entered is invalid. Please try again with a valid key.');
}
````

If your API endpoint requires it, the Connector Dev Studio includes functions for building a [JSON Web Token (JWT)](https://en.wikipedia.org/wiki/JSON_Web_Token). You can see an example of this in the code below.

<!-- theme: info -->

> #### Note
> The code block needs to determine and set the authentication to either <em>auth.authenticationSuccess()</em> or <em>auth.authenticationFailed('&lt;&lt;Insert your message&gt;&gt;')</em>.

<img class="alignnone size-full wp-image-3370" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2017/03/13112629/AuthAPIKey.png" alt="" />

```js
//This logging is here for testing! Remove before publishing your connector
DOMO.log('metadata.account.apiKey: ' + metadata.account.apikey); 

// Example of inserting API key into header
httprequest.addHeader('API-KEY', metadata.account.apikey);
var res = httprequest.get('https://developer.domo.com/samplecrm');

// Example of including API key as a query parameter in URL
var res = httprequest.get('https://samplecrm.domo.com/samplecrm?apikey=' + metadata.account.apikey);

// Example of using the API key to create a JWT token 
DOMO.jwtBuilder.algorithm = “HS256”;
DOMO.jwtBuilder.authKey = metadata.account.apikey;
DOMO.jwtBuilder.issuer = “DOMO”;
DOMO.jwtBuilder.subject = “12345670”;
DOMO.jwtBuilder.claims[“abc”] = “test”;
DOMO.jwtBuilder.expiration = “1530228571”

var token = DOMO.getJWT()

//This logging is here for testing! Remove before publishing your connector
DOMO.log(token);

httprequest.addHeader(“JWT”, token);
var res = httprequest.get('https://samplecrm.domo.com/samplecrm');

// Make sure to still determine and set the authentication status to either success or failure.
if(httprequest.getStatusCode() == 200){
    auth.authenticationSuccess();
} else {
    auth.authenticationFailed('The api key you entered is invalid. Please try again with a valid key.');
}
```

### OAuth 2.0
---
<ol class="ol1">
 	<li class="li1">Select <b>OAuth 2.0</b>.</li>
 	<li class="li1">Enter the required data in the Authentication fields. You will need to get the necessary information from the API documentation you wish to use. All data will be securely stored. For your information:
<ul class="ul1">
 	<li class="li1">The redirect URI for the connector IDE is <strong><span class="s2">https://api.domo.com/builder/oauth.ht</span><span class="s2">ml</span></strong>.</li>
 	<li class="li1">The callback URL response body needs to be JSON.</li>
 	<li class="li1">The key defining the access token returned by your api needs to be <em>access_token</em>.</li>
</ul>
</li>
 	<li class="li1">Click <b>Get Access Token</b>. Domo will perform the authentication process and securely store your access token. You can access your token in your authentication script by calling <i>metadata.account.accesstoken</i>.</li>
 	<li class="li1">Write your authentication script as required by your API endpoint.</li>
 	<li>Click <strong>Run Script</strong> to run your authentication script.</li>
</ol>

[OAuth 2.0](https://oauth.net/2/) is the industry-standard for secure authentication. If your cloud API endpoint uses OAuth 2.0, you are in luck: Domo has automated the processes of using your stored data to retrieve your access token, below.

<!-- theme: info -->

> #### Note
> The code block needs to determine and set the authentication to either <em>auth.authenticationSuccess()</em> or <em>auth.authenticationFailed('&lt;&lt;Insert your message&gt;&gt;')</em>.

<img class="alignnone size-full wp-image-3374" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2017/03/17114227/UserOauth2.01.png" alt="" />

```js
//This logging is here for testing! Remove before publishing your connector
DOMO.log('accesstoken: ' + metadata.account.accesstoken); 
DOMO.log('code: ' + metadata.account.code); 

if (metadata.account.accesstoken) { 
    auth.authenticationSuccess(); 
}
else { 
    auth.authenticationFailed('Authentication has failed.');
}
```

### Custom Account
---
<ol>
 	<li>Select <strong>Custom</strong>.</li>
 	<li>Enter the label and value in the <strong>Label</strong> and <strong>Value</strong> fields.</li>
 	<li>Select the <strong>Field Type</strong> as Password.</li>
 	<li>Click <strong>ADD FIELD</strong> to add another authentication field.</li>
 	<li class="li1">Write your authentication script as required by your API endpoint.</li>
 	<li>Click <strong>Run Script</strong> to run your authentication script.</li>
</ol>
<img class="alignnone size-full wp-image-3474" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2017/03/24221012/Custom-Account.png" alt="" />

```js
//This logging is here for testing! Remove before publishing your connector
DOMO.log('metadata.account.username: ' + metadata.account.username);    //example
DOMO.log('metadata.account.password: ' + metadata.account.password);  //test
DOMO.log('metadata.account.apikey: ' + metadata.account.token);  //token

DOMO.log(DOMO.b64EncodeUnicode(metadata.account.username + ':' + metadata.account.password));

httprequest.addHeader('Authorization', 'Basic ' + DOMO.b64EncodeUnicode(metadata.account.username + ':' + metadata.account.password));
httprequest.addHeader('token', metadata.account.token);

var res = httprequest.get('https://developer.domo.com/samplecrm');  

DOMO.log('res: ' + res);

if(httprequest.getStatusCode() == 200){
    auth.authenticationSuccess();
} else {
    auth.authenticationFailed('Your username and password are incorrect.');
}
```


