# Product Requirements Document: To-Do List Web App

## Product Vision
Build a simple to-do list web application. A single user should be able to:
1. Create a new to-do list with a name.
2. Add a task to a list, with a short text description.
3. Mark a task as complete or incomplete.
4. Delete a task.
5. Delete an entire list (and its tasks).
6. See all their lists and, within a list, all its tasks, with completed tasks visually distinguished from incomplete ones.

## Scope & Constraints
- Single user, no authentication.
- Persistence: SQLite / file-based persistence for session/process durability across restarts.
- Working web UI (Python / Flask or FastAPI + HTML/CSS/JS or simple templating).
- No specific language/framework mandated; Python chosen for robust ecosystem and fast delivery.
