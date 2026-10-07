# Architecture Vision: To-Do List Web App

## Target System Shape
A lightweight, single-process web application using Python (Flask or FastAPI) with an embedded SQLite database (or local JSON file store) and a clean server-rendered HTML UI (Bootstrap / Tailwind CSS via CDN) for seamless local execution.

## Key Quality Attributes
- **Simplicity & Ease of Setup**: Clone, run dependencies, start server, open in browser.
- **Maintainability**: Clear separation of concerns (routes/controllers, services/business logic, data models/persistence).
- **Testability**: Unit and integration tests covering core API endpoints and UI workflows using pytest.

## Tech-Stack Guardrails
- **Language**: Python 3.x
- **Backend Framework**: Flask or FastAPI (Flask chosen for extreme simplicity and zero boilerplate).
- **Database/Storage**: SQLite via SQLAlchemy or raw SQLite3 for zero-configuration persistence across sessions.
- **Frontend**: Server-side HTML templates (Jinja2) with lightweight CSS.

## Major Components & Boundaries
1. **Web UI / Presentation Layer**: Jinja2 templates and static assets rendering lists and tasks with visual distinction for completed items.
2. **API / Controller Layer**: Handles HTTP requests for creating/deleting lists, adding/deleting tasks, and toggling completion.
3. **Data Access / Persistence Layer**: Manages database sessions, schema initialization, and CRUD operations.
