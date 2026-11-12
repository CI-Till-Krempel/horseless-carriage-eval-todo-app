# User Story

- Story ID: US-0003
- Title: Mark Task Complete or Incomplete
- Status: Reviewed
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-11-12

## As a user, I want to mark a task as complete or incomplete so that I can monitor my progress.

## Acceptance Criteria
- Given an existing task, When the user clicks to mark it complete or incomplete, Then its status toggles and is visually updated.

## Notes
Users can track task completion status visually.
- ⚠️ REVIEW DENIED at Tested by QA: Test collection still failing: ImportError: cannot import name 'todo_lists' from 'app' in test_app.py (root level vs tests/test_app.py path). Please ensure test_app.py is located under tests/ and imports correctly.

## Test Approach
Pytest for task completion and incompleteness.

### Tasks
- Add completion toggle endpoint/UI
- Write tests
