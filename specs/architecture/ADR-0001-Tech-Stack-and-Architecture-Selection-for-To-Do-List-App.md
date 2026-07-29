# Architecture Decision Record (ADR)

- ADR-ID: ADR-0001
- Title: Tech Stack and Architecture Selection for To-Do List App
- Status: Accepted
- Date: 2026-07-29
- Owners: Architect

## Context
We need to choose a technology stack and data persistence strategy for the To-Do List Web App within a 5-sprint budget and single-user constraint.

## Decision
We will use Python with Flask for the web backend, lightweight in-memory storage (backed optionally by JSON file serialization if needed) for session persistence, and server-rendered HTML with Tailwind CSS (or simple vanilla CSS/Bootstrap) for a clean, accessible web UI.

## Options Considered
- Option A — pros/cons
- Option B — pros/cons
- Option C — pros/cons

## Consequences
- Python/Flask (or FastAPI) offers rapid web UI prototyping with minimal boilerplate and robust JSON handling.
- In-memory data store for the evaluation MVP avoids database configuration overhead while meeting session persistence requirements.
- Simple HTML/CSS/JS frontend served directly by the backend ensures zero complex build tooling is needed for Sprint 1.

## References
- Links to related PRs, stories, requirements
- Diagrams or documents
