# User Story

- Story ID: US-0003
- Title: Mark Task Complete or Incomplete
- Status: Reviewed
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-11-02

## As a user, I want to mark a task as complete or incomplete so that I can monitor my progress.

## Acceptance Criteria
- Given an existing task, When the user clicks complete/incomplete, Then the task status toggles and is visually distinct.

## Notes

- ⚠️ REVIEW DENIED at Tested by QA: Test suite still fails: tests/test_app.py raises AttributeError because it accesses flask_app.lists which does not exist in app.py.
- 🚫 BLOCKED (technical) - raised by QA: advance_story_stage('US-0003', 'Tested') has been rejected 3 times in a row for the same reason - most recently: Cannot mark 'US-0003' Tested - posting the review via gh_pr_review failed: failed to create review: GraphQL: Review Can not approve your own pull request (addPullRequestReview)

## Test Approach
Write pytest test cases checking task status toggle behavior.

### Tasks
- Add route for toggling task completion status
- Update frontend template to include toggle button/checkbox
- Add unit/integration test for toggling task status
