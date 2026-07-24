# Product Requirements Document: To-Do List Web App (MVP)

## 1. Product Vision & Goals
Build a simple to-do list web application. A single user should be able to:
1. Create a new to-do list with a name.
2. Add a task to a list, with a short text description.
3. Mark a task as complete or incomplete.
4. Delete a task.
5. Delete an entire list (and its tasks).
6. See all their lists and, within a list, all its tasks, with completed tasks visually distinguished from incomplete ones.

## 2. Scope & Constraints
- **Single user, no authentication.** Do not build login/accounts — out of scope.
- **Persistence:** Local persistence / session storage or simple file/DB storage (to be decided by Architecture / Dev Team).
- **Working Web UI:** Deliverable is something a person can open in a browser and actually use.
- **Out of Scope:** Multiple users, sharing, permissions, due dates, reminders, priorities, tags, sub-tasks, mobile app, offline support, real-time sync, deployment beyond running locally.

## 3. Release Plan (5 Sprints)
- **Sprint 1:** Core infrastructure, project setup, and List Creation & Viewing (Stories 1 & 6 part 1).
