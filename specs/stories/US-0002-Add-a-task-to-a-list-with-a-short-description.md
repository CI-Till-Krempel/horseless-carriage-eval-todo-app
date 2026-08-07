# User Story

- Story ID: US-0002
- Title: Add a task to a list with a short description
- Status: Ready
- Priority: P0
- Owner: Scrum Team
- Last Updated: 2026-08-07

## As a user, I want to add a task with a short text description to a to-do list so that I can track what needs to be done.

## Acceptance Criteria
- Given an existing to-do list, When the user adds a task with a short text description, Then the task appears within that list.

## Notes
Users can add descriptive tasks to their lists.

## Test Approach
Run pytest to verify task addition correctly associates tasks to lists.

### Tasks
- Confirm task addition endpoint and UI form
- Add dedicated test coverage for task addition
