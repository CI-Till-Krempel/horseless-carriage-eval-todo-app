# Product Requirements Document: To-Do List Web App

## Product Vision
Build a simple to-do list web application. A single user should be able to:
1. Create a new to-do list with a name.
2. Add a task to a list, with a short text description.
3. Mark a task as complete or incomplete.
4. Delete a task.
5. Delete an entire list (and its tasks).
6. See all their lists and, within a list, all its tasks, with completed tasks visually distinguished from incomplete ones.

## Constraints
- Single user, no authentication.
- Persistence approach: Local file or SQLite for simplicity across sessions.
- A working web UI is required.
- No specific language/framework mandated (Python/Flask or FastAPI + HTML/JS recommended for rapid delivery).

## Out of Scope
- Multiple users, sharing, or permissions.
- Due dates, reminders, priorities, tags, or sub-tasks.
- Mobile app, offline support, or real-time sync.
- Deployment/hosting beyond running locally.
