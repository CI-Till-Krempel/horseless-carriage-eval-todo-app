# Architecture Vision: To-Do List Web App

## Target System Shape
A lightweight, single-process web application using Python (Flask or FastAPI) with an in-memory/SQLite data store and a simple HTML/CSS/JS frontend rendered via server templates or served statically. 

## Key Quality Attributes
- **Simplicity & Maintainability**: Clean, readable code with minimal dependencies to ensure robust execution within the 5-sprint budget.
- **Usability**: Straightforward web UI matching the "Done" criteria where a user can perform all CRUD operations on lists and tasks end-to-end without reading code.
- **Testability**: Clear separation of routes/controllers from core logic to enable straightforward unit and integration testing.

## Tech-Stack Guardrails
- **Language**: Python 3.x
- **Backend Framework**: Flask (lightweight, minimal boilerplate)
- **Data Persistence**: SQLite (via SQLAlchemy or raw sqlite3) to guarantee simple local file storage across sessions without heavy database setup.
- **Frontend**: HTML5, CSS (e.g. basic Bootstrap or custom vanilla CSS), and vanilla JavaScript.

## Major Components & Boundaries
1. **Data Access Layer**: Handles database connection, models (List, Task), and CRUD helpers.
2. **Web Routes / API Endpoints**: Handles HTTP requests, input validation, and rendering/JSON responses.
3. **Frontend Views**: Simple responsive pages to display lists and tasks, interact via forms/AJAX.
