# To-Do List Web App (v1.2.0)

A polished, lightweight, production-ready to-do list web application built with Python, Flask, and SQLite.

## Features
1. **Create Lists**: Create multiple named to-do lists.
2. **Add Tasks**: Add short text descriptions to specific lists.
3. **Complete/Incomplete**: Toggle task completion with instant visual feedback (strikethrough).
4. **Delete Tasks**: Remove individual tasks.
5. **Delete Lists**: Remove entire lists along with all their tasks in one action.
6. **Responsive UI**: Modern, clean CSS design optimized for both desktop and mobile devices.
7. **Input Validation & Flash Feedback**: User-friendly success and error notifications.

## Getting Started

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application**:
   ```bash
   flask --app app run
   ```

3. **Open your browser**:
   Navigate to `http://127.0.0.1:5000`.

## Running Tests
```bash
pytest -v
```

## Documentation
- See `specs/product-docs/USER-GUIDE.md` for detailed user workflows.
- See `specs/requirements/PRD-ToDo-MVP.md` for requirements and scope.
