# Product Roadmap

Use this living roadmap to plan releases and track user stories across states. It doubles as a lightweight task board and a release planning tool.

## How to use
- Story IDs should match files in `specs/stories/` (e.g., `ST-001` corresponds to `specs/stories/ST-001-some-title.md`).
- Move story references between states as work progresses.
- Keep titles short; full details live in the story file.
- For each planned version, list goals and the set of stories targeted for that release.
- When a release is cut, freeze the section by adding the actual tag (e.g., `v0.1.0`) and dates.

Legend
- `[ST-###] Title` → a user story reference and its short title
- Checkbox states: `- [ ]` To Do, `- [~]` In Progress (use `- [~]` to signal WIP), `- [R]` In Review, `- [x]` Done

Tip: If you prefer standard checkboxes only, use the Kanban tables below and keep raw lists unchecked.

---

## Release plan (versions → stories)

### v0.1 — MVP (target: YYYY-MM)
Goals

Stories:

### v0.2 — Next iteration (target: YYYY-MM)
Goals

Stories

### Backlog (unplanned)


Stories
- [US-0001] US-0001: Create and view to-do lists
  - [x] DRAFT
  - [x] READY
  - [x] IMPLEMENTED
  - [x] REVIEWED
  - [ ] TESTED
  - [ ] ACCEPTED
- [US-0002] US-0002: Add tasks to a to-do list
  - [ ] DRAFT
  - [ ] READY
  - [ ] IMPLEMENTED
  - [ ] REVIEWED
  - [ ] TESTED
  - [ ] ACCEPTED
---

### v0.1.0
Goals
- Establish project architecture and data model
- Implement core To-Do List creation and task management UI/backend for Sprint 1

Stories
- [US-0001: Create and view to-do lists] US-0001: Create and view to-do lists
  - [ ] DRAFT
  - [ ] READY
  - [ ] IMPLEMENTED
  - [ ] REVIEWED
  - [ ] TESTED
  - [ ] ACCEPTED
- [US-0002: Add tasks to a to-do list] US-0002: Add tasks to a to-do list
  - [ ] DRAFT
  - [ ] READY
  - [ ] IMPLEMENTED
  - [ ] REVIEWED
  - [ ] TESTED
  - [ ] ACCEPTED


### v0.2.0
Goals
- Implement task completion toggling and task/list deletion features for Sprint 2

Stories
- [US-0003: Mark tasks as complete or incomplete] US-0003: Mark tasks as complete or incomplete
  - [ ] DRAFT
  - [ ] READY
  - [ ] IMPLEMENTED
  - [ ] REVIEWED
  - [ ] TESTED
  - [ ] ACCEPTED
- [US-0004: Delete tasks and entire lists] US-0004: Delete tasks and entire lists
  - [ ] DRAFT
  - [ ] READY
  - [ ] IMPLEMENTED
  - [ ] REVIEWED
  - [ ] TESTED
  - [ ] ACCEPTED


## Task board (Kanban)

Use either the per-version boards below or one global board; duplicate as needed for each active version.

### v0.1 Kanban

| To Do | In Progress | In Review | Done |
|------|-------------|-----------|------|

Notes
- Update this table in PRs alongside code changes.
- Keep the board limited to the current sprint scope if you’re also running sprints.

### v0.2 Kanban

| To Do | In Progress | In Review | Done |
|------|-------------|-----------|------|

---

## Cross-cutting initiatives (optional)
Track broader themes/epics that span multiple versions. Link constituent stories.

---

## Release checklist (for when cutting a release)
- [ ] All included stories are in `Done` and meet Definition of Done
- [ ] Docs updated (stories, PRD/SRS, ADRs as needed)
- [ ] Version/tag created (e.g., `v0.1.0`) and changelog drafted
- [ ] Known issues captured and follow-ups added to backlog

---

## Index of story references
Group story references by planned version for quick scanning.

- v0.1
- v0.2
- Unplanned

Replace placeholders with your actual story IDs and titles. Keep this file updated in the same PRs that move work forward.