# User Story

- Story ID: US-0002
- Title: Add a Task to a List
- Status: Accepted
- Priority: P0
- Owner: Scrum Team
- Last Updated: 2026-08-07

## As a user, I want to add a task to a list with a short text description so that I can track what needs to be done.

## Acceptance Criteria
- Given an existing list, When the user adds a task description and submits, Then the task appears within that list.

## Notes
Users can successfully add tasks to specific lists.

## Test Approach
pytest coverage for task addition.

### Tasks
- Add Task model relation to List
- Implement add task route
- Update UI to render tasks under lists
- Write unit tests
