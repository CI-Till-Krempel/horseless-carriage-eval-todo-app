# User Story

- Story ID: US-0001
- Title: Create To-Do List
- Status: Ready
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-10-12

## As a user, I want to create a new to-do list with a name so that I can organize my tasks.

## Acceptance Criteria
- Given I am on the home page, When I enter a list name and click create, Then a new to-do list is created and displayed.

## Notes
Users can successfully create and view multiple to-do lists.

## Test Approach
Use pytest and Flask test client to verify list creation.

### Tasks
- Create Flask app with list store
- Create index page to view and create lists
- Add automated tests
