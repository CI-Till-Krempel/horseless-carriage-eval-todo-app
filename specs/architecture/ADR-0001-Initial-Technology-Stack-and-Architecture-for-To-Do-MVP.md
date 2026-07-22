# Architecture Decision Record (ADR)

<!-- AGENT SAFEGUARD: Do NOT implement or fill out this template file directly. -->
<!-- This is a blueprint. Always create a new file (e.g., ADR-0001-My-Decision.md) for actual content. -->

- ADR-ID: ADR-0001
- Title: Initial Technology Stack and Architecture for To-Do MVP
- Status: Approved
- Date: 2026-07-22
- Owners: Architect

## Context
Sprint 1 of To-Do List Web App. We need to choose a stack and architecture that enables rapid delivery of a working web UI and core CRUD operations within a 5-sprint budget without unnecessary deployment or auth complexity.

## Decision
We choose Python with FastAPI (or Flask) and a lightweight HTML/CSS/JS frontend (or Jinja2 templates) storing data in-memory or a local SQLite database. SQLite/in-memory provides zero-friction local execution while maintaining clean separation of concerns.

## Options Considered
- Option A — pros/cons
- Option B — pros/cons
- Option C — pros/cons

## Consequences
Fast setup, zero external dependencies to configure, fully testable locally in browser or via test suite. State resets on server restart, which is acceptable for single-user session-scoped MVP.

## References
- Links to related PRs, stories, requirements
- Diagrams or documents
