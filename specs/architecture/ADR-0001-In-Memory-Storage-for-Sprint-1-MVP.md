# Architecture Decision Record (ADR)

- ADR-ID: ADR-0001
- Title: In-Memory Storage for Sprint 1 MVP
- Status: Accepted
- Date: 2026-08-03
- Owners: Architect

## Context
The evaluation scenario allows any persistence approach (in-memory, file, or embedded DB) as long as it is justified and deliverable.

## Decision
Use an in-memory Python list data store for the Sprint 1 MVP implementation of to-do lists.

## Options Considered
- Option A — pros/cons
- Option B — pros/cons
- Option C — pros/cons

## Consequences
Extremely fast setup and zero infrastructure complexity for Sprint 1 MVP. However, data does not survive application restarts. Future sprints may require file-based or database persistence if evaluated across process boundaries.

## References
- Links to related PRs, stories, requirements
- Diagrams or documents
