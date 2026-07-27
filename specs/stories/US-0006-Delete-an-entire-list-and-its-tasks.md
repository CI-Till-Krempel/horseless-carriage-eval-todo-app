# User Story

- Story ID: US-0006
- Title: Delete an entire list and its tasks
- Status: Accepted
- Priority: P1
- Owner: Scrum Team
- Last Updated: 2026-07-27

## As a single user, I want to delete an entire list and its tasks so that I can clean up completed or unneeded projects.

## Acceptance Criteria
- Given a to-do list with zero or more tasks exists, When the user clicks delete on the entire list, Then the list and all its contained tasks are deleted.

## Notes
Users can delete lists and all associated tasks in one action.

## Test Approach
Pytest checks list deletion.

### Tasks
- Verify list deletion implementation
