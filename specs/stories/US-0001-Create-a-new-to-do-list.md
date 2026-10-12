# User Story

- Story ID: US-0001
- Title: Create a new to-do list
- Status: Tested
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-10-12

## As a user, I want to create a new to-do list with a name so that I can organize my tasks.

## Acceptance Criteria
- Given the app is running, When the user submits a new list name, Then a new to-do list is created and displayed.

## Notes
Users can successfully initialize and view separate to-do lists.

## Test Approach
Pytest testing of Flask endpoints and HTML output.

### Tasks
- Initialize Flask app and setup routing
- Create HTML frontend with form for list creation
- Implement backend API for creating lists
- Write unit/integration tests for list creation
