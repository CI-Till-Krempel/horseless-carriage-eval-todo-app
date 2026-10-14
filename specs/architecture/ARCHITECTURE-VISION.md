# Architecture Vision: To-Do List Web App MVP

## 1. Target System Shape
A lightweight, monolithic web application providing a clean UI for managing to-do lists and tasks. 
- **Backend / Frontend**: Flask or FastAPI (Python) serving server-rendered HTML via Jinja2 templates with Tailwind CSS (or simple CSS) for styling, OR a lightweight single-file FastAPI/Flask API paired with static HTML/JS. Given the speed and simplicity requirements for an MVP, a monolithic Python web app (e.g. Flask with SQLite/in-memory storage) minimizes deployment and coordination complexity.
- **Persistence**: SQLite (via SQLAlchemy or raw sqlite3) to ensure reliable state persistence across requests within the local process execution, satisfying the MVP requirements cleanly.

## 2. Key Quality Attributes
- **Simplicity**: Minimal architectural overhead, clear separation of routes/controllers, services, and data models.
- **Maintainability**: Clean directory structure (`app/`, `specs/`, `tests/`) matching standard Python application conventions.
- **Testability**: Pytest suite covering all CRUD operations on lists and tasks.

## 3. Tech-Stack Guardrails
- **Language**: Python 3.10+
- **Framework**: Flask or FastAPI
- **Database**: SQLite
- **Testing**: Pytest

## 4. Major Components & Boundaries
- `app/models.py` or database schema layer.
- `app/routes.py` or controllers handling HTTP requests.
- `app/templates/` for the web UI frontend.
- `tests/` for automated unit and integration tests.
