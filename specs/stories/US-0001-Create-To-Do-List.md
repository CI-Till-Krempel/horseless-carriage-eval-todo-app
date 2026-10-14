# User Story

- Story ID: US-0001
- Title: Create To-Do List
- Status: Accepted
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-10-14

## As a user, I want to create a new to-do list with a name so that I can organize my tasks.

## Acceptance Criteria
- Given the user is on the main page, When they enter a list name and click create, Then a new to-do list appears with that name.

## Notes
Users can successfully create and view named lists.

## Test Approach
Pytest unit tests for the Flask route and database persistence.

### Tasks
- Set up Flask app structure and requirements.txt
- Implement database models and schema for lists
- Implement route for creating a to-do list
- Write automated test for list creation
