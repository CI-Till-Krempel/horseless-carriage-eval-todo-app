import os
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DB_NAME = 'todo.db'

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS lists (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            list_id INTEGER NOT NULL,
            description TEXT NOT NULL,
            completed BOOLEAN NOT NULL DEFAULT 0,
            FOREIGN KEY (list_id) REFERENCES lists (id) ON DELETE CASCADE
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = get_db()
    lists = conn.execute('SELECT * FROM lists').fetchall()
    lists_with_tasks = []
    for lst in lists:
        tasks = conn.execute('SELECT * FROM tasks WHERE list_id = ?', (lst['id'],)).fetchall()
        lists_with_tasks.append({
            'id': lst['id'],
            'name': lst['name'],
            'tasks': tasks
        })
    conn.close()
    return render_template('index.html', lists=lists_with_tasks)

@app.route('/lists', methods=['POST'])
def create_list():
    name = request.form.get('name')
    if name:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO lists (name) VALUES (?)', (name,))
        conn.commit()
        list_id = cursor.lastrowid
        conn.close()
        if request.headers.get('Accept') == 'application/json' or request.is_json:
            return {'id': list_id, 'name': name}, 201
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/delete', methods=['POST'])
def delete_list(list_id):
    conn = get_db()
    conn.execute('DELETE FROM tasks WHERE list_id = ?', (list_id,))
    conn.execute('DELETE FROM lists WHERE id = ?', (list_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/tasks', methods=['POST'])
def add_task(list_id):
    description = request.form.get('description')
    if description:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO tasks (list_id, description, completed) VALUES (?, ?, 0)', (list_id, description))
        conn.commit()
        task_id = cursor.lastrowid
        conn.close()
        if request.headers.get('Accept') == 'application/json' or request.is_json:
            return {'id': task_id, 'list_id': list_id, 'description': description, 'completed': False}, 201
    return redirect(url_for('index'))

@app.route('/tasks/<int:task_id>/toggle', methods=['POST'])
def toggle_task(task_id):
    conn = get_db()
    task = conn.execute('SELECT * FROM tasks WHERE id = ?', (task_id,)).fetchone()
    if task:
        new_status = 0 if task['completed'] else 1
        conn.execute('UPDATE tasks SET completed = ? WHERE id = ?', (new_status, task_id))
        conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/tasks/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    conn = get_db()
    conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)
else:
    init_db()
