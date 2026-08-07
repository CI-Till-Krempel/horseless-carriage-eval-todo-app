# Product Requirements Document: To-Do List Web App (MVP)

## 1. Product Vision & Goals
Build a simple to-do list web application as specified in the evaluation scenario. The product allows a single user (no auth, single session/local persistence) to manage to-do lists and tasks with a working web UI.

### Goals (Sprint 1 - MVP & Foundation)
- Establish the application foundation, framework choice, and architecture.
- Support creating a new to-do list with a name.
- Support adding a task to a list with a short text description.
- Support marking a task as complete or incomplete.
- Support viewing all lists and tasks within a list with visual distinction for completed tasks.

## 2. Scope & Boundaries (Sprint 1)
### In Scope (MVP)
- Project structure & tech stack setup (Python/Flask or Node/Express or similar lightweight stack).
- In-memory or simple file/DB persistence for lists and tasks.
- Web UI (HTML/CSS/JS or templates) meeting core visibility and interaction needs.
- Core stories: Create list, Add task, View lists/tasks, Toggle task completion.

### Out of Scope (Later Sprints or Explicitly Excluded)
- Delete task (Sprint 2)
- Delete list (Sprint 2)
- Authentication / Multiple users (Excluded entirely)
- Due dates, priorities, tags, sub-tasks (Excluded entirely)

## 3. User Stories (Sprint 1 Backlog)
1. **US-0001**: As a user, I want to create a new to-do list with a name so that I can organize my tasks.
2. **US-0002**: As a user, I want to add a task with a short text description to a to-do list so that I can track what needs to be done.
3. **US-0003**: As a user, I want to see all my lists and all tasks within a list with completed tasks visually distinguished so that I can review my progress.
4. **US-0004**: As a user, I want to mark a task as complete or incomplete so that I can update its status.
