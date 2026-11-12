# Architecture Decision Record (ADR)

- ADR-ID: ADR-0001
- Title: Tech Stack and Persistence Selection
- Status: Accepted
- Date: 2026-11-12
- Owners: Architect

## Context
We need a simple, reliable stack and persistence model for a single-user to-do list web app that can be delivered within 5 sprints and run locally without complex setup.

## Decision
Use Python with Flask and SQLite for backend and persistence, paired with a simple server-rendered or lightweight frontend UI.

## Options Considered
- Option A — pros/cons
- Option B — pros/cons
- Option C — pros/cons

## Consequences
Enables rapid implementation with zero external database server setup, ensuring a straightforward local run experience for evaluators.

## References
- Links to related PRs, stories, requirements
- Diagrams or documents
