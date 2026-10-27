# Architecture Vision: To-Do List Web App

## Target System Shape
A lightweight, self-contained Python web application using Flask (or FastAPI) and SQLite (or in-memory store with simple persistence), providing a clean HTML/CSS/JS frontend for managing to-do lists and tasks.

## Key Quality Attributes
- **Simplicity & Maintainability**: Easy to run locally with zero complex setup.
- **Reliability**: Proper handling of task and list CRUD operations.
- **Usability**: Intuitive UI with clear visual distinction for completed tasks.

## Tech-Stack Guardrails
- Language: Python 3
- Framework: Flask or FastAPI
- Frontend: HTML5, CSS3, Vanilla JavaScript
- Storage: SQLite for session/local data persistence

## Major Components & Boundaries
- `app.py`: Main web server and API/view routes.
- `models.py` / DB layer: Data structures and database operations for lists and tasks.
- `templates/` & `static/`: Frontend user interface templates and assets.
- `tests/`: Automated unit and integration tests verifying all CRUD and UI features.
