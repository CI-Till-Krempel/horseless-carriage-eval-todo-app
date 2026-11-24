# To-Do List Web App

A simple, single-user to-do list web application built with Python and Flask. Organize your tasks into named lists and track completion status.

## Overview

This application allows you to:
1. Create multiple to-do lists with custom names
2. Add tasks to lists with text descriptions
3. Mark tasks as complete or incomplete
4. Delete individual tasks
5. Delete entire lists (and all their tasks)
6. View all lists and tasks with clear visual distinction between completed and incomplete work

## Tech Stack

### Why Python + Flask?

**Backend: Python 3.11 + Flask**
- Lightweight microframework focused on HTTP routing and request/response handling
- Minimal overhead - no bloated abstraction layers
- Excellent test framework integration via pytest
- Rapid scaffolding and iteration - full app structure in just a few files
- Easy debugging and inspection for developers
- Production-grade but simple enough for MVP scope

**Frontend: Vanilla HTML/CSS/JavaScript**
- No build step, no transpilation, no webpack complexity
- Direct DOM manipulation for immediate visual feedback
- Easier manual testing and debugging in browser
- Simpler deployment - no npm, no bundling, no additional infrastructure
- Files served directly by Flask's static file handler

### Technology Stack Summary

| Layer | Technology | Rationale |
|-------|-----------|-----------|
| **Backend** | Python 3.11 + Flask | Lightweight, integrated testing, rapid MVP iteration |
| **Frontend** | HTML5 + CSS3 + Vanilla JavaScript | No build complexity, direct UX feedback, simple deployment |
| **Data Model** | In-memory dictionary (default) | Session-based MVP; SQLite upgrade available if durability needed |
| **Testing** | pytest + pytest-flask | Comprehensive backend test coverage, Flask test client |
| **Dev Server** | Flask development server | Sufficient for local development and testing |

## Project Goals

**Usability**: The UI is clean, intuitive, and self-explanatory - users can clone, run, and use it immediately without reading documentation beyond the README.

**Correctness**: All 6 required features function exactly as specified, without data loss or unexpected behavior.

**Simplicity**: No feature creep, no over-engineering - focuses strictly on core MVP scope (no authentication, no sharing, no due dates, no cloud hosting).

**Testability**: Automated test coverage for all backend operations and core user workflows.

## Persistence Strategy

### Default: In-Memory Storage

The initial implementation uses an in-memory dictionary to store lists and tasks. This approach:
- Requires zero external dependencies (no database setup)
- Allows the team to focus on core features rather than DB configuration
- Provides immediate feedback during development
- Clears all data when the server restarts (acceptable for MVP/development)
- Is perfectly suitable for single-user, session-based use

Data structure (conceptual):
```python
{
  "lists": {
    "1": {"id": "1", "name": "Shopping", "tasks": [...]},
    "2": {"id": "2", "name": "Work", "tasks": [...]}
  }
}
```

### Future: SQLite Upgrade Path

If durability beyond the current process lifetime becomes required, SQLite can be introduced as a drop-in replacement:
- File-based database stored locally (no server infrastructure)
- SQL ORM (SQLAlchemy) can handle schema and queries
- Existing API contracts remain unchanged
- Minimal migration effort from in-memory model

This design allows the team to prove all features work first, then optimize storage if needed post-MVP.

## Architecture

### High-Level Design

```
┌─────────────────────────────────────────────────────────────┐
│                        Web Browser                           │
│  HTML UI + CSS Styling + JavaScript Event Handlers          │
└────────────────────────┬────────────────────────────────────┘
                         │ HTTP (fetch API)
                         ↓
┌─────────────────────────────────────────────────────────────┐
│                  Flask Web Application                       │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  API Routes (/api/lists, /api/lists/:id/tasks, etc)  │   │
│  └────────────────────────┬─────────────────────────────┘   │
│                           │                                   │
│  ┌────────────────────────▼─────────────────────────────┐   │
│  │  Data Models (List, Task, DataStore)                 │   │
│  │  - CRUD Operations                                    │   │
│  │  - Validation & Error Handling                        │   │
│  └────────────────────────┬─────────────────────────────┘   │
│                           │                                   │
│  ┌────────────────────────▼─────────────────────────────┐   │
│  │  Persistence Layer (In-Memory Dictionary)             │   │
│  │  - Session-scoped storage                             │   │
│  │  - Cascade delete on list removal                     │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

### API Endpoints

**Base URL:** `http://localhost:5000/api`

#### Lists
- `GET /lists` - Retrieve all lists
- `POST /lists` - Create new list (body: `{"name": "..."}`)
- `GET /lists/:id` - Retrieve specific list with tasks
- `DELETE /lists/:id` - Delete list and cascade delete all tasks

#### Tasks
- `GET /lists/:id/tasks` - Retrieve all tasks in a list
- `POST /lists/:id/tasks` - Create task (body: `{"text": "..."}`)
- `PATCH /lists/:id/tasks/:taskId` - Update task completion (body: `{"completed": true/false}`)
- `DELETE /lists/:id/tasks/:taskId` - Delete task

All endpoints return JSON and use appropriate HTTP status codes:
- `200 OK` - Successful operation
- `201 Created` - Resource created
- `400 Bad Request` - Invalid input
- `404 Not Found` - Resource not found
- `500 Internal Server Error` - Server error

### Data Model

**List:**
```python
{
  "id": "1",
  "name": "Shopping List",
  "tasks": [...]  # Array of Task objects
}
```

**Task:**
```python
{
  "id": "1",
  "text": "Buy milk",
  "completed": False,
  "list_id": "1"
}
```

## Setup Instructions

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)
- A text editor or IDE
- A modern web browser (Chrome, Firefox, Safari, Edge)

### Local Development Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. **Create a Python virtual environment (recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python run.py
   ```
   Or with Flask directly:
   ```bash
   flask --app app run --debug
   ```

5. **Open in browser:**
   - Navigate to `http://localhost:5000`
   - You should see the to-do list home page

### Running Tests

```bash
pytest                    # Run all tests
pytest -v                 # Verbose output
pytest --cov              # With coverage report
pytest tests/test_app.py  # Run specific test file
```

## Project Structure

```
.
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── run.py                    # Entry point
├── app/
│   ├── __init__.py          # Flask app initialization
│   ├── data.py              # Data model (List, Task, DataStore)
│   ├── routes.py            # API endpoint definitions
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css    # UI styling
│   │   └── js/
│   │       └── app.js       # Frontend JavaScript
│   └── templates/
│       └── index.html       # Main HTML page
├── tests/
│   ├── __init__.py
│   ├── test_data.py         # Data model unit tests
│   ├── test_routes.py       # API route tests
│   └── conftest.py          # pytest configuration
└── specs/                   # Product specifications
    ├── stories/             # User stories
    └── architecture/        # Architecture decisions
```

## Development Workflow

### Adding a Feature

1. Create a feature branch: `git checkout -b feature/<name>`
2. Write tests first (TDD approach)
3. Implement the feature
4. Ensure all tests pass: `pytest`
5. Commit: `git commit -m "feat: <description>"`
6. Push to GitHub and create a Pull Request
7. After review and approval, merge to develop

### Code Style

- Follow PEP 8 for Python code (use black for formatting)
- Use meaningful variable and function names
- Keep functions small and focused (single responsibility)
- Add docstrings to functions and classes
- Use type hints where helpful

## Assumptions & Constraints

### Assumptions
- Single user (no authentication or multi-user support)
- In-memory data storage (acceptable for MVP; session-scoped)
- Local execution only (no cloud deployment)
- Flask development server sufficient for testing

### Out of Scope
- Multiple user support or authentication
- Due dates, priorities, reminders, or sub-tasks
- Mobile app or offline support
- Real-time synchronization
- Production deployment infrastructure

## Future Enhancements

After MVP delivery, possible improvements:
1. **Persistence:** Upgrade to SQLite for data durability
2. **UI:** Add animations and transitions for smoother UX
3. **Features:** Tags, priorities, due dates, recurring tasks
4. **Multi-user:** Add authentication and user accounts
5. **Deployment:** Docker containerization and cloud hosting
6. **PWA:** Progressive Web App support for offline use

## Troubleshooting

**Port 5000 already in use:**
```bash
flask --app app run --debug -p 5001  # Use different port
```

**ModuleNotFoundError when running:**
- Ensure virtual environment is activated
- Run `pip install -r requirements.txt`

**Tests failing:**
- Ensure pytest is installed: `pip install pytest pytest-flask`
- Run from project root directory
- Check test database state isn't persisting

**UI not updating after API call:**
- Check browser console for JavaScript errors (F12)
- Verify API endpoint in browser's Network tab
- Ensure CORS is properly configured in Flask app

## Contributing

This is a team-developed MVP under the Scrum methodology. For questions or suggestions:
1. Check existing GitHub issues
2. File a new issue with detailed description
3. Submit a pull request with proposed changes
4. Engage with the team during sprint reviews

## License

[To be determined by project lead]

## References

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Architecture Vision Document](specs/architecture/ARCHITECTURE-VISION.md)
- [Sprint Planning & Stories](specs/stories/)
- [Product Requirements](specs/requirements/)

---

**Last Updated:** Sprint 1 initialization
**Team:** Scrum Team (DevTeam, Architect, QA, Product Owner, Scrum Master)
**Status:** In Development
