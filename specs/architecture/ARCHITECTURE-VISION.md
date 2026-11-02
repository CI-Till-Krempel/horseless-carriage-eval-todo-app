# Architecture Vision: To-Do List Web App

## Target System Shape
A lightweight, self-contained single-page or simple server-rendered web application built with Python (Flask or FastAPI) or Node.js to ensure fast delivery and robust local execution within the 5-sprint budget.

## Key Quality Attributes
- **Simplicity**: Minimal dependencies, easy local setup via a single command (e.g. `python app.py` or `npm start`).
- **Reliability**: Clean handling of in-memory or lightweight file-backed data storage.
- **Usability**: Responsive, clean UI with clear visual indicators for completed tasks.

## Tech-Stack Guardrails
- **Language/Framework**: Python with Flask/FastAPI or Node.js with Express.
- **Persistence**: In-memory store with optional JSON file backup to meet session persistence expectations simply.
- **Frontend**: HTML5, CSS (e.g., Tailwind or vanilla CSS), JavaScript for dynamic interactions.

## Major Components & Boundaries
1. **Backend API / Server**: Handles CRUD routes for lists and tasks.
2. **Data Store**: Manages lists and tasks in-memory/JSON.
3. **Frontend UI**: Renders lists and tasks, handles user events (create, delete, toggle complete).
