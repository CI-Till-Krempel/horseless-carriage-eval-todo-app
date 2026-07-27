# User Story

- Story ID: US-0007
- Title: Persistent Storage of Lists and Tasks
- Status: Draft
- Priority: P0
- Owner: Scrum Team
- Last Updated: 2026-07-27

## As a user, I want my lists and tasks to be saved to disk so that I do not lose my data when the server restarts.

## Acceptance Criteria
- Given the application is running, When lists and tasks are created or modified, Then they are persisted to local storage (JSON file) so that data survives application restarts.

## Notes
Users retain their to-do lists and tasks across application restarts.

## Test Approach
Pytest unit tests verifying that data written via routes is correctly stored in `data.json` and reloaded.

### Tasks
- Add load_data and save_data helper functions reading/writing `data.json`
- Update Flask routes to persist changes immediately
- Add unit tests verifying data persistence across reloads
