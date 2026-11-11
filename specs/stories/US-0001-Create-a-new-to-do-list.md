# User Story

- Story ID: US-0001
- Title: Create a new to-do list
- Status: Implemented
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-11-11

## As a user, I want to create a new to-do list with a name so that I can organize my tasks.

## Acceptance Criteria
- Given the user is on the main page, When they enter a list name and click create, Then a new to-do list with that name is created and displayed.

## Notes
Users can organize tasks into distinct lists.

## Test Approach
Write pytest unit/integration tests covering list creation.

### Tasks
- Create requirements.txt with Flask
- Create app.py with list creation route
- Create templates/index.html with list creation form
- Write tests for list creation
