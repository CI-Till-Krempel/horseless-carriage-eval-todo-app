import os
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# In-memory data store for MVP
lists_db = {}
tasks_db = {}
next_list_id = 1
next_task_id = 1

@app.route('/')
def index():
    global lists_db, tasks_db
    # Prepare lists with their tasks
    all_lists = []
    for l_id, l_data in lists_db.items():
        l_tasks = [t for t in tasks_db.values() if t['list_id'] == l_id]
        all_lists.append({
            'id': l_id,
            'name': l_data['name'],
            'tasks': l_tasks
        })
    return render_template('index.html', lists=all_lists)

@app.route('/lists', methods=['POST'])
def create_list():
    global next_list_id
    name = request.form.get('name') or (request.json and request.json.get('name'))
    if not name:
        return jsonify({'error': 'List name is required'}), 400
    
    l_id = str(next_list_id)
    next_list_id += 1
    lists_db[l_id] = {'id': l_id, 'name': name}
    
    if request.is_json or request.headers.get('Accept') == 'application/json':
        return jsonify(lists_db[l_id]), 201
    return redirect(url_for('index'))

@app.route('/lists/<list_id>', methods=['POST', 'DELETE'])
def delete_list(list_id):
    global lists_db, tasks_db
    # Support method override via form or header/method
    method = request.form.get('_method', request.method)
    if method == 'DELETE' or request.method == 'DELETE':
        if list_id in lists_db:
            del lists_db[list_id]
            # Cascade delete tasks
            to_delete = [t_id for t_id, t in tasks_db.items() if t['list_id'] == list_id]
            for t_id in to_delete:
                del tasks_db[t_id]
        if request.is_json or request.headers.get('Accept') == 'application/json':
            return jsonify({'success': True}), 200
        return redirect(url_for('index'))
    return jsonify({'error': 'Method not allowed'}), 405

@app.route('/lists/<list_id>/tasks', methods=['POST'])
def create_task(list_id):
    global next_task_id
    if list_id not in lists_db:
        return jsonify({'error': 'List not found'}), 404
    
    description = request.form.get('description') or (request.json and request.json.get('description'))
    if not description:
        return jsonify({'error': 'Task description is required'}), 400
    
    t_id = str(next_task_id)
    next_task_id += 1
    task = {
        'id': t_id,
        'list_id': list_id,
        'description': description,
        'completed': False
    }
    tasks_db[t_id] = task
    
    if request.is_json or request.headers.get('Accept') == 'application/json':
        return jsonify(task), 201
    return redirect(url_for('index'))

@app.route('/tasks/<task_id>/toggle', methods=['POST'])
def toggle_task(task_id):
    if task_id not in tasks_db:
        return jsonify({'error': 'Task not found'}), 404
    
    tasks_db[task_id]['completed'] = not tasks_db[task_id]['completed']
    
    if request.is_json or request.headers.get('Accept') == 'application/json':
        return jsonify(tasks_db[task_id]), 200
    return redirect(url_for('index'))

@app.route('/tasks/<task_id>', methods=['POST', 'DELETE'])
def delete_task(task_id):
    global tasks_db
    method = request.form.get('_method', request.method)
    if method == 'DELETE' or request.method == 'DELETE':
        if task_id in tasks_db:
            del tasks_db[task_id]
        if request.is_json or request.headers.get('Accept') == 'application/json':
            return jsonify({'success': True}), 200
        return redirect(url_for('index'))
    return jsonify({'error': 'Method not allowed'}), 405

if __name__ == '__main__':
    app.run(debug=True, port=5000)
