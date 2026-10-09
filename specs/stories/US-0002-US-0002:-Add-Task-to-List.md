# User Story

- Story ID: US-0002
- Title: US-0002: Add Task to List
- Status: Ready
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-10-09

## As a user, I want to add a task to a list with a short text description so that I can keep track of what needs to be done.

## Acceptance Criteria
- Given an existing list, When the user adds a task with a description, Then the task appears within that list.

## Notes
Users can add descriptive tasks to their to-do lists.

## Test Approach
Use pytest and Flask test client to verify adding tasks to lists.

### Tasks
- Add task form to templates/index.html
- Verify route handling in app.py
- Add unit tests for adding tasks
