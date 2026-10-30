# Issue

- Issue ID: SPEC-ISSUE-0002
- Title: GitHub pull request review API prevents authors from self-approving PRs when acting across roles in automated runs.
- Status: Ready
- Priority: Must
- Owner: Architect
- Last Updated: 2026-10-30

## Overview
GitHub pull request review API prevents authors from self-approving PRs when acting across roles in automated runs.

## Acceptance Criteria
- Given an automated run where agents act across roles, When a PR is reviewed, Then authorization checks do not prevent merging due to author self-approval limitations.

## Notes


## Test Approach
Confirm PR comment sign-offs work correctly.

### Tasks
- Log decision for SPEC-ISSUE-0002
