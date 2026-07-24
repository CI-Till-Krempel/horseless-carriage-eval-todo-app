# Architecture Decision Record (ADR)

- ADR-ID: ADR-0001
- Title: Technology Stack and Persistence Strategy
- Status: Accepted
- Date: 2026-07-24
- Owners: Architect

## Context
We are building a to-do list web application as an MVP across 5 sprints. We need to choose the technology stack, architecture, and data persistence approach.

## Decision
Use a Python-based backend (Flask or FastAPI) with a clean HTML/CSS/JS frontend (or templates) and simple JSON/in-memory persistence suitable for single-user local usage.

## Options Considered
- Option A — pros/cons
- Option B — pros/cons
- Option C — pros/cons

## Consequences
Enables rapid iteration with clean, testable separation of concerns. Using a lightweight web framework (e.g. Flask or FastAPI) with in-memory or JSON file persistence keeps deployment and local running trivial while satisfying all MVP requirements.

## References
- Links to related PRs, stories, requirements
- Diagrams or documents
