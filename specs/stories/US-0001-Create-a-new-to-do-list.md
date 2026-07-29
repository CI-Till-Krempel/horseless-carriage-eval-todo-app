# User Story

- Story ID: US-0001
- Title: Create a new to-do list
- Status: Accepted
- Priority: P0
- Owner: Scrum Team
- Last Updated: 2026-07-29

## As a user, I want to create a new to-do list with a name so that I can organize my tasks.

## Acceptance Criteria
- - Given the application is running, When the user views the home page, Then they see an option to create a new to-do list with a name.
- - Given the user enters a list name, When they submit the form, Then a new to-do list is created and displayed in the lists view.

## Notes
Users can successfully initialize and view named to-do lists.

## Test Approach
Unit tests for Flask routes and database models using pytest.

### Tasks
- 1. Initialize Flask app structure with templates and static folders
- 2. Implement database schema for Lists and Tasks
- 3. Implement routes and UI for creating lists and adding tasks
