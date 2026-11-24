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
pytest with Flask test client for all HTTP routes

### Tasks
- Implement POST /api/lists/:id/tasks endpoint
- Implement GET /api/lists/:id/tasks endpoint
- Implement PATCH /api/lists/:id/tasks/:taskId endpoint for toggling completion
- Implement DELETE /api/lists/:id/tasks/:taskId endpoint
- Add validation for all endpoints
- Add error handling (list not found, task not found, etc.)
- Write tests for all routes
