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
- 🚫 BLOCKED (technical) - raised by QA: advance_story_stage('US-0001', 'Tested') has been rejected 3 times in a row for the same reason - most recently: Cannot mark 'US-0001' Tested - running the test suite found no tests actually ran (no tests collected). A story can't be Tested with an empty or unrunnable test suite.

## Test Approach
pytest unit tests for list creation API/route.
