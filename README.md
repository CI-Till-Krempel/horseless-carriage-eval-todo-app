# To-Do List Web Application

A simple, clean, and responsive to-do list web application built with Python (Flask), SQLAlchemy, and Tailwind CSS.

## Features

1. **Create Lists**: Organize tasks into separate to-do lists.
2. **Add Tasks**: Add short text descriptions to specific lists.
3. **Toggle Completion**: Mark tasks as complete or incomplete with immediate visual feedback (strikethrough styling).
4. **Delete Tasks**: Remove individual tasks that are no longer needed.
5. **Delete Lists**: Delete entire lists along with all their contained tasks (cascade deletion).
6. **Complete Overview**: View all lists and tasks on a single intuitive dashboard.

---

## Getting Started

### Prerequisites

- Python 3.9+
- `pip`

### Installation & Running Locally

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

4. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

---

## Running Tests

Run the automated test suite using `pytest`:
```bash
pytest
```
