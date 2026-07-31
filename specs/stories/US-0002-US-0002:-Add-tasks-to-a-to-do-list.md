# User Story

- Story ID: US-0002
- Title: US-0002: Add tasks to a to-do list
- Status: Draft
- Priority: P0
- Owner: Scrum Team
- Last Updated: 2026-07-31

## As a user, I want to add a task with a short text description to a to-do list so that I can track what needs to be done.

## Acceptance Criteria
- Given an existing to-do list, When the user adds a task with a text description, Then the task appears within that list.
- Given a task inside a list, When the user views the list, Then the task description is shown.

## Notes
Users can record actionable tasks within their lists.

## Test Approach
Pytest unit tests for task creation.

### Tasks
- Add task form in list view UI
- Implement backend route for adding task to list
- Add tests for task addition
