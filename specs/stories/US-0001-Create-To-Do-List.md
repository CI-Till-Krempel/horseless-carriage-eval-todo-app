# User Story

- Story ID: US-0001
- Title: Create To-Do List
- Status: Ready
- Priority: P0
- Owner: Scrum Team
- Last Updated: 2026-08-07

## As a user, I want to create a new to-do list with a name so that I can organize my tasks.

## Acceptance Criteria
- Given the user is on the home page, When they enter a list name and click create, Then a new to-do list is created and displayed.

## Notes
Users can organize tasks into named categories.

## Test Approach
Automated unit tests using pytest and Flask test client, verifying list creation, task addition, and viewing functionality.

### Tasks
- Initialize Flask app structure and requirements.txt
- Implement in-memory storage model for lists and tasks
- Implement Flask routes for creating lists and adding tasks
- Implement main view showing lists and tasks with visual styling for completed items
- Write unit/integration tests with pytest
