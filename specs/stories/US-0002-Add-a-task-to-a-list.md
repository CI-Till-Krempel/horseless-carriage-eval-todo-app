# User Story

- Story ID: US-0002
- Title: Add a task to a list
- Status: Implemented
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-11-11

## As a user, I want to add a task to a list with a short text description so that I can keep track of what needs to be done.

## Acceptance Criteria
- Given an existing to-do list, When the user adds a task with a short text description, Then the task appears in that list.

## Notes
Users can add specific action items to their lists.

## Test Approach
Write pytest tests verifying task addition to a list.

### Tasks
- Add task route/logic in app.py
- Update index.html to display task input form per list
- Write unit tests for adding tasks
