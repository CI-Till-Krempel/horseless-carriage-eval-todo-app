# User Story

- Story ID: US-0003
- Title: Mark task complete or incomplete
- Status: Reviewed
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-10-09

## As a user, I want to mark a task as complete or incomplete so that I can see progress.

## Acceptance Criteria
- Given a task exists in a list, When the user clicks complete/incomplete, Then the task status toggles and is visually distinguished.

## Notes


## Test Approach
Pytest verification of task toggle endpoint.

### Tasks
- Add toggle route in Flask
- Update template for visual distinction
- Add unit tests for completion toggle
