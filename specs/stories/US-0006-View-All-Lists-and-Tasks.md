# User Story

- Story ID: US-0006
- Title: View All Lists and Tasks
- Status: Reviewed
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-10-27

## As a user, I want to see all my lists and all their tasks with completed tasks visually distinguished so that I have a clear overview.

## Acceptance Criteria
- Given multiple lists and tasks exist, When the user views the main view, Then they see all their lists and all tasks within each list, with completed tasks visually distinguished.

## Notes
Users can view all lists and tasks with clear visual status.
- ⚠️ REVIEW DENIED at Tested by QA: Test suite run failed with test_delete_list failing in tests/test_todo.py.

## Test Approach
pytest

### Tasks
- Implement view endpoint/logic for lists and tasks
- Add tests for viewing all lists and tasks
