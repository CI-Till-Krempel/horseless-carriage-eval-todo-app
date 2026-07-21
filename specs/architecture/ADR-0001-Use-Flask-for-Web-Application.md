# Architecture Decision Record (ADR)

<!-- AGENT SAFEGUARD: Do NOT implement or fill out this template file directly. -->
<!-- This is a blueprint. Always create a new file (e.g., ADR-0001-My-Decision.md) for actual content. -->

- ADR-ID: ADR-0001
- Title: Use Flask for Web Application
- Status: Accepted
- Date: 2026-07-21
- Owners: DevTeam

## Context
Need to choose a web framework for the To-Do list application. Constraints are: web UI required, single-user, no authentication, locally running.

## Decision
Use Python with the Flask framework and Jinja2 templates. Store data in-memory during the development phase, with a simple file-based JSON storage planned for subsequent sprints if needed.

## Options Considered
- Option A — pros/cons
- Option B — pros/cons
- Option C — pros/cons

## Consequences
Flask is lightweight, has a large ecosystem, and is easy to set up for a single-user application. No complex ORM needed for the initial in-memory persistence.

## References
- Links to related PRs, stories, requirements
- Diagrams or documents
