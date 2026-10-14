# Product Requirements Document: To-Do List Web App

## Goals & Vision
Build a simple, intuitive to-do list web application adhering strictly to the Fixed Evaluation Scenario vision:
1. Create a new to-do list with a name.
2. Add a task to a list, with a short text description.
3. Mark a task as complete or incomplete.
4. Delete a task.
5. Delete an entire list (and its tasks).
6. See all lists and tasks with completed tasks visually distinguished.

## Scope & Constraints
- Single user, no authentication.
- No persistence beyond session/process unless decided by team (using SQLite / file storage recommended for simplicity and usability).
- Working web UI required.
- No specific language/framework mandated (Python/Flask or FastAPI + HTML/JS is a lightweight, reliable choice).
