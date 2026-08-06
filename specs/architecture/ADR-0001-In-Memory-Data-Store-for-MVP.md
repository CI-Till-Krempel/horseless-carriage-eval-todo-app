# Architecture Decision Record (ADR)

- ADR-ID: ADR-0001
- Title: In-Memory Data Store for MVP
- Status: Accepted
- Date: 2026-08-06
- Owners: Architect

## Context
The MVP requires managing to-do lists and tasks without a complex multi-user authentication system or heavy external database.

## Decision
Use an in-memory data store with thread-safe data structures in Python for Sprint 1, with optional JSON persistence if needed later.

## Options Considered
- Option A — pros/cons
- Option B — pros/cons
- Option C — pros/cons

## Consequences
- Keeps dependencies low and eliminates external database setup overhead.
- Meets the core requirement of session persistence for the MVP scenario.
- Easily testable via unit tests.

## References
- Links to related PRs, stories, requirements
- Diagrams or documents
