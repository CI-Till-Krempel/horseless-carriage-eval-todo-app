# User Story

- Story ID: US-0002
- Title: Add Task to a List
- Status: Reviewed
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-11-03

## As a user, I want to add a task to a list with a short text description so that I can track what needs to be done.

## Acceptance Criteria
- Given an existing to-do list, When the user enters a task description and clicks add, Then the task is added to that list.

## Notes
Users can successfully add tasks with descriptions to existing lists.
- ⚠️ REVIEW DENIED at Tested by QA: Test suite failure: test_app.py fails to import lists_store from app because app.py was refactored to use Flask-SQLAlchemy without lists_store.

## Test Approach
Write pytest for adding tasks to lists and test UI submission.

### Tasks
- Add POST route for tasks
- Update UI to submit task description
- Add tests for adding task
