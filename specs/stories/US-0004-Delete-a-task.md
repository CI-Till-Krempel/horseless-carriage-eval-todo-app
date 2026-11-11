# User Story

- Story ID: US-0004
- Title: Delete a task
- Status: Implemented
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-11-11

## As a user, I want to delete a task so that I can remove items I no longer need.

## Acceptance Criteria
- Given a task in a list, When the user clicks delete on the task, Then the task is removed from the list.

## Notes
Users can clean up unwanted tasks.

## Test Approach
Write pytest tests verifying task deletion.

### Tasks
- Add delete task route in app.py
- Update index.html with delete task button/form
- Write unit tests for task deletion
