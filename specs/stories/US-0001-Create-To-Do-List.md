# User Story

- Story ID: US-0001
- Title: Create To-Do List
- Status: Reviewed
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-11-02

## As a user, I want to create a new to-do list with a name so that I can organize my tasks.

## Acceptance Criteria
- Given the user is on the main page, When they enter a list name and click create, Then a new to-do list is created and displayed.

## Notes

- ⚠️ REVIEW DENIED at Tested by QA: Tests test_delete_task and test_delete_list still fail because global lists and tasks lists are not cleared between test functions in tests/test_app.py (or test client requests don't clear app-level state), causing leftover tasks/lists from prior tests to interfere with assertions.

## Test Approach
Use pytest and Flask test client to verify list creation endpoint and UI rendering.
