# User Story

- Story ID: US-0001
- Title: Create To-Do List
- Status: Reviewed
- Priority: P0
- Owner: Scrum Team
- Last Updated: 2026-08-07

## As a user, I want to create a new to-do list with a name so that I can organize my tasks.

## Acceptance Criteria
- Given the user is on the home page, When they enter a list name and click create, Then a new to-do list is created and displayed.

## Notes
Users can organize tasks into named categories.
- 🚫 BLOCKED (technical) - raised by QA: advance_story_stage('US-0001', 'Tested') has been rejected 3 times in a row for the same reason - most recently: Cannot mark 'US-0001' Tested - 5 of 5 tests failed. Fix the failing tests before retrying.

## Test Approach
Automated unit tests using pytest and Flask test client, verifying list creation, task addition, and viewing functionality.

### Tasks
- Initialize Flask app structure and requirements.txt
- Implement in-memory storage model for lists and tasks
- Implement Flask routes for creating lists and adding tasks
- Implement main view showing lists and tasks with visual styling for completed items
- Write unit/integration tests with pytest
