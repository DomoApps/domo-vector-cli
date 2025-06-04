---
stoplight-id: dc6vadk2yrjcw
---

# Embedded Capabilities

Provide more functionality to your external customers by empowering them to create, edit, save, and share their own content from the embedded experience.

The most advanced companies integrate the full power of the platform. Domo Everywhere allows you to share the rich data experience of the entire Domo platform -- any data, application, or visualization -- packaged together for your customers and partners that aligns with your brand and while maintaining the ability to easily govern and distribute at scale. You decide what tools and capabilities to enable. Start with the majority of your functionality already built so you can focus on your expertise.

https://player.vimeo.com/video/530952420?badge=0&amp;autopause=0&amp;player_id=0&amp

Your most strategic customers and partners demand more than dashboards. OEM all of Domo in your interface so your partners and customers can:
- Create totally new content
- Create their own alerts
- Schedule their own reports
- Connect their own data
- Transform both sides together

## Domo Identity Broker
---
### What does the Domo Identity Broker do?
The Domo Identity Broker allows you to have one entity they can authenticate users against. The Identity Broker will then route that user to the appropriate Domo environment and authenticate them as a user. The identity broker can accept a variety of different authentication methods to make it easy for our customer to leverage their existing infrastructure. See basic architecture diagram below.

<img class="alignnone" src="https://web-assets.domo.com/blog/wp-content/uploads/2021/06/domo-identity-broker-3.png" alt=""/>

[**UPDATE GRAPHIC**]

#### Supported Technologies
The Domo Identity Broker supports SAML2, OIDC, JWT or OAuth2.


#### Authenticating using a JWT (JSON Web Token)
JWT’s can be sent to the Domo Identity Broker as a GET parameter (in the URL) or a POST parameter (in the post body). A quick way for validation is to send a URL parameter to the Identity Broker URL, followed by /JWT?token={{token}}. You can also pass a destination parameter in the URL, which will determine which page is loaded (assuming you want to load something beyond the default landing page). Example: `https://modocorp.identity.domo.com/jwt?token={{token}}&amp;destination=/page/{{page_ID}}`

The minimum items required in the payload are:

- Sub (email address)
- Key attribute (unique customer identifier from mapping section)
- IAT (JWT issued at in EPOCH time)
- Exp (JWT expiration in EPOCH time - no more than 900 seconds greater than IAT)
- JTI (Unique string or number to identify this JWT. Recommended to use a UUID.)


In addition to the required items you can also include any of the following optional attributes which can be used by Domo. Any SAML2 accepted attributes will work. These can be used in dynamic PDP policies, for group assignments and to complete the users profile within Domo:

| Attribute       | XML attribute name | Description                                                                                                                                                                                                                                                                                                                         |
|-----------------|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Name            | name               | The display name for the user in Domo. This is the only name field displayed in Domo.                                                                                                                                                                                                                                               |
| Email           | email              | The user's email address. Domo uses this value as the unique identifier for the person's account, so any value included for Email will overwrite the SAML Subject value in the SAML assertion. Domo also uses this email address to send any notifications and alerts to the user.                                                  |
| Alternate email | email.secondary    | A secondary contact email for the user. Domo does not use this email address for any communications.                                                                                                                                                                                                                                |
| Role            | role               | The IdP can set the role of the user at each login. The role must match exactly (including case sensitivity) a valid role in your Domo instance.                                                                                                                                                                                    |
| Employee ID     | employee.id        | Must be alphanumeric                                                                                                                                                                                                                                                                                                                |
| Hire date       | hire.date          | Format: YYYY-MM-DD                                                                                                                                                                                                                                                                                                                  |
| Title           | title              | Example: Software Engineer                                                                                                                                                                                                                                                                                                          |
| Department      | department         | Example: Sales                                                                                                                                                                                                                                                                                                                      |
| Location        | location           | Example: Utah                                                                                                                                                                                                                                                                                                                       |
| Mobile Phone    | user.phone         | Accepts any combination of numbers and the characters +()-x. For example: +1 (555) 555-5555 x 5555                                                                                                                                                                                                                                  |
| Desk phone      | desk.phone         | Accepts any combination of numbers and the characters +()-x. For example: +1 (555) 555-5555 x 5555                                                                                                                                                                                                                                  |
| Locale          | locale             | Sets the preferred language, metrics, and formatting in Domo. Valid values: de-DE, de-AT, de-CH, en-AU, en-CA, en-150, en-HK, en-IE, en-IN, en-IL, en-MO, en-NZ, en-SG, en-GB, en-US, en-001, es-ES, es-US, es-419, es-MX, fr-BE, fr-CA, fr-FR, fr-CH, nl-BE, nl-NL, pt-BR, pt-PT, ja-JP, zh-CN, zh-Hans-HK, zh-Hans-MO, zh-Hans-SG |
| Timezone        | timezone           | For example: America/Denver or Asia/Tokyo. For a full list of valid timezone settings, see this article: timezones                                                                                                                                                                                                                  |
| Group           | group              | A list of XML escaped strings                                                                                                                                                                                                                                                                                                       |

The payload must be signed using the provided secret and be encoded using an HS algorithm (we encourage HS256). A great site for learning more about JWT’s, creating them for testing purposes and finding access to different code repositories for creating and signing JWT’s is <a href="http://jwt.io" target="_blank" rel="noopener">jwt.io</a>.

Sample JWT payload:

```json
{ 

  "sub": "alex.lee@modocorp.co", 
  "name": "Alex Lee", 
  "customer_id": 1000, 
  "role": "Embedded Editor", 
  "groups": ["a","b","c"],
  "iat": 1716238922, 
  "exp": 1716239022, 
  "jti": "4556-uihb-8765" 
} 
```

#### Authenticating using SAML2
When using SAML2 to authenticate against the Domo Identity Broker the following details are required for configuration of the IDP:
<ul>
 	<li>SAML Assertion Endpoint URL: {{identitybrokerURL}}/auth/saml</li>
</ul>
Once the configuration is completed in the IDP, you need to provide your technical resource at Domo with the following details from your IDP:
<ul>
 	<li>Identity Provider Endpoint URL</li>
 	<li>Entity ID</li>
 	<li>X.509 certificate</li>
</ul>

## Next Steps
---
For more information also see the [Domo Knowledge Base](https://domo-support.domo.com/s/topic/0TO5w000000ZanbGAC/domo-everywhere?language=en_US). In particular, this article on [Routing, Creation, and Mapping](https://domo-support.domo.com/s/article/6523741250455?language=en_US) may be helpful.

