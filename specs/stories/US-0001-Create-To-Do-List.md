# User Story

- Story ID: US-0001
- Title: Create To-Do List
- Status: Implemented
- Priority: P0
- Owner: Scrum Team
- Last Updated: 2026-07-30

## As a user, I want to create a new to-do list with a name so that I can organize my tasks.

## Acceptance Criteria
- Given the user is on the main page, When they enter a name for a new list and submit, Then a new to-do list is created and displayed.

## Notes
Users can successfully create and view named to-do lists.

## Test Approach
Write pytest unit tests covering list creation, adding tasks, and viewing lists/tasks, and run them via pytest.

### Tasks
- Set up Flask application structure and requirements.txt
- Implement data model and routes for creating lists (US-0001)
- Implement routes and UI for adding tasks to a list (US-0002)
- Implement main page UI to view lists and tasks with visual distinction for completed tasks (US-0006)
- Write unit tests and verify CI checks
