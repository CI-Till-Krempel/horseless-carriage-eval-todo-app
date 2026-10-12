# User Story

- Story ID: US-0006
- Title: Persistent storage across application restarts
- Status: Ready
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-10-12

## As a user, I want my lists and tasks to persist across application restarts so that I do not lose data.

## Acceptance Criteria
- Given the app is running, When lists and tasks are modified, Then state is automatically saved to a local storage file (JSON/SQLite) so data persists across application restarts.

## Notes
Data survives application restart.
- 🚫 BLOCKED (technical) - raised by DevTeam: US-0004 state ordering conflict is blocking US-0006 from starting. How can we bypass or resolve this sequential backlog requirement?

## Test Approach
Pytest testing of persistence serialization and reloading.

### Tasks
- Add load/save JSON helper functions in app.py
- Load lists and tasks from JSON file on app startup
- Save lists and tasks to JSON file after mutations
- Add automated test for persistence across restarts
