# User Story

- Story ID: US-0001
- Title: Create To-Do List
- Status: Ready
- Priority: P0
- Owner: Scrum Team
- Last Updated: 2026-09-24

## As a user, I want to create a new to-do list with a name so that I can organize my tasks.

## Acceptance Criteria
- Given the user is on the home page, When they enter a list name and click Create List, Then a new to-do list is created and displayed in the list view.

## Notes
Users can successfully create and see a new list.

## Test Approach
Pytest unit tests for web endpoints using Flask test client.

### Tasks
- Create requirements.txt with Flask
- Create app.py with routes for listing and creating to-do lists
- Create templates/index.html web UI
- Add tests for list creation and viewing
