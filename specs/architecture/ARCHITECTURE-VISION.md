# Architecture Vision: To-Do List Web App

## Target System Shape
A lightweight, single-process web application built with Python (Flask or FastAPI) and a simple frontend (HTML/CSS/JS with Jinja templates or a micro-frontend), using an embedded lightweight database (SQLite) or file-based persistence for simplicity and robustness.

## Key Quality Attributes
- **Simplicity & Maintainability**: Clean, readable code with modular boundaries separating routing, business logic, and data access.
- **Ease of Setup**: Runs locally with minimal commands (`pip install -r requirements.txt`, python app.py) as required by the MVP definition.
- **Reliability**: Robust error handling and basic input validation.

## Tech-Stack Guardrails
- **Language**: Python 3.9+
- **Backend Framework**: Flask (chosen for rapid setup, minimal boilerplate, and excellent fit for single-process web apps).
- **Database/Persistence**: SQLite via SQLAlchemy or plain SQLite for zero-config local persistence across sessions.
- **Frontend**: Server-rendered HTML with Tailwind CSS or plain CSS for a clean, responsive UI without complex build toolchains.

## Major Components & Boundaries
1. **Web / API Layer**: Handles HTTP requests, input validation, and rendering views or JSON responses.
2. **Domain / Service Layer**: Encapsulates business logic for lists and tasks.
3. **Data Access Layer**: Abstracts persistence operations (SQLite / ORM).
