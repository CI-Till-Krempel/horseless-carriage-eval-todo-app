# User Story

- Story ID: US-0002
- Title: Add Task to List
- Status: Accepted
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-10-12

## As a user, I want to add a task to a list with a short text description so that I can track what needs to be done.

## Acceptance Criteria
- Given an existing to-do list, When the user adds a task with a text description, Then the task appears under that list.

## Notes
Enables users to record items to accomplish within a specific list.

## Test Approach
Add unit tests for adding tasks to an existing list.

### Tasks
- Update todo_lists data structure for tasks
- Implement add_task route
- Add task input form in index.html
- Write pytest tests for task addition
