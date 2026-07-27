# User Story

- Story ID: US-0010
- Title: Local JSON file persistence
- Status: Ready
- Priority: P1
- Owner: Scrum Team
- Last Updated: 2026-07-27

## As a single user, I want persistent storage using a local JSON file so that my lists and tasks are not lost when the application restarts.

## Acceptance Criteria
- Given the application is running, When lists and tasks are created, updated, or deleted, Then state is automatically persisted to a local JSON file and retained across application restarts.

## Notes
Data persists across server restarts via local JSON file storage.

## Test Approach
Pytest tests verifying persistence across state loads.

### Tasks
- Add load/save JSON helper functions in app.py
- Update all CRUD routes to load and save state to todos.json
- Add unit tests verifying persistence across app re-initialization
- Commit and create PR
