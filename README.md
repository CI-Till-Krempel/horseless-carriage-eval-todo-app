# To-Do List Web App

A clean, modern, and persistent web application for managing to-do lists and tasks, built with Python (Flask) and HTML/CSS.

## Features

1. **Create Lists**: Organize tasks by creating named to-do lists.
2. **Task Management**: Add short text descriptions to tasks.
3. **Completion Tracking**: Mark tasks complete or incomplete with visual strike-through differentiation.
4. **Task Filtering**: Filter view by **All**, **Active**, or **Completed** tasks instantly.
5. **Data Persistence**: All lists and tasks automatically persist across server restarts via JSON storage (`todos.json`).
6. **Deletion**: Delete individual tasks or entire lists with confirmation prompts.
7. **Task Counters**: Real-time active and total task count badges per list.

## Local Setup & Running

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**:
   ```bash
   python app.py
   ```

3. **Open in Browser**:
   Navigate to `http://127.0.0.1:5000`.

## Running Tests

```bash
pytest
```
