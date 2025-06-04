---
internal: true
tags: [Tutorial]
---

# Reactjs Barcode Scanner Tutorial

This tutorial walks through how to build a PWA Reactjs app that can scan a barcode and display the scanned text.


### Step 1: Setup and Installation

---

Before beginning, please make sure you’ve successfully installed the Domo Apps CLI and followed the basic setup and installation instructions found [here](https://developer.domo.com/docs/dev-studio-quick-start/set-up).

### Step 2: Create a new Reactjs project
---
After setting up your local environment, please initialize a Reactjs project using domo's template found in this [article](https://developer.domo.com/portal/u8w475o2245yp-starter-kits).

### Step 3: Launch a Local Development Environment
---
Start the app using either `yarn start` or `npm start`, depending which package manager you chose to generate your app. A new tab will open in your browser with this url `http://localhost:3000/`. Any change you do in the app will be shown here in real time.

### Step 4: Setting up Progressive Web App (PWA) Features.
---
Here we will set up your app to be PWA ready, just follow the following steps.

1. Create a new file named `service-worker.js` in the `public` directory of your project. This file will contain the service worker logic.

   ```ts
   /* eslint-disable no-restricted-globals */
   const CACHE_NAME = `barcode-scanner-cache-v1`;
   const urlsToCache = [
     `/`,
     `/index.html`,
     `/static/js/bundle.js`,
     `/static/js/0.chunk.js`,
     `/static/js/main.chunk.js`,
     `/favicon.ico`,
     `/logo192.png`,
   ];

   self.addEventListener(`install`, (event) => {
     event.waitUntil(
       caches.open(CACHE_NAME).then((cache) => cache.addAll(urlsToCache))
     );
   });

   self.addEventListener(`fetch`, (event) => {
     event.respondWith(
       caches.match(event.request).then((response) => {
         if (response) {
           return response;
         }
         return fetch(event.request);
       })
     );
   });
   ```

2. Add a script tag to register the service worker in your index.html file. Place this script tag inside the <head> section.

   ```ts
     <head>
     <meta charset="utf-8" />
     <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
     <meta name="viewport" content="width=device-width, initial-scale=1" />
     <meta name="theme-color" content="#000000" />
     <meta
       name="description"
       content="Web site created using create-react-app"
     />
     <link rel="apple-touch-icon" href="%PUBLIC_URL%/logo192.png" />
     <!--
       manifest.json provides metadata used when your web app is installed on a
       user`s mobile device or desktop. See https://developers.google.com/web/fundamentals/web-app-manifest/
     -->
     <link rel="manifest" href="%PUBLIC_URL%/manifest.json" />
     <!--
       Notice the use of %PUBLIC_URL% in the tags above.
       It will be replaced with the URL of the `public` folder during the build.
       Only files inside the `public` folder can be referenced from the HTML.

       Unlike "/favicon.ico" or "favicon.ico", "%PUBLIC_URL%/favicon.ico" will
       work correctly both with client-side routing and a non-root public URL.
       Learn how to configure a non-root public URL by running `npm run build`.
     -->
     <title>React App</title>
     <script>
       if (`serviceWorker` in navigator) {
         window.addEventListener(`load`, () => {
           navigator.serviceWorker.register(`/service-worker.js`).then(
             (registration) => {
               console.log(
                 `ServiceWorker registration successful with scope: `,
                 registration.scope
               );
             },
             (error) => {
               console.log(`ServiceWorker registration failed: `, error);
             }
           );
         });
       }
     </script>
   </head>
   ```

3. Edit your `manifest.json` and add the PWA metadata.

   ```ts
   {
     "name": "Barcode Scanner",
     "version": "0.0.1",
     "size": {
         "width": 3,
         "height": 3
     },
     "short_name": "Scanner",
     "icons": [
         {
             "src": "logo192.png",
             "sizes": "192x192",
             "type": "image/png"
         },
         {
             "src": "logo512.png",
             "sizes": "512x512",
             "type": "image/png"
         }
     ],
     "start_url": "/",
     "display": "standalone",
     "theme_color": "#007bff",
     "background_color": "#ffffff",
     "mapping": []
   }
   ```

### Step 5: Creating the App component
---
These are the steps necessary to create your app component, including the barcode scanner part of it. You may subdivide the component into smaller components, but that will not be addressed in this tutorial. 

1. Open the new directory created by the template generator with Visual Studio Code.

4. Start by creating a new folder called `components` this is where we will be creating each of the apps components. In our case, we will only be using one component, App, but it\`s good practice organizing the app directory.

5. Create a new folder inside called `app`. Here is where we will move our `App.xx` files.
   - a. Move all the files that has `App.` in it to the `app` folder. For example: `App.js`

6. Inside `index.js` change the import of `App` to reflect the change in directory.
   - from `import App from './App';` to `import App from './components/app/App';`

7. Now we will install a library that will take care of scanning and decoding the barcode.
   - `yarn add html5-qrcode` or `npm install html5-qrcode`, depending on which package manager you have.

8. Import `Html5Qrcode` module from the library in our `App.jsx` file. this is done in the top of the file.
   - import { Html5Qrcode } from `html5-qrcode`;

9. Also import other dependencies and css

   ```ts
   import React, { useEffect, useRef, useState } from `react`;
   import { Html5Qrcode } from `html5-qrcode`;
   import styles from `./App.module.css`;
   ```

10. Now we create the scanner component inside the `App.jsx` file. Lets start by removing all the previous unnecessary code and replace them.

11. Lets create some local states to track scanner status and results

    ```ts
    function App() {
    const html5QrCodeRef = useRef(null);
    const [isScannerRunning, setScannerRunning] = useState(false);
    const [isScannerInitialized, setScannerInitialized] = useState(false);
    const [scannedResult, setScannedResult] = useState(``);
    ```

    - html5QrCodeRef is used to store the instance. Its necessary for the library.

12. We create a `handleScan()` function to handle the start and stoping of the scanner.

    ```ts
      const handleScan = () => {
      if (!isScannerRunning && html5QrCodeRef.current) {
        const config = { fps: 10, qrbox: { width: 250, height: 250 } };
        const qrCodeSuccessCallback = (decodedText, decodedResult) => {
          setScannedResult(decodedText)
        };
        html5QrCodeRef.current.start({ facingMode: `user` }, config, qrCodeSuccessCallback);
        setScannerRunning(true);
      } else {
        if (html5QrCodeRef.current && isScannerRunning) {
          html5QrCodeRef.current.stop().then((ignore) => {
            setScannerRunning(false)
          }).catch((err) => {
            window.alert(`Stop unsucessful`)
          });
        }
      }
    };

    ```

    Inside the function we are calling various methods from the library, such as `.start` and `.stop`. We are also telling the library what the camera parameters will be, and also the size of the scanner zone. We are checking if the scanner is not running and that we have the instance (where the scanner will be displayed) in the DOM, before we start the library. If this is true, then we start the scanner and save the decodedText in the local state. If not, the app will try to stop the scanner.

13. This useEffect was created to find the instance where the scanner will be displayed in the DOM. We will call it `reader` in the render part of the code.

    ```ts
      useEffect(() => {
        if (!isScannerInitialized) {
          html5QrCodeRef.current = new Html5Qrcode(`reader`);
          setScannerInitialized(true);
        }
      }, [isScannerInitialized]);
    ```

14. Finally, the render is added. Here we will add the rendered parts of the app and style them. We require a `div` with a specific id so we can instance it, named `reader`. All you need is the scanner div, and a button. Everything else is extra. You may style it as you like.

    ```ts
      return (
      <div className={styles.container}>
        <button className={styles.button} onClick={handleScan}>
          {isScannerRunning ? `Stop Scanner` : `Start Scanner`}
        </button>
        <div className={styles.reader} id=`reader` style={{ width: `400px`, alignContent: `center` }} />
        <span className={styles.scannedText}>{scannedResult}</span>
      </div>
    );
    ```

15. Export the component to be accessed from `index.js`.

    ```ts
    export default App;
    ```

16. Create a `.env` file inside the main directory and add this code to it. Without it, the library may throw errors.

    ```ts
    GENERATE_SOURCEMAP=false
    ```

### Extra information
---
Here are some additional files and information. What CSS styles was used and the whole `app` component will be here, as well as the file directory, for easier navigation and reference.

#### CSS styles used

```css
  .container {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 8px;
  }

button {
  background-color: #007bff;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #0056b3;
}

.reader {
  width: 400px; 
  height: 300px;
  border: 1px solid #ccc;
  margin-top: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  background-color: #f9f9f9; 
}

.scannedText {
  font-size: 16px;
  color: #333;
  padding: 10px;
  margin-top: 20px;
  min-width: 380px;
  background-color: #f9f9f9;
  border: 1px solid #ccc;
  text-align: center;
}
```

#### App.jsx file

```ts
import React, { useEffect, useRef, useState } from `react`;
import { Html5Qrcode } from `html5-qrcode`;
import styles from `./App.module.css`;

function App() {
  const html5QrCodeRef = useRef(null);
  const [isScannerRunning, setScannerRunning] = useState(false);
  const [isScannerInitialized, setScannerInitialized] = useState(false);
  const [scannedResult, setScannedResult] = useState(``);

  const handleScan = () => {
    if (!isScannerRunning && html5QrCodeRef.current) {
      const config = { fps: 10, qrbox: { width: 250, height: 250 } };
      const qrCodeSuccessCallback = (decodedText, decodedResult) => {
        setScannedResult(decodedText)
      };
      html5QrCodeRef.current.start({ facingMode: `user` }, config, qrCodeSuccessCallback);
      setScannerRunning(true);
    } else {
      if (html5QrCodeRef.current && isScannerRunning) {
        html5QrCodeRef.current.stop().then((ignore) => {
          setScannerRunning(false)
        }).catch((err) => {
          window.alert(`Stop unsucessful`)
        });
      }
    }
  };

  useEffect(() => {
    if (!isScannerInitialized) {
      html5QrCodeRef.current = new Html5Qrcode(`reader`);
      setScannerInitialized(true);
    }
  }, [isScannerInitialized]);

  return (
    <div className={styles.container}>
      <button className={styles.button} onClick={handleScan}>
        {isScannerRunning ? `Stop Scanner` : `Start Scanner`}
      </button>
      <div className={styles.reader} id=`reader` style={{ width: `400px`, alignContent: `center` }} />
      <span className={styles.scannedText}>{scannedResult}</span>
    </div>
  );
}

export default App;
```

#### File directory structure

```
  |____yarn.lock
  |____public
  | |____favicon.ico
  | |____index.html
  | |____logo512.png
  | |____manifest.json
  | |____thumbnail.png
  | |____service-worker.js
  | |____robots.txt
  | |____logo192.png
    |____src
  | |____reportWebVitals.js
  | |____setupProxy.js
  | |____index.js
  | |____index.css
  | |____components
  | | |____app
  | | | |____App.module.css
  | | | |____App.test.js
  | | | |____App.jsx
  | |____setupTests.js
  |____package.json
  |____.env
```
