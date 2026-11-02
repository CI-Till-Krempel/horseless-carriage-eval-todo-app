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

- ⚠️ REVIEW DENIED at Tested by QA: Tests test_delete_task and test_delete_list still fail because route parameters in test requests (e.g. /lists/1/tasks or /lists/1/delete) use hardcoded ID 1, whereas the auto-incrementing ID counters continue incrementing across requests without resetting per test, leading to 404 or non-matching IDs on deletion routes.

## Test Approach
Use pytest and Flask test client to verify list creation endpoint and UI rendering.
