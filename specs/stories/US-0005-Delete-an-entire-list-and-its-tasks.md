# User Story

- Story ID: US-0005
- Title: Delete an entire list and its tasks
- Status: Ready
- Priority: P0
- Owner: Scrum Team
- Last Updated: 2026-07-29

## As a user, I want to delete an entire list and its tasks so that I can clean up obsolete projects or categories.

## Acceptance Criteria
- - Given an existing list with tasks, When the user clicks delete on the entire list, Then the list and all its associated tasks are removed.

## Notes
Users can delete lists and all contained tasks cleanly.

## Test Approach
Run pytest to verify list deletion and cascade cleanup.

### Tasks
- 1. Verify list deletion route and UI form
- 2. Add test case for list deletion and cascade task cleanup in test_app.py
- 3. Run pytest
