# User Story

- Story ID: US-0001
- Title: Create To-Do List
- Status: Reviewed
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-10-27

## As a user, I want to create a new to-do list with a name so that I can organize my tasks.

## Acceptance Criteria
- Given the app is running, When the user views the home page, Then they see an option to create a new to-do list with a name.

## Notes
Users can successfully create and name distinct to-do lists.
- ⚠️ REVIEW DENIED at Tested by QA: Automated tests failed during the test suite run: 2 tests failed (test_add_task and test_delete_list) due to list ID counter incrementing behavior/index assumptions in tests.

## Test Approach
Write pytest unit and integration tests using Flask test client.
