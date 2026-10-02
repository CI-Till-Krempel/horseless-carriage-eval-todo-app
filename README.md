# To-Do List Web App

A simple, lightweight to-do list web application built with Python, Flask, and SQLite.

## Features
- Create to-do lists with custom names.
- Add tasks with short text descriptions to any list.
- Mark tasks as complete or incomplete with visual distinction.
- Delete individual tasks.
- Delete entire lists along with all their associated tasks.

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/CI-Till-Krempel/horseless-carriage-eval-todo-app.git
   cd horseless-carriage-eval-todo-app
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to `http://127.0.0.1:5000`.

## Running Tests
```bash
python run_tests.py
```

## Development Workflow & Branch Synchronization
To prevent integration delays and merge conflicts, active feature branches should be regularly synchronized with `develop`:
```bash
git fetch origin
git rebase origin/eval/0.1.0-run44/develop
```
