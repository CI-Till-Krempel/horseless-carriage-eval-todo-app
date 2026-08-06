# Architecture Decision Record (ADR)

- ADR-ID: ADR-0001
- Title: In-Memory Storage for Sprint 1 MVP
- Status: Accepted
- Date: 2026-08-06
- Owners: Architect

## Context
Sprint 1 requires building a to-do list web app MVP with session/in-memory persistence or simple local storage per constraints.

## Decision
Use an in-memory dictionary store (`todos_db`) in Python Flask for Sprint 1 data management.

## Options Considered
- Option A — pros/cons
- Option B — pros/cons
- Option C — pros/cons

## Consequences
In-memory dictionary storage simplifies local deployment and testing without external database dependencies, satisfying MVP requirements. However, data is ephemeral and will reset on application restart.

## References
- Links to related PRs, stories, requirements
- Diagrams or documents
