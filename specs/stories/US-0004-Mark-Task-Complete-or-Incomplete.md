# User Story

- Story ID: US-0004
- Title: Mark Task Complete or Incomplete
- Status: Ready
- Priority: P0
- Owner: Scrum Team
- Last Updated: 2026-09-24

## As a user, I want to mark a task as complete or incomplete so that I can track my progress.

## Acceptance Criteria
- Given a task in a list, When the user clicks the checkbox or button to mark it complete/incomplete, Then the task's completion status toggles and is visually updated.

## Notes
Users can toggle task completion status.

## Test Approach
Pytest client testing task completion toggle.

### Tasks
- Add toggle route in app.py
- Update template to include completion checkbox/toggle and visual styling
- Add unit tests for toggling completion
