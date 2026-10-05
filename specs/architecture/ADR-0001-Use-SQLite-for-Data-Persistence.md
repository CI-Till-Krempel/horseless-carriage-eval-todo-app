# Architecture Decision Record (ADR)

- ADR-ID: ADR-0001
- Title: Use SQLite for Data Persistence
- Status: Accepted
- Date: 2026-10-05
- Owners: Architect

## Context
The application needs to store lists and tasks. We evaluated in-memory storage vs. SQLite.

## Decision
Use SQLite with Flask-SQLAlchemy for data persistence.

## Options Considered
- Option A — pros/cons
- Option B — pros/cons
- Option C — pros/cons

## Consequences
Using SQLite via Flask-SQLAlchemy allows data to persist across server restarts, meeting the evaluation criteria robustly while remaining extremely easy to run locally without external database setup.

## References
- Links to related PRs, stories, requirements
- Diagrams or documents
