# Architecture Decision Record (ADR)

- ADR-ID: ADR-0002
- Title: Nested Task Representation in Memory
- Status: Accepted
- Date: 2026-07-27
- Owners: Architect

## Context
We need to decide how tasks are associated with lists in memory for US-0002.

## Decision
Nest tasks within the corresponding list dictionary in the in-memory lists collection.

## Options Considered
- Option A — pros/cons
- Option B — pros/cons
- Option C — pros/cons

## Consequences
Tasks are stored as dictionaries within a list attribute of each to-do list dictionary, keeping lookups fast and straightforward without requiring an external database.

## References
- Links to related PRs, stories, requirements
- Diagrams or documents
