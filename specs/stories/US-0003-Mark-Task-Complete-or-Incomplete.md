# User Story

- Story ID: US-0003
- Title: Mark Task Complete or Incomplete
- Status: Reviewed
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-11-03

## As a user, I want to mark a task as complete or incomplete so that I can track my progress.

## Acceptance Criteria
- Given a task in a list, When the user clicks the complete/incomplete toggle, Then the task status updates accordingly.

## Notes
Users can toggle task completion states easily.
- ⚠️ REVIEW DENIED at Tested by QA: Test failure in tests/test_todo.py::test_add_task_to_list: AttributeError: 'NoneType' object has no attribute 'id'. Please ensure app.py route handlers and legacy tests are fully compatible with the TodoList model schema.

## Test Approach
Verify via pytest.

### Tasks
- Add task completion route
- Add tests
