# User Story

- Story ID: US-0004
- Title: Delete a task
- Status: Accepted
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-11-11

## As a user, I want to delete a task so that I can remove items I no longer need.

## Acceptance Criteria
- Given a task in a list, When the user clicks delete on the task, Then the task is removed from the list.

## Notes
Users can clean up unwanted tasks.
- 🚫 BLOCKED (technical) - raised by ProductOwner: CHANGELOG.md uncommitted changes block checkout in create_release_pr.

## Test Approach
Pytest test for task deletion.

### Tasks
- Implement delete task backend route and frontend delete button.
