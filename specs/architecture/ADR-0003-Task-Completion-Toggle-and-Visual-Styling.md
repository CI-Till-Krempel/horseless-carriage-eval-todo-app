# Architecture Decision Record (ADR)

- ADR-ID: ADR-0003
- Title: Task Completion Toggle and Visual Styling
- Status: Accepted
- Date: 2026-07-27
- Owners: Architect

## Context
We need to establish how task completion state is mutated and visually represented for US-0003.

## Decision
Use a dedicated toggle route `/lists/<list_id>/tasks/<task_id>/toggle` and conditional CSS class binding for completed task rendering.

## Options Considered
- Option A — pros/cons
- Option B — pros/cons
- Option C — pros/cons

## Consequences
Toggle action updates the boolean `completed` flag on the task dictionary in-memory and re-renders the UI with corresponding CSS class application.

## References
- Links to related PRs, stories, requirements
- Diagrams or documents
