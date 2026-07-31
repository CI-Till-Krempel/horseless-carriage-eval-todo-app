# Product Requirements Document (PRD): To-Do List Web App

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
- **No persistence requirement beyond the current session/process is assumed** unless the team's own design calls for it — persistence approach (in-memory, file, or simple embedded DB) is a legitimate design decision.
- **A working web UI is required** — something a person can open in a browser and actually use.
- **No specific language/framework is mandated.** Choose something deliverable within budget and time.
- **Explicitly out of scope:** Multiple users, sharing, permissions, due dates, reminders, priorities, tags, sub-tasks, mobile app, offline support, real-time sync, deployment beyond local running.
