# User Story

- Story ID: US-0003
- Title: US-0003: Mark Task Complete or Incomplete
- Status: Reviewed
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-10-09

## As a user, I want to mark a task as complete or incomplete so that I can track my progress.

## Acceptance Criteria
- Given a task exists in a list, When the user marks it as complete, Then its status changes and it is visually distinguished from incomplete tasks.

## Notes
Users can easily toggle task status and visually see completion.

## Test Approach
Use pytest and Flask test client to verify task completion toggling.

### Tasks
- Add toggle route in app.py
- Add toggle button in templates/index.html
- Add unit tests for toggling task completion
