# User Story

- Story ID: US-0003
- Title: Mark Task Complete or Incomplete
- Status: Implemented
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-10-12

## As a user, I want to mark a task as complete or incomplete so that I can track my progress.

## Acceptance Criteria
- Given a task in a list, When the user clicks complete/incomplete, Then its status toggles and is visually distinguished.

## Notes
Provides feedback on task completion status.

## Test Approach
Test toggling task completion state from incomplete to complete and back.

### Tasks
- Implement toggle_task route in app.py
- Update templates/index.html with toggle button and visual distinction (strike-through)
- Write pytest tests for toggling task completion
