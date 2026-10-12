# User Story

- Story ID: US-0004
- Title: Delete Task
- Status: Reviewed
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-10-12

## As a user, I want to delete a task so that I can remove unwanted items.

## Acceptance Criteria
- Given a task, When the user clicks delete, Then the task is removed from the list.

## Notes
Allows cleanup of unwanted or obsolete tasks.

## Test Approach
Test deleting a task from an existing list and verifying removal.

### Tasks
- Implement delete_task route in app.py
- Add delete task button/form in templates/index.html
- Write pytest test for task deletion
