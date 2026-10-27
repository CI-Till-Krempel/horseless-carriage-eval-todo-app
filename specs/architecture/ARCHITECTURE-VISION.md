# Architecture Vision: To-Do List Web App

## Target System Shape
A lightweight, single-process web application built in Python using Flask. It provides a clean server-rendered or simple AJAX-powered HTML user interface for managing to-do lists and their corresponding tasks. Persistence is handled via a simple local file or lightweight SQLite database to ensure data survives process restarts within the single-user session context.

## Key Quality Attributes
- **Simplicity & Maintainability**: Clean separation of concerns (routes, models/storage, templates) keeping the codebase easy to read and test.
- **Reliability**: Robust handling of storage operations and clean error states for UI interactions.
- **Usability**: Responsive, intuitive web interface meeting all user story requirements without requiring complex client-side build pipelines.

## Tech-Stack Guardrails
- **Language**: Python 3.x
- **Framework**: Flask (lightweight, highly reliable for small-scale web apps)
- **Database/Storage**: SQLite with SQLAlchemy or pure JSON/SQLite file storage for straightforward local persistence.
- **Testing**: Pytest for unit and integration tests covering backend logic and route handling.

## Major Components & Boundaries
1. **Web / Controller Layer**: Flask routes handling HTTP requests for lists and tasks.
2. **Domain / Storage Layer**: Data models and persistence adapters managing list and task records.
3. **UI Layer**: Jinja2 HTML templates and static assets (CSS/JS) providing the user interface.
