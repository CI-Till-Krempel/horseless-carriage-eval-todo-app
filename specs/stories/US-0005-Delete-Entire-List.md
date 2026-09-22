# User Story

- Story ID: US-0005
- Title: Delete Entire List
- Status: Implemented
- Priority: P0
- Owner: Scrum Team
- Last Updated: 2026-09-22

## As a user, I want to delete an entire list and its tasks so that I can clean up old lists.

## Acceptance Criteria
- Given a to-do list with or without tasks exists, When the user clicks delete on the list, Then the list and all its contained tasks are removed.

## Notes
Users can clean up whole lists and associated tasks.

## Test Approach
Pytest unit test for list cascade deletion.
