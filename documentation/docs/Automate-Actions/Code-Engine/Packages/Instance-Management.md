# Domo Instance Management

This package gives you more granular control over provisioning Domo instances for Publish and Managed Embed.

The key differences between this function and the default behavior in Instance Management are the ability to specify the Region and add Additional Users.

In order to use this code, you will need to have the following:

- A Domo instance
- Access to Code Engine and basic knowledge of how to create a package

<!--
title: "Instance Management Code Engine Package"
lineNumbers: true
-->

```js
const codeengine = require('codeengine');

class Helpers {
  /**
   * Helper function to handle API requests and errors
   *
   * @param {string} method - The HTTP method
   * @param {string} url - The endpoint URL
   * @param {Object} [body=null] - The request body
   * @returns {Object} The response data
   * @throws {Error} If the request fails
   */
  static async handleRequest(method, url, body = null) {
    try {
      return await codeengine.sendRequest(method, url, body);
    } catch (error) {
      console.error(`Error with ${method} request to ${url}:`, error);
      throw error;
    }
  }
}

/**
 * Provision a Domo instance
 *
 * @param {text} customerName - The name of the customer
 *  Rules for customerName:
 *   1) Starts with number or letter
 *   2) Only contain numbers, letters, or dashes
 *   3) No double dashes
 *   4) Length of domainPrefix and customerName cannot exceed 49 (50 if you include the dash joining the two)
 *   5) Won't allow "bad" words. Client won't know what the bad words are, but will return a 400 Client Error.
 * @param {text} domainPrefix - The domain prefix making the request, everything left of '.domo.com.' (optional)
 * @param {text} configId - The name of the Configuration template '<CUSTOMER>-subscriber'. You can request the config name from your account representative. (optional)
 * @param {UUID} templateId - The ID of the Instance template. Use getInstanceTemplates() to get the list of available templates. (optional)
 * @param {text} regionId - The Region to provision in (US, EU, OR, CA, AU, JP, AZURE). (optional)
 * @param {text} keyAttribute - The key attribute used for mapping & routing. (optional)
 * @param {list} additionalUsers - Additonal user to add to the instance. Must define at least one, generally this is the Major Domo who will be managing the instance.
 * {
 *    "displayName": "John Doe",
 *    "emailAddress": "john@doe.com",
 *    "role": "Admin",
 *    "password": "Testing123!",
 *    "sendMail": false
 *  }
 *
 * @returns {object} - The response
 * {
 *     "id": "<INSTANCE_ID>",
 *     "customerDomain": "<DOMAIN>.domo.com"
 * }
 */
async function provisionInstance(
  customerName,
  domainPrefix = null,
  configId = null,
  templateId = '',
  region = null,
  keyAttribute = null,
  additionalUsers,
) {
  try {
    const body = {
      teamName: customerName,
      ...(domainPrefix && { domainPrefix }),
      ...(configId && { configId }),
      orgTemplateId: templateId,
      ...(keyAttribute && { keyAttribute }),
      ...(region && { region }),
      additionalUsers: additionalUsers,
    };

    return await Helpers.handleRequest(
      'post',
      '/api/publish/v2/controlcenter/subscribers',
      body,
    );
  } catch (error) {
    throw new Error('Unable to provision instance.', error);
  }
}

async function getInstanceTemplates() {
  return await Helpers.handleRequest('get', '/api/publish/v2/org-templates');
}
```
