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

---

### v1.0.0
Goals
- Establish MVP architecture, core data structures, and foundational user stories (US-0001 to US-0006) for the To-Do List Web App.

Stories
- [US-0001] Create a new to-do list
  - [x] READY
  - [x] IMPLEMENTED
  - [x] REVIEWED
  - [x] TESTED
  - [x] ACCEPTED
- [US-0002] Add a task to a list
  - [ ] READY
  - [ ] IMPLEMENTED
  - [ ] REVIEWED
  - [ ] TESTED
  - [ ] ACCEPTED
- [US-0003] Mark a task as complete or incomplete
  - [ ] READY
  - [ ] IMPLEMENTED
  - [ ] REVIEWED
  - [ ] TESTED
  - [ ] ACCEPTED
- [US-0004] Delete a task
  - [ ] READY
  - [ ] IMPLEMENTED
  - [ ] REVIEWED
  - [ ] TESTED
  - [ ] ACCEPTED
- [US-0005] Delete an entire list and its tasks
  - [ ] READY
  - [ ] IMPLEMENTED
  - [ ] REVIEWED
  - [ ] TESTED
  - [ ] ACCEPTED
- [US-0006] View lists and tasks with visual distinction for completed items
  - [ ] READY
  - [ ] IMPLEMENTED
  - [ ] REVIEWED
  - [ ] TESTED
  - [ ] ACCEPTED


### v1.1.0
Goals
- Enhance Sprint 1 MVP by expanding test coverage, improving UI error handling and user feedback, and adding robust documentation/user guide for v1.1.0.

Stories
- [US-0004] Delete a task
  - [x] READY
  - [x] IMPLEMENTED
  - [x] REVIEWED
  - [x] TESTED
  - [x] ACCEPTED


### v1.2.0
Goals
- Deliver US-0005 (Delete an entire list and its tasks) for v1.2.0, ensuring robust list teardown and cascade testing.

Stories
- [US-0005] Delete an entire list and its tasks
  - [x] READY
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