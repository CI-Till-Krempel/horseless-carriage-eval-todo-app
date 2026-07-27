# User Story

- Story ID: US-0004
- Title: Delete tasks and entire lists
- Status: Implemented
- Priority: P0
- Owner: Scrum Team
- Last Updated: 2026-07-27

## As a user, I want to delete tasks and entire lists so that I can keep my to-do application organized and clutter-free.

## Acceptance Criteria
- Given an existing task in a list, When the user clicks the delete button for the task, Then the task is removed from the list.
- Given an existing to-do list, When the user clicks the delete button for the list, Then the entire list and all its contained tasks are removed.

## Notes
Users can clean up completed or obsolete tasks and lists.

## Test Approach
Test deleting tasks from lists and deleting entire lists along with their contained tasks using pytest and Flask test client.

### Tasks
- Add delete list and delete task endpoints in app.py
- Update templates/index.html with delete buttons for lists and tasks
- Write unit tests for list and task deletion
