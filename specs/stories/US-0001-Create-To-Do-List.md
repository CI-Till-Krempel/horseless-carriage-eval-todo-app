# User Story

- Story ID: US-0001
- Title: Create To-Do List
- Status: Implemented
- Priority: P0
- Owner: Scrum Team
- Last Updated: 2026-08-07

## As a user, I want to create a new to-do list with a name so that I can organize my tasks.

## Acceptance Criteria
- Given the user is on the home page, When they enter a list name and click create, Then a new to-do list is created and displayed.

## Notes
Allows users to structure and categorize their work items.

## Test Approach
Pytest integration tests checking Flask test client endpoints for list creation, task addition, completion toggling, deletion, and dashboard view.

### Tasks
- Create Flask application setup and in-memory data structures
- Implement routes for creating lists, adding tasks, toggling completion, deleting tasks, and deleting lists
- Create HTML template with clean styling for lists and tasks dashboard
- Add unit/integration tests with pytest
