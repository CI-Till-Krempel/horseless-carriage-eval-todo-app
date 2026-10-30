# Product Requirements Document (PRD): To-Do List Web App MVP

## 1. Introduction & Product Vision
Build a simple to-do list web application. A single user should be able to:
1. Create a new to-do list with a name.
2. Add a task to a list, with a short text description.
3. Mark a task as complete or incomplete.
4. Delete a task.
5. Delete an entire list (and its tasks).
6. See all their lists and, within a list, all its tasks, with completed tasks visually distinguished from incomplete ones.

## 2. Scope & Constraints
- **Single user, no authentication.** Do not build login/accounts — out of scope.
- **Persistence:** In-memory or simple local file/embedded DB storage within the session/process environment.
- **Web UI:** A clean, functional web UI accessible in a browser.
- **No specific framework mandated:** Choose lightweight, robust tooling (e.g., Python Flask/FastAPI or Node.js with HTML/CSS/JS) deliverable within the 5 sprints.

## 3. Out of Scope
- Multiple users, sharing, permissions.
- Due dates, reminders, priorities, tags, sub-tasks.
- Mobile app, offline support, real-time sync.
- Cloud deployment beyond local execution.
