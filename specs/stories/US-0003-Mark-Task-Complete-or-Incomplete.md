# User Story

- Story ID: US-0003
- Title: Mark Task Complete or Incomplete
- Status: Accepted
- Priority: P0
- Owner: Scrum Team
- Last Updated: 2026-07-30

## As a user, I want to mark tasks as complete or incomplete so that I can track my progress.

## Acceptance Criteria
- Given an existing task, When the user clicks complete/incomplete, Then the task status toggles and is visually updated.

## Notes
Users can toggle task completion states.

## Test Approach
Pytest unit test specifically asserting task completion toggle behavior.

### Tasks
- Review existing toggle route and UI button styling
- Add dedicated test cases for toggling task completion state
- Push changes and verify CI
