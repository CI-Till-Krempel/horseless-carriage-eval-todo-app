# Architecture Vision: To-Do List Web App

## Target System Shape
A lightweight, single-process Python web application built using Flask (or FastAPI) and SQLite for persistence, rendering a clean HTML/CSS web interface (or lightweight SPA).

## Key Quality Attributes
- **Simplicity & Maintainability**: Minimal dependencies, easy to run locally via Python and a simple README.
- **Reliability**: Robust handling of in-memory or file-backed database state via SQLite.
- **Testability**: Pytest for unit and integration testing of endpoints and database operations.

## Tech-Stack Guardrails
- **Language**: Python 3.x
- **Framework**: Flask or FastAPI
- **Database**: SQLite with SQLAlchemy
- **Frontend**: HTML5, CSS (Bootstrap or vanilla CSS for clean styling)

## Major Components & Boundaries
1. **Web / API Layer**: Handles HTTP requests, form submissions, and JSON/HTML rendering.
2. **Data / Domain Layer**: SQLAlchemy models representing To-Do Lists and Tasks, with CRUD operations.
3. **Test Suite**: Pytest validating core functionalities (list creation, task addition, toggling, deletion).
