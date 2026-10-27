# User Story

- Story ID: US-0001
- Title: Create a new to-do list
- Status: Reviewed
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-10-27

## As a user, I want to create a new to-do list with a name so that I can organize my tasks.

## Acceptance Criteria
- Given the user is on the main page, When they enter a name for a new list and submit, Then a new to-do list is created and displayed in the UI.

## Notes
Users can organize their tasks into distinct named lists.
- ⚠️ REVIEW DENIED at Tested by QA: Test `test_add_and_complete_task` failed due to `NameError: name 'database' is not defined` in `tests/test_app.py:36`. Please fix the test import or reference to `database`.

## Test Approach
Unit test with pytest.

### Tasks
- Create requirements.txt
- Create database.py
- Create app.py
- Create templates/index.html
