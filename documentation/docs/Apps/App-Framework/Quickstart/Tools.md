---
stoplight-id: 37rc8izzjzj7z
---

# Tools

#### domo.js (also known as ryuu.js)
The `domo.js` library provides some convenient utilities for building custom Apps. For more important [see documentation here](../Tools/domo.js.md).

#### Domo Apps CLI
The [Domo Apps Command Line Interface (CLI)](../Tools/domo-CLI.md) will be the main tool to create, publish, and edit custom app designs to your Domo instance.

#### Domo Phoenix Charting Engine
Domo has built a JavaScript wrapper for using Phoenix in your custom app. The wrapper is hosted in GitHub: <a href="https://github.com/DomoApps/domo-phoenix">Domo Phoenix</a> with links to the <a href="https://domoapps.github.io/domo-phoenix/">Documentation</a>  as well as examples.


#### Query Library
One of the most common issues app developers run into when building custom apps is malformed query requests. This is due, in large part, to the error-prone nature of complex string manipulation needed to format queries. To help overcome this hurdle, our own internal app developers <a href="https://www.npmjs.com/package/@domoinc/query">created a query library that takes a more object-oriented approach to creating the needed query strings</a>.

#### Proxy Middleware
The Dev Studio CLI command `domo dev` launches a local development server and proxies requests to Domo App APIs so you can develop locally with data from your Domo instance. This <a href="https://www.npmjs.com/package/@domoinc/ryuu-proxy">npm module</a> encapsulates a similar proxy so that you can add it to whichever node-based development server you're using.
