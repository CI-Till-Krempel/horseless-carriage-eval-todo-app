# Architecture Decision Record (ADR)

- ADR-ID: ADR-0001
- Title: Tech Stack Selection: Flask, SQLite, and Vanilla Web UI
- Status: Accepted
- Date: 2026-07-31
- Owners: DevTeam

## Context
We need to select a tech stack for the To-Do List Web App MVP that can be delivered quickly and reliably within a 5-sprint budget, with a working web UI and local persistence.

## Decision
We choose Python with Flask, SQLite (via SQLAlchemy or sqlite3), and simple HTML/CSS/JS templates for the web UI. This allows rapid development, simple local execution, and robust persistence.

## Options Considered
- Option A — pros/cons
- Option B — pros/cons
- Option C — pros/cons

## Consequences
- Simple and self-contained web app.
- Python ecosystem provides robust web frameworks and easy testing.
- Easy to run locally with simple requirements.txt.

## References
- Links to related PRs, stories, requirements
- Diagrams or documents
