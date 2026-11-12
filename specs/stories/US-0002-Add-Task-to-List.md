# User Story

- Story ID: US-0002
- Title: Add Task to List
- Status: Reviewed
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-11-12

## As a user, I want to add a task to a list with a short text description so that I can track what needs to be done.

## Acceptance Criteria
- Given an existing to-do list, When the user adds a task with a text description, Then the task appears within that list.

## Notes
Users can break down their lists into actionable task items.
- ⚠️ REVIEW DENIED at Tested by QA: Unit test test_add_task failed: 'Finish report' was not found in response data when adding a task to list 1 because the list ID generated was '1' but global counters or list indexing logic caused a mismatch or re-created list in fixture without clearing task state properly.

## Test Approach
Add pytest test case for adding tasks to a list.
