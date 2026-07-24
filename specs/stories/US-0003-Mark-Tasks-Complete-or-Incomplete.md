# User Story

- Story ID: US-0003
- Title: Mark Tasks Complete or Incomplete
- Status: Ready
- Priority: P1
- Owner: Scrum Team
- Last Updated: 2026-07-24

## As a user, I want to mark a task as complete or incomplete so that I can track my progress.

## Acceptance Criteria
- Given a task in a list, When the user clicks to mark it complete, Then the task is visually distinguished as complete.
- Given a completed task, When the user clicks to mark it incomplete, Then the task returns to incomplete status.

## Notes
Users can toggle task completion status and see visual differentiation.

## Test Approach
Pytest tests checking task completion toggle endpoints and status persistence.
