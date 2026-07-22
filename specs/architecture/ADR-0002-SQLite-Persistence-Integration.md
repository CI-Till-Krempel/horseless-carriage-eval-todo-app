# Architecture Decision Record (ADR)

- ADR-ID: ADR-0002
- Title: SQLite Persistence Integration
- Status: Accepted
- Date: 2026-07-22
- Owners: Architect

## Context
Sprint 1 used in-memory dictionary storage which resets on server restart. Sprint 2 requires robust data persistence per US-0007.

## Decision
Integrate SQLite for persistent storage of to-do lists and tasks.

## Options Considered
- Option A — pros/cons
- Option B — pros/cons
- Option C — pros/cons

## Consequences
Data survives application restarts using a standard local SQLite database accessed via Flask-SQLAlchemy or built-in sqlite3.

## References
- Links to related PRs, stories, requirements
- Diagrams or documents
