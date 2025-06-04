# Export Domo cards to PDF

The code below can be utilized in a Code Engine package which will generate a PDF for each card on a page. If the content includes a table, you may get paginated results.

In order to use this code, you will need to have the following:

- A Domo instance
- A page with cards on it
- Access to Code Engine and basic knowledge of how to create a package

<!--
title: "Cards to PDF Code Engine Package"
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
 * Get all the Cards on a Page
 *
 * @param {string} pageID - The ID of the page
 * @returns {Object} An array of Card ID's
 * @throws {Error} If the request fails
 */
async function getCardsOnPage(pageID) {
  try {
    var url = `/api/content/v1/pages/${pageID}/cards?parts=metadata`;

    return await Helpers.handleRequest('get', url);
  } catch (error) {
    throw new Error('getCardsOnPage: ', error);
  }
}

/**
 * Get a PDF of a Card.
 * If the Card is a chart it will return a single image
 * If the Card is a Table, you can specify the number of pages returned
 *
 * @param {string} cardID - The ID of the card
 * @param {number} numTablePages - The number of pages you want returned
 * One nuance on the “pages” property… let’s say you specify 30 pages, and its actually 22 pages…
 * you’ll get 22 pages. If you specifcy 30 pages and it’s actually 32 pages, you’ll get 30 pages.
 * So err on the high side.
 *
 * You can also get a PNG of the Card by changing the URL param: parts=image
 * There is a 25MB limit. The default url param is parts=image, which will return PNG’s. Changing that
 * to parts=imagePDF will save tons of space and you should get back all your pages.
 *
 * @returns {Object} base64 encoded PDF
 * @throws {Error} If the request fails
 */
async function getPDF(cardID, numTablePages) {
  try {
    const body = {
      queryOverrides: {},
      width: 1800,
      height: 2000,
      scale: 2, // We recommend a 2x scale for cleaner output
      treatLongsAsStrings: true,
      ...(numTablePages && { numTablePages }),
      cardLoadContext: {},
    };

    return await Helpers.handleRequest(
      'put',
      '/api/content/v1/cards/kpi/' + cardID + '/render?parts=imagePDF',
      body,
    );
  } catch (error) {
    throw new Error('getPDF: ', error);
  }
}

/**
 * Return all content of a Page as PDFs.
 **/
async function page2PDF(pageID) {
  try {
    const cardArray = await getCardsOnPage(pageID);
    // console.log('cardArray: ', cardArray);

    for (var i = 0; i < cardArray.length; i++) {
      var md = cardArray[i].metadata;

      if (md.chartType != 'badge_basic_table') {
        const c_pdf = await getPDF(cardArray[i].id);

        console.log('c_pdf: ', c_pdf.image.data);
      } else {
        const t_pdf = await getPDF(cardArray[i].id, 100);

        console.log('t_pdf: ', t_pdf.image.message);
      }
    }
  } catch (error) {
    throw new Error('page2PDF: ', error);
  }
}
```
