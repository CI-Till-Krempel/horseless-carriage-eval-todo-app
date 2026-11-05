from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# In-memory database stores
lists_db = {}
tasks_db = {}

next_list_id = 1
next_task_id = 1

def wants_json():
    return request.is_json or (request.headers.get('Content-Type') == 'application/json') or ('application/json' in request.accept_mimetypes.best)

@app.route('/')
def index():
    return render_template('index.html', lists=lists_db.values(), tasks=tasks_db.values())

@app.route('/lists', methods=['POST'])
def create_list():
    global next_list_id
    name = request.form.get('name') or (request.json and request.json.get('name'))
    if not name:
        if wants_json():
            return jsonify({'error': 'Name is required'}), 400
        return redirect(url_for('index'))
    
    list_id = str(next_list_id)
    next_list_id += 1
    lists_db[list_id] = {'id': list_id, 'name': name}
    
    if wants_json():
        return jsonify(lists_db[list_id]), 201
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/tasks', methods=['POST'])
def add_task(list_id):
    global next_task_id
    if list_id not in lists_db:
        if wants_json():
            return jsonify({'error': 'List not found'}), 404
        return redirect(url_for('index'))
    
    description = request.form.get('description') or (request.json and request.json.get('description'))
    if not description:
        if wants_json():
            return jsonify({'error': 'Description is required'}), 400
        return redirect(url_for('index'))
    
    task_id = str(next_task_id)
    next_task_id += 1
    tasks_db[task_id] = {
        'id': task_id,
        'list_id': list_id,
        'description': description,
        'completed': False
    }
    
    if wants_json():
        return jsonify(tasks_db[task_id]), 201
    return redirect(url_for('index'))

@app.route('/tasks/<task_id>/toggle', methods=['POST'])
def toggle_task(task_id):
    if task_id not in tasks_db:
        if wants_json():
            return jsonify({'error': 'Task not found'}), 404
        return redirect(url_for('index'))
    
    tasks_db[task_id]['completed'] = not tasks_db[task_id]['completed']
    
    if wants_json():
        return jsonify(tasks_db[task_id]), 200
    return redirect(url_for('index'))

@app.route('/tasks/<task_id>/delete', methods=['POST'])
def delete_task(task_id):
    if task_id not in tasks_db:
        if wants_json():
            return jsonify({'error': 'Task not found'}), 404
        return redirect(url_for('index'))

    del tasks_db[task_id]
    
    if wants_json():
        return jsonify({'success': True}), 200
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/delete', methods=['POST'])
def delete_list(list_id):
    if list_id not in lists_db:
        if wants_json():
            return jsonify({'error': 'List not found'}), 404
        return redirect(url_for('index'))

    del lists_db[list_id]
    # Cascade delete associated tasks
    to_delete = [tid for tid, t in tasks_db.items() if t['list_id'] == list_id]
    for tid in to_delete:
        del tasks_db[tid]
            
    if wants_json():
        return jsonify({'success': True}), 200
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
