# Architecture Vision: To-Do List Web App

## Target System Shape
A lightweight, single-process web application built in Python using Flask. It provides a server-rendered HTML/CSS/JavaScript web interface alongside a minimal JSON API structure if needed, backed by a simple SQLite database or in-memory state store persisted locally.

## Key Quality Attributes
- **Simplicity:** Minimal dependencies, easy to run locally via standard Python commands (`pip install` and `python app.py`).
- **Usability:** Clean, responsive web UI allowing effortless list and task management.
- **Maintainability:** Clear separation of concerns (routes, models/storage, templates) within a single repository structure.

## Tech-Stack Guardrails
- **Language:** Python 3.10+
- **Framework:** Flask (or FastAPI/Streamlit if suitable, but Flask provides direct server-side HTML rendering with Jinja2).
- **Database / Storage:** SQLite via SQLAlchemy for robust, zero-configuration local persistence across sessions.
- **Testing:** Pytest for unit and integration testing.

## Major Components & Boundaries
1. **Web UI / Routes:** Handles HTTP requests, renders Jinja2 templates, and captures user actions.
2. **Data Layer / Models:** Defines `List` and `Task` entities and manages database operations.
3. **Test Suite:** Verifies end-to-end functionality of lists and tasks.
