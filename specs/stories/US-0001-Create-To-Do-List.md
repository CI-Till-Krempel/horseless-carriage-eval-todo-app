# User Story

- Story ID: US-0001
- Title: Create To-Do List
- Status: Reviewed
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-11-11

## As a user, I want to create a new to-do list with a name so that I can organize my tasks.

## Acceptance Criteria
- Given the user is on the home page, When they submit a new list name, Then a new to-do list is created and displayed.

## Notes
Allows users to group and manage separate sets of tasks.

## Test Approach
Pytest testing HTTP endpoints via Flask test client for list/task operations.

### Tasks
- Create requirements.txt and app.py with Flask backend
- Create templates/index.html web UI
- Implement routes for lists and tasks (create list, add task, toggle, delete task, delete list)
- Write pytest tests for all US-0001 through US-0006 criteria
- Create user guide doc
