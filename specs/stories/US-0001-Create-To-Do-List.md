# User Story

- Story ID: US-0001
- Title: Create To-Do List
- Status: Accepted
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-10-09

## As a user, I want to create a new to-do list with a name so that I can organize my tasks.

## Acceptance Criteria
- Given the user is on the home page, When they enter a list name and click create, Then a new to-do list is created and displayed.

## Notes
Users can create lists to categorize their tasks.

## Test Approach
Write pytest test suite covering list creation, task addition, completion toggling, deletion of tasks and lists, and overview rendering.

### Tasks
- Initialize Flask app and SQLAlchemy models
- Implement list creation (US-0001)
- Implement task addition (US-0002)
- Implement task completion toggle (US-0003)
- Implement task deletion (US-0004)
- Implement list deletion (US-0005)
- Implement overview page (US-0006)
- Write tests and verify build
