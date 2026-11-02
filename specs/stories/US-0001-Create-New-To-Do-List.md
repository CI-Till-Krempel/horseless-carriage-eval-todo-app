# User Story

- Story ID: US-0001
- Title: Create New To-Do List
- Status: Implemented
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-11-02

## As a user, I want to create a new to-do list with a name so that I can organize my tasks.

## Acceptance Criteria
- Given the user is on the home page, When they enter a list name and click create, Then a new to-do list is created and displayed.

## Notes
Allows users to start organizing their tasks into named lists.

## Test Approach
Write pytest tests testing the Flask test client for creating a new list.

### Tasks
- Initialize Flask app and requirements.txt
- Implement create list route and form in index.html
- Write pytest unit tests for list creation
