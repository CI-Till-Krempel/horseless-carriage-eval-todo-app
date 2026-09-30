# User Story

- Story ID: US-0001
- Title: Create a new to-do list
- Status: Ready
- Priority: P0
- Owner: Scrum Team
- Last Updated: 2026-09-30

## As a user, I want to create a new to-do list with a name so that I can organize my tasks.

## Acceptance Criteria
- Given the user is on the home page, When they enter a list name and click create, Then a new to-do list is created and displayed.

## Notes
Users can start organizing work by creating named lists.

## Test Approach
Pytest tests covering list creation, task addition, completion toggling, task deletion, and list deletion.

### Tasks
- Create requirements.txt with flask and flask-sqlalchemy
- Create models.py with ToDoList and Task models
- Create app.py with routes for list creation, task addition, toggling, and deletion
- Create templates/index.html for the web UI
- Create tests/test_todo.py for unit and integration testing
- Run pytest and verify all tests pass
