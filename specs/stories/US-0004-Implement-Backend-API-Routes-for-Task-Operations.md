# User Story

- Story ID: US-0004
- Title: Implement Backend API Routes for Task Operations
- Status: Ready
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-11-24

## As a frontend, I need API routes to create, read, update, and delete tasks, so that the UI can manage tasks.

## Acceptance Criteria
- POST /lists/:id/tasks creates a new task with text
- GET /lists/:id/tasks returns all tasks in a list
- PATCH /lists/:id/tasks/:taskId updates task completion status
- DELETE /lists/:id/tasks/:taskId deletes a task
- Errors are handled gracefully

## Notes
Frontend can interact with tasks via API

## Test Approach

