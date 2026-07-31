# User Story

- Story ID: US-0001
- Title: US-0001: Create and view to-do lists
- Status: Implemented
- Priority: P0
- Owner: Scrum Team
- Last Updated: 2026-07-31

## As a user, I want to create a new to-do list with a name so that I can organize my tasks into separate lists.

## Acceptance Criteria
- Given the user is on the main page, When they enter a name for a new list and submit, Then the new list is created and displayed in the list of all lists.
- Given existing lists are present, When the user views the main page, Then all lists are displayed clearly.

## Notes
Users can successfully group related tasks into distinct lists.

## Test Approach
Pytest unit and integration tests verifying list creation and task addition.

### Tasks
- Initialize Flask app and SQLite DB
- Create HTML template and routes for lists and tasks
- Write unit tests for list creation, viewing, and task addition
