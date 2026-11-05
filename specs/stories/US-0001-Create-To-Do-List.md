# User Story

- Story ID: US-0001
- Title: Create To-Do List
- Status: Reviewed
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-11-05

## As a user, I want to create a new to-do list with a name so that I can organize my tasks.

## Acceptance Criteria
- Given the user is on the main page, When they enter a list name and click create, Then a new to-do list is created and displayed.

## Notes
Enables basic organization of tasks into named lists.
- ⚠️ REVIEW DENIED at Tested by QA: pytest unit tests test_toggle_task, test_delete_task, and test_delete_list_cascade are failing with status 302 instead of 200. The delete and toggle endpoints in app.py need to properly inspect request.is_json or Content-Type headers to return jsonify responses when called with JSON.

## Test Approach
Write pytest unit/integration tests covering list creation via HTTP requests.

### Tasks
- Create Flask app structure
- Implement list creation endpoint and UI
- Write pytest tests for list creation
