# User Story

- Story ID: US-0001
- Title: Create and view to-do lists
- Status: Implemented
- Priority: P0
- Owner: Scrum Team
- Last Updated: 2026-08-06

## As a user, I want to create a new to-do list with a name so that I can organize my tasks.

## Acceptance Criteria
- Given the user is on the main page, When they enter a name for a new list and submit, Then a new to-do list is created and displayed in the list of all lists.

## Notes
Users can successfully organize their tasks into named lists and view all existing lists.

## Test Approach
Manual / automated unit tests using pytest for Flask routes

### Tasks
- Create requirements.txt and Flask app structure
- Implement list creation and viewing (US-0001)
- Implement task addition and viewing (US-0002)
- Implement task completion toggle (US-0003)
- Implement deletion of tasks and lists (US-0004)
- Write README.md with clear run instructions
