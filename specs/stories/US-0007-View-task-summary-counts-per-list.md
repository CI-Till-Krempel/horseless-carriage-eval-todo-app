# User Story

- Story ID: US-0007
- Title: View task summary counts per list
- Status: Reviewed
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-10-30

## As a user, I want to see a summary count of tasks and completed tasks for each list on the main view so that I can track progress at a glance.

## Acceptance Criteria
- Given the user is viewing the list of to-do lists, When they look at the list details, Then they see a count of total tasks and completed tasks for each list.

## Notes


## Test Approach
pytest unit tests verifying task counts per list.

### Tasks
- Update or create app.py with task count queries/properties
- Update templates/index.html to display task summary counts
- Write unit and integration tests for summary counts
