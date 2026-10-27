# User Story

- Story ID: US-0002
- Title: Add a task to a list
- Status: Reviewed
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-10-27

## As a user, I want to add a task to a list with a short text description so that I can track what needs to be done.

## Acceptance Criteria
- Given an existing to-do list, When the user adds a task with a short text description, Then the task appears under that list.

## Notes
Users can add tasks with descriptions to any created list.
- ⚠️ REVIEW DENIED at Tested by QA: test_toggle_task failed with 'assert True is False' because task completion state defaulted or toggled unexpectedly in the test setup.

## Test Approach
Pytest test_add_task.

### Tasks
- Add task route and UI form
- Automated test for adding tasks
