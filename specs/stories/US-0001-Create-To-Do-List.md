# User Story

- Story ID: US-0001
- Title: Create To-Do List
- Status: Reviewed
- Priority: P0
- Owner: Scrum Team
- Last Updated: 2026-09-29

## As a user, I want to create a new to-do list with a name so that I can organize my tasks.

## Acceptance Criteria
- Given the user opens the app, When they enter a list name and click create, Then a new to-do list is created and displayed.

## Notes
Users can successfully create and view multiple named to-do lists.
- ⚠️ REVIEW DENIED at Tested by QA: pytest reports 2 test failures in test_app.py (test_add_task and test_toggle_task failed because todo_lists dictionary state persistence / counter management across test requests caused list IDs or task IDs to mismatch or persist incorrectly between test client fixtures).

## Test Approach
Write unit tests using pytest for list creation, task addition, and toggling status.
