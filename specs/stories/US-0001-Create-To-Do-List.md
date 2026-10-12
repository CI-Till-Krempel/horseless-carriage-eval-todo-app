# User Story

- Story ID: US-0001
- Title: Create To-Do List
- Status: Accepted
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-10-12

## As a user, I want to create a new to-do list with a name so that I can organize my tasks.

## Acceptance Criteria
- Given the user opens the web app, When they enter a list name and click create, Then a new to-do list is created and displayed on the screen.

## Notes
Users can successfully create and view named to-do lists via the web UI.

## Test Approach
Run pytest on test suite covering all CRUD operations.

### Tasks
- Create Flask app and in-memory data store
- Implement templates and static UI
- Write unit and integration tests via pytest
