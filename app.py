import os
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DB_NAME = 'todo.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS todo_lists (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            list_id INTEGER,
            description TEXT NOT NULL,
            completed BOOLEAN NOT NULL DEFAULT 0,
            FOREIGN KEY (list_id) REFERENCES todo_lists (id) ON DELETE CASCADE
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM todo_lists')
    lists = cursor.fetchall()
    
    selected_list_id = request.args.get('list_id', type=int)
    selected_list = None
    tasks = []
    
    if selected_list_id:
        cursor.execute('SELECT * FROM todo_lists WHERE id = ?', (selected_list_id,))
        selected_list = cursor.fetchone()
        cursor.execute('SELECT * FROM tasks WHERE list_id = ?', (selected_list_id,))
        tasks = cursor.fetchall()
    elif lists:
        selected_list = lists[0]
        cursor.execute('SELECT * FROM tasks WHERE list_id = ?', (selected_list['id'],))
        tasks = cursor.fetchall()

    conn.close()
    return render_template('index.html', lists=lists, selected_list=selected_list, tasks=tasks)

@app.route('/lists', methods=['POST'])
def create_list():
    name = request.form.get('name')
    if name:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO todo_lists (name) VALUES (?)', (name,))
        conn.commit()
        new_id = cursor.lastrowid
        conn.close()
        return redirect(url_for('index', list_id=new_id))
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/tasks', methods=['POST'])
def add_task(list_id):
    description = request.form.get('description')
    if description:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO tasks (list_id, description, completed) VALUES (?, ?, 0)', (list_id, description))
        conn.commit()
        conn.close()
    return redirect(url_for('index', list_id=list_id))

@app.route('/tasks/<int:task_id>/toggle', methods=['POST'])
def toggle_task(task_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT completed, list_id FROM tasks WHERE id = ?', (task_id,))
    row = cursor.fetchone()
    if row:
        completed, list_id = row[0], row[1]
        new_status = 0 if completed else 1
        cursor.execute('UPDATE tasks SET completed = ? WHERE id = ?', (new_status, task_id))
        conn.commit()
        conn.close()
        return redirect(url_for('index', list_id=list_id))
    conn.close()
    return redirect(url_for('index'))

@app.route('/tasks/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT list_id FROM tasks WHERE id = ?', (task_id,))
    row = cursor.fetchone()
    list_id = row[0] if row else None
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index', list_id=list_id))

@app.route('/lists/<int:list_id>/delete', methods=['POST'])
def delete_list(list_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE list_id = ?', (list_id,))
    cursor.execute('DELETE FROM todo_lists WHERE id = ?', (list_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)
else:
    init_db()
