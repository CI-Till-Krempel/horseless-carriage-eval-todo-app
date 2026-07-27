# User Story

- Story ID: US-0001
- Title: Create a New To-Do List
- Status: Ready
- Priority: P0
- Owner: Scrum Team
- Last Updated: 2026-07-27

## As a user, I want to create a new to-do list with a name so that I can organize my tasks.

## Acceptance Criteria
- Given the user is on the main page, When they click 'Create List' and enter a valid name, Then a new to-do list is created and displayed in the application UI.

## Notes
Users can successfully create and view multiple named to-do lists.

## Test Approach
Manual and automated unit tests using pytest for backend routes and core CRUD operations.

### Tasks
- Initialize Flask app structure
- Implement storage model for lists and tasks
- Create routes for creating lists, adding tasks, toggling task status, deleting tasks, deleting lists, and viewing all lists
- Create HTML template with clean styling and visual distinction for completed tasks
- Write unit/integration tests and README with instructions
