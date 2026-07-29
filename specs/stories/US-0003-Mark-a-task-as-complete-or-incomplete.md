# User Story

- Story ID: US-0003
- Title: Mark a task as complete or incomplete
- Status: Draft
- Priority: P0
- Owner: Scrum Team
- Last Updated: 2026-07-29

## As a user, I want to mark a task as complete or incomplete so that I can track my progress.

## Acceptance Criteria
- - Given a task exists in a list, When the user clicks to mark it complete/incomplete, Then its status toggles and is visually updated.

## Notes
Users can toggle task completion status with visual feedback.

## Test Approach
Run pytest to verify task completion toggle and test suite.

### Tasks
- 1. Verify task toggle route and UI button
- 2. Add test case verifying task completion toggle in test_app.py
- 3. Run pytest
