# User Story

- Story ID: US-0001
- Title: Create a New To-Do List
- Status: Tested
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-11-03

## As a user, I want to create a new to-do list with a name so that I can organize my tasks.

## Acceptance Criteria
- Given the user is on the home page, When they enter a list name and submit, Then a new to-do list is created and displayed.

## Notes
Users can successfully create and view a new to-do list by name.

## Test Approach
pytest unit test for creating a list via Flask test client.

### Tasks
- Initialize Flask app and requirements.txt
- Implement list creation route and HTML template
- Write unit tests for list creation
