# User Story

- Story ID: US-003
- Title: Mark a task as complete or incomplete
- Status: Implemented
- Priority: P1
- Owner: Scrum Team
- Last Updated: 2026-09-30

## As a user, I want to mark a task as complete or incomplete so that I can monitor task progress.

## Acceptance Criteria
- Given a task in a list, When the user clicks the complete/incomplete toggle, Then its completion status updates visually and in storage.

## Notes
Allows tracking progress on individual items.
- Dependencies: ['US-002']

## Test Approach
Existing pytest suite covers task completion toggle.
