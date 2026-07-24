# Architecture Decision Record (ADR)

- ADR-ID: ADR-0001
- Title: In-Memory Storage for Sprint 1 MVP
- Status: Accepted
- Date: 2026-07-24
- Owners: Architect

## Context
Sprint 1 MVP requires establishing a backend storage mechanism for to-do lists and tasks while adhering strictly to a single-user, no-auth constraint.

## Decision
Use an in-memory Python dictionary storage structure within the Flask application for Sprint 1 MVP.

## Options Considered
- Option A — pros/cons
- Option B — pros/cons
- Option C — pros/cons

## Consequences
- Fast setup and easy local execution for evaluation.
- No database dependencies required for MVP.
- Data is volatile and lost upon server restart, which is acceptable for Sprint 1 MVP scope but must be addressed in subsequent sprints.

## References
- Links to related PRs, stories, requirements
- Diagrams or documents
