# Architecture Decision Record (ADR)

- ADR-ID: ADR-0001
- Title: Use SQLite for Local Persistence
- Status: Accepted
- Date: 2026-07-24
- Owners: Architect

## Context
Sprint 1 requires a persistence approach for the To-Do List Web App. We need to decide between in-memory storage, file-based SQLite, or an external database.

## Decision
Use SQLite (`todo.db`) as the local file-based database backend for state persistence.

## Options Considered
- Option A — pros/cons
- Option B — pros/cons
- Option C — pros/cons

## Consequences
- Zero external database services needed; extremely fast setup.
- File-based SQLite (`todo.db`) preserves state across application restarts during local evaluation.
- SQLite connection management must be carefully handled to avoid leaks.

## References
- Links to related PRs, stories, requirements
- Diagrams or documents
