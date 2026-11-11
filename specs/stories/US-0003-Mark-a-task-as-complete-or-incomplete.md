# User Story

- Story ID: US-0003
- Title: Mark a task as complete or incomplete
- Status: Ready
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-11-11

## As a user, I want to mark a task as complete or incomplete so that I can track my progress.

## Acceptance Criteria
- Given a task in a list, When the user clicks the complete/incomplete toggle, Then the task status updates and is visually distinguished.

## Notes
Users can visually track finished vs unfinished items.

## Test Approach
Write pytest tests verifying task completion toggling and visual distinction.

### Tasks
- Add toggle task completion route in app.py
- Update index.html with completion toggle and styling for completed tasks
- Write unit tests for task completion toggle
