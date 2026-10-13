# User Story

- Story ID: US-0005
- Title: Delete List API
- Status: Ready
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-10-13

## As a user, I want to delete an entire list and its tasks so that I can clean up obsolete projects.

## Acceptance Criteria
- Given an existing list with tasks, When the user deletes the list, Then both the list and its associated tasks are removed.

## Notes
Lists and their tasks can be deleted entirely.

## Test Approach
Add pytest test for deleting a list and verifying tasks are removed.

### Tasks
- Implement POST /lists/<list_id>/delete route
