# Architecture Vision: To-Do List Web App MVP

## Target System Shape
A lightweight, single-process web application built with Python (Flask or FastAPI) and a simple embedded SQLite database or JSON file store, rendering a server-side HTML UI (or simple SPA/templates) for managing to-do lists and tasks.

## Key Quality Attributes
- **Simplicity & Maintainability:** Minimal dependencies, clear separation of concerns (routes, models/storage, UI).
- **Usability:** Clean, intuitive browser-based UI meeting all functional requirements out of the box.
- **Reliability:** Simple robust data handling suitable for a single-session local web app.

## Tech-Stack Guardrails
- **Language:** Python 3.x
- **Web Framework:** Flask or FastAPI
- **Data Persistence:** SQLite via SQLAlchemy / SQLModel or JSON file storage
- **UI:** HTML/CSS templates (Jinja2) or lightweight frontend rendering

## Major Components & Boundaries
1. **Data Layer / Models:** Defines lists and tasks schemas, persistence logic.
2. **Web Controller / Routes:** Handles HTTP requests for creating, updating, and deleting lists and tasks.
3. **Frontend Views:** Jinja templates providing a clean HTML user interface.
