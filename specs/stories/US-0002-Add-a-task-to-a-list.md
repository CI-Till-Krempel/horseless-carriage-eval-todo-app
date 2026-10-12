# User Story

- Story ID: US-0002
- Title: Add a task to a list
- Status: Ready
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-10-12

## As a user, I want to add a task to a list with a short text description so that I can track what needs to be done.

## Acceptance Criteria
- Given an existing to-do list, When the user adds a task with a text description, Then the task appears within that list.

## Notes
Users can successfully record tasks under specific lists.

## Test Approach
Pytest tests verifying task addition to lists.

### Tasks
- Add task creation endpoint in Flask
- Update UI to display and add tasks under lists
- Add automated tests for task creation
