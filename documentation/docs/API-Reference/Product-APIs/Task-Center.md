---
stoplight-id:
---

# Task Center API

Task Center allows you to organize manual tasks into different queues of work and control who can access them. They are often used in concert with [Workflows](https://domo-support.domo.com/s/article/000005108?language=en_US).

For more [background on Task Center, please see the Knowledge Base](https://domo-support.domo.com/s/article/000005172?language=en_US).

### Get Queues

---

Returns all queues the user has access to.

#### Code Example

```js
const getQueues = async (combineAttributes = true, archived = false) => {
  const queues = await domo.get(
    `/api/queues/v1/?combineAttributes=${combineAttributes}&archived=${archived}`
  );
  return queues;
};

const queues = getQueues();
```

#### HTTP Request

```text
GET /api/queues/v1/?combineAttributes={boolean}&archived={boolean}
```

#### HTTP Response

Returns a list of all queue objects the user has access to.

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8

[
    {
        "id": "168ecd84-4a15-45f6-89d9-021fbbce0481",
        "name": "Review Airplane Part Action Items",
        "description": "Human review of AI generated recommendations for QA process improvements based on product defects in manufacturing QA.",
        "active": true,
        "taskLevelFiltersEnabled": true,
        "taskLevelFilters": null,
        "owner": "8811501",
        "createdBy": "8811501",
        "createdOn": "2023-10-18T14:48:23.314Z",
        "updatedBy": "8811501",
        "updatedOn": "2023-10-18T14:48:23.314Z"
    }
]
```

### Get Queue by ID

---

Returns a queue by ID.

#### Code Example

```js
const getQueueByID = async (queueId) => {
  const queue = await domo.get(`/api/queues/v1/${queueId}`);
  return queue;
};

const queue = getQueueByID("168ecd84-4a15-45f6-89d9-021fbbce0481");
```

#### HTTP Request

```text
GET /api/queues/v1/{queueId}
```

#### HTTP Response

Returns the queue object based on the `queueId` specified.

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8

{
    "id": "168ecd84-4a15-45f6-89d9-021fbbce0481",
    "name": "Review Airplane Part Action Items",
    "description": "Human review of AI generated recommendations for QA process improvements based on product defects in manufacturing QA.",
    "active": true,
    "taskLevelFiltersEnabled": true,
    "taskLevelFilters": null,
    "owner": "8811501",
    "createdBy": "8811501",
    "createdOn": "2023-10-18T14:48:23.314Z",
    "updatedBy": "8811501",
    "updatedOn": "2023-10-18T14:48:23.314Z"
}
```

### Get Tasks

---

Returns tasks based on the filters provided in the body. If the body is an empty object, it returns all tasks the user has access to.

#### Code Example

```js
const body = {
  queueId: ["168ecd84-4a15-45f6-89d9-021fbbce0481"],
  displayType: ["ENIGMA_FORM", "EMAIL", "UNKNOWN"],
  status: ["OPEN", "COMPLETED", "VOIDED"],
  createdOn: [["2023-10-04T12:22:54.239Z", "2024-01-02T13:22:54.239Z"]],
};

const getTasks = async (body) => {
  const queue = await domo.post(
    `/api/queues/v1/tasks/list?render=true&renderParts=NAME,DESCRIPTION,MAPPING,METADATA,VERSIONS`,
    body
  );
  return queue;
};

const tasks = getTasks(body);
```

#### HTTP Request

```text
POST /api/queues/v1/tasks/list?render={boolean}&renderParts={NAME, DESCRIPTION, MAPPING, METADATA, VERSIONS}

```

#### Request Body

The request body accepts an object containing filters to apply to the request for tasks. All properties are optional and the body can be passed as an empty object to return all tasks.

| Property Name | Type     | Required | Description                                                                                                                                                                                    |
| ------------- | -------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| queueId       | String   | Optional | An array of queue ids.                                                                                                                                                                         |
| displayType   | String   | Optional | An array of display types for tasks. Options are `ENIGMA_FORM`, `EMAIL`, `UNKNOWN`.                                                                                                            |
| status        | String   | Optional | An array of statuses. Options are `OPEN`, `COMPLETED`, `VOIDED`.                                                                                                                               |
| assignedBy    | String   | Optional | An array of user ids corresponding to the user that assigned the task to.                                                                                                                      |
| assignedTo    | String   | Optional | An array of user ids corresponding to the user that the task was assigned to.                                                                                                                  |
| createdOn     | DateTime | Optional | An array containing an array with two elements: a start datetime and and end datetime, which define the createdOn date range. E.g. `[["2023-10-04T12:22:54.239Z","2024-01-02T13:22:54.239Z"]]` |
| createdBy     | String   | Optional | An array of user ids corresponding to the user that created the task.                                                                                                                          |
| assignedOn    | DateTime | Optional | An array containing an array with two elements: a start datetime and and end datetime, which define the assigedOn date range.                                                                  |
| updatedOn     | DateTime | Optional | An array containing an array with two elements: a start datetime and and end datetime, which define the updatedOn date range.                                                                  |
| completedOn   | DateTime | Optional | An array containing an array with two elements: a start datetime and and end datetime, which define the completedOn date range.                                                                |
| completedBy   | String   | Optional | An array of user ids corresponding to the user that completed the task.                                                                                                                        |
| orderByString | String   | Optional | An array of strings corresponding to the properties from this body that the list of tasks should be ordered by.                                                                                |
| version       | String   | Optional | An array version numbers to filter by                                                                                                                                                          |

#### HTTP Response

Returns a list of tasks.

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8

[
    {
        "id": "18OCT23_1JUTZM",
        "attributes": [],
        "queueId": "168ecd84-4a15-45f6-89d9-021fbbce0481",
        "version": 1,
        "createdOn": "2023-10-18T15:23:22.991Z",
        "createdBy": "8811501",
        "updatedOn": "2023-11-28T16:18:29.716Z",
        "updatedBy": "8811501",
        "completedOn": null,
        "completedBy": null,
        "assignedOn": "2023-10-18T15:23:22.991Z",
        "assignedBy": "8811501",
        "assignedTo": "8811501",
        "assigneeType": "USER",
        "lockedOn": null,
        "lockedBy": null,
        "status": "OPEN",
        "tags": [],
        "comments": [],
        "sourceSystem": "ODYSSEY",
        "sourceInfo": {
            "modelId": "6a701240-76bf-4b9a-8145-199156b371cc",
            "modelVersion": "1.2.0",
            "instanceId": "99d0d944-1d90-4622-8a49-2878b37fda10",
            "deploymentId": "0fa42581-918b-4ba4-b77f-356c55735e52",
            "instanceCreatedBy": "8811501",
            "taskKey": "6755399651689301",
            "workflowInstanceId": "6755399651689244",
            "flowNodeId": "iVpiDJGGzWIPilg",
            "elementInstanceKey": "6755399651689298"
        },
        "displayType": "ENIGMA_FORM",
        "displayId": "cce35d38-95bc-4f87-ba92-849affb13c78",
        "displayEntity": {
            "id": "cce35d38-95bc-4f87-ba92-849affb13c78",
            "name": "Airplane Part Action Items Review Form",
            "description": "",
            "settings": {},
            "createdBy": "8811501",
            "createdOn": "2023-10-18T15:03:10.728Z",
            "updatedBy": "8811501",
            "updatedOn": "2023-10-18T15:03:57.589Z",
            "version": "1.0.0",
            "sections": [
                {
                    "id": "d7186dcf-2b17-4124-b0d1-d69f0c1bcec7",
                    "title": "Please review AI generated action items for QA improvement",
                    "fields": [
                        {
                            "id": "8e9cf127-e4a3-40f5-bd2e-31a80b1e31a5",
                            "label": "Suggested Action Items",
                            "description": "These are AI generated action items based on recent product defect data. Please review and edit before sending to QA team.",
                            "optional": false,
                            "fieldType": "PARAGRAPH",
                            "dataType": "text",
                            "acceptsInput": true,
                            "acceptsOutput": true,
                            "options": {
                                "values": []
                            },
                            "alias": "Suggested_Action_Items",
                            "isList": false,
                            "useExternalValues": false
                        },
                        {
                            "id": "ca23a591-f080-430e-a9c7-83673fe963ac",
                            "label": "Send to QA Team",
                            "optional": false,
                            "fieldType": "SINGLE_CHOICE",
                            "dataType": "boolean",
                            "acceptsInput": false,
                            "acceptsOutput": true,
                            "options": {
                                "values": []
                            },
                            "value": false,
                            "alias": "Send_to_QA_Team",
                            "isList": false,
                            "useExternalValues": false
                        }
                    ]
                }
            ],
            "releasedOn": "2023-10-18T15:03:57.785Z"
        },
        "contract": {
            "input": [
                {
                    "name": "Suggested_Action_Items",
                    "displayName": "Suggested_Action_Items",
                    "type": "text",
                    "required": true,
                    "list": false,
                    "validValues": null
                }
            ],
            "output": [
                {
                    "name": "Suggested_Action_Items",
                    "displayName": null,
                    "type": "text",
                    "required": true,
                    "list": false,
                    "validValues": null
                },
                {
                    "name": "Send_to_QA_Team",
                    "displayName": null,
                    "type": "boolean",
                    "required": true,
                    "list": false,
                    "validValues": null
                }
            ]
        },
        "inputVariables": {
            "Suggested_Action_Items": "1. Investigate assembly line for misalignment issues near the hinge area\n2. Inspect and replace seals in the actuator's main chamber to prevent hydraulic leaks\n3. Address the issue of missing or loose fasteners with the supplier\n"
        },
        "outputVariables": {}
    },
    {
        "id": "18OCT23_Y9A3HR",
        "attributes": [],
        "queueId": "168ecd84-4a15-45f6-89d9-021fbbce0481",
        "version": 1,
        "createdOn": "2023-10-18T15:23:24.945Z",
        "createdBy": "8811501",
        "updatedOn": "2023-10-18T15:23:24.945Z",
        "updatedBy": "8811501",
        "completedOn": null,
        "completedBy": null,
        "assignedOn": "2023-10-18T15:23:24.945Z",
        "assignedBy": "8811501",
        "assignedTo": "8811501",
        "assigneeType": "USER",
        "lockedOn": null,
        "lockedBy": null,
        "status": "OPEN",
        "tags": [],
        "comments": [],
        "sourceSystem": "ODYSSEY",
        "sourceInfo": {
            "modelId": "6a701240-76bf-4b9a-8145-199156b371cc",
            "modelVersion": "1.2.0",
            "instanceId": "6e75dc76-47fa-4fa6-b157-3dc71e08d32b",
            "deploymentId": "0fa42581-918b-4ba4-b77f-356c55735e52",
            "instanceCreatedBy": "8811501",
            "taskKey": "2251800022518420",
            "workflowInstanceId": "2251800022518320",
            "flowNodeId": "iVpiDJGGzWIPilg",
            "elementInstanceKey": "2251800022518417"
        },
        "displayType": "ENIGMA_FORM",
        "displayId": "cce35d38-95bc-4f87-ba92-849affb13c78",
        "displayEntity": {
            "id": "cce35d38-95bc-4f87-ba92-849affb13c78",
            "name": "Airplane Part Action Items Review Form",
            "description": "",
            "settings": {},
            "createdBy": "8811501",
            "createdOn": "2023-10-18T15:03:10.728Z",
            "updatedBy": "8811501",
            "updatedOn": "2023-10-18T15:03:57.589Z",
            "version": "1.0.0",
            "sections": [
                {
                    "id": "d7186dcf-2b17-4124-b0d1-d69f0c1bcec7",
                    "title": "Please review AI generated action items for QA improvement",
                    "fields": [
                        {
                            "id": "8e9cf127-e4a3-40f5-bd2e-31a80b1e31a5",
                            "label": "Suggested Action Items",
                            "description": "These are AI generated action items based on recent product defect data. Please review and edit before sending to QA team.",
                            "optional": false,
                            "fieldType": "PARAGRAPH",
                            "dataType": "text",
                            "acceptsInput": true,
                            "acceptsOutput": true,
                            "options": {
                                "values": []
                            },
                            "alias": "Suggested_Action_Items",
                            "isList": false,
                            "useExternalValues": false
                        },
                        {
                            "id": "ca23a591-f080-430e-a9c7-83673fe963ac",
                            "label": "Send to QA Team",
                            "optional": false,
                            "fieldType": "SINGLE_CHOICE",
                            "dataType": "boolean",
                            "acceptsInput": false,
                            "acceptsOutput": true,
                            "options": {
                                "values": []
                            },
                            "value": false,
                            "alias": "Send_to_QA_Team",
                            "isList": false,
                            "useExternalValues": false
                        }
                    ]
                }
            ],
            "releasedOn": "2023-10-18T15:03:57.785Z"
        },
        "contract": {
            "input": [
                {
                    "name": "Suggested_Action_Items",
                    "displayName": "Suggested_Action_Items",
                    "type": "text",
                    "required": true,
                    "list": false,
                    "validValues": null
                }
            ],
            "output": [
                {
                    "name": "Suggested_Action_Items",
                    "displayName": null,
                    "type": "text",
                    "required": true,
                    "list": false,
                    "validValues": null
                },
                {
                    "name": "Send_to_QA_Team",
                    "displayName": null,
                    "type": "boolean",
                    "required": true,
                    "list": false,
                    "validValues": null
                }
            ]
        },
        "inputVariables": {
            "Suggested_Action_Items": "1. Investigate assembly line for misalignment issues near the hinge area\n2. Inspect and replace seals in the actuator's main chamber to prevent hydraulic leaks\n3. Address the issue of missing or loose fasteners with the supplier\n"
        },
        "outputVariables": {}
    }
]
```

### Get Task by ID

---

Returns a task by its id.

#### Code Example

```js
const getTaskByID = async (queueId, taskId) => {
  const task = await domo.get(
    `/api/queues/v1/${queueId}/tasks/${taskId}?render=true`
  );
  return task;
};

const task = getTaskByID(
  "168ecd84-4a15-45f6-89d9-021fbbce0481",
  "18OCT23_1JUTZM"
);
```

#### HTTP Request

```text
GET /api/queues/v1/{queueId}/tasks/{taskId}?render={boolean}

```

#### HTTP Response

Returns the task object based requested.

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8

{
    "id": "18OCT23_1JUTZM",
    "attributes": [],
    "queueId": "168ecd84-4a15-45f6-89d9-021fbbce0481",
    "version": 1,
    "createdOn": "2023-10-18T15:23:22.991Z",
    "createdBy": "8811501",
    "updatedOn": "2023-11-28T16:18:29.716Z",
    "updatedBy": "8811501",
    "completedOn": null,
    "completedBy": null,
    "assignedOn": "2023-10-18T15:23:22.991Z",
    "assignedBy": "8811501",
    "assignedTo": "8811501",
    "assigneeType": "USER",
    "lockedOn": null,
    "lockedBy": null,
    "status": "OPEN",
    "tags": [],
    "comments": [],
    "sourceSystem": "ODYSSEY",
    "sourceInfo": {
        "modelId": "6a701240-76bf-4b9a-8145-199156b371cc",
        "modelVersion": "1.2.0",
        "instanceId": "99d0d944-1d90-4622-8a49-2878b37fda10",
        "deploymentId": "0fa42581-918b-4ba4-b77f-356c55735e52",
        "instanceCreatedBy": "8811501",
        "taskKey": "6755399651689301",
        "workflowInstanceId": "6755399651689244",
        "flowNodeId": "iVpiDJGGzWIPilg",
        "elementInstanceKey": "6755399651689298"
    },
    "displayType": "ENIGMA_FORM",
    "displayId": "cce35d38-95bc-4f87-ba92-849affb13c78",
    "displayEntity": {
        "id": "cce35d38-95bc-4f87-ba92-849affb13c78",
        "name": "Airplane Part Action Items Review Form",
        "description": "",
        "settings": {},
        "createdBy": "8811501",
        "createdOn": "2023-10-18T15:03:10.728Z",
        "updatedBy": "8811501",
        "updatedOn": "2023-10-18T15:03:57.589Z",
        "version": "1.0.0",
        "sections": [
            {
                "id": "d7186dcf-2b17-4124-b0d1-d69f0c1bcec7",
                "title": "Please review AI generated action items for QA improvement",
                "fields": [
                    {
                        "id": "8e9cf127-e4a3-40f5-bd2e-31a80b1e31a5",
                        "label": "Suggested Action Items",
                        "description": "These are AI generated action items based on recent product defect data. Please review and edit before sending to QA team.",
                        "optional": false,
                        "fieldType": "PARAGRAPH",
                        "dataType": "text",
                        "acceptsInput": true,
                        "acceptsOutput": true,
                        "options": {
                            "values": []
                        },
                        "alias": "Suggested_Action_Items",
                        "isList": false,
                        "useExternalValues": false
                    },
                    {
                        "id": "ca23a591-f080-430e-a9c7-83673fe963ac",
                        "label": "Send to QA Team",
                        "optional": false,
                        "fieldType": "SINGLE_CHOICE",
                        "dataType": "boolean",
                        "acceptsInput": false,
                        "acceptsOutput": true,
                        "options": {
                            "values": []
                        },
                        "value": false,
                        "alias": "Send_to_QA_Team",
                        "isList": false,
                        "useExternalValues": false
                    }
                ]
            }
        ],
        "releasedOn": "2023-10-18T15:03:57.785Z",
        "userPermissions": []
    },
    "contract": {
        "input": [
            {
                "name": "Suggested_Action_Items",
                "displayName": "Suggested_Action_Items",
                "type": "text",
                "required": true,
                "list": false,
                "validValues": null
            }
        ],
        "output": [
            {
                "name": "Suggested_Action_Items",
                "displayName": null,
                "type": "text",
                "required": true,
                "list": false,
                "validValues": null
            },
            {
                "name": "Send_to_QA_Team",
                "displayName": null,
                "type": "boolean",
                "required": true,
                "list": false,
                "validValues": null
            }
        ]
    },
    "inputVariables": {
        "Suggested_Action_Items": "1. Investigate assembly line for misalignment issues near the hinge area\n2. Inspect and replace seals in the actuator's main chamber to prevent hydraulic leaks\n3. Address the issue of missing or loose fasteners with the supplier\n"
    },
    "outputVariables": {}
}
```

### Save Task Progress

---

Saves current task values given in the body, which contains the key value pairs for each input property of the task in question.

#### Code Example

![Screenshot 2024-01-02 at 8.50.40 AM.png](<../../assets/images/Screenshot 2024-01-02 at 8.50.40 AM.png>)

```js
const body = {
  Suggested_Action_Items:
    "1. Investigate assembly line for misalignment issues near the hinge area\n2. Inspect and replace seals in the actuator's main chamber to prevent hydraulic leaks\n3. Address the issue of missing or loose fasteners with the supplier\n",
  Send_to_QA_Team: true,
};

const saveTask = async (queueId, taskId, body) => {
  const task = await domo.put(
    `/api/queues/v1/${queueId}/tasks/${taskId}/outputs`,
    body
  );
  return task;
};

const task = saveTask(
  "168ecd84-4a15-45f6-89d9-021fbbce0481",
  "18OCT23_1JUTZM",
  body
);
```

#### HTTP Request

```text
PUT /api/queues/v1/{queueId}/tasks/{taskId}/outputs
```

#### Request Body

The request body accepts an object containing key value pairs for each input property of the task in question.

#### HTTP Response

The current saved state of the task.

```json
{
  "id": "18OCT23_1JUTZM",
  "attributes": [],
  "queueId": "168ecd84-4a15-45f6-89d9-021fbbce0481",
  "version": 1,
  "createdOn": "2023-10-18T15:23:22.991Z",
  "createdBy": "8811501",
  "updatedOn": "2024-01-02T13:52:27.182Z",
  "updatedBy": "8811501",
  "completedOn": null,
  "completedBy": null,
  "assignedOn": "2023-10-18T15:23:22.991Z",
  "assignedBy": "8811501",
  "assignedTo": "8811501",
  "assigneeType": "USER",
  "lockedOn": "2024-01-02T13:47:53.613Z",
  "lockedBy": "8811501",
  "status": "OPEN",
  "tags": [],
  "comments": [],
  "sourceSystem": "ODYSSEY",
  "sourceInfo": {
    "modelId": "6a701240-76bf-4b9a-8145-199156b371cc",
    "modelVersion": "1.2.0",
    "instanceId": "99d0d944-1d90-4622-8a49-2878b37fda10",
    "deploymentId": "0fa42581-918b-4ba4-b77f-356c55735e52",
    "instanceCreatedBy": "8811501",
    "taskKey": "6755399651689301",
    "workflowInstanceId": "6755399651689244",
    "flowNodeId": "iVpiDJGGzWIPilg",
    "elementInstanceKey": "6755399651689298"
  },
  "displayType": "ENIGMA_FORM",
  "displayId": "cce35d38-95bc-4f87-ba92-849affb13c78",
  "displayEntity": null,
  "contract": {
    "input": [
      {
        "name": "Suggested_Action_Items",
        "displayName": "Suggested_Action_Items",
        "type": "text",
        "required": true,
        "list": false,
        "validValues": null
      }
    ],
    "output": [
      {
        "name": "Suggested_Action_Items",
        "displayName": null,
        "type": "text",
        "required": true,
        "list": false,
        "validValues": null
      },
      {
        "name": "Send_to_QA_Team",
        "displayName": null,
        "type": "boolean",
        "required": true,
        "list": false,
        "validValues": null
      }
    ]
  },
  "inputVariables": {
    "Suggested_Action_Items": "1. Investigate assembly line for misalignment issues near the hinge area\n2. Inspect and replace seals in the actuator's main chamber to prevent hydraulic leaks\n3. Address the issue of missing or loose fasteners with the supplier\n"
  },
  "outputVariables": {
    "Suggested_Action_Items": "1. Investigate assembly line for misalignment issues near the hinge area\n2. Inspect and replace seals in the actuator's main chamber to prevent hydraulic leaks\n3. Address the issue of missing or loose fasteners with the supplier\n",
    "Send_to_QA_Team": false
  }
}
```

### Complete Task

---

Completes the task with the values given in the body.

#### Code Example

![Screenshot 2024-01-02 at 8.50.40 AM.png](<../../assets/images/Screenshot 2024-01-02 at 8.50.40 AM.png>)

```js
const body = {
  Suggested_Action_Items:
    "1. Investigate assembly line for misalignment issues near the hinge area\n2. Inspect and replace seals in the actuator's main chamber to prevent hydraulic leaks\n3. Address the issue of missing or loose fasteners with the supplier\n",
  Send_to_QA_Team: true,
};

const completeTask = async (queueId, taskId, body) => {
  const task = await domo.post(
    `/api/queues/v1/${queueId}/tasks/${taskId}/complete?version=1`,
    body
  );
  return task;
};

const task = completeTask(
  "168ecd84-4a15-45f6-89d9-021fbbce0481",
  "24OCT23_CI27D1",
  body
);
```

#### HTTP Request

```text
POST /api/queues/v1/{queueId}/tasks/{taskId}/complete?version={VERSION}
```

#### Request Body

The request body accepts an object containing key value pairs for each input property of the task in question.

#### HTTP Response

The completed task.

### Transfer Task

---

Transfer a task to another queue.

#### Code Example

```js
const transferTask = async (currentQueueId, taskId, newQueueId) => {
  const task = await domo.put(
    `/api/queues/v1/${currentQueueId}/tasks/${taskId}/move?targetQueueId=${newQueueId}`
  );
  return task;
};

const task = transferTask(
  "bca21fad-e06b-4905-b43a-ea0929850e47",
  "13AUG24_RZY4WA",
  "23890539-9543-4507-b68b-12e08094ca09"
);
```

#### HTTP Request

```text
PUT /api/queues/v1/{currentQueueId}/tasks/{taskId}/move?targetQueueId={newQueueId}
```

#### HTTP Response

The transfered task.

### Transfer Task to Another User

---

Transfer a task to another User.

#### Code Example

```js
const body = {
  tasksId: [],
  type: "USER",
  userId: "700632941",
};

const transferTaskToUser = async (currentQueueId, taskId, body) => {
  const task = await domo.put(
    `/api/queues/v1/${queueId}/tasks/${taskId}/assign`,
    body
  );
  return task;
};

const task = transferTaskToUser(
  "bca21fad-e06b-4905-b43a-ea0929850e47",
  "13AUG24_RZY4WA",
  body
);
```

#### HTTP Request

```text
PUT /api/queues/v1/${queueId}/tasks/${taskId}/assign
```

#### Request Body

The request body accepts an object containing an array of task ids, type and userId.

#### HTTP Response

The transfered task.

### Void a Task

---

Void a task.

#### Code Example

```js
const voidedTask = async (queueId, taskId) => {
  const task = await domo.post(
    `/api/queues/v1/${queueId}/tasks/${taskId}/void`
  );
  return task;
};

const task = voidedTask(
  "bca21fad-e06b-4905-b43a-ea0929850e47",
  "13AUG24_RZY4WA"
);
```

#### HTTP Request

```text
POST /api/queues/v1/{queueId}/tasks/{taskId}/void
```

#### HTTP Response

The voided task.

### Update permissions

---

Update a queue's user/group permissions.

#### Code Example

```js
const body = [
  {
    id: "337992616",
    permissions: [
      "ADMIN",
      "SHARE",
      "DELETE",
      "WRITE",
      "READ",
      "CREATE_CONTENT",
      "READ_CONTENT",
      "UPDATE_CONTENT",
    ],
    name: "Daniel Bateman",
    type: "USER",
  },
  {
    id: "700632923",
    permissions: ["ADMIN"],
    name: "Daniel's Test User",
    type: "USER",
  },
  {
    id: "519150798",
    permissions: [],
    name: "Jordan Tiller",
    type: "USER",
  },
  {
    id: "264236964",
    name: "Daniel's Test Group",
    type: "GROUP",
    permissions: [
      "DELETE",
      "WRITE",
      "SHARE",
      "EXPORT",
      "EXECUTE",
      "CREATE_CONTENT",
      "READ_CONTENT",
      "UPDATE_CONTENT",
      "DELETE_CONTENT",
    ],
  },
];

const updatePermissions = async (queueId, body) => {
  const queue = await domo.post(`/api/queues/v1/${queueId}/permissions`, body);
  return queue;
};

const task = updatePermissions("bca21fad-e06b-4905-b43a-ea0929850e47", body);
```

#### HTTP Request

```text
POST /api/queues/v1/{queueId}/permissions
```

#### HTTP Body

A array of user or group objects containing the updated permissions

| Property Name | Type   | Required | Description                                                                                                                                                                                                                   |
| ------------- | ------ | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id            | String | Required | The user or group id.                                                                                                                                                                                                         |
| permissions   | String | Required | An array of permissions. The array can be empty (Removes an permissions). Options are `ADMIN`, `SHARE`, `DELETE`, `WRITE`, `READ`, `CREATE_CONTENT`, `READ_CONTENT`, `UPDATE_CONTENT`, `DELETE_CONTENT`, `EXPORT`, `EXECUTE`. |
| name          | String | Required | The display name of the user or group.                                                                                                                                                                                        |
| type          | String | Required | The type of entity. Options are `USER` or `GROUP`                                                                                                                                                                             |

#### HTTP Response

n/a
