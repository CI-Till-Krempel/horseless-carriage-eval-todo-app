# Architecture Decision Record (ADR)

- ADR-ID: ADR-0001
- Title: Use SQLite for Local Data Persistence
- Status: Accepted
- Date: 2026-10-05
- Owners: Architect

## Context
We need a persistence strategy for the to-do list web app that works locally out of the box without requiring external database services.

## Decision
Use SQLite with Python's built-in sqlite3 library or SQLAlchemy for local lightweight persistence.

## Options Considered
- Option A — pros/cons
- Option B — pros/cons
- Option C — pros/cons

## Consequences
Ensures data persists across server restarts while keeping deployment extremely simple and self-contained without needing a separate database server.

## References
- Links to related PRs, stories, requirements
- Diagrams or documents
