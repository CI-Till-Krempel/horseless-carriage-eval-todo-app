from flask import Flask, render_template, request, redirect, url_for
from database import init_db, get_db

app = Flask(__name__)

@app.route('/')
def index():
    db = get_db()
    lists_cursor = db.execute('SELECT * FROM lists').fetchall()
    lists = []
    for row in lists_cursor:
        lst = dict(row)
        tasks = db.execute('SELECT * FROM tasks WHERE list_id = ?', (lst['id'],)).fetchall()
        lst['tasks'] = [dict(t) for t in tasks]
        lists.append(lst)
    db.close()
    return render_template('index.html', lists=lists)

@app.route('/lists', methods=['POST'])
def create_list():
    name = request.form.get('name')
    if name:
        db = get_db()
        db.execute('INSERT INTO lists (name) VALUES (?)', (name,))
        db.commit()
        db.close()
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/delete', methods=['POST'])
def delete_list(list_id):
    db = get_db()
    db.execute('DELETE FROM tasks WHERE list_id = ?', (list_id,))
    db.execute('DELETE FROM lists WHERE id = ?', (list_id,))
    db.commit()
    db.close()
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/tasks', methods=['POST'])
def add_task(list_id):
    description = request.form.get('description')
    if description:
        db = get_db()
        db.execute('INSERT INTO tasks (list_id, description, completed) VALUES (?, ?, 0)', (list_id, description))
        db.commit()
        db.close()
    return redirect(url_for('index'))

@app.route('/tasks/<int:task_id>/toggle', methods=['POST'])
def toggle_task(task_id):
    db = get_db()
    task = db.execute('SELECT completed FROM tasks WHERE id = ?', (task_id,)).fetchone()
    if task:
        new_status = 0 if task['completed'] else 1
        db.execute('UPDATE tasks SET completed = ? WHERE id = ?', (new_status, task_id))
        db.commit()
    db.close()
    return redirect(url_for('index'))

@app.route('/tasks/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    db = get_db()
    db.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    db.commit()
    db.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)
