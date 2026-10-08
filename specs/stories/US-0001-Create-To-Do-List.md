# User Story

- Story ID: US-0001
- Title: Create To-Do List
- Status: Ready
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-10-08

## As a user, I want to create a new to-do list with a name so that I can organize my tasks.

## Acceptance Criteria
- Given the user is on the home page, When they enter a list name and submit, Then a new to-do list is created and displayed.

## Notes
Allows users to start organizing work by category or project.

## Test Approach
Write pytest unit tests for creating a list via the web route/API and verifying database persistence.

### Tasks
- Initialize Flask app and database models
- Create home page template for viewing and creating lists
- Add tests for list creation
