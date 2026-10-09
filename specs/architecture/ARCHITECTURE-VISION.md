# Architecture Vision: To-Do List Web App

## Target System Shape
A lightweight, self-contained single-page web application built with Python and Flask, storing state in an in-memory database or simple local JSON/SQLite file for simplicity and zero-configuration startup.

## Key Quality Attributes
- **Simplicity & Zero Config:** Clone and run immediately with minimal dependencies (`requirements.txt`).
- **Usability:** Clean, responsive HTML/CSS UI rendered via Jinja2 templates or lightweight frontend assets.
- **Maintainability:** Modular Python package structure separating routes, data models/storage, and UI templates.

## Tech-Stack Guardrails
- **Backend:** Python 3 with Flask web framework.
- **Data Persistence:** SQLite or SQLAlchemy with SQLite for reliable local file persistence across requests.
- **Frontend:** HTML5, CSS3, minimal vanilla JS or simple server-rendered templates.

## Major Components & Boundaries
1. **Web Layer (`app.py` & routes):** Handles HTTP requests, form submissions, and template rendering.
2. **Data Layer (`models.py` or `database.py`):** Encapsulates lists and tasks database models and CRUD operations.
3. **Template Layer (`templates/`):** Jinja2 templates providing the To-Do list web UI.
