# Architecture Vision: To-Do List Web App

## Target System Shape
A lightweight, single-process web application built in Python using Flask, leveraging SQLite for robust local data persistence across sessions. The UI will be server-rendered HTML using Jinja2 templates styled with a clean CSS framework (e.g., Bootstrap or Tailwind via CDN) to provide an immediately usable browser interface.

## Key Quality Attributes
- **Simplicity & Maintainability**: Minimal dependencies, easy local setup, single command startup.
- **Reliability & Persistence**: Data persists across server restarts using SQLite.
- **Usability**: Clean, intuitive responsive layout meeting all functional requirements.

## Tech-Stack Guardrails
- **Backend**: Python 3.x with Flask and SQLite.
- **Frontend**: HTML5, CSS (Bootstrap/Tailwind via CDN), minimal vanilla JS if needed.
- **Testing**: pytest for backend and integration tests.

## Major Components & Boundaries
- `app.py`: Main Flask application entry point, routing, and HTTP request handling.
- `database.py` / models: SQLite database connection and schema management for Lists and Tasks.
- `templates/`: Jinja2 HTML templates for the user interface.
- `tests/`: Automated test suite ensuring correct functionality of list and task operations.
