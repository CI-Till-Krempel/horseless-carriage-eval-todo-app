# Architecture Decision Record (ADR)

- ADR-ID: ADR-0001
- Title: Technology Stack and Persistence Approach
- Status: Accepted
- Date: 2026-07-22
- Owners: Architect

## Context
We need to choose a technology stack and persistence mechanism for a single-user to-do list web application within a 5-sprint budget.

## Decision
Use Python with Flask and SQLite (or simple JSON file storage) for robust yet lightweight web UI and data management.

## Options Considered
- Option A — pros/cons
- Option B — pros/cons
- Option C — pros/cons

## Consequences
Ensures simplicity, zero installation friction, and rapid delivery. State persists in memory or simple local JSON file for the session.

## References
- Links to related PRs, stories, requirements
- Diagrams or documents
