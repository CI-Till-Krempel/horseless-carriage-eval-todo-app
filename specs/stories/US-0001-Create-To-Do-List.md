# User Story

- Story ID: US-0001
- Title: Create To-Do List
- Status: Reviewed
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-09-30

## As a user, I want to create a new to-do list with a name so that I can organize my tasks.

## Acceptance Criteria
- Given the user is on the home page, When they enter a list name and click create, Then a new to-do list is created and displayed.

## Notes
Users can create lists to categorize tasks.
- ⚠️ REVIEW DENIED at Tested by QA: pytest execution failed with ModuleNotFoundError for flask because requirements.txt was emptied and flask is not installed in the test environment.

## Test Approach
pytest unit tests for list creation API/route.
