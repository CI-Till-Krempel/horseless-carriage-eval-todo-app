# User Story

- Story ID: US-0006
- Title: Implement Create List Form
- Status: Ready
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-11-24

## As a user, I want to create a new list by entering a name, so that I can organize my tasks into separate lists.

## Acceptance Criteria
- Form accepts a list name
- Form submits to backend via API
- New list appears in the lists view after creation
- User gets feedback (success/error) after submission
- Form can be opened from the home page

## Notes
User can create lists through the UI

## Test Approach
Manual testing - create lists via form, verify they appear

### Tasks
- Create HTML form for list name input
- Implement form submission handler
- POST to /api/lists with list name
- Handle success/error responses
- Add form validation (non-empty, length check)
- Close form and refresh lists view after success
- Show error messages to user
