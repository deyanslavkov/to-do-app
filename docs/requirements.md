## Project Goal

The goal of this project is to develop a lightweight and simple web-based to-do application that helps users effectively manage and complete small, spontaneous tasks.
Unlike complex task management tools aimed at planning large projects, this app is focused on immediate action. It provides a minimal and distraction-free interface where users can quickly write down detailed tasks and complete them as soon as time allows. The purpose is to encourage productivity by offering a quick glance at actionable items—users can simply open the app, choose a task, and get to work.
The application supports task creation with titles, descriptions, tags, deadlines, and repetition options. It also allows filtering and searching by multiple criteria and automatically archives completed tasks to keep the workspace clear.

---

## User Stories

1. As a user, I want to create a new task with a title and description, so that I can remember what needs to be done.
2. As a user, I want to tag my tasks, so that I can group them by category or type.
3. As a user, I want to assign a deadline to a task, so that I know when it should be completed.
4. As a user, I want to search tasks by title, description, tags, or completion status, so that I can quickly find specific tasks.
5. As a user, I want to mark a task as completed, so that I know I don't need to do it anymore.
6. As a user, I want completed tasks to move into an archive, so that they don’t clutter my active list.
7. As a user, I want to set a task to repeat on a schedule, so that I’m reminded to do regular routines.
8. As a user, I want to edit or delete a task, so that I can correct mistakes or remove outdated entries.
9. As a user, I want to see a simple list of all tasks sorted by deadline, so that I can decide what’s most urgent.
10. As a user, I want to open the app and immediately see useful tasks I could do, so that I can be productive even with little time.

---

## Use Cases

### Use Case 1: **Create a Task**

* **Name:** Create a Task
* **Actor:** User
* **Goal:** To add a new task to the task list
* **Main Flow:**

  1. The user opens the app.
  2. The user clicks the "New Task" button.
  3. A form appears for task title, description, tags, deadline, and repeat option.
  4. The user fills in the fields and clicks "Save".
  5. The task is added to the main task list.
* **Alternative Flow:**

  * If no title is entered, the app shows an error and prevents saving.

### Use Case 2: **Complete a Task**

* **Name:** Complete a Task
* **Actor:** User
* **Goal:** To mark a task as completed
* **Main Flow:**

  1. The user views their task list.
  2. The user clicks the "Mark as Completed" button next to a task.
  3. The task is moved to the archive.
  4. The active list is updated without the completed task.

### Use Case 3: **Search for Tasks**

* **Name:** Search for Tasks
* **Actor:** User
* **Goal:** To find specific tasks by keywords or attributes
* **Main Flow:**

  1. The user enters a search query in the search bar.
  2. The app filters tasks by title, description, tags, or completion status.
  3. The matching results are displayed.
* **Alternative Flow:**

  * If no results are found, the app shows a "No tasks found" message.

### Use Case 4: **Edit a Task**

* **Name:** Edit a Task
* **Actor:** User
* **Goal:** To modify the contents of an existing task
* **Main Flow:**

  1. The user clicks the "Edit" icon on a task.
  2. A form appears with current task information.
  3. The user makes changes and clicks "Update".
  4. The task is updated in the list.

### Use Case 5: **View Suggested Tasks**

* **Name:** View Suggested Tasks
* **Actor:** User
* **Goal:** To see a list of quick and relevant tasks that can be done immediately
* **Main Flow:**

  1. The user opens the app.
  2. The app displays tasks sorted by deadline and importance.
  3. The user reviews the list and selects a task to begin.
