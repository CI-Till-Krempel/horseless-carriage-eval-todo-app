# Architecture Decision Record (ADR)

- ADR-ID: ADR-0001
- Title: Python Flask and SQLite Stack
- Status: Accepted
- Date: 2026-10-09
- Owners: Architect

## Context
We need to choose a technology stack for the To-Do List Web App that satisfies the constraints of being a simple local web app with zero complex setup.

## Decision
Adopt Python, Flask, and SQLite/SQLAlchemy as the core technology stack for the application.

## Options Considered
- Option A — pros/cons
- Option B — pros/cons
- Option C — pros/cons

## Consequences
Using Flask with SQLite/SQLAlchemy provides a robust yet extremely lightweight architecture that requires zero external database servers, allowing the app to run instantly upon clone.

## References
- Links to related PRs, stories, requirements
- Diagrams or documents
