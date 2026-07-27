# User Story

- Story ID: US-0007
- Title: Input validation for list creation
- Status: Ready
- Priority: P0
- Owner: Scrum Team
- Last Updated: 2026-07-27

## As a single user, I want input validation for list creation so that I do not accidentally create empty or blank list names.

## Acceptance Criteria
- Given the user submits an empty or whitespace-only list name, When the form is submitted, Then a user-friendly validation error message is displayed and no empty list is created.

## Notes
Users receive clear validation feedback when attempting to create blank lists.

## Test Approach
Pytest tests verifying flash messages and rejection of blank submissions.

### Tasks
- Implement validation in create_list and add_task routes
- Add flash message banner in templates/index.html
- Add unit tests for validation error scenarios
- Commit changes and create PR
