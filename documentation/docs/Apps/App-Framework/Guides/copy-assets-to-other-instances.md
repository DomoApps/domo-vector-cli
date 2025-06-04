
# Copy Assets to a Different Instance

Sometimes we have multiple instances that all need to use the same app. In some cases it can be easier to just download the code without having to rebuild it.

<!-- theme: info -->
> #### You need to have the Domo CLI installed
> - [Instruction how to install the Domo CLI](../Quickstart/Setup-and-Installation.md) 
> - [Domo Apps CLI documentation](../Tools/domo-CLI.md)


1. Download the asset from the asset library
![asset-download-screenshot.png](../../../../assets/images/asset-download-screenshot.png)

2. Unzip the downloaded bundle

3. Open command line and navigate to the new folder

4. Log into the new instance using `domo login` 

5. Remove the `id` from `manifest.json`

6. Publish the asset using `domo publish`