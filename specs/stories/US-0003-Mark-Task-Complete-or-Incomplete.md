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
- ⚠️ REVIEW DENIED at Tested by QA: Database schema tests failed: sqlalchemy.exc.OperationalError: table todo_list has no column named title. Please fix the database models/migrations/schema setup so tables are created correctly.

## Test Approach
Verify via pytest.

### Tasks
- Add task completion route
- Add tests
