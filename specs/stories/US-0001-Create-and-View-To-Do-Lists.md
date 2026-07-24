# User Story

- Story ID: US-0001
- Title: Create and View To-Do Lists
- Status: Ready
- Priority: P0
- Owner: Scrum Team
- Last Updated: 2026-07-24

## As a user, I want to create a new to-do list with a name and see all my lists so that I can organize my tasks into categories.

## Acceptance Criteria
- Given the user is on the home page, When they enter a list name and click create, Then a new to-do list is created and displayed.
- Given lists exist, When the user views the home page, Then they see all their lists.

## Notes
Users can successfully create and view separate lists.

## Test Approach
Pytest tests checking Flask test client endpoints for listing and creating to-do lists.
