# Architecture Decision Record (ADR)

- ADR-ID: ADR-0001
- Title: Flask In-Memory Architecture for MVP
- Status: Accepted
- Date: 2026-07-27
- Owners: Architect

## Context
We need a persistence and architecture approach for the To-Do List Web App MVP that fits within the single-user, no authentication, session-scoped constraints without over-engineering.

## Decision
Use Python Flask with server-rendered Jinja2 HTML templates and an in-memory dictionary store for lists and tasks.

## Options Considered
- Option A — pros/cons
- Option B — pros/cons
- Option C — pros/cons

## Consequences
Simple and fast setup with zero external DB dependencies, perfectly fitting single-user session constraints. Data resets when the server restarts, which is acceptable for the MVP scope.

## References
- Links to related PRs, stories, requirements
- Diagrams or documents
