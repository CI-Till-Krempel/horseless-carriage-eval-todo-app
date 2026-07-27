# User Story

- Story ID: US-0003
- Title: Mark a task as complete or incomplete
- Status: Implemented
- Priority: P0
- Owner: Scrum Team
- Last Updated: 2026-07-27

## As a user, I want to mark a task as complete or incomplete so that I can track progress on my action items.

## Acceptance Criteria
- Given a task in a list, When the user clicks the complete/incomplete toggle for the task, Then the task status toggles between complete and incomplete.
- Given a completed task, When displayed in the list view, Then it is visually distinguished from incomplete tasks (e.g. strikethrough or styling).

## Notes
Users can track completed items separately from pending work.

## Test Approach
Test toggling task completion from incomplete to complete and back using pytest and Flask test client.

### Tasks
- Add toggle task endpoint in app.py
- Update templates/index.html with toggle button and completed task CSS styling
- Write unit tests for task completion toggle
