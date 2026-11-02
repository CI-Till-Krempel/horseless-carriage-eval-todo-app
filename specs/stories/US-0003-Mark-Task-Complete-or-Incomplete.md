# User Story

- Story ID: US-0003
- Title: Mark Task Complete or Incomplete
- Status: Reviewed
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-11-02

## As a user, I want to mark a task as complete or incomplete so that I can track progress.

## Acceptance Criteria
- Given a task exists in a list, When the user marks it as complete, Then its status changes and it is visually distinguished.

## Notes


## Test Approach
Write unit tests using pytest and Flask test client.

### Tasks
- Add toggle route in app.py
- Add UI toggle button/checkbox
- Add tests for task completion toggle
