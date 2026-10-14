# User Story

- Story ID: US-0004
- Title: Toggle Task Completion
- Status: Reviewed
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-10-14

## As a user, I want to mark a task as complete or incomplete so that I can see my progress.

## Acceptance Criteria
- Given a task exists in a list, When the user marks it as complete or incomplete, Then its status updates and is visually distinguished.

## Notes
Users can toggle task completion.
- ⚠️ REVIEW DENIED at Tested by QA: SQLAlchemy foreign key error during test collection: Task table references todolist table before todolist is defined or table order/relationships need adjustment.

## Test Approach
pytest test_todo.py

### Tasks
- Add toggle route
- Add CSS class for completed tasks
