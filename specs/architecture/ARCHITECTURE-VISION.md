# Architecture Vision: To-Do List Web App

## 1. Target System Shape
A lightweight, single-process web application built with Python (Flask) and a file-based or SQLite persistence layer, serving a responsive HTML/CSS/JS user interface.

## 2. Key Quality Attributes
- **Simplicity & Maintainability**: Clean, modular code structure suitable for a 5-sprint delivery cycle.
- **Reliability**: Persistence of lists and tasks across restarts via SQLite.
- **Usability**: Intuitive single-page or multi-page web UI allowing seamless list and task management.

## 3. Tech-Stack Guardrails
- **Language**: Python 3.x
- **Framework**: Flask (lightweight, easy to test and run)
- **Database**: SQLite with SQLAlchemy or native sqlite3
- **Frontend**: HTML5, CSS (Bootstrap or Tailwind CDN for rapid UI styling), vanilla JavaScript

## 4. Major Components & Boundaries
- **Web App / Controller Layer**: Flask routes handling HTTP requests for lists and tasks.
- **Data / Storage Layer**: SQLite database managing lists and tasks tables.
- **UI Presentation Layer**: Jinja2 HTML templates styled with CSS for viewing and interacting with lists and tasks.
