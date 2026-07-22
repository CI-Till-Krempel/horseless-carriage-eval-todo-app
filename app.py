import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
DB_PATH = 'todo.db'

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db(db_path=DB_PATH):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS lists (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            list_id INTEGER NOT NULL,
            text TEXT NOT NULL,
            completed BOOLEAN NOT NULL DEFAULT 0,
            FOREIGN KEY (list_id) REFERENCES lists (id) ON DELETE CASCADE
        )
    ''')
    conn.commit()
    conn.close()

# Initialize DB on startup
init_db()

@app.route('/')
def index():
    status_filter = request.args.get('filter', 'all')
    conn = get_db()
    lists = conn.execute('SELECT * FROM lists').fetchall()
    
    if status_filter == 'active':
        tasks = conn.execute('SELECT * FROM tasks WHERE completed = 0').fetchall()
    elif status_filter == 'completed':
        tasks = conn.execute('SELECT * FROM tasks WHERE completed = 1').fetchall()
    else:
        tasks = conn.execute('SELECT * FROM tasks').fetchall()
        
    conn.close()
    return render_template('index.html', lists=lists, tasks=tasks, current_filter=status_filter)

@app.route('/lists', methods=['POST'])
def create_list():
    name = request.form.get('name', '').strip()
    if name:
        conn = get_db()
        conn.execute('INSERT INTO lists (name) VALUES (?)', (name,))
        conn.commit()
        conn.close()
    return redirect(url_for('index', filter=request.args.get('filter', 'all')))

@app.route('/lists/<int:list_id>/delete', methods=['POST'])
def delete_list(list_id):
    conn = get_db()
    conn.execute('DELETE FROM tasks WHERE list_id = ?', (list_id,))
    conn.execute('DELETE FROM lists WHERE id = ?', (list_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index', filter=request.args.get('filter', 'all')))

@app.route('/lists/<int:list_id>/tasks', methods=['POST'])
def add_task(list_id):
    text = request.form.get('text', '').strip()
    if text:
        conn = get_db()
        conn.execute('INSERT INTO tasks (list_id, text, completed) VALUES (?, ?, 0)', (list_id, text))
        conn.commit()
        conn.close()
    return redirect(url_for('index', filter=request.args.get('filter', 'all')))

@app.route('/tasks/<int:task_id>/toggle', methods=['POST'])
def toggle_task(task_id):
    conn = get_db()
    task = conn.execute('SELECT completed FROM tasks WHERE id = ?', (task_id,)).fetchone()
    if task:
        new_status = 0 if task['completed'] else 1
        conn.execute('UPDATE tasks SET completed = ? WHERE id = ?', (new_status, task_id))
        conn.commit()
    conn.close()
    return redirect(url_for('index', filter=request.args.get('filter', 'all')))

@app.route('/tasks/<int:task_id>/edit', methods=['POST'])
def edit_task(task_id):
    new_text = request.form.get('text', '').strip()
    if new_text:
        conn = get_db()
        conn.execute('UPDATE tasks SET text = ? WHERE id = ?', (new_text, task_id))
        conn.commit()
        conn.close()
    return redirect(url_for('index', filter=request.args.get('filter', 'all')))

@app.route('/tasks/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    conn = get_db()
    conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index', filter=request.args.get('filter', 'all')))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
