# Architecture Decision Record (ADR)

- ADR-ID: ADR-0001
- Title: Tech Stack and In-Memory Architecture for To-Do List App
- Status: Accepted
- Date: 2026-07-27
- Owners: Architect

## Context
We are building a To-Do List web application for a single user with no persistence requirement beyond the current session/process unless designed otherwise. We need to decide on the technology stack and architecture.

## Decision
We will use Python with Flask for the backend, an in-memory repository with optional JSON/file persistence for simplicity, and HTML/CSS/JavaScript with Tailwind CSS (via CDN) for the web UI.

## Options Considered
- Option A — pros/cons
- Option B — pros/cons
- Option C — pros/cons

## Consequences
Simple, low-friction, runs anywhere without DB setup. State resets on server restart, which is acceptable for single-user session demo per constraints.

## References
- Links to related PRs, stories, requirements
- Diagrams or documents
