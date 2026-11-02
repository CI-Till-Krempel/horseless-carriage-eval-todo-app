import os
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# In-memory storage for MVP
lists = []
tasks = []

@app.route('/')
def index():
    return render_template('index.html', lists=lists, tasks=tasks)

@app.route('/lists', methods=['POST'])
def create_list():
    name = request.form.get('name')
    if name:
        list_id = len(lists) + 1
        lists.append({'id': list_id, 'name': name})
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/tasks', methods=['POST'])
def add_task(list_id):
    content = request.form.get('content') or request.form.get('description')
    if content:
        task_id = len(tasks) + 1
        tasks.append({
            'id': task_id,
            'list_id': list_id,
            'content': content,
            'description': content,
            'completed': False
        })
    return redirect(url_for('index'))

@app.route('/tasks/<int:task_id>/toggle', methods=['POST'])
def toggle_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = not task['completed']
            break
    return redirect(url_for('index'))

@app.route('/tasks/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/delete', methods=['POST'])
def delete_list(list_id):
    global lists, tasks
    lists = [l for l in lists if l['id'] != list_id]
    tasks = [t for t in tasks if t['list_id'] != list_id]
    return redirect(url_for('index'))

@app.route('/api/lists', methods=['GET', 'POST'])
def api_lists():
    global lists
    if request.method == 'POST':
        data = request.get_json() or {}
        name = data.get('name')
        if not name:
            return jsonify({'error': 'Name is required'}), 400
        list_id = len(lists) + 1
        new_list = {'id': list_id, 'name': name}
        lists.append(new_list)
        return jsonify(new_list), 201
    return jsonify(lists)

@app.route('/api/lists/<int:list_id>/tasks', methods=['GET', 'POST'])
def api_tasks(list_id):
    global tasks
    if request.method == 'POST':
        data = request.get_json() or {}
        content = data.get('content') or data.get('description')
        if not content:
            return jsonify({'error': 'Content is required'}), 400
        task_id = len(tasks) + 1
        new_task = {
            'id': task_id,
            'list_id': list_id,
            'content': content,
            'description': content,
            'completed': False
        }
        tasks.append(new_task)
        return jsonify(new_task), 201
    list_tasks = [t for t in tasks if t['list_id'] == list_id]
    return jsonify(list_tasks)

if __name__ == '__main__':
    app.run(debug=True)
