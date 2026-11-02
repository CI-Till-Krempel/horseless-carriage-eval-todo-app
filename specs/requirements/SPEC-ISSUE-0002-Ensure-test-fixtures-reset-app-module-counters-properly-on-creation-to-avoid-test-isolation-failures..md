# Issue

- Issue ID: SPEC-ISSUE-0002
- Title: Ensure test fixtures reset app module counters properly on creation to avoid test isolation failures.
- Status: Tested
- Priority: Must
- Owner: DevTeam
- Last Updated: 2026-11-02

## Overview
Ensure test fixtures reset app module counters properly on creation to avoid test isolation failures.

## Acceptance Criteria
- - Given test fixtures are created, When they are initialized, Then app module counters reset properly on creation to avoid test isolation failures.

## Notes


## Test Approach
Run pytest to ensure test isolation holds

### Tasks
- Inspect app module state initialization and test fixtures
- Update fixture creation to reset internal counters
