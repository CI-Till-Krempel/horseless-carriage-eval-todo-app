# Architecture Decision Record (ADR)

- ADR-ID: ADR-0001
- Title: JSON File Persistence for To-Do Lists and Tasks
- Status: Accepted
- Date: 2026-07-27
- Owners: Architect

## Context
The MVP to-do app currently uses volatile in-memory data structures, meaning all lists and tasks are lost when the Flask server restarts. We need a lightweight persistence mechanism that requires no external database setup.

## Decision
Use a local JSON file (`data.json`) to persist lists and tasks, loaded into memory on startup and saved on every mutation.

## Options Considered
- Option A — pros/cons
- Option B — pros/cons
- Option C — pros/cons

## Consequences
- Pros: Zero external database dependencies, easy to inspect and debug, robust across application restarts, fits within single-user no-auth scope.
- Cons: Not suited for concurrent multi-process writes without file locking (acceptable for single-user local web app).

## References
- Links to related PRs, stories, requirements
- Diagrams or documents
