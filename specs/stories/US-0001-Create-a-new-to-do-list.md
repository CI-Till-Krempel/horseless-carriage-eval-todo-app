# User Story

- Story ID: US-0001
- Title: Create a new to-do list
- Status: Implemented
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-10-14

## As a user, I want to create a new to-do list with a name so that I can organize my tasks.

## Acceptance Criteria
- Given the user is on the home page, When they enter a list name and click create, Then a new to-do list is created and displayed.

## Notes
Users can successfully create and view named to-do lists.

## Test Approach
Pytest unit tests verifying list creation API and database persistence.

### Tasks
- Initialize Flask app structure
- Create database model and migration/init
- Implement list creation route
- Write pytest tests
