# SPEC-ISSUE-0004: GraphQL API prevents self-approval on pull requests

- Status: Implemented
- Owner: ScrumMaster

## Description
GraphQL API prevents self-approval on pull requests, requiring comment overrides or admin merges.

## Resolution
Documented that comment-based sign-offs and human approval records via `record_human_approval` are used when self-approval restrictions are encountered.
