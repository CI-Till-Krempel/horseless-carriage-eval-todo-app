# User Story

- Story ID: US-0002
- Title: Add a task to a list
- Status: Tested
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-10-29

## As a user, I want to add a task to a list with a short text description so that I can track what needs to be done.

## Acceptance Criteria
- Given a specific list exists, When the user enters a task description and clicks add, Then the task is added to that list.

## Notes
Users can successfully add tasks to existing lists.

## Test Approach
Write pytest unit and integration tests for adding tasks to a list.

### Tasks
- Verify US-0001 base app and models
- Add task creation endpoint/logic
- Write tests for adding tasks
- Verify CI checks
