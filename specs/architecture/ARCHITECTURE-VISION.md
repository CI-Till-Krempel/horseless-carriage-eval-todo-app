# Architecture Vision: To-Do List Web App (MVP)

## Target System Shape
A lightweight, single-process web application designed for a single user with no authentication requirement. The architecture emphasizes simplicity, minimal dependencies, and rapid deliverability across a 5-sprint budget.

## Key Quality Attributes
- **Simplicity & Maintainability**: Clean, readable code structure following standard web framework conventions.
- **Reliability & Responsiveness**: Immediate in-process state updates with a responsive, intuitive user interface.
- **Extensibility**: Modular design allowing core entity separation (Lists vs. Tasks).

## Tech-Stack Guardrails
- **Backend**: Python (Flask or FastAPI) or a similarly lightweight framework allowing fast implementation and reliable local execution.
- **Frontend**: Server-rendered HTML (e.g., Jinja2 templates) with vanilla CSS/JS or a lightweight component setup to ensure a working web UI without complex bundling overhead.
- **Persistence**: In-memory store or simple file-based/embedded SQLite database ensuring data survives page interactions during the session.

## Major Components & Boundaries
1. **Web UI Layer**: Renders lists and tasks, provides forms for creating lists/tasks, and interactive controls for completion and deletion.
2. **Application Core / Service Layer**: Encapsulates business logic for managing lists, tasks, completion states, and cascade deletions.
3. **Data / Storage Layer**: Handles entity persistence and retrieval.
