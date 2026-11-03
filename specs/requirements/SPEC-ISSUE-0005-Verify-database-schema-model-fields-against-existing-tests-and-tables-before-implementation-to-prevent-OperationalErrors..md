# Issue

- Issue ID: SPEC-ISSUE-0005
- Title: Verify database schema model fields against existing tests and tables before implementation to prevent OperationalErrors.
- Status: Reviewed
- Priority: Must
- Owner: DevTeam
- Last Updated: 2026-11-03

## Overview
Verify database schema model fields against existing tests and tables before implementation to prevent OperationalErrors.

## Acceptance Criteria
- Given database schema updates, When model fields are added or modified, Then verify against existing tests and tables to prevent OperationalErrors.

## Notes

- ⚠️ REVIEW DENIED at Tested by QA: Test failed in test_schema_verification.py: assertion error during attribute verification. Please ensure the assertions correctly match the attributes defined on TodoList and Task models.
- 🚫 BLOCKED (technical) - raised by QA: advance_story_stage('SPEC-ISSUE-0005', 'Tested') has been rejected 3 times in a row for the same reason - most recently: Cannot mark 'SPEC-ISSUE-0005' Tested - 1 of 6 tests failed. Fix the failing tests before retrying.

pytest output (tail, last 2000 chars):
Alchemy and becomes a legacy construct in 2.0. The method is now available as Session.get() (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    rv = self.get(ident)

tests/test_us0003.py::test_toggle_task
  /app/eval-output/clone/tests/test_us0003.py:28: LegacyAPIWarning: The Query.get() method is considered legacy as of the 1.x series of SQLAlchemy and becomes a legacy construct in 2.0. The method is now available as Session.get() (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    updated_task = Task.query.get(task_id)

tests/test_us0004.py::test_delete_task
  /app/eval-output/clone/tests/test_us0004.py:28: LegacyAPIWarning: The Query.get() method is considered legacy as of the 1.x series of SQLAlchemy and becomes a legacy construct in 2.0. The method is now available as Session.get() (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    deleted_task = Task.query.get(task_id)

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
================================ tests coverage ================================
_______________ coverage: platform linux, python 3.11.18-final-0 _______________

Name                                Stmts   Miss  Cover
-------------------------------------------------------
app.py                                 52      1    98%
tests/test_schema_verification.py       9      4    56%
tests/test_todo.py                     30      0   100%
tests/test_us0003.py                   25      0   100%
tests/test_us0004.py                   25      0   100%
tests/test_workflow_adherence.py        2      0   100%
-------------------------------------------------------
TOTAL                                 143      5    97%
=========================== short test summary info ============================
FAILED tests/test_schema_verification.py::test_db_schema_verification - Asser...
1 failed, 5 passed, 4 warnings in 0.63s

## Test Approach
Pytest verification
