# User Story

- Story ID: US-0002
- Title: Add Task to List
- Status: Tested
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-10-30

## As a user, I want to add a task to a list with a short text description so that I can track what needs to be done.

## Acceptance Criteria
- Given an existing to-do list, When the user adds a task with a short text description, Then the task appears within that list.

## Notes
Users can populate lists with specific tasks.

## Test Approach
Pytest with Flask test client.

### Tasks
- Add POST /lists/<list_id>/tasks route
- Update HTML template to include task input form under each list
- Write unit test for adding tasks
