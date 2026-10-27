# Issue

- Issue ID: SPEC-ISSUE-0001
- Title: Ensure QA checks test suite run locally before marking Tested
- Status: Ready
- Priority: Must
- Owner: QA
- Last Updated: 2026-10-27

## Overview
Ensure QA checks test suite run locally before marking Tested to catch integration/ID mismatches early.

## Acceptance Criteria
- Given a test suite exists, when QA checks the stories, then QA runs the local test suite and verifies it passes before marking Tested.

## Notes


## Test Approach
pytest

### Tasks
- Create test file
- Run tests
