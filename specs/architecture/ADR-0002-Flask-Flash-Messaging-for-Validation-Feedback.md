# Architecture Decision Record (ADR)

- ADR-ID: ADR-0002
- Title: Flask Flash Messaging for Validation Feedback
- Status: Accepted
- Date: 2026-07-27
- Owners: Architect

## Context
Sprint 2 introduces input validation and error feedback requirements (US-0007, US-0008). We need a consistent error messaging architecture for form submission rejections.

## Decision
Adopt Flask flash messaging and template conditional banners for user-facing input validation errors.

## Options Considered
- Option A — pros/cons
- Option B — pros/cons
- Option C — pros/cons

## Consequences
Using Flask's built-in `flash()` messaging system provides a lightweight, session-scoped mechanism for displaying error banners across form submissions without introducing heavy database or framework dependencies.

## References
- Links to related PRs, stories, requirements
- Diagrams or documents
