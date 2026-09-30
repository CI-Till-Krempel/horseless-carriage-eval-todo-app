# User Story

- Story ID: US-001
- Title: Create a new to-do list
- Status: Ready
- Priority: P0
- Owner: Scrum Team
- Last Updated: 2026-09-30

## As a user, I want to create a new to-do list with a name so that I can organize my tasks.

## Acceptance Criteria
- Given the app is running, When the user opens the home page, Then they see a form to create a new list and a list of existing lists.
- Given the user enters a list name, When they submit the form, Then a new to-do list is created and displayed.

## Notes
Allows users to organize tasks into separate categories/lists.
- Dependencies: ['None']

## Test Approach
Write comprehensive unit and integration tests using pytest and Flask's test client covering list creation, task addition, completion toggle, task deletion, and list deletion.
