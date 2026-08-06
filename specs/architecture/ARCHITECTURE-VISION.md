# Architecture Vision: To-Do List Web App

## Target System Shape
A lightweight, single-page web application featuring a Python-based backend (e.g., Flask or FastAPI) serving both REST API endpoints and dynamic/static web templates (or a simple single-page frontend using HTML/CSS/JS). 

## Key Quality Attributes
1. **Simplicity & Maintainability:** Minimal dependencies and clear separation of concerns (routes, business logic, storage).
2. **Usability:** Fast, responsive UI with immediate feedback on user actions (creation, toggling, deletion).
3. **Robustness:** Reliable session-based state management (in-memory with optional simple JSON file persistence) ensuring smooth evaluation runs.

## Tech-Stack Guardrails
- **Backend:** Python (FastAPI or Flask) for clean, rapid implementation and easy automated testing.
- **Frontend:** Vanilla HTML/CSS/JavaScript or lightweight templating (Jinja2) to avoid heavy build steps and keep dependencies minimal.
- **Testing:** pytest for backend and integration testing.

## Major Components & Boundaries
1. **Data Model Layer:** In-memory store or lightweight repository managing `List` and `Task` entities.
2. **API / Controller Layer:** Endpoints or routes handling HTTP requests for lists and tasks.
3. **Web UI Layer:** Static/templated frontend rendering lists, tasks, status toggles, and delete actions.
