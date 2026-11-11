# Issue

- Issue ID: SPEC-ISSUE-0001
- Title: Maintain robust test ID management and avoid hardcoded assumptions in test suites.
- Status: Tested
- Priority: Must
- Owner: DevTeam
- Last Updated: 2026-11-11

## Overview
Maintain robust test ID management and avoid hardcoded assumptions in test suites.

## Acceptance Criteria
- Given a test suite running against the app, When tests execute, Then test IDs and locators are robust and do not rely on hardcoded fragile assumptions that break across iterations.

## Notes


## Test Approach
Run pytest across the test suite to ensure robust execution without brittle ID assumptions.

### Tasks
- Review existing test suite for hardcoded IDs/locators
- Implement robust test ID management helper or conventions
- Verify all tests pass successfully
