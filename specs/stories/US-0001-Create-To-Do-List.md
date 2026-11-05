# User Story

- Story ID: US-0001
- Title: Create To-Do List
- Status: Ready
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-11-05

## As a user, I want to create a new to-do list with a name so that I can organize my tasks.

## Acceptance Criteria
- Given the user is on the main page, When they enter a list name and click create, Then a new to-do list is created and displayed.

## Notes
Enables basic organization of tasks into named lists.

## Test Approach
Write pytest unit/integration tests covering list creation via HTTP requests.

### Tasks
- Create Flask app structure
- Implement list creation endpoint and UI
- Write pytest tests for list creation
