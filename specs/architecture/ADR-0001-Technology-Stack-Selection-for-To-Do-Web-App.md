# Architecture Decision Record (ADR)

<!-- AGENT SAFEGUARD: Do NOT implement or fill out this template file directly. -->
<!-- This is a blueprint. Always create a new file (e.g., ADR-0001-My-Decision.md) for actual content. -->

- ADR-ID: ADR-0001
- Title: Technology Stack Selection for To-Do Web App
- Status: Proposed
- Date: 2026-07-21
- Owners: Architect

## Context
We need to build a simple to-do list web application as part of a 5-sprint evaluation. We need a stack that is easy to implement and maintain.

## Decision
We will use Python with Flask for the backend, Jinja2 for templating, and standard HTML/CSS/JS for the frontend. We will use an in-memory data store for this sprint, with the option to move to a file-based storage or SQLite in future sprints if needed.

## Options Considered
- Option A — pros/cons
- Option B — pros/cons
- Option C — pros/cons

## Consequences
Using a lightweight Python-based stack will allow for fast development and easy deployment for a local evaluation. We will use Flask as it is simple and well-documented for small web applications. Data will be stored in-memory initially for simplicity as per the project constraints.

## References
- Links to related PRs, stories, requirements
- Diagrams or documents
