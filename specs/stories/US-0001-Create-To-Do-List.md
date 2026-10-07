# User Story

- Story ID: US-0001
- Title: Create To-Do List
- Status: Ready
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-10-07

## As a user, I want to create a new to-do list with a name so that I can organize my tasks.

## Acceptance Criteria
- Given the user is on the home page, When they click create list and provide a name, Then a new to-do list is created and displayed.

## Notes
Allows users to organize tasks into separate lists.

## Test Approach
Pytest unit tests verifying list/task creation, completion, and deletion.

### Tasks
- Create Flask app and SQLite models
- Implement HTML templates with Jinja2
- Implement CRUD routes for lists and tasks
- Add automated pytest test suite
