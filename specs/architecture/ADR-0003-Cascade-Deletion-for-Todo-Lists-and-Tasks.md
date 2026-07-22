# Architecture Decision Record (ADR)

<!-- AGENT SAFEGUARD: Do NOT implement or fill out this template file directly. -->
<!-- This is a blueprint. Always create a new file (e.g., ADR-0001-My-Decision.md) for actual content. -->

- ADR-ID: ADR-0003
- Title: Cascade Deletion for Todo Lists and Tasks
- Status: Approved
- Date: 2026-07-22
- Owners: Architect

## Context
Sprint 3 delivers US-0005 (Delete Entire List and its Tasks). We need to verify that SQLAlchemy cascade delete behavior is correctly configured and fully tested.

## Decision
Use SQLAlchemy relationship configuration with `cascade="all, delete-orphan"` on the TodoList -> Tasks relationship, ensuring that deleting a TodoList automatically removes all child tasks.

## Options Considered
- Option A — pros/cons
- Option B — pros/cons
- Option C — pros/cons

## Consequences
Ensures cascade deletion of associated tasks when a list is deleted, maintaining referential integrity in SQLite and preventing orphaned task records.

## References
- Links to related PRs, stories, requirements
- Diagrams or documents
