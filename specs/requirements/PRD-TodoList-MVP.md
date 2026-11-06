# Product Requirements Document: To-Do List Web App

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
- **Persistence:** In-memory, file, or a simple embedded DB chosen and justified by the team.
- **Web UI:** A working web UI that can be opened and used directly in a browser.
- **Technology Stack:** Chosen by the team for delivery within budget.

## 3. Out of Scope
- Multiple users, sharing, or permissions.
- Due dates, reminders, priorities, tags, or sub-tasks.
- Mobile app, offline support, or real-time sync.
- Any deployment/hosting beyond running locally.
