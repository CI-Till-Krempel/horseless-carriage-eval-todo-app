import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for MVP
lists_db = {}
tasks_db = {}
task_id_counter = 1
list_id_counter = 1

@app.route('/')
def index():
    return render_template('index.html', lists=lists_db, tasks=tasks_db)

@app.route('/lists', methods=['POST'])
def create_list():
    global list_id_counter
    title = request.form.get('title')
    if title:
        list_id = str(list_id_counter)
        list_id_counter += 1
        lists_db[list_id] = {'id': list_id, 'title': title}
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/tasks', methods=['POST'])
def add_task(list_id):
    global task_id_counter
    content = request.form.get('content')
    if content and list_id in lists_db:
        task_id = str(task_id_counter)
        task_id_counter += 1
        tasks_db[task_id] = {'id': task_id, 'list_id': list_id, 'content': content, 'completed': False}
    return redirect(url_for('index'))

@app.route('/tasks/<task_id>/toggle', methods=['POST'])
def toggle_task(task_id):
    if task_id in tasks_db:
        tasks_db[task_id]['completed'] = not tasks_db[task_id]['completed']
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
