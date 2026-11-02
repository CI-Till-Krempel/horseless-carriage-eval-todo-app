# User Story

- Story ID: US-0001
- Title: Create To-Do List
- Status: Reviewed
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-11-02

## As a user, I want to create a new to-do list with a name so that I can organize my tasks.

## Acceptance Criteria
- Given the user is on the main page, When they enter a list name and click create, Then a new to-do list is created and displayed.

## Notes

- ⚠️ REVIEW DENIED at Tested by QA: Tests test_delete_task and test_delete_list still fail because when calling client.post with follow_redirects=True or standard test client requests, importing lists and tasks from app module references the global list object in test_app.py which may not reflect the app context state if app is reloaded or if multiple test clients/modules are used. Specifically, len(tasks) is 1 after deletion because tasks list in test scope was bound at import time.

## Test Approach
Use pytest and Flask test client to verify list creation endpoint and UI rendering.
