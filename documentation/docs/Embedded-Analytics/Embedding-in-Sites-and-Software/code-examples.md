---
stoplight-id: 4soguofca8clp
---

# Code Examples

## React Code Example
---
The React example uses an express server for secure server-side programmatic filtering and for an Edit Embed experience. Download the sample code from the example GitHub repository to access even more detailed instructions in the readme file or check out example code: [React sample code repo](https://github.com/DomoApps/domo-react-embed-filters)

## Javascript Code Example
---
The JavaScript version uses a Node.js repository for secure server-side programmatic filters. Download the sample code from the example GitHub repository to access even more detailed instructions in the readme file or check out example code: [JS sample code repo](https://github.com/domoinc/domo-node-embed-filters)

## .Net Code Example
---
Download the sample code from the example GitHub repository to access even more detailed instructions in the readme file or check out example code: [ASP.NET sample code repo](https://github.com/domoinc/domo-asp-embed-filters)

- The ASP version is based on a .NET repository

## SalesForce Code Example
---
Domo cards and dashboards can be privately embedded in Salesforce. This is accomplished with the same programmatic filters used for row-level security in other types of websites and software. In Salesforce, these invisible and immutable filters are driven by these Apex examples in Visualforce pages and Lightning web components.

The functioning example in this GitHub repository can be deployed to production with minimal changes. Just focus on updating the filter logic and token storage. After you download the example, don’t forget these final three essential steps:

- Populate the 4 variables at the top of the “domoEmbedExampleController” with your Client ID, secret, embed ID, and embed type
- Add "ht<span>tp://</span>api.domo.com" to your Remote Site Settings
- Add the code to your Lightning layouts using the Visualforce component type or add to existing Lightning Web Components or Visualforce pages with an iframe
- [Download SFDC sample code repo](https://github.com/michaelforce-repo/domo-salesforce-embed-example)


## Python Code Example
---

### Full code example for programmatic filtering using Python

```python
#!/usr/bin/env python3

import requests
import base64
import json

api_host = "https://api.domo.com"

embed_host = "https://public.domo.com"

access_token_url = api_host + "/oauth/token?grant_type=client_credentials&scope=data%20audit%20user%20dashboard"

embed_token_url = api_host + "/v1/stories/embed/auth"
embed_url = embed_host + "/embed/pages/"

# Replace the string below with your encoded passphrase
usrPass = ""
b64Val = base64.b64encode(usrPass.encode('utf8'))

response = requests.get(access_token_url, 
                        headers={"Authorization": "Basic %s" % b64Val.decode('utf8'),
                                 "Accept": "*/*"})
auth_response = json.loads(response.text)
access_token = "Bearer %s" % auth_response['access_token']
# print(access_token)

# Replace the string below with the 5 character embed page id
embed_id = ""
payload = {"sessionLength":1440, 
           "authorizations":[{"token": embed_id, 
                              "permissions":["READ",
                                             "FILTER",
                                             "EXPORT"], 
                              "filters": []}
                            ]
           }
response = requests.post(embed_token_url, 
                         headers={"Authorization": access_token, 
                                  "Accept": "application/json", 
                                  "Content-Type": "application/json"}, 
                         data = json.dumps(payload))
# print(response.text)

embed_response = json.loads(response.text)

index_html = '''<html>
<body>
<form id="form" action="https://public.domo.com/embed/pages/{}" method="post">
<input type="hidden" name="embedToken" value="{}">
</form>
<script>document.forms[0].submit();</script>
</body>
</html>'''.format(embed_id, embed_response['authentication'])

# print(index_html)
with open("index.html", "w") as f:
    f.write(index_html)
    
```

## PHP Code Example
---

### Full code example for programmatic filtering using PHP

```php
<?php
    $request = $_SERVER['REQUEST_URI'];
    if ($request == "/card") {
        $secret='ENTER_SECRET';
        $clientid='ENTER_CLIENT_ID';
        $embedId = 'ENTER_EMBED_ID';

        $curl = curl_init();

        curl_setopt_array($curl, array(
        CURLOPT_URL => "https://api.domo.com/oauth/token?grant_type=client_credentials&scope=data%20user%20dashboard",
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_ENCODING => "",
        CURLOPT_MAXREDIRS => 10,
        CURLOPT_TIMEOUT => 30,
        CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
        CURLOPT_CUSTOMREQUEST => "GET",
        CURLOPT_POSTFIELDS => "",
        CURLOPT_HTTPAUTH => CURLAUTH_BASIC,
        CURLOPT_USERPWD => "$clientid:$secret"
        ));
        $response = curl_exec($curl);
        $err = curl_error($curl);
        curl_close($curl);
        if ($err) {
            echo "<br>cURL Error #: $err";
        }
        else {
            $responsearray = json_decode($response, true);
            $curl2 = curl_init();
            curl_setopt_array($curl2, array(
            CURLOPT_URL => "https://api.domo.com/v1/cards/embed/auth",
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_ENCODING => "",
            CURLOPT_MAXREDIRS => 10,
            CURLOPT_TIMEOUT => 30,
            CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
            CURLOPT_CUSTOMREQUEST => "POST",
            CURLOPT_POSTFIELDS => '{
            "sessionLength": 1440,
            "authorizations" :[
                {
                "token" : "'.$embedId.'",
                "permissions" : ["READ", "FILTER", "EXPORT"],
                "filters" : [
                    {
                        "column": "advertiserid",
                        "operator": "IN",
                        "values": ["3"]
                    }
                ]
                }
            ]
            }',
            CURLOPT_HTTPHEADER => array(
                "Authorization: Bearer ".$responsearray['access_token'],
                "Content-Type: application/json; chartset=utf-8",
                "Accept: */*"
            ),
            ));
            $response2 = curl_exec($curl2);
            $err2 = curl_error($curl2);
            curl_close($curl2);
            $responsearray = json_decode($response2, true);
            $embedToken = $responsearray['authentication'];
            
            http_response_code(200);
            echo <<<EOT
                <form id="form" action="https://public.domo.com/cards/$embedId" method="post">
                    <input type="hidden" name="embedToken" value="$embedToken">
                </form>
                <script>
                    document.getElementById("form").submit();
                </script>
            EOT;
        }
    }
    else {
        echo <<<EOT
        <html>
          <head>
            <title>Domo Programmatic Filtering</title>
          </head>
          <body>
            <hr>
              <div id="iframe-container" style="display: flex; flex-direction: column; align-items: center; justify-content: space-evenly; margin-top: 40px;">
                <h1>Domo Programmatic Filtering</h1>
                <iframe src="/card" width="600" height="600"></iframe>
              </div>      
          </body>
        </html>        
        EOT;
    }
?>
```