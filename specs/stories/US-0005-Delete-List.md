# User Story

- Story ID: US-0005
- Title: Delete List
- Status: Tested
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-10-08

## As a user, I want to delete an entire list and its tasks so that I can remove completed projects.

## Acceptance Criteria
- Given an existing to-do list, When the user clicks delete list, Then the list and all its contained tasks are removed.

## Notes
Allows removal of obsolete lists.

## Test Approach
Run pytest on test_todo.py covering list deletion.

### Tasks
- Verify list deletion route, cascade delete, and tests
