# Architecture Decision Record (ADR)

- ADR-ID: ADR-0001
- Title: Use Python Flask and SQLite for To-Do List Web App MVP
- Status: Accepted
- Date: 2026-07-22
- Owners: DevTeam

## Context
We need a simple web app stack that can be set up and run easily by anyone cloning the repository, with minimal dependencies.

## Decision
Use Python with Flask and SQLite (or simple in-memory/JSON storage) with a clean HTML/CSS/JS frontend served directly by Flask.

## Options Considered
- Option A — pros/cons
- Option B — pros/cons
- Option C — pros/cons

## Consequences
Fast startup, zero setup for users, lightweight, fully fulfills local run requirement for single-user web app without database complexity.

## References
- Links to related PRs, stories, requirements
- Diagrams or documents
