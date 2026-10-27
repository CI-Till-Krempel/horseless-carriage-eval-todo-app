# User Story

- Story ID: US-0002
- Title: US-02: Add Task to List
- Status: Reviewed
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-10-26

## As a user, I want to add a task to a list with a short text description so that I can track what needs to be done.

## Acceptance Criteria
- Given a to-do list exists, When the user enters a short text description and adds it to the list, Then the task appears under that list.

## Notes

- ⚠️ REVIEW DENIED at Tested by QA: pytest execution failed: tests/test_app.py has a failing test or assertion error.
- 🚫 BLOCKED (technical) - raised by QA: advance_story_stage('US-0002', 'Tested') has been rejected 3 times in a row for the same reason - most recently: Cannot mark 'US-0002' Tested - 1 of 3 tests failed. Fix the failing tests before retrying.

## Test Approach
Pytest with Flask test client

### Tasks
- Add task route
- Update template
- Add unit test
