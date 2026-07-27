# User Story

- Story ID: US-0002
- Title: Add a task to a list with a short text description
- Status: Accepted
- Priority: P0
- Owner: Scrum Team
- Last Updated: 2026-07-27

## As a user, I want to add a task to a list with a short text description so that I can track what needs to be done.

## Acceptance Criteria
- Given an existing to-do list, When the user adds a task with valid text description, Then the task appears under that list.
- Given a task description is empty, When the user attempts to add the task, Then an error message is shown and the task is not added.

## Notes
Users can add concrete action items into specific lists.

## Test Approach
Test task addition success and empty description validation using pytest and Flask test client.

### Tasks
- Add task creation endpoint in app.py
- Update templates/index.html to display tasks and task creation form per list
- Write unit tests for adding tasks and validation
