# To-Do List Web App

A simple, lightweight, and robust to-do list web application built with Python Flask, SQLite, and a responsive HTML/CSS web UI.

## Features
1. **Create Lists**: Organize tasks into distinct named to-do lists.
2. **Manage Tasks**: Add, edit, toggle completion, and delete tasks.
3. **Status Filtering**: Filter tasks by All, Active, or Completed status.
4. **Data Persistence**: Durable SQLite database storage ensuring data survives server restarts.
5. **Responsive UI**: Clean, mobile-friendly interface with visual distinction for completed tasks.

## Quick Start & Installation
1. Ensure Python 3.8+ is installed.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Open your browser at `http://localhost:5000`.

For detailed usage instructions, please refer to the [User Guide](specs/product-docs/USER-GUIDE.md).

## Running Tests
```bash
pytest
```
