# Architecture Decision Record (ADR)

- ADR-ID: ADR-0001
- Title: Flask and SQLite Backend Architecture
- Status: Accepted
- Date: 2026-07-29
- Owners: Architect

## Context
Sprint 1 of the To-Do List Web App evaluation requires establishing the core application architecture, persistence model, and UI framework.

## Decision
Adopt Python with Flask as the web framework and SQLite via Python's built-in `sqlite3` module as the data store for the MVP.

## Options Considered
- Option A — pros/cons
- Option B — pros/cons
- Option C — pros/cons

## Consequences
Using Flask and SQLite provides a lightweight, dependency-free (standard library sqlite3) backend with zero external database server requirements, perfectly fitting the single-user local evaluation constraints. It enables rapid feature development and simple testing via pytest.

## References
- Links to related PRs, stories, requirements
- Diagrams or documents
