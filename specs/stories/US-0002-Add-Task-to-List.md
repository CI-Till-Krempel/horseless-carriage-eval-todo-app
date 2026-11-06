# User Story

- Story ID: US-0002
- Title: Add Task to List
- Status: Implemented
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-11-06

## As a user, I want to add a task to a list with a short text description so that I can track what needs to be done.

## Acceptance Criteria
- Given an existing to-do list, When the user enters a task description and clicks add, Then the task is added to that list.

## Notes
Enables users to break down their lists into actionable tasks.

## Test Approach
Write pytest test verifying task addition to an existing list.

### Tasks
- Add task addition endpoint in app.py
- Update index.html to display task form and tasks per list
- Write unit test for adding tasks
