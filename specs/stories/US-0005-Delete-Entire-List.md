# User Story

- Story ID: US-0005
- Title: Delete Entire List
- Status: Reviewed
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-10-12

## As a user, I want to delete an entire list and its tasks so that I can clean up when a list is no longer needed.

## Acceptance Criteria
- Given an entire list with tasks, When the user clicks delete list, Then the list and all its tasks are deleted.

## Notes
Allows removal of entire completed or unneeded project lists.

## Test Approach
Test deleting an entire list and verifying all lists and tasks are correctly displayed.

### Tasks
- Implement delete_list route in app.py
- Add delete list button in templates/index.html
- Write pytest test for list deletion and full view dashboard
