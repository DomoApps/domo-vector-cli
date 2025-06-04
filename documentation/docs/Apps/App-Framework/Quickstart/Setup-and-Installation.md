---
stoplight-id: 6hlzv1hinkq19
---

# Setup and Installation

### Step 1: Install the Domo Apps CLI
---
The [Domo Apps CLI](../Tools/domo-CLI.md) is the command line tool you can use to authenticate against your Domo Instance and publish your apps there.


<!--
type: tab
title: Mac OSX / Linux
-->

If you are a Mac or Linux user, you will need to have <a href="https://brew.sh/">Homebrew</a> installed on your machine.

<strong>Mac:</strong>
<pre><code>brew install DomoApps/ryuu/domo
</code></pre>
<strong>Linux:</strong>
<pre><code>brew install DomoApps/ryuu/domo-linux
</code></pre>

<!--
type: tab
title: Windows
-->

If you are a Windows user, you will need to have <a href="https://chocolatey.org/">Chocolatey</a> installed on your machine. You may also need to run your commands in PowerShell rather than the standard command prompt.

<pre><code>choco install domo
</code></pre>

<!--
type: tab
title: npm
-->

The DomoApps CLI is distributed through the Homebrew and Chocolately package managers for long term support (LTS). However, there are also canary versions available via npm (Node Package Manager) that have the most recent updates that are being staged for LTS. If you have previously installed the DomoApps CLI using npm and wish to install the LTS version, <strong>you will need to uninstall the npm version first.</strong>

To uninstall the canary version so that you can install the LTS version run the following command from your terminal: <pre><code>npm uninstall -g ryuu </code></pre>

Once you have successfully uninstalled the canary version, <strong>close your terminal</strong> before proceeding. Open a new terminal and run `which domo` to ensure that there are no `domo` packages that exist within the node binaries on your machine.

If you would rather use the canary version, you can run the following command from your terminal to install it from npm: <pre><code>npm install -g ryuu </code></pre>

<!-- type: tab-end -->

Confirm that `domo` has been installed successfully by running `domo --version` from the terminal. If a version number is returned then you have successfully installed the CLI.

### Step 2: Login to your Domo Instance
---
From your command-line, run `domo login` and then select `new instance`.

Enter your assigned instance URL and then press enter. You'll then be presented with a login screen and the Domo CLI will be authorized on your instance.

**Connecting Through a Proxy**

If your organization has a firewall set up that blocks you from hitting Domo endpoints, you'll need to work with your network administrators to use the Domo Apps CLI with a proxy server. Otherwise, you can skip this step.

Set the CLI to route requests through your proxy with the following command: 
```bash
domo proxy <Proxy server name> <Port number>
```

Note: if your proxy requires an authentication step, you can add the `-a` flag (`domo proxy -a`), which will ask for your proxy username and will then also require the proxy password on all subsequent `domo` apps cli commands.




### Step 3: Create a New App
---
Run the following commands from your command line to set up a new Domo App project.
<pre><code>domo init
</code></pre>

### Step 4: Leverage Domo App Platform APIs in your Web Application
---
You can now easily integrate Domo APIs into any front-end web application. See [Tutorials](../Tutorials/Vanilla-Javascript/SugarForce.md) or [API Reference](../../../Domo-App-APIs/AppDB-API.md) for code examples. If you don’t have a pre-existing web application, in addition to the simple `domo init` templates, we have a number of [Starter Kits](Starter-Kits.md) you can use to get up and running quickly whether you prefer React, Angular, or Vue for front-end development.

### Step 5: Publish App to Domo Instance
---

We publish our final product to Domo using
<pre><code>domo publish</code></pre>

Once your app is deployed as a card, you can share it like you would any other content in Domo.
