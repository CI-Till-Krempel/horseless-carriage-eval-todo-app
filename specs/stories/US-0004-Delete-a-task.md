# User Story

- Story ID: US-0004
- Title: Delete a task
- Status: Ready
- Priority: P0
- Owner: Scrum Team
- Last Updated: 2026-07-29

## As a user, I want to delete a task so that I can remove unwanted items.

## Acceptance Criteria
- - Given a task exists in a list, When the user clicks delete on the task, Then the task is removed from the list.

## Notes
Users can remove individual tasks from lists.

## Test Approach
Run pytest to verify task deletion and overall test suite.

### Tasks
- 1. Verify task deletion route and UI element
- 2. Add dedicated test case for task deletion in test_app.py
- 3. Run pytest and verify functionality
