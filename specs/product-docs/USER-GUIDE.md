# To-Do List Web App - User Guide

Welcome to the To-Do List Web App! This guide will help you get started quickly and make the most of all features.

## Getting Started

### Prerequisites
- Python 3.8+ installed on your system.
- `pip` package manager.

### Installation & Running Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/CI-Till-Krempel/horseless-carriage-eval-todo-app.git
   cd horseless-carriage-eval-todo-app
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Open your web browser and navigate to:
   `http://localhost:5000`

---

## Core Features & Usage

### 1. Creating a To-Do List
- Type a name for your list in the "New List Name..." input field at the top of the page.
- Click **Create List**. Your new list will appear instantly.

### 2. Adding Tasks
- Inside any list card, type your task description in the "New task description..." input box.
- Click **Add Task**. The task will be added to that specific list.

### 3. Toggling Task Completion
- Click the checkbox next to any task to mark it as complete or incomplete.
- Completed tasks are automatically displayed with a strikethrough and muted text style so you can visually distinguish them from pending tasks.

### 4. Editing Tasks
- Click the **Edit** button next to a task to open the inline editing form.
- Update the task text and click **Save** to update the task description.

### 5. Filtering Tasks
- Use the filter bar at the top of the page (**All**, **Active**, **Completed**) to view only the tasks matching your current focus.

### 6. Deleting Tasks
- Click the **Delete** button next to any task to remove it permanently from the list.

### 7. Deleting Entire Lists
- Click the **Delete List** button in the header of any list card to remove the list and all its associated tasks.

---

## Data Persistence
- All lists and tasks are automatically stored in a local SQLite database (`todo.db`). Your data persists safely across application restarts.
