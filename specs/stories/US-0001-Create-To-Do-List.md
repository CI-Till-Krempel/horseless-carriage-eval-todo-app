# User Story

- Story ID: US-0001
- Title: Create To-Do List
- Status: Reviewed
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-10-26

## As a user, I want to create a new to-do list with a name so that I can organize my tasks.

## Acceptance Criteria
- Given the application is running, When the user creates a new list with a name, Then a new to-do list is created and displayed.

## Notes
Enables the user to start organizing their tasks into named categories.
- 🚫 BLOCKED (technical) - raised by QA: advance_story_stage('US-0001', 'Tested') has been rejected 3 times in a row for the same reason - most recently: Cannot mark 'US-0001' Tested - 6 of 6 tests failed. Fix the failing tests before retrying.

## Test Approach
Pytest for backend routes and HTML response verification.

### Tasks
- Create Flask app structure
- Implement list creation route/UI
