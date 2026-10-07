# User Story

- Story ID: US-0001
- Title: Create To-Do List
- Status: Tested
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-10-07

## As a user, I want to create a new to-do list with a name so that I can organize my tasks.

## Acceptance Criteria
- Given the app is running, When the user opens the web interface, Then they see a clean view to create a new to-do list.
- Given the user enters a list name, When they submit the form, Then a new list is created and displayed.

## Notes
Enables users to start organizing their work into separate lists.

## Test Approach
Use pytest and Flask test client to verify list creation and task addition.
