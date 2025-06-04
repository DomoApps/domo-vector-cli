---
stoplight-id: u8w475o2245yp
---

# Starter Kits

### Bring Your Own Stack (BYOS)
---
Does `domo init` not give you enough of what you’re used to for starting new projects If you have a generator or starter kit you’re partial to, you can still use it. All you have to do is update your local development server to handle requests for data from Domo. Here are a few examples of how you can leverage the <a href="https://www.npmjs.com/package/@domoinc/ryuu-proxy">ryuu-proxy</a> module to turn any existing web application into a Domo App.

<!--
type: tab
title: React
-->

<!-- theme: info -->
> #### Advanced React Template
>
> In addition to the **basic template below**, Domo also has a more advanced template available that Domo teams use when building apps. Contact your Account Executive for more information on how to obtain access to the Advanced App Platform Package. 

#### Basic Create React App

DomoApps has a basic create-react-app template that can be installed that includes all the Domo-specific dependencies and configurations. Follow the instructions from the <a href="https://create-react-app.dev/docs/getting-started#creating-an-app">create-react-app documentation</a> to install a new react app with the [`@domoinc/cra-template`] template based on the package manager of your choice (`npx`, `yarn`, or `npm`).

[`@domoinc/cra-template`]: https://www.npmjs.com/package/@domoinc/cra-template?activeTab=readme

Replace the word `my-app` in the following commands with the app name of your choice.

<strong>yarn</strong>
<pre><code>yarn create react-app my-app --template @domoinc
</code></pre>
<strong>npx</strong>
<pre><code>npx create-react-app my-app --template @domoinc
</code></pre>
<strong>npm</strong>
<pre><code>npm init react-app my-app -- --template @domoinc
</code></pre>

These commands will create your project in a `my-app` folder with the following included:

- The manifest and thumbnail are provided in the `public` folder.
- The proxy server is setup with `@domoinc/ryuu-proxy` for local development to your domo instance.
- An upload script has been added to the package.json for easy upload.

#### Upload and configure

- Use the [domoapps cli](/docs/Apps/App-Framework/Quickstart/Setup-and-Installation.md) to login to your Domo instance with `domo login`
- Upload the boilerplate app to your Domo instance using `yarn upload` or `npm run upload`
  - The project will build, add all assets to the `build` folder, and then upload the assets to Domo
  - The `manifest.json` file in the `build` folder will be modified by the domoapps cli to include an `id` property—you will want to copy this `id` into the manifest in your `public` folder so that it doesn't continue to create a new `id` on each upload
- If you intend to use endpoints provided by the App Platform (e.g. datasets, AppDB, etc), make sure to also add a `proxyId` to the `manifest.json` file in your `public` folder. See [proxy documentation](../Guides/manifest.md#getting-a-proxyid-advanced) for more info.</li>

#### Local Development


Run the `yarn start` (or `npm start`) command (after you've uploaded your app at least once) to start developing locally.


<!--
type: tab
title: Angular
-->

#### Prerequisites

You'll need the <a href="http://cli.angular.io/">Angular CLI</a> installed in order to run the `ng add` command.

#### Create a new project

<pre>
<code>$ ng new domo-app
$ cd domo-app
</code>
</pre>

Select NO when prompted whether SSR should be enabled for the new project.

#### Add Ryuu Angular

<pre><code>$ ng add @domoinc/ryuu-angular
</code></pre>
This will add the following:

- Domo `manifest.json` and `thumbnail.png` to a new `domo` directory at the root of the project
- `extra-webpack.config.js` at the root of the project that configures a local proxy.
- `domo:upload` helper script to `package.json` to upload to Domo.

#### Local development

In order for the proxy to work in local development you need to have uploaded your app at least once with `npm run domo:upload`

After this you should be able to run `ng serve` like normal and you'll be able to proxy domo requests in your local development.

<!--
type: tab
title: Vue
-->

#### Prerequisites

Install <a href="https://github.com/vuejs/vue-cli">Vue CLI</a>


#### Create new project

<pre>
<code>vue init webpack my-app
cd my-app
</code>
</pre>

#### Add Domo Assets

Add a `manifest.json` and `thumbnail.png` to a `./domo` directory at the root of the project. Then modify the copy plugin patterns in the `./build/webpack.prod.conf.js` to copy over Domo assets.

<pre>
<code>new CopyWebpackPlugin([
  { from: path.resolve(__dirname, '../static'), to: config.build.assetsSubDirectory, ignore: ['.*'] },
  { from: path.resolve(__dirname, '../domo') },
])
</code>
</pre>

#### Add Domo Dev Proxy

<pre>
<code>npm install --save-dev @domoinc/ryuu-proxy
</code>
</pre>

Add the following to `./config/index.js`
<pre>
<code>var { Proxy } = require('@domoinc/ryuu-proxy')
var manifest = require('../domo/manifest.json')
var domoProxy = new Proxy({ manifest })
</code>
</pre>

Now add the following to `dev:{}` within the same file `./config/index.js`
<pre>
<code>dev: {
    // existing scaffolded options
    // ...
    // ...
    "before": app =&gt; app.use(domoProxy.express())
}
</code>
</pre>

Open `./build/webpack.dev.conf.js` and add the following to the end of `devServer: {}`
<pre>
<code>devServer: {
    // existing scaffolded options
    // ...
    // ...
    before: config.dev.before
}
</code>
</pre>

Add `id` to `manifest.json` if not already done, and run:
<pre>
<code>domo publish
</code>
</pre>

<!-- type: tab-end -->
