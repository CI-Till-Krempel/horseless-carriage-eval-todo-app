# User Story

- Story ID: US-0002
- Title: Add a task to a list
- Status: Implemented
- Priority: P0
- Owner: Scrum Team
- Last Updated: 2026-09-16

## As a user, I want to add a task to a list with a short text description so that I can track what needs to be done.

## Acceptance Criteria
- Given an existing to-do list, When the user adds a task with a description, Then the task appears under that list.

## Notes
Allows users to record specific action items within a list.

## Test Approach
Pytest integration test for task creation.

### Tasks
- Add task endpoint in app.py
- Add task form in index.html
- Add tests for task creation
