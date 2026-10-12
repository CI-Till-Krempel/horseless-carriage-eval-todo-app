# Architecture Vision: To-Do List Web App

## Target System Shape
A lightweight, monolithic web application comprising a minimal Python backend (e.g., Flask or FastAPI) and a responsive HTML/CSS/JS frontend served directly by the backend.

## Key Quality Attributes
- **Simplicity & Maintainability**: Minimal dependencies, easy to run locally with a single command.
- **Reliability**: Robust in-memory or simple file-based persistence (e.g., JSON or SQLite) to ensure state survives page reloads during a session.
- **Usability**: Clean, intuitive single-page or multi-page web UI satisfying all user interaction requirements without complex client-side build pipelines.

## Tech-Stack Guardrails
- **Language**: Python 3.x for the backend server.
- **Web Framework**: Flask or FastAPI (lightweight, rapid development).
- **Frontend**: Vanilla JavaScript, HTML5, and CSS (with optional CSS framework like Tailwind CSS via CDN if needed for styling) to avoid complex node_modules build steps.
- **Persistence**: SQLite or simple JSON file storage for local persistence.

## Major Components and Boundaries
1. **Web Server / Routing Layer**: Handles HTTP requests, serves static files, and routes API endpoints.
2. **Domain/Service Layer**: Manages business logic for lists and tasks (creation, completion, deletion).
3. **Data Access Layer**: Abstracts persistence (SQLite/JSON file).
4. **Frontend UI**: Renders lists and tasks, handles user interactions and API calls via Fetch API.
