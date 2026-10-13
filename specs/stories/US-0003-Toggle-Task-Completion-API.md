# User Story

- Story ID: US-0003
- Title: Toggle Task Completion API
- Status: Ready
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-10-13

## As a user, I want to mark a task as complete or incomplete so that I can track my progress.

## Acceptance Criteria
- Given an existing task, When the user toggles its completion status, Then the task completion status updates accordingly.

## Notes
Tasks can be marked complete/incomplete.

## Test Approach
Add pytest test for toggling task completion.

### Tasks
- Implement POST /tasks/<task_id>/toggle route
