# User Story

- Story ID: US-001
- Title: Create and view To-Do Lists
- Status: Implemented
- Priority: P0
- Owner: Scrum Team
- Last Updated: 2026-07-31

## As a user, I want to create a new to-do list with a name and see all my lists so that I can organize my tasks.

## Acceptance Criteria
- Given the user is on the home page, When they enter a name for a new list and click create, Then a new to-do list is created and displayed in the list of all lists.
- Given existing lists are present, When the user views the application home page, Then all lists are displayed clearly.

## Notes
Users can successfully initiate organization by creating and viewing named lists.

## Test Approach
Write pytest unit tests for Flask routes checking list creation and home page rendering, plus a basic end-to-end test.

### Tasks
- Initialize Flask project structure and dependencies
- Implement backend routes for creating and listing to-do lists
- Create clean HTML/CSS UI for listing and adding to-do lists
- Write unit/integration tests for list creation and viewing
- Update README with instructions to run the app
