import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
DB_NAME = 'todo.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS lists (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            list_id INTEGER NOT NULL,
            description TEXT NOT NULL,
            completed INTEGER NOT NULL DEFAULT 0,
            FOREIGN KEY (list_id) REFERENCES lists (id) ON DELETE CASCADE
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM lists')
    lists = c.fetchall()
    
    lists_with_tasks = []
    for lst in lists:
        c.execute('SELECT * FROM tasks WHERE list_id = ?', (lst['id'],))
        tasks = c.fetchall()
        lists_with_tasks.append({
            'id': lst['id'],
            'name': lst['name'],
            'tasks': tasks
        })
    conn.close()
    return render_template('index.html', lists=lists_with_tasks)

@app.route('/list/create', methods=['POST'])
def create_list():
    name = request.form.get('name')
    if name:
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute('INSERT INTO lists (name) VALUES (?)', (name,))
        conn.commit()
        conn.close()
    return redirect(url_for('index'))

@app.route('/list/<int:list_id>/task/add', methods=['POST'])
def add_task(list_id):
    description = request.form.get('description')
    if description:
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute('INSERT INTO tasks (list_id, description, completed) VALUES (?, ?, 0)', (list_id, description))
        conn.commit()
        conn.close()
    return redirect(url_for('index'))

@app.route('/task/<int:task_id>/toggle', methods=['POST'])
def toggle_task(task_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT completed FROM tasks WHERE id = ?', (task_id,))
    row = c.fetchone()
    if row:
        new_status = 0 if row[0] else 1
        c.execute('UPDATE tasks SET completed = ? WHERE id = ?', (new_status, task_id))
        conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/task/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/list/<int:list_id>/delete', methods=['POST'])
def delete_list(list_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('DELETE FROM tasks WHERE list_id = ?', (list_id,))
    c.execute('DELETE FROM lists WHERE id = ?', (list_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
else:
    init_db()
