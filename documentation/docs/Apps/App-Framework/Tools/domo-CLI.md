---
stoplight-id: rmfbkwje8kmqj
---

# Domo Apps CLI

The Domo Apps Command Line Interface (CLI) will be your main tool to 

- create,
- publish, and
- edit

Custom App designs to your Domo instance. 

Here's how to [install it](/docs/Apps/App-Framework/Quickstart/Setup-and-Installation.md). 

The following is an enhanced **reference** for the more **common** CLI commands. 

For a **complete** list of commands available, use `domo --help` (refer to the Help section below).

### Help
---
If at any point you need a reminder on the available commands for the CLI, you can run

```
$ domo -h
```

Additionally, you can get available options for a specific command with

```
$ domo [command] -h
```

#### OPTIONS
* `-v, --version`: output the version number
* `-s, --ssl`: disable SSL
* `-m, --manifest <filename>`: specify a manifest file. Defaults to `manifest.json` in the current working directory.
* `-h, --help`: output usage information


### Common Commands
---
#### dev

Spins up a local development server with the following features:

  * **Live Reload**: Reloads when code changes are detected.
  * **App Sizing**: Renders the app in a frame that honors the sizing and fullpage settings from the app manifest.
  * **Data Proxy**: Proxies basic XHR requests for data to the appropriate Domo instance, enabling local development with live data.

```
$ domo dev [options]
```

#### OPTIONS
* `-u, --userId`: Utilizes a specific user. Helpful for testing app states where user ID is important.
* `-e, --external`: Exposes the dev server on a public IP address.

#### Advanced Data Proxy for Developing Locally
In order to enable proxying for advanced requests (like the AppDB, Files, Code Engine, and Workflows APIs), you must provide the ID of an app in your instance that the CLI can proxy to (e.g., impersonate a particular Card). You can add this app ID to your manifest under the property `proxyId`. Assuming the ID is valid, proxying advanced requests with `domo dev` will automatically start working.

All proxy IDs for your app can be found on the App Design page under the "Cards" tab.

Proxy IDs tie apps to Cards. If you delete the Card from which you retrieved the ID, you will have to get a new one from another card created from your app design.

#### init

Asks you questions to initialize a new Custom App design template. Once complete, be sure to follow the "Next Steps" provided.

<!-- theme: info -->
> #### No `mkdir` necessary
>
> `domo init` will create the folder for you.

#### PROMPTS
* design name
* select a starter: see "STARTERS" section
* would you like to connect to any datasets? (Y/n): see "DATASET MAPPING PROMPTS"

#### STARTERS
* hello world: creates a basic project in a new directory with the following content

```
design-name
  - app.css
  - app.js
  - domo.js
  - index.html
  - manifest.json
```

* manifest only: Adds a single `manifest.json` file to the current working directory.

* basic chart: Gets you started rendering a basic [Domo Phoenix] bar chart.

* map chart: Gets you started rendering a [Domo Phoenix] world map chart.

* sugarforce: Creates an app with multiple screens; it shows how to handle tabbing between screens, database CRUD operations, and more.

[Domo Phoenix]: https://domoapps.github.io/domo-phoenix/

#### DATASET MAPPING PROMPTS
* dataset id: Can be found in the URL of the DataSet detail page in the Domo instance. `https://[customer].domo.com/datasources/[dataset id]/details/overview`
* dataset alias: The alias your app will use when requesting data from Domo. Make sure it has no spaces or special characters.

**Note**: Be sure to complete the field mapping portion in the `manifest.json`. Refer to the [manifest](/docs/Apps/App-Framework/Guides/manifest.md#mapping) reference docs for more details on data mapping.

#### login [options]

Authenticate to your Domo instance from the CLI. This is a requirement before doing other commands like `publish`, and for fetching data during `domo dev`. If no options are provided, you'll be prompted to choose from a list of previous instances or a "new instance", at which point you'll be prompted for instance name, username, and password.

```
$ domo login [options]
```

#### OPTIONS
* `i, --instance`: Domo instance (e.g. customer.domo.com)
* `u, --user-email`: User email
* `--no-upgrade-check`: Prevent the CLI from checking for new versions and prompting for user input to upgrade or not

#### owner <add|rm|ls>

Manage the owners of the Custom App design. 

Only owners of a design are able to manage that design from the CLI or the Asset Library within the Domo instance. Additionally, only owners of a design are authorized to deploy new apps based on that design.

```
$ domo owner [options] [add|rm|ls] joe.bob@mycompany.com
```

#### OPTIONS
* `-i, --design_id`: specify a design ID or defaults to the ID from the manifest file in the current working directory

#### publish 

Uploads all the assets of your current working directory as a Custom App design.

You can choose to [ignore certain files]((/docs/Apps/App-Framework/Guides/manifest.md#ignore)), meaning `domo publish` will not upload those files. Any node_modules directories are ignored by default. Refer to the [manifest](/docs/Apps/App-Framework/Guides/manifest.md#ignore) reference docs for more details on ignoring files.

If an existing ID is not found in the manifest, a new design will be created, and the manifest file will be updated with the newly created design ID. Existing designs will be updated.

```
$ domo publish [options]
```

#### OPTIONS
* `-g, --go`: Opens the design in the Asset Library after publishing.

#### release

Locks a design version for submitting to the Domo Appstore. Once a version is released, you can't make further changes to it. You can, however, work on a new version by bumping the version in the manifest file. 

```
$ domo release
```
