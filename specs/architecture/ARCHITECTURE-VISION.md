# Architecture Vision: To-Do List Web App

## Target System Shape
A lightweight, self-contained web application built using Python (Flask or FastAPI) with a simple HTML/CSS/JS frontend (or Jinja templates) to ensure quick bootstrap and easy local execution for evaluation.

## Key Quality Attributes
- **Simplicity & Maintainability**: Minimal dependencies, clear file structure, easily runnable via `pip install` and a single script (`app.py`).
- **Reliability**: Simple in-memory or SQLite-based state persistence to ensure data stability within a session/run.
- **Usability**: Intuitive, responsive web UI meeting all functional requirements without complex client-side build steps.

## Tech-Stack Guardrails
- **Backend**: Python 3.9+ with Flask or FastAPI.
- **Persistence**: SQLite (via SQLAlchemy) or a lightweight JSON file store for simplicity and robustness.
- **Frontend**: Vanilla HTML5, CSS (e.g., Pico CSS or Tailwind via CDN), and vanilla JavaScript.

## Major Components & Boundaries
1. **Web Server / Routing**: Handles HTTP requests for listing, creating, and deleting lists/tasks.
2. **Data Model / Storage Layer**: Abstracts persistence for Lists and Tasks.
3. **UI Layer**: Templates and static assets rendering the to-do lists and task interactions.
