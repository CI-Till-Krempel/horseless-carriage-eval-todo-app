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

### v0.1.0
Goals
- Deliver MVP To-Do List Web App core features: list creation, task addition, viewing, completion toggling, and deletion.

Stories
- [US-0001] Create a new to-do list
  - [x] READY
  - [x] IMPLEMENTED
  - [x] REVIEWED
  - [x] TESTED
  - [x] ACCEPTED
- [US-0002] Add a task to a list
  - [x] READY
  - [x] IMPLEMENTED
  - [x] REVIEWED
  - [x] TESTED
  - [x] ACCEPTED
- [US-0003] View lists and tasks with visual completion status
  - [x] READY
  - [x] IMPLEMENTED
  - [x] REVIEWED
  - [x] TESTED
  - [x] ACCEPTED
- [US-0004] Mark a task as complete or incomplete
  - [x] READY
  - [x] IMPLEMENTED
  - [x] REVIEWED
  - [x] TESTED
  - [x] ACCEPTED
- [US-0005] Delete a task
  - [x] READY
  - [x] IMPLEMENTED
  - [x] REVIEWED
  - [x] TESTED
  - [x] ACCEPTED
- [US-0006] Delete an entire list and its tasks
  - [x] READY
  - [x] IMPLEMENTED
  - [x] REVIEWED
  - [x] TESTED
  - [x] ACCEPTED


### v0.2.0
Goals
- Deliver Sprint 2 Usability & Polish enhancements including robust input validation and user feedback messages for lists and tasks.

Stories
- [US-0007] Input validation for list creation
  - [x] READY
  - [x] IMPLEMENTED
  - [x] REVIEWED
  - [x] TESTED
  - [x] ACCEPTED
- [US-0008] Input validation for task creation
  - [x] READY
  - [x] IMPLEMENTED
  - [x] REVIEWED
  - [x] TESTED
  - [x] ACCEPTED


### v0.3.0
Goals
- Deliver Sprint 3 documentation polish and user guide enhancement (US-0009) ensuring complete end-to-end usability guidance.

Stories
- [US-0009] User Guide / README instructions enhancement
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