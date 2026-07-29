# User Story

- Story ID: US-0006
- Title: View lists and tasks with visual distinction for completed items
- Status: Ready
- Priority: P0
- Owner: Scrum Team
- Last Updated: 2026-07-29

## As a user, I want to see all my lists and their tasks with completed tasks visually distinguished so that I have a clear overview of my work.

## Acceptance Criteria
- - Given multiple lists and tasks exist, When the user views the main application page, Then all lists and their tasks are displayed, with completed tasks visually distinguished (e.g., struck-through or grayed out) from incomplete ones.

## Notes
Users get a clear overview of all lists and tasks with visual distinction for completion.

## Test Approach
Run pytest to verify visual distinction and test suite.

### Tasks
- 1. Verify template and CSS styling for completed tasks
- 2. Add test case verifying completed task styling in test_app.py
- 3. Run pytest
