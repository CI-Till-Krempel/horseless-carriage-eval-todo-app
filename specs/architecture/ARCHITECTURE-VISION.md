# Architecture Vision: To-Do List Web App

## Target System Shape
A lightweight, containerized Python/Flask web application providing a single-user To-Do List interface. It uses an in-memory or SQLite-backed data store to manage lists and tasks.

## Key Quality Attributes
- **Simplicity**: Easy to run locally with zero complex setup.
- **Maintainability**: Clean modular structure separating routes, models, and UI templates.
- **Testability**: Comprehensive unit and integration test suite via pytest.

## Tech-Stack Guardrails
- **Backend**: Python 3 with Flask.
- **Frontend**: HTML5, CSS (Bootstrap or vanilla), and Jinja2 templates.
- **Testing**: pytest and Flask-Testing.

## Major Components & Boundaries
- `app.py`: Application factory and route handlers.
- `models.py`: Data models and persistence layer.
- `templates/`: HTML views for list and task management.
- `tests/`: Automated test suite.
