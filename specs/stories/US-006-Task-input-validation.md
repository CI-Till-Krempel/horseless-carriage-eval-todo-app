# User Story

- Story ID: US-006
- Title: Task input validation
- Status: Ready
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-08-06

## As a user, I want validation on task and list creation, so that I do not accidentally create empty items.

## Acceptance Criteria
- Given a user adds a task without text, When they submit, Then an appropriate validation message is shown and the task is not created.

## Notes
Prevents empty tasks and lists from cluttering the app.

## Test Approach
Test validation error responses via test client.
