# To-do App Tutorial

### Intro
---

This tutorial will walk you through building a task management app. You will learn how to create a web app from scratch using Domo's React app template.

You can check out [complete code examples of the To-do App on Github](https://github.com/DomoApps/basic-react-app-todo-tutorial).

#### What we're building

We will go through how to create a basic React app, use Domo's AppDB to implement CRUD functionality, and deploy the application on the Domo platform.

### Step 1: Setup and Installation
---

For this tutorial, we will use yarn as a node package manager, but you can follow the instructions from the <a href="https://create-react-app.dev/docs/getting-started#creating-an-app">create-react-app documentation</a> to install a new react app with the `@domoinc` template based on the package manager of your choice (`npx`, `yarn`, or `npm`). Before starting, make sure you've successfully [installed the Domo Apps CLI](Setup-and-Installation.md) and completed the `domo login` command to authenticate against your instance of Domo.

#### Create Basic React App

```
yarn create react-app todo-app --template @domoinc
```

This command will create your project in a `todo-app` folder with the following included:

- The manifest and thumbnail are provided in the `public` folder.
- The proxy server is setup with `@domoinc/ryuu-proxy` for local development to your Domo instance.
- An upload script has been added to the `package.json` for easy upload.

You can see more details on the dependencies and utility scripts setup in this template by default in the `package.json` file.

```json
{
  "name": "todo-app",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "@domoinc/ryuu-proxy": "^4.0.6",
    "@testing-library/jest-dom": "^5.11.4",
    "@testing-library/react": "^11.0.4",
    "@testing-library/user-event": "^12.1.4",
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "react-scripts": "5.0.1",
    "web-vitals": "^0.2.4"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject",
    "upload": "yarn build && cd build && domo publish && cd .."
  },
  "eslintConfig": {
    "extends": "react-app"
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  }
}

```

### Step 2: Create an AppDB collection to store tasks
---

[AppDB](../../../../Domo-App-APIs/AppDB-API.md) is a nosql database for storing arbitrary JSON documents, we can use it to persist data in our app.

#### Define a collection

The collections reference has to be specified in the `manifest.json` file, by adding the `collections` attribute array, for this tutorial we will add a collection named TasksCollection using the following code.

```json
    "collections": [
        {
            "name": "TasksCollection",
            "schema": {
              "columns": [
                { "name": "title", "type": "STRING" },
                { "name": "description", "type": "STRING" },
                { "name": "dueDate", "type": "STRING" },
                { "name": "status", "type": "STRING" },
                { "name": "priority", "type": "STRING" }
              ]
            }
        }
    ]
```

Your manifest.json will look like the following.

```json
{
    "name": "To-do app",
    "version": "0.0.1",
    "size": {
        "width": 3,
        "height": 3
    },
    "mapping": [],
    "collections": [
        {
            "name": "TasksCollection",
            "schema": {
              "columns": [
                { "name": "title", "type": "STRING" },
                { "name": "description", "type": "STRING" },
                { "name": "dueDate", "type": "STRING" },
                { "name": "status", "type": "STRING" },
                { "name": "priority", "type": "STRING" }
              ]
            }
        }
    ]
}
```

### Step 3: Wire the local instance to Domo
---

Now that we have our `manifest.json` ready, we can publish the initial design of our app, which will allow us to wire our app to resources in our Domo instance like AppDB.

To publish the app, you need to be authenticated in the terminal first; you can run `domo login` if you are not. As mentioned in the first step of this tutorial, an `upload` script was added to the `package.json` for easy upload. We will use that command to build and upload the app.

#### Upload command

```
yarn upload
```

After running the command, you will get an output like the following with the information of the new design.

![yarn_upload_output.png](../../../../../assets/images/yarn_upload_output.png)

#### Create a new card for the app

Let's create the card that we will wire to the AppDB collection. To do this, we need to open the created design in the link that we got from the command output and click the "New Card" option.

![create_card.png](../../../../../assets/images/create_card.png)

We need to map the collection we added to the `manifest.json`. Click "Select Collection".

![select_collection.png](../../../../../assets/images/select_collection.png)

Since we are creating the collection for the app, let's create a new one by clicking on "Create New".

![Screenshot 2024-05-15 at 10.49.19 AM.png](<../../../../../assets/images/Screenshot 2024-05-15 at 10.49.19 AM.png>)

Click "Create Collection" to start with an empty collection.

![Screenshot 2024-05-15 at 10.51.20 AM.png](<../../../../../assets/images/Screenshot 2024-05-15 at 10.51.20 AM.png>)

After creating the collection we can save the card.

![save_collection.png](../../../../../assets/images/save_collection.png)

Once we've saved our card, you should be able to see details about the card on the page for your App Design. You can locate it using the link provided in the console output earlier in this tutorial or by going to "More" > "Asset Library" > Selecting your App Design.

![proxy.png](../../../../../assets/images/proxy.png)

Now, with the card created, you can tell your app which resources to develop against locally. You have to add the following attributes to your `manifest.json` file.

- `id` for linking your app to the published design and
- `proxyId` for wiring your development instance to the card

You can see in the image above where you can locate the App Design `id` property as well as the `proxyId` property.

Your manifest.json will now look similar to this:

```json
{
    "name": "To-do app",
    "version": "0.0.1",
    "size": {
        "width": 3,
        "height": 3
    },
    "mapping": [],
    "collections": [
        {
            "name": "TasksCollection",
            "schema": {
              "columns": [
                { "name": "title", "type": "STRING" },
                { "name": "description", "type": "STRING" },
                { "name": "dueDate", "type": "STRING" },
                { "name": "status", "type": "STRING" },
                { "name": "priority", "type": "STRING" }
              ]
            }
        }
    ],
    "id": "23307940-6dfe-40c4-86f8-8a7b0f5d8b3a",
    "proxyId": "95bd96f9-0385-465a-b485-c16935cf771a"
}
```

### Step 4: Create a tasks collection service
---

With our App connected to the Domo card and the collection created, you are ready to start making requests to appDB, for this we will use the `AppDBClient` that can be found in `@domoinc/toolkit` package, add this package by running the following command. See more on the [Domo Toolkit library here](https://domoapps.github.io/toolkit/).

```
yarn add @domoinc/toolkit
```

Let's create the CRUD service that the app will use to interact with the tasks collection.

You can create a new file `taskService.js` in the `src` directory and place the following code:

```js
import { AppDBClient } from '@domoinc/toolkit';

const TaskTableClient = new AppDBClient.DocumentsClient('TasksCollection');

const fetchTasks = async (
    status,
) => {
    const queryParams = {};

    if (status !== undefined) {
        queryParams['content.status'] = { $eq: status };
    }
    const response = await TaskTableClient.get(queryParams);
    const data = Array.isArray(response.data)
        ? response.data.map((document) => ({
            ...document.content,
            id: document.id,
        }))
        : [{ ...data.content }];;

    return data
};

const createTask = async (task) => {
    const response = await TaskTableClient.create(task);
    return {id: response.data.id, ...response.data.content};
};

const deleteTasks = async (tasksIds) =>
    await TaskTableClient.delete(tasksIds);

const updateTask = async (id, content) => {
    const response = await TaskTableClient.update({ id, content });
    return response.data.content;
};

export const TaskService = {
    fetchTasks,
    createTask,
    deleteTasks,
    updateTask,
};

```

The code above implements simple functions for interacting with our tasks in AppDB. These functions cover CREATE, READ (FETCH), UPDATE, and DELETE capabilities and should be relatively self-explanatory.

### Step 5: Create App UI
---

Now that the app is able to interact with AppDB, let's add some React components to display and manage our tasks.

#### Install sass

For this app we will use sass to speed up styling our app.

```
yarn add sass
```

### App components

One of the best parts of working with the React framework is how it makes [Component Driven Development](https://www.geeksforgeeks.org/what-are-some-advantages-of-component-driven-development/) easier. We'll break down the components we need for this app as follows:

1. TasksContainer
2. TaskListItem
3. TaskForm

For each of our components, we'll create a separate file within `src/components/TasksContainer/`

#### TasksContainer
App content section, this is the wrapper where all the tasks will be listed.

**Code**

For this parent component, we'll place the following Javascript code in `src/components/TasksContainer/index.jsx`.

```js
import React, { useEffect, useState, useRef } from 'react';
import { TaskService } from '../../taskService';
import styles from './index.module.scss';
import { TaskListITem } from './TaskListItem'
import { TaskForm } from './TaskForm';

const TasksEmptyState = () => (
  <div className={styles.List__empty}>
    You have no tasks
  </div>
);
const TaskList = ({ tasks = [], onCheck, onClick }) => (
  tasks.map((task) => (
    <TaskListITem key={task.id} task={task} onCheck={onCheck} onTaskClick={onClick} />
  ))
);

const Content = () => {
  const [tasks, setTasks] = useState([])
  const [selectedTasks, setSelectedTasks] = useState([])
  const [editingTask, setEditingTask] = useState({})
  const [loading, setLoading] = useState(false)
  const dialogRef = useRef(null);

  useEffect(() => {
    setLoading(true)
    TaskService.fetchTasks('active').then(response => {
      setTasks(response)
      setLoading(false)
    })
  }, [])

  const handleSave = async (task) => {
    try {
      let request;
      const newTasks = [...tasks]
      if (task.id !== undefined) {
        const updatedTask = newTasks.find(newTask => newTask.id === task.id);
        Object.assign(updatedTask, task);
        const { id, isSelected, ...content } = task;
        request = TaskService.updateTask(id, content)
      } else {
        request = TaskService.createTask(task)
        newTasks.push(task);
      }
      const savedTask = await request;
      setTasks(newTasks);
      return savedTask;
    } catch (error) {
      return null
    }
  }

  const completeTasks = async () => {
    try {
      const newTasks = [...tasks]
      const requests = tasks.filter(task => selectedTasks.includes(task.id)).map(task => {
        const newTask = { ...task, status: 'completed' }
        const completedTask = newTasks.find(newTask => newTask.id === task.id);
        Object.assign(completedTask, newTask);
        const { id, isSelected, ...content } = newTask;
        return TaskService.updateTask(id, content)
      })
      await Promise.all[requests];
      setTasks(newTasks);
    } catch (error) {
      return null
    }
  }

  const deleteTasks = async () => {
    try {
      const newTasks = tasks.filter(task => !selectedTasks.includes(task.id))
      TaskService.deleteTasks(selectedTasks)
      setTasks(newTasks);
    } catch (error) {
      return null
    }
  }

  const onTaskCheck = (taskId) => {
    const isSelected = selectedTasks.includes(taskId);
    if (isSelected) {
      const newSelected = selectedTasks.filter(task => task !== taskId);
      setSelectedTasks(newSelected);
    } else {
      setSelectedTasks([...selectedTasks, taskId])
    }
    const newTasks = tasks.map(task => task.id === taskId ? { ...task, isSelected: !isSelected } : task)
    setTasks(newTasks);
  };

  const onTaskClick = (task) => {
    setEditingTask(task);
    dialogRef.current.showModal()
  }

  const onClose = () => {
    dialogRef.current.close()
    setEditingTask({})
  }

  if (loading ?? false)
    return <div>Loading...</div>;

  return (
    <>
      <div className={styles.List__container}>
        {tasks.length === 0 ? <TasksEmptyState /> : <TaskList tasks={tasks} onCheck={onTaskCheck} onClick={onTaskClick} />}
      </div>
      <button className={styles.List__addButton} onClick={() => dialogRef.current.showModal()}> Add Task</button>
      {selectedTasks.length > 0 && <>
        <button className={styles.List__addButton} onClick={completeTasks}> Complete Tasks</button>
        <button className={styles.List__addButton} onClick={deleteTasks}> Delete Tasks</button>
      </>}
      <dialog ref={dialogRef}><TaskForm onClose={onClose} onSave={handleSave} task={editingTask} /> </dialog>
    </>
  );
};

export const TasksContainer = () => <div className={styles.List__container}>
  <Content />
</div>

```

We'll also add the following CSS to a new file: `src/components/TasksContainer/index.module.scss`.

```css
.List__container {
  margin: 3% auto;
}

.List__empty{
  margin: 2% auto;
}

.List__add {
  float: right;
  margin-right: 16px;
  background-color: #99CCEE;
}

.List__addButton{
  min-width: 100px;
  margin: 4px;
  padding: 8px;
  font-weight: 500;
}

.List__loading {
  margin-top: 24px;
}
```

#### TaskListItem

Next, we'll add the Javascript and CSS for our `TaskListItem` component which is used to represent each of the tasks in our Todo App.

Add the following Javascript in a new directory inside of the `TasksContainer` with the following path: `/src/components/TasksContainer/TaskListItem/index.jsx`.

**Code**

```js
import React from "react";
import styles from "./index.module.scss";

const COLOR_MAP = {
  High: "#fbad56",
  Urgent: "#fd9a93",
  Low: "#fdecad",
};

export const TaskListITem = ({ task, onCheck, onTaskClick }) => 
    <div>
      <div className={styles.Main__wrapper}>
        <div className={styles.Row_content_wrapper}>
          <input
            type="checkbox"
            disabled={task.status === "completed" }
            className={styles.Row__checkbox}
            checked={task.isSelected}
            onChange={(event) => onCheck(task.id)}
          />
          <div className={styles.Row__content}>
            {task.status === "completed" ? (
              <div className={styles.Row__completedTask__subtitle}>
                {task.title}
              </div>
            ) : (
              <div className={styles.Row__tasktitle} onClick={() => onTaskClick(task)}>{task.title}</div>
            )}
            <div className={styles.Row__subtitle}>{task?.description}</div>
          </div>
          <div label={task.priority} className={styles.Row__priority} style={{ background: COLOR_MAP[task.priority] }} />
        </div>
      </div>
    </div>

```

The CSS specific to this component can then go in: `src/components/TasksContainer/TaskListItem/index.module.scss`.

```css
.Main__wrapper {
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    padding: 8px 0px;
}

.Row_content_wrapper {
    display: flex;
    flex-direction: row;
}

.Row__checkbox{
    margin-right: 8px;
}

.Row__content{
    display: flex;
    width: 300px;
    flex-direction: column;
    justify-content: center;
    align-content: flex-start;
}

.Row__subtitle {
    color: gray;
}

.Row__completedTask__subtitle{
    text-decoration: line-through;
}

.Row__tasktitle{
    cursor: pointer;
    margin: 4px 0px;
    &:hover{
        text-decoration: underline;
    }
}

.Row__priority{
    width: 20px;
    height: 20px;
}

```

#### TaskForm

Finally, let's add the form that we can use to create new tasks.

**Code**

We'll add the following Javascript to a new directory in `TaskContainer` with the following path: `src/components/TasksContainer/TaskForm/index.jsx`;

```js
import React, { useState, useEffect } from 'react';
import styles from './index.module.scss';

export const TaskForm = ({ onSave, onClose, task = {} }) => {
  const [stagedTask, setStagedTask] = useState(task);
  const [alert, setAlert] = useState('');

  useEffect(() => {
    setStagedTask(task)
  }, [task])

  const handleStagedTaskUpdate = (key, value) => {
    const newStagedData = { ...stagedTask, [key]: value };
    setStagedTask(newStagedData);
  };

  const handleSave = async () => {
    const task = {
      id: stagedTask.id,
      title: stagedTask.title,
      description: stagedTask.description,
      priority: stagedTask.priority || 'Low',
      dueDate: stagedTask?.dueDate,
      status: 'active',
    };
    const response = await onSave(task)
    if (response?.id !== undefined) setStagedTask({});
    setAlert(`Task ${task.id !== undefined ? 'updated' : 'created'} Successfully!`);
    setTimeout(() => {
      onClose();
      setAlert('');
    }, 1000);
  };

  return (
    <div className={styles.TaskForm}>
      <div className={styles.TaskForm__titleBox}>
        {task.id !== undefined ? 'Update Task' : 'Add your new To-Do'}
      </div>
      <div className={styles.TaskForm__formBox}>
        <div className={styles.TaskForm__formBoxContent}>
          <input
            id="title-input"
            className={styles.TaskForm__formInput}
            placeholder="Task Title"
            onChange={(event) =>
              handleStagedTaskUpdate('title', event.target.value)
            }
            value={stagedTask?.title || ''}
          />
          <textarea
            multiline
            maxRows={3}
            id="description-input"
            className={styles.TaskForm__formNotes}
            placeholder="Notes"
            value={stagedTask?.description || ''}
            onChange={(event) =>
              handleStagedTaskUpdate('description', event.target.value)
            }
          />
          <div
            className={styles.TaskForm__formSubTitle}
          >
            Completion Due Date
          </div>
          <div>
            <input
              className={styles.TaskForm__formInput}
              type="date"
              value={stagedTask?.dueDate}
              onChange={(event) =>
                handleStagedTaskUpdate('dueDate', new Date(event.target.value).toISOString().split('T')[0])
              }
            />
          </div>
          <div className={styles.TaskForm__formSubTitle}>Set Priority</div>
          <select className={styles.TaskForm__formInput} value={stagedTask.priority} onChange={(event) =>
            handleStagedTaskUpdate('priority', event.target.value)
          }>
            <option value="Low">Low</option>
            <option value="High">High</option>
            <option value="Urgent">Urgent</option>
          </select>
          <div className={styles.TaskForm__ButtonsWrapper}>
            <button
              className={styles.TaskForm__createButton}
              disabled={!stagedTask.title}
              onClick={handleSave}
            >
              SAVE
            </button>
            <button
              onClick={onClose}
            >
              CANCEL
            </button>
          </div>
        </div>
        {alert !== '' && (
          <div className={styles.TaskForm__alert}>
            {alert}
          </div>
        )}
      </div>
    </div>
  );
};

```

Then, we can add the CSS for our form at `src/components/TasksContainer/TaskForm/index.module.scss`;

```css

.TaskForm {
  border-radius: 12px;
  background-color: #FAFAFA;  
  width: 500px;
  height: 575px;
  & input, select, textarea {
    width: 85%;
    border: 1px solid #999999;
  }
}

.TaskForm__ButtonsWrapper{
  margin-top: 30px;
  display: flex;
  gap: 2%;
   & > button {
     width: 48%;
   }
}

.TaskForm__titleBox {
  padding: 24px 12px;
}

.TaskForm__formBox {
  display: flex;
  flex-direction: column;
}

.TaskForm__formBoxContent {
  padding: 19px 16px !important;
}

.TaskForm__formInput {
  padding: 16px 22px 17px 22px;
  background-color: white;
  border-color: white;
  border-radius: 8px;
  color: black !important;
  margin-bottom: 12px !important;

  & > input {
    padding: 0;
  }
  fieldset {
    border: none !important;
  }
}

.TaskForm__formNotes {
  min-height: 98px;
  background-color: white;
  border-color: white;
  border-radius: 8px;
  color: black !important;
  margin-bottom: 12px !important;
  &::placeholder{
    padding: 12px !important;
  }
}

.TaskForm__formSubTitle {
  padding-top: 12px;
  color: rgba(0, 0, 0, 0.5);;
}

.TaskForm__createButton {
  padding: 8px;
  background-color: #FC9927 !important;
  color: white !important;
  font-weight: 700 !important;
  font-size: 12px !important;
}

.TaskForm__createButton:disabled {
  border: 1px solid #999999;
  background-color: #cccccc !important;
  color: #666666;
}

.TaskForm__alert {
  margin: auto;
}
```

With the custom components created, we just need to call the TasksContainer in the app index.js located at `src/index.js`.

```js
import React from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import { TasksContainer } from "./components/TasksContainer";
import reportWebVitals from "./reportWebVitals";

const container = document.getElementById("root");
const root = createRoot(container);
root.render(
  <React.StrictMode>
    <h1>Tasks Manager</h1>
    <TasksContainer />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
```

Your final file directory structure should look like this. You

```
├── README.md
├── build
│   ├── asset-manifest.json
│   ├── favicon.ico
│   ├── index.html
│   ├── logo192.png
│   ├── logo512.png
│   ├── manifest.json
│   ├── robots.txt
│   ├── static
│   │   ├── css
│   │   │   ├── main.71624b60.css
│   │   │   └── main.71624b60.css.map
│   │   └── js
│   │       ├── 422.c8d9e89e.chunk.js
│   │       ├── 422.c8d9e89e.chunk.js.map
│   │       ├── main.f9359c52.js
│   │       ├── main.f9359c52.js.LICENSE.txt
│   │       └── main.f9359c52.js.map
│   └── thumbnail.png
├── package.json
├── public
│   ├── favicon.ico
│   ├── index.html
│   ├── logo192.png
│   ├── logo512.png
│   ├── manifest.json
│   ├── robots.txt
│   └── thumbnail.png
├── src
│   ├── App.css
│   ├── App.js
│   ├── App.test.js
│   ├── components
│   │   └── TasksContainer
│   │       ├── TaskForm
│   │       │   ├── index.jsx
│   │       │   └── index.module.scss
│   │       ├── TaskListItem
│   │       │   ├── index.jsx
│   │       │   └── index.module.scss
│   │       ├── index.jsx
│   │       └── index.module.scss
│   ├── index.css
│   ├── index.js
│   ├── logo.svg
│   ├── reportWebVitals.js
│   ├── setupProxy.js
│   ├── setupTests.js
│   └── taskService.js
├── yarn-error.log
└── yarn.lock
```

### Step 6: Test your App Locally

---

Before you publish your App to your Domo instance you can test that it is functioning as expected using the built in local server. Just run the `yarn start` script command.

Your app should look like the screenshot below and you should be able to create, edit, deleete, and mark tasks as completed.

![Screenshot 2024-07-18 at 3.40.01 PM.png](<../../../../../assets/images/Screenshot 2024-07-18 at 3.40.01 PM.png>)

![Screenshot 2024-07-18 at 3.40.52 PM.png](<../../../../../assets/images/Screenshot 2024-07-18 at 3.40.52 PM.png>)

### Step 7: Publish App to Domo instance

---

To publish your finished app, you can use the upload script we used to publish the initial design.

`yarn upload`

You should now be able to create new instances of your App, which has been successfully deployed into your Domo instance.

![Screenshot 2024-07-18 at 3.42.47 PM.png](<../../../../../assets/images/Screenshot 2024-07-18 at 3.42.47 PM.png>)
