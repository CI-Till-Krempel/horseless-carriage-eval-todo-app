# User Story

- Story ID: US-0003
- Title: Mark Task Complete or Incomplete
- Status: Reviewed
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-10-27

## As a user, I want to mark a task as complete or incomplete so that I can track my progress.

## Acceptance Criteria
- Given a task exists in a list, When the user marks the task as complete or incomplete, Then its completion status updates and it is visually distinguished.

## Notes
Users can toggle task status and see visual distinction.
- ⚠️ REVIEW DENIED at Tested by QA: Test collection failed due to ImportError: cannot import name 'lists_db' from 'app'. Please fix the test imports and failing tests.

## Test Approach
pytest

### Tasks
- Add toggle endpoint
- Add tests
