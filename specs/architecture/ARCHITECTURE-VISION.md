# Architecture Vision: To-Do List Web App

## Target System Shape
A lightweight, single-process web application using Python (Flask or FastAPI) with an embedded database (like SQLite via SQLAlchemy) or in-memory storage, backed by a simple HTML/CSS frontend (vanilla CSS or Bootstrap/Tailwind via CDN) so that no heavy build toolchain is required.

## Key Quality Attributes
- **Simplicity & Maintainability**: Clean, straightforward code structure making it easy for a single user/evaluator to run and inspect.
- **Ease of Deployment**: Clear instructions in the README allowing execution via a virtual environment and a single command.
- **Reliability**: Robust handling of basic tasks and lists without requiring external services.

## Tech-Stack Guardrails
- **Language**: Python 3.10+
- **Backend Framework**: Flask or FastAPI
- **Storage**: SQLite / SQLAlchemy for reliable data persistence during session/process.
- **Frontend**: Server-rendered templates (Jinja2) with lightweight CSS for styling and visual distinction of completed tasks.

## Major Components & Boundaries
1. **Web / API Layer**: Handles incoming HTTP requests and renders templates or returns JSON.
2. **Domain / Data Layer**: Models for To-Do Lists and Tasks, with persistence logic.
3. **Template / UI Layer**: HTML templates providing the user interface for creating, viewing, updating, and deleting lists and tasks.
