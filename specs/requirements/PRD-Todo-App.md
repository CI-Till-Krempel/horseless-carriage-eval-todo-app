# Product Requirements Document: To-Do List Web App

## 1. Vision & Goals
Build a simple to-do list web application. A single user should be able to:
1. Create a new to-do list with a name.
2. Add a task to a list, with a short text description.
3. Mark a task as complete or incomplete.
4. Delete a task.
5. Delete an entire list (and its tasks).
6. See all their lists and, within a list, all its tasks, with completed tasks visually distinguished from incomplete ones.

## 2. Constraints
- Single user, no authentication.
- Persistence approach: SQLite or file-based JSON persistence to ensure state is maintained.
- A working web UI is required (Flask/FastAPI with HTML/CSS or simple frontend).
- No specific language/framework mandated; Python (Flask/FastAPI) is recommended for simplicity and delivery speed within budget.

## 3. Scope & Release Planning (v1.0.0)
- MVP / Sprint 1: Project setup, UI skeleton, and core CRUD for Lists and Tasks.
