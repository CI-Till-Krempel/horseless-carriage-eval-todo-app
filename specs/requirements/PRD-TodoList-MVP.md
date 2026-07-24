# PRD: To-Do List Web App (MVP)

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
- Persistence approach: Local file storage / SQLite or in-memory (to be decided via architecture).
- A working web UI is required.
- Explicitly out of scope: Multiple users, sharing, permissions, due dates, reminders, priorities, tags, sub-tasks, mobile app, offline support, real-time sync, hosting beyond local execution.
