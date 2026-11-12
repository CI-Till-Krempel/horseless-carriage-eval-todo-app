# User Story

- Story ID: US-0002
- Title: Add Task to List
- Status: Reviewed
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-11-12

## As a user, I want to add a task to a list with a short text description so that I can keep track of what needs to be done.

## Acceptance Criteria
- Given the user is viewing a specific to-do list, When the user enters a task description and clicks 'Add Task', Then the task is added to the list and displayed.

## Notes
Enables users to record actionable items within their lists.
- ⚠️ REVIEW DENIED at Tested by QA: tests/test_todo.py has test setup errors because 'app' has no attribute 'init_db'. Existing tests need to be aligned with the current implementation.

## Test Approach
Test adding task.

### Tasks
- Add task API and frontend
