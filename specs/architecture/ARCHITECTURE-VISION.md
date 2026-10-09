# Architecture Vision: To-Do List Web App

## 1. Target System Shape
A lightweight, single-process Python web application built using Flask (or FastAPI/LiteStar) with a clean separation of concerns:
- **Presentation Layer**: HTML templates (Jinja2) rendered via web routes, styled cleanly (e.g. Vanilla CSS or a light utility framework like Pico CSS).
- **Application / Domain Layer**: Core to-do list and task management logic, enforcing the rules of list creation, task addition, status toggling, and deletion.
- **Data Persistence Layer**: Simple in-memory storage backed by a JSON file (or lightweight SQLite database) to persist lists and tasks across runs within the local environment.

## 2. Key Quality Attributes
- **Simplicity & Usability**: Out-of-the-box local execution with minimal setup (e.g. `pip install -r requirements.txt` and `python app.py`).
- **Correctness & Reliability**: Robust error handling for missing lists/tasks, verified by automated unit and integration tests.
- **Maintainability**: Clear folder structure (`app.py` or a standard Flask app factory package layout, `templates/`, `static/`, `tests/`).

## 3. Tech-Stack Guardrails
- **Language**: Python 3.9+
- **Framework**: Flask (lightweight, standard, highly compatible with simple templates and testing via pytest).
- **Testing**: Pytest + Flask Test Client.
- **Frontend**: Server-rendered HTML with Jinja2.

## 4. Major Components & Boundaries
- `app.py` (or application package): Entry point, route handlers.
- `models.py` / storage helper: Data structures for List and Task, plus file persistence logic.
- `templates/`: HTML views for dashboard, lists, and task management.
- `tests/`: Automated test suite covering all CRUD operations.
