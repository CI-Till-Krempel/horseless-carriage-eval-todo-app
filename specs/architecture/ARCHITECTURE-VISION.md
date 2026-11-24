# Architecture Vision: To-Do List Web App

## Target System Shape

A simple, single-user to-do list web application where users can organize tasks into named lists and track completion status. The system consists of:

1. **Backend API Layer**: RESTful endpoints for CRUD operations on lists and tasks
2. **Frontend UI Layer**: Interactive web interface (HTML/CSS/JavaScript) for user interactions  
3. **Data Persistence Layer**: Pluggable storage (in-memory default, file-based, or SQLite for future persistence)
4. **Presentation Layer**: Real-time UI updates reflecting data changes without full page reloads

## Key Quality Attributes

- **Usability**: Intuitive interface requiring no code knowledge - users can clone, run, and use immediately
- **Correctness**: All 6 core features work as specified without data loss or unexpected behavior
- **Simplicity**: No over-engineering; lean stack focusing on core MVP only
- **Testability**: Automated test coverage for all backend operations and core UI workflows
- **Maintainability**: Clear separation between backend/frontend; easy for future developers to understand and extend

## Tech Stack Guardrails

- **Backend Framework**: Python + Flask (lightweight, rapid development, integrated testing via pytest)
- **Frontend**: Vanilla HTML/CSS/JavaScript (no heavy framework overhead; direct DOM manipulation acceptable for MVP scope)
- **Data Persistence**: SQLite (or in-memory dictionary as default) - decision per story US-0001
- **Testing**: pytest for backend, manual/automated UI testing for frontend
- **Deployment**: Local execution only (no cloud hosting in scope)

## Major Components & Boundaries

### Backend (Flask Application)
- **Models**: `List` (id, name, tasks[]), `Task` (id, text, completed, list_id)
- **API Routes**:
  - `GET /api/lists` - retrieve all lists
  - `POST /api/lists` - create new list
  - `GET /api/lists/:id` - retrieve specific list with tasks
  - `DELETE /api/lists/:id` - delete list and cascading tasks
  - `GET /api/lists/:id/tasks` - retrieve tasks in a list
  - `POST /api/lists/:id/tasks` - create task
  - `PATCH /api/lists/:id/tasks/:taskId` - update task completion
  - `DELETE /api/lists/:id/tasks/:taskId` - delete task

### Frontend (Web UI)
- **Views**:
  - Lists view: displays all user's lists with create button
  - List detail view: shows tasks in a list with completion state visual distinction
  - Create/Edit forms: modal or inline forms for entering list names and task text
- **Styling**: CSS for visual distinction of complete/incomplete tasks (strikethrough, opacity, color)
- **Interactions**: Click handlers for toggle, delete, navigation; form submission to backend

### Data Flow
1. User clicks in UI → JavaScript event handler
2. Handler makes API call to backend (fetch/XMLHttpRequest)
3. Backend processes request, updates data model
4. Backend returns JSON response
5. JavaScript updates DOM to reflect new state

## Cross-Cutting Concerns

### Error Handling
- Backend returns appropriate HTTP status codes (200, 400, 404, 500)
- Frontend displays user-friendly error messages (e.g., "Could not create list" with retry option)
- No silent failures; all operations provide user feedback

### Data Validation
- List names: non-empty, reasonable length (≤255 chars)
- Task text: non-empty, reasonable length (≤500 chars)
- Both validated on frontend (UX) and backend (security/correctness)

### Persistence Strategy
- Default: In-memory dictionary (session-based) for MVP speed
- Future: SQLite file-based persistence if deeper storage investigation needed
- No authentication/multi-user; all data belongs to implicit single user

## Evolutionary Boundaries (Out of Scope)

The following are explicitly NOT in this architecture:
- User authentication or multi-user support
- Realtime synchronization (not needed for single-user)
- Mobile apps or offline support
- Advanced features (due dates, priorities, sharing, etc.)
- Deployment/hosting beyond local dev execution

This design can be extended post-MVP if any of these become needed, but the current MVP scope is intentionally narrow.

## Decision Rationale

**Why Python/Flask?** 
- Minimal framework overhead; Flask focuses on routing and request/response handling
- Excellent pytest integration for comprehensive backend testing
- Fast scaffolding - full app structure in a few files
- Easy debugging and inspection for developers

**Why vanilla frontend?**
- No build step or transpilation needed for MVP
- Direct, immediate visual feedback on interactions
- Easier manual testing and debugging
- Simpler deployment (no npm, no webpack, no bundling)

**Why in-memory default persistence?**
- Simplest possible implementation for MVP
- Allows team to focus on core features rather than DB setup
- Storage approach is not a blocker for feature completeness
- Can upgrade to SQLite later if needed for durability

---

**Status**: Active (Sprint 1)  
**Last Updated**: Sprint 1 initialization
