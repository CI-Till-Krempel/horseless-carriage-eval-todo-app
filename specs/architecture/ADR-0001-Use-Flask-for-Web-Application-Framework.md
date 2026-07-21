# Architecture Decision Record (ADR)

<!-- AGENT SAFEGUARD: Do NOT implement or fill out this template file directly. -->
<!-- This is a blueprint. Always create a new file (e.g., ADR-0001-My-Decision.md) for actual content. -->

- ADR-ID: ADR-0001
- Title: Use Flask for Web Application Framework
- Status: Proposed
- Date: 2026-07-21
- Owners: DevTeam

## Context
We need a web framework to build the To-Do List application. The requirements are simple (single user, local run) and we have a strict 5-sprint timeframe. We need something that allows us to move fast and maintain high quality.

## Decision
We will use Flask (Python) as our primary web framework. It is easy to set up, flexible, and sufficient for this requirement. We will store data in-memory initially, with an option to persist to a JSON file if required in later sprints.

## Options Considered
- Option A — pros/cons
- Option B — pros/cons
- Option C — pros/cons

## Consequences
Using Flask provides a lightweight and quick path for building web applications in Python, which is well-suited for a small-scale, 5-sprint project. It allows us to keep the codebase simple without the overhead of larger frameworks, while still providing robust enough features for UI rendering and basic state management.

## References
- Links to related PRs, stories, requirements
- Diagrams or documents
