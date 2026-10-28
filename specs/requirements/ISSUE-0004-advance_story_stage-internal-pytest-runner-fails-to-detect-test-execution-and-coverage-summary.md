# Issue

- Issue ID: ISSUE-0004
- Title: advance_story_stage internal pytest runner fails to detect test execution and coverage summary
- Status: Draft
- Priority: P0
- Owner: Scrum Team
- Last Updated: 2026-07-31

## Overview
The `advance_story_stage` tool runs pytest internally to verify test execution and coverage summary, but its environment or invocation command fails to discover tests or load configuration (like setup.cfg / pytest-cov), blocking stories at the Tested stage.

## Acceptance Criteria


## Notes


## Test Approach

