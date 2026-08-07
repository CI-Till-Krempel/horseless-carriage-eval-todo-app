# User Story

- Story ID: US-0001
- Title: Create a new to-do list with a name
- Status: Implemented
- Priority: P0
- Owner: Scrum Team
- Last Updated: 2026-08-07

## As a user, I want to create a new to-do list with a name so that I can organize my tasks.

## Acceptance Criteria
- Given the user is on the home page, When they enter a list name and submit the create form, Then a new to-do list is created and displayed in the lists view.

## Notes
Users can successfully create and see named lists.

## Test Approach
Use pytest and Flask test client to thoroughly verify routes, list creation, task management, completion toggling, and deletion.

### Tasks
- Create Flask app structure and requirements.txt
- Implement in-memory models/storage for lists and tasks
- Implement HTML template with styling for list creation, task addition, status toggling, and deletion
- Write unit and integration tests covering US-0001 to US-0006
- Update README with instructions to run and test the app
