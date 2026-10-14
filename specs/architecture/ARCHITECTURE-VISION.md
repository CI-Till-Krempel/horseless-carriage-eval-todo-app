# Architecture Vision: To-Do List Web App

## Target System Shape
A lightweight, single-process web application built with Python (Flask/FastAPI) and a simple embedded storage mechanism (such as in-memory data structures or SQLite) to satisfy the To-Do List MVP requirements without external database overhead.

## Key Quality Attributes
- **Simplicity & Maintainability**: Clean, modular code structure enabling easy extension and testing.
- **Reliability**: Robust handling of basic CRUD operations for lists and tasks.
- **Usability**: Responsive, intuitive web UI with clear visual distinction for completed tasks.

## Tech-Stack Guardrails
- **Backend**: Python with lightweight framework (e.g., Flask or FastAPI).
- **Frontend**: HTML/CSS/JavaScript rendered via server templates (e.g., Jinja2) or a simple single-page frontend.
- **Testing**: Pytest for backend unit and integration tests.

## Major Components & Boundaries
1. **Web Server / Routing Layer**: Handles incoming HTTP requests and serves views/API endpoints.
2. **Application / Business Logic Layer**: Manages to-do lists, tasks, creation, completion toggling, and deletions.
3. **Storage / Persistence Layer**: In-memory or lightweight DB persistence for session/process lifetime.
4. **User Interface**: HTML templates and CSS styling for visual feedback and list/task management.
