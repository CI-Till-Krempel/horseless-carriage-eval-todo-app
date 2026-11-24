# User Story

- Story ID: US-0002
- Title: Implement Data Model for Lists and Tasks
- Status: Ready
- Priority: Must
- Owner: Scrum Team
- Last Updated: 2026-11-24

## As the system, I need a data model that represents lists (with names) and tasks (with text and completion status), so that the app can store and retrieve this data.

## Acceptance Criteria
- List entity has id and name
- Task entity has id, text, completion status, and belongs to a list
- Create operations work for both lists and tasks
- Data persists according to chosen strategy
- Data model supports all required operations (read, update, delete)

## Notes
Core data layer is in place for all other features to build on

## Test Approach
Unit tests for all CRUD operations using pytest

### Tasks
- Define List entity with id and name
- Define Task entity with id, text, completed status, and list_id
- Implement DataStore class with in-memory storage
- Implement CRUD methods for lists and tasks
- Write unit tests for data model
- Test cascade deletion (delete list → delete all tasks)
