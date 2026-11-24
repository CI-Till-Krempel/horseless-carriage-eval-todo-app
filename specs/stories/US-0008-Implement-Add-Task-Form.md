# User Story

- Story ID: US-0008
- Title: Implement Add Task Form
- Status: Ready
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-11-24

## As a user, I want to add a new task to a list by typing a description, so that I can track what needs to be done.

## Acceptance Criteria
- Form accepts task text
- Form submits to backend via API
- New task appears in the task list after creation
- Task is marked as incomplete by default
- User gets feedback (success/error) after submission
- Form is accessible from the list detail view

## Notes
User can create tasks through the UI

## Test Approach
Manual testing - add tasks via form, verify they appear in list

### Tasks
- Create HTML form for task text input
- Implement form submission handler
- POST to /api/lists/:id/tasks with task text
- Handle success/error responses
- Add form validation (non-empty, length check)
- Close form and refresh tasks view after success
- Show error messages to user
