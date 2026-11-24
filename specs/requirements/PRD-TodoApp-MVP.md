# Product Requirements Document: To-Do List Web App MVP

## Product Vision

Build a simple to-do list web application. A single user should be able to:

1. Create a new to-do list with a name.
2. Add a task to a list, with a short text description.
3. Mark a task as complete or incomplete.
4. Delete a task.
5. Delete an entire list (and its tasks).
6. See all their lists and, within a list, all its tasks, with completed tasks visually distinguished from incomplete ones.

## Constraints

- **Single user, no authentication.** Do not build login/accounts — out of scope.
- **No persistence requirement beyond the current session/process is assumed** unless the team's own design calls for it — persistence approach (in-memory, file, or a simple embedded DB) is a legitimate design decision for the team to make and justify, not a hidden requirement.
- **A working web UI is required** — the deliverable is something a person could open in a browser and actually use, not just a backend API with no way to interact with it.
- **No specific language/framework is mandated.** The team should choose something it can deliver completely and correctly within budget, and should say why.

## Out of Scope

- Multiple users, sharing, or permissions
- Due dates, reminders, priorities, tags, or sub-tasks
- Mobile app, offline support, or real-time sync
- Any deployment/hosting beyond running locally

## Success Criteria

A person can clone the repo, follow the README, run the app, and actually:
- Create a list
- Add a few tasks
- Mark one complete
- Delete one task
- Delete a list
- See all changes reflected in the UI immediately

This end-to-end flow should work without reading any code first.

## Product Goals

1. **Usability**: Core features work intuitively with no documentation needed beyond a README
2. **Correctness**: All required features function as specified
3. **Completeness**: All 6 requirements are fully implemented and testable
4. **Delivery**: Complete within 5 sprints with high code quality
