# User Story

- Story ID: US-0001
- Title: Create a new to-do list with a name
- Status: Implemented
- Priority: P0
- Owner: Scrum Team
- Last Updated: 2026-07-27

## As a user, I want to create a new to-do list with a name so that I can organize my tasks.

## Acceptance Criteria
- Given the user is on the home page, When they enter a name for a new list and submit, Then a new to-do list is created and displayed with that name.
- Given a list name is empty or whitespace, When the user attempts to create a list, Then an error message is displayed and no list is created.

## Notes
Users can successfully establish separate categorized lists.

## Test Approach
Unit test the Flask routes and list creation logic using pytest and Flask test client.

### Tasks
- Initialize Flask app and routes
- Implement list creation and validation
- Add HTML templates and styling
- Write tests for list creation
