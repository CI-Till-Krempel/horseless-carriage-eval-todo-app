# Architecture Vision: To-Do List Web App

## Target System Shape
A lightweight, single-user to-do list web application built with Python and Flask, featuring a clean server-rendered web UI and robust session/in-memory or file-based persistence.

## Key Quality Attributes
- **Simplicity & Maintainability**: Clean separation of concerns (routes, models, templates) using Flask blueprints or modular views.
- **Usability**: Responsive, intuitive UI with clear visual differentiation of completed tasks.
- **Testability**: Comprehensive unit and integration tests using `pytest` and `pytest-flask`.

## Tech-Stack Guardrails
- **Language**: Python 3.11+
- **Framework**: Flask
- **Testing**: Pytest & pytest-flask
- **Frontend**: Server-rendered HTML templates with CSS styling.

## Major Components & Boundaries
- **Web Layer**: Flask routes handling HTTP requests for lists and tasks.
- **Business/Data Model**: In-memory / file-backed persistence layer managing lists and tasks.
- **Presentation**: HTML templates with CSS for visual status distinction.
