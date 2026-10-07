# Product Requirements Document: To-Do List Web App (MVP)

## Vision
Build a simple to-do list web application enabling a single user to manage to-do lists and their tasks through a clean web interface.

## Goals
1. Create a new to-do list with a name.
2. Add a task to a list, with a short text description.
3. Mark a task as complete or incomplete.
4. Delete a task.
5. Delete an entire list (and its tasks).
6. See all lists and tasks with visual distinction for completed tasks.

## Scope & Constraints
- Single user, no authentication.
- Simple local persistence (e.g. SQLite or JSON file storage) to satisfy session and restart expectations.
- Working web UI (Python/Flask or FastAPI with a simple frontend template).
