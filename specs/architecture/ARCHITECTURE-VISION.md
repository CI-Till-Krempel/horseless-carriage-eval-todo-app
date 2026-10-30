# Architecture Vision: To-Do List Web App

## Target System Shape
A lightweight, self-contained single-user web application built with Python (Flask or FastAPI) and a simple embedded SQLite database or JSON file store, rendering a clean responsive HTML/CSS/JS interface directly or via server-rendered templates.

## Key Quality Attributes
- **Simplicity & Zero Configuration:** Can be run locally with minimal dependencies (`pip install ...`, then run).
- **Correctness:** Fully implements all required CRUD operations for lists and tasks, with visual indicators for completed items.
- **Maintainability:** Clear separation between data persistence layer, business logic/routes, and frontend presentation.

## Tech-Stack Guardrails
- **Language:** Python 3.x
- **Framework:** Flask (chosen for simplicity and rapid development of small web apps)
- **Persistence:** SQLite via SQLAlchemy or plain SQLite for robust and clean local file persistence.
- **Frontend:** HTML5, CSS3, vanilla JavaScript or simple CSS framework (e.g. Tailwind via CDN or Bootstrap).

## Major Components & Boundaries
1. **Data Layer (`models.py` / database):** Defines `List` and `Task` entities and persistence operations.
2. **Web/API Layer (`app.py`):** Handles HTTP routes for listing, creating, updating, and deleting lists and tasks.
3. **Presentation Layer (`templates/` & `static/`):** User interface for interacting with the to-do lists and tasks.
