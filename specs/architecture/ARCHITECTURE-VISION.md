# Architecture Vision: To-Do List Web App

## Target System Shape
A lightweight, monolithic Python web application using **Flask** and an in-memory or SQLite database with SQLAlchemy for clean, robust state management across sessions. The front-end will use server-rendered HTML templates (Jinja2) with basic CSS (Bootstrap or clean custom CSS) to provide an intuitive, responsive user experience without heavy client-side build steps.

## Key Quality Attributes
1. **Simplicity & Maintainability**: Clean separation of concerns (models, routes, templates) adhering to standard Flask patterns.
2. **Reliability & Persistence**: Utilizing SQLite via SQLAlchemy ensures state persists across server restarts while keeping deployment strictly local and dependency-free (no external DB server required).
3. **Usability**: Clear visual distinction between completed and incomplete tasks, with straightforward forms for list/task management.

## Tech-Stack Guardrails
- **Language**: Python 3.10+
- **Framework**: Flask
- **ORM**: SQLAlchemy / Flask-SQLAlchemy
- **Frontend**: Jinja2 templates, standard HTML5/CSS3, optional lightweight CSS framework (Bootstrap via CDN).
- **Testing**: `pytest` for unit and integration testing.

## Major Components & Boundaries
- `app.py`: Application factory, configuration, and main entrypoint.
- `models.py`: SQLAlchemy database models (`TodoList`, `Task`).
- `routes.py` (or blueprint): HTTP request handlers for lists and tasks.
- `templates/`: HTML views for index, list detail, etc.
- `tests/`: Automated test suite ensuring core CRUD operations.
