# Shipping Logs to SIEM

## Domo Activity Logs 

Domo provides the Activity logs in which you can view events for all individuals in your instance. As well as you can ship these logs to SIEM to analysis and create alerts around the logs. 

This document focused on how you can send these logs to external SIEM solution using webhook. 

## Access the Activity Logs 

From the Admin Settings under **Governance**, select  **Activity log**. 

You can only view the Activity log if you have an Admin default security role or a custom role with the View Activity Logs grant enabled. 

## SHIP logs to SIEM 

In this document we are taking Sentinel as our SIEM solution, you can use any other SIEM as well if it supports integration using Webhook, which most of the SIEM solution supports. 

## Part I – Configure Sentinel to receive logs via Webhook. 

### STEP 1 

1. Go to Azure Portal. 
2. Search for Logic Apps and Open Logic Apps dashboard. 
3. Click the Add button on top.
<img class="size-full wp-image-3271 aligncenter" src="../../assets/images/siem1.png" alt=""  />

4. Select the **Resource Group**, provide a useful **Logic App Name** and **region**. 
5. Select the Storage, Networking configuration and monitoring in next steps. 
6. Provide appropriate tags. 
7. Click Create to deploy the app. 

### STEP 2

1. Under **Workflows** click **Workflows**.
<img class="size-full wp-image-3271 aligncenter" src="../../assets/images/siem2.png" alt=""  />

2. Click Add**Add** -> **Add**. 
3. Provide a useful name and choose **Stateful** or **Stateless** depending on your use case and Click **CREATE**.
4. Now select your created workflow. 
5. In the above selected workflow click **Developer -> Designer**. 

### STEP 3

1. Click **Add-a-Trigger**. 
2. In the search bar search for **“When a HTTP request is received”**. Click it. 
3. Select the method as **POST**

### STEP 4
1. Click the + sign. 
2. Search for **Azure Log Analytics** and then **Send Data**. 
3. In the **Json Request Body**, click **Fx**
<img class="size-full wp-image-3271 aligncenter" src="../../assets/images/siem3.png" alt=""  />

4. After that click **Dynamic Content**Dynamic Content and then **body**.
<img class="size-full wp-image-3271 aligncenter" src="../../assets/images/siem4.png" alt=""  />

5. Add a Custom Log Name which you want to keep for log table
6. Then Click **Save**, once you click save the webhook URL will appear.
<img class="size-full wp-image-3271 aligncenter" src="../../assets/images/siem5.png" alt=""  />

7. You can see the webhook URL as shown in the below image.
<img class="size-full wp-image-3271 aligncenter" src="../../assets/images/siem6.png" alt=""  />

## Part II – Configure Domo to send logs via Webhook. 

### STEP 1

Go to your Domo instance and sign in using your preferred method. 

### STEP 2

Once logged in go to **More -> Admin**. 

<img class="size-full wp-image-3271 aligncenter" src="../../assets/images/siem7.png" alt=""  />

### STEP 3

Go to **Activity Logs** under **Governance**. 

<img class="size-full wp-image-3271 aligncenter" src="../../assets/images/siem8.png" alt=""  />

### STEP 4

Once you click the **Activity Logs**, you will see all of the activity happening in your instance. 

Once on this page click the **Webhook** icon as shown in image below. 

<img class="size-full wp-image-3271 aligncenter" src="../../assets/images/siem9.png" alt=""  />

### STEP 5

In the highlighted field enter your webhook URL as highlighted in image, if your webhook url has secret as well put it in the field below webhook URL. If webhook doesn’t require secret, enter any random value. 

<img class="size-full wp-image-3271 aligncenter" src="../../assets/images/siem10.png" alt=""  />

### STEP 6

Here you will see the **Webhook Filtering** field as well. You can choose for which **categories** you want to forward the logs as well as to go more granule you can select the **subfields** under that category. 
 
**NOTE:** If you don’t select any field nothing will be forwarded. 

<img class="size-full wp-image-3271 aligncenter" src="../../assets/images/siem11.png" alt=""  />


### STEP 7

Verify the logs from this dashboard itself. Once the logs are forwarded to webhook these logs will be available on the same page under **Activity Log Webhook Recent Deliveries**. 

That’s All! 