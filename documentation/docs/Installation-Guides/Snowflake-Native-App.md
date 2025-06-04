# Snowflake Native App

## Intro

Setting up Snowflake Cloud Amplifier integrations from the Domo side requires the execution of SQL statements on Snowflake to prepare the environment to accept connections from Domo, and to be able to setup read and write. The Native Cloud Amplifier app in Snowflake helps simplify this process by leveraging the advantages of running on Snowflake, which allows it to run configurations that otherwise would require additional permissions from the Domo side.

## Initial configuration

### Configure the Storage Integration

- On the top bar, select Snowflake Administration.
- Click on the Storage Integration button on the left navigation panel.

![Image](../../assets/images/ca-api-admin.png)

- Enter the following information:

| Field                         | Description                                                                     |
| ----------------------------- | ------------------------------------------------------------------------------- |
| Default Role                  | Snowflake default role to be used by the application.                           |
| Snowflake Write Database      | Snowflake database where the outputs from Domo will be written.                 |
| Snowflake Storage Integration | Name of the storage integration that will be used by Domo storage integrations. |

- Click on the **Generate SQL** button.

![Image](../../assets/images/ca-snowflake-admin.png)

- Copy the generated SQL code and execute it on Snowflake.

![Image](../../assets/images/ca-admin-sql.png)

### Configure OAuth on the Snowflake side

- On the top bar, select Snowflake Administration.
- Click on the OAuth button on the left navigation panel.

### Configure the Domo Admin section

- On the top bar, select Domo Administration.
- Click on the Admin button on the left navigation panel.

![Image](../../assets/images/ca-admin-oauth.png)

- To set or update your Domo instance, enter the name of your **Domo instance** (e.g., `some-company.domo.com`) and click on **Update Domo Instance**.
- To update your API token, create an API token in Domo, enter it in the **API Token** field, and then click on the **Update API Token** button to save it. Please check the [Manage Access Tokens](https://domo-support.domo.com/s/article/360042934494) KB article for more information.
- To check the validity of your API token, click on the **Test API Token**.

## Managing Domo Cloud Amplifier Integrations

### Access the Integrations Section

- On the top bar, select Domo Administration.
- Click on the Integrations button on the left navigation panel.
- You will be presented with a list of existing integrations.

![Image](../../assets/images/ca-access-int.png)

### Create / Edit an integration

To create a new integration, click on the **New Integration** button located at the top of the screen. If you want to edit an integration, find it in the list and click on **Edit**.

- On the **Integration Name** field, enter a name to help you later identify your Cloud Amplifier integration.
- Enter a **Description** for the purpose of the integration (Optional).
- Choose a connection method between **Keypair** or **Username & Password**. You may want to use **Keypair** as the username & password method will soon be deprecated by Snowflake. You can find information about how to set up keypair [here](https://docs.snowflake.com/en/user-guide/key-pair-auth).

![Image](../../assets/images/ca-keypair.png)

- You will see that the **Snowflake connection URL** for your instance is already there.
- Enter your **Snowflake username**.

For keypair connection:

- On the **Snowflake Keypair Private Key**, paste the Private Key you created.
- Enter the **Snowflake private key passphrase**.

For username & password:

- Enter your **Password**.

![Image](../../assets/images/ca-enter-creds.png)

- Choose one option from the **Snowflake role settings.** You can choose to use the **Default** role, the **Secondary roles**, or you can choose to **Specify a role** in which case you will need to provide the name of the **Snowflake primary role.**
- At the end of this screen, you can decide if you want to turn OAuth on or not, by using the **Use OAuth per-user authentication** switch.
- When you are done, click on the **Next** button.

![Image](../../assets/images/ca-role-setting.png)

- Configure the **Data Freshness** options and then click on **Next**. See [here](https://domo-support.domo.com/s/article/4412849158167?language=en_US#advanced_scheduling) for additional information about data freshness.

![Image](../../assets/images/ca-set-int.png)

## Adding write access to an Integration

- Navigate to the **Domo Integrations** page by following the instructions detailed in the **Access the Integrations Section** part of this document.
- Locate your integration in the list and click on the **Write** button.

![image](../../assets/images/ca-write-access-int.png)

- Enter the **Default Role** that the integration will use, a **Snowflake Database** and the **Schema** where Domo will write, and then click on the **Generate SQL** button.

![image](../../assets/images/ca-run-sql.png)

- A script will be generated below. Review it and then click on the **Run Script** button.

![image](../../assets/images/ca-run-script.png)

## Checking the details of an Integration

- Navigate to the **Domo Integrations** page by following the instructions detailed in the **Access the Integrations Section** part of this document.
- Locate your integration in the list and click on the **Details** button.

![image](../../assets/images/ca-domo-int-detail.png)

- A dialog will be presented with the details of your integration

![image](../../assets/images/ca-int-detail-dialog.png)

## Deleting an Integration

- Navigate to the **Domo Integrations** page by following the instructions detailed in the **Access the Integrations Section** part of this document.
- Locate your integration in the list and click on the **Write** button.

![image](../../assets/images/ca-delete-int.png)

- A confirmation modal will be presented. Click on **Delete** if you want to proceed with the deletion or **Cancel** to go back to the list of integrations.

![image](../../assets/images/ca-delete-int-dialog.png)
