# User Story

- Story ID: US-0005
- Title: Delete an entire list
- Status: Ready
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-10-12

## As a user, I want to delete an entire list and its tasks so that I can clean up obsolete projects.

## Acceptance Criteria
- Given an existing list with tasks, When the user deletes the list, Then the list and all its contained tasks are removed.

## Notes
Users can delete lists and cascade delete their tasks.
- 🚫 BLOCKED (product) - raised by DevTeam: US-0005 is marked as Ready in the roadmap and specs, but the system workflow checks consider US-0005 unaccepted, preventing US-0006 from starting. How should we proceed with completing or re-verifying US-0005?

## Test Approach
Pytest testing of list and cascade task deletion.

### Tasks
- Add delete list endpoint with task cascade
- Update UI with delete list buttons
- Add automated test for list deletion
