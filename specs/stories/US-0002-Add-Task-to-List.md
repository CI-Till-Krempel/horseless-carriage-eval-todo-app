# User Story

- Story ID: US-0002
- Title: Add Task to List
- Status: Reviewed
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-11-02

## As a user, I want to add a task to a list with a short text description so that I can track what needs to be done.

## Acceptance Criteria
- Given a to-do list exists, When the user adds a task with a description, Then the task appears within that list.

## Notes

- ⚠️ REVIEW DENIED at Tested by QA: Test failure in tests/test_todo.py: test_add_task fails because the template does not render tasks for the list or the list ID doesn't match the URL parameter.

## Test Approach
Pytest unit/integration tests for adding a task to a list.

### Tasks
- Write backend/frontend code for adding tasks
- Write tests for adding tasks
