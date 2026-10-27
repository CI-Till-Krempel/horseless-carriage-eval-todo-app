# User Story

- Story ID: US-0002
- Title: Add Task to List
- Status: Implemented
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-10-27

## As a user, I want to add a task to a list with a short text description so that I can track what needs to be done.

## Acceptance Criteria
- Given a to-do list exists, When the user adds a task with a short text description, Then the task appears under that list.

## Notes
Users can add descriptive tasks to any created list.

## Test Approach
Add pytest test cases verifying adding tasks to lists via Flask test client.

### Tasks
- Update app.py to handle adding tasks to lists
- Update index.html to display task input form per list
- Add unit tests for adding tasks in test_app.py
