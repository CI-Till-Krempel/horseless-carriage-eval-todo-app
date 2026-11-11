# User Story

- Story ID: US-0001
- Title: Create a new to-do list
- Status: Reviewed
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-11-11

## As a user, I want to create a new to-do list with a name so that I can organize my tasks.

## Acceptance Criteria
- Given the user is on the main page, When they enter a list name and click create, Then a new to-do list is created and displayed.

## Notes
Enables users to start organizing their tasks by category or project.

## Test Approach
Write pytest tests verifying list creation API and UI endpoint.

### Tasks
- Create app.py with Flask route for creating a list
- Create templates/index.html with a form for list creation
- Add unit test for list creation
