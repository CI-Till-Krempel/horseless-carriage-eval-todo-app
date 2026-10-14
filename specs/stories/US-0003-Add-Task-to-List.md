# User Story

- Story ID: US-0003
- Title: Add Task to List
- Status: Implemented
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-10-14

## As a user, I want to add a task with a description to a list so that I can track what needs to be done.

## Acceptance Criteria
- Given an existing to-do list, When the user adds a task with a text description, Then the task appears within that list.

## Notes
Users can add tasks to lists.

## Test Approach
Test via pytest.

### Tasks
- Add POST /lists/<list_id>/tasks route
- Add task form in templates/index.html
