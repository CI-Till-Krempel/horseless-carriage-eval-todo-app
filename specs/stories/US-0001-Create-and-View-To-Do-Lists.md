# User Story

- Story ID: US-0001
- Title: Create and View To-Do Lists
- Status: Implemented
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-10-01

## As a user, I want to create a new to-do list with a name and view all my lists so that I can organize my tasks into separate categories.

## Acceptance Criteria
- Given the user is on the home page, When they enter a list name and click create, Then a new to-do list is created and displayed in the list of all lists.
- Given the user has created lists, When they view the home page, Then all created to-do lists are listed with links to view their tasks.

## Notes
Users can successfully group tasks by creating distinct lists and viewing them.

## Test Approach
Use pytest and Flask test client to verify list creation and rendering.

### Tasks
- Create requirements.txt with Flask and pytest
- Create app.py with SQLAlchemy models for List and Task
- Create home template for listing and creating lists
- Write unit tests for list creation and viewing
