# User Story

- Story ID: US-0002
- Title: Add Task to List
- Status: Reviewed
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-11-02

## As a user, I want to add a task to a list with a short text description so that I can track what needs to be done.

## Acceptance Criteria
- Given a to-do list exists, When the user adds a task with a description, Then the task appears under that list.

## Notes

- ⚠️ REVIEW DENIED at Tested by QA: Automated test suite reports 5 failing tests (including test_add_task_form and multiple regressions in test_app.py). DevTeam needs to fix these test failures before US-0002 can pass the Tested stage.
- 🚫 BLOCKED (technical) - raised by QA: advance_story_stage('US-0002', 'Tested') has been rejected 3 times in a row for the same reason - most recently: Cannot mark 'US-0002' Tested - posting the review via gh_pr_review failed: failed to create review: GraphQL: Review Can not approve your own pull request (addPullRequestReview)

## Test Approach
Pytest integration tests for task creation

### Tasks
- Implement task addition route/logic
- Add unit and integration tests
- Verify CI checks passing
