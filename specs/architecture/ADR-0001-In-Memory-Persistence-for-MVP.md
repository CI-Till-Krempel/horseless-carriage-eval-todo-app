# Architecture Decision Record (ADR)

- ADR-ID: ADR-0001
- Title: In-Memory Persistence for MVP
- Status: Accepted
- Date: 2026-07-27
- Owners: Architect

## Context
We need to choose a persistence layer for the to-do list web app for Sprint 1.

## Decision
Use a simple in-memory Python data structure (list/dict) in Flask for Sprint 1.

## Options Considered
- Option A — pros/cons
- Option B — pros/cons
- Option C — pros/cons

## Consequences
Fast development and simple setup. Data will not persist across server restarts, which is acceptable for Sprint 1 MVP.

## References
- Links to related PRs, stories, requirements
- Diagrams or documents
