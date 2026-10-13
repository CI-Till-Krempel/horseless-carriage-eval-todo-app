# User Story

- Story ID: US-0002
- Title: Add Task to List API
- Status: Ready
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-10-13

## As a user, I want to add a task to a list with a short text description so that I can track what needs to be done.

## Acceptance Criteria
- Given an existing list ID, When the user adds a task with a description, Then the task is saved and associated with that list.

## Notes
Tasks can be successfully added to lists.

## Test Approach
Add pytest test for adding a task to a list.

### Tasks
- Implement POST /lists/<list_id>/tasks route
