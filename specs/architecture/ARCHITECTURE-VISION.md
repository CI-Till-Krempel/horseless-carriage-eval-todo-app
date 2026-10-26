# Architecture Vision: To-Do List Web App

## 1. System Shape & Tech Stack
- **Architecture**: Lightweight Full-Stack Web Application.
- **Backend**: Python (Flask or FastAPI) providing a clean REST API and HTML/JSON rendering.
- **Frontend**: HTML5, CSS (e.g., Tailwind CSS via CDN or simple vanilla CSS), and JavaScript (fetch API) for dynamic updates without full-page reloads.
- **Persistence**: In-memory data store with optional simple JSON file persistence to satisfy session/process state retention without requiring a heavy external database.

## 2. Key Quality Attributes
- **Simplicity**: Minimal dependencies, easy local setup via standard package managers (`pip`).
- **Usability**: Responsive, clean UI with clear visual distinction for completed tasks.
- **Maintainability**: Modular layout separating routing, business logic/data handling, and frontend views.

## 3. Major Components & Boundaries
- `app.py` or `main.py`: Entry point and HTTP routing.
- `models.py` / `storage.py`: In-memory list/task data structures and persistence logic.
- `templates/` & `static/`: HTML templates and frontend assets.
