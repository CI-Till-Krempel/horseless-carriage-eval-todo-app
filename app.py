from flask import Flask, render_template, request, jsonify
import uuid

app = Flask(__name__)

# In-memory database
# lists = { list_id: { "id": str, "name": str, "tasks": [ { "id": str, "description": str, "completed": bool } ] } }
lists_db = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/lists', methods=['GET'])
def get_lists():
    return jsonify(list(lists_db.values()))

@app.route('/api/lists', methods=['POST'])
def create_list():
    data = request.json or {}
    name = data.get('name', '').strip()
    if not name:
        return jsonify({'error': 'List name is required'}), 400
    
    list_id = str(uuid.uuid4())
    new_list = {
        'id': list_id,
        'name': name,
        'tasks': []
    }
    lists_db[list_id] = new_list
    return jsonify(new_list), 201

@app.route('/api/lists/<list_id>/tasks', methods=['POST'])
def add_task(list_id):
    if list_id not in lists_db:
        return jsonify({'error': 'List not found'}), 404
    
    data = request.json or {}
    description = data.get('description', '').strip()
    if not description:
        return jsonify({'error': 'Task description is required'}), 400
    
    task_id = str(uuid.uuid4())
    new_task = {
        'id': task_id,
        'description': description,
        'completed': False
    }
    lists_db[list_id]['tasks'].append(new_task)
    return jsonify(new_task), 201

@app.route('/api/lists/<list_id>', methods=['DELETE'])
def delete_list(list_id):
    if list_id not in lists_db:
        return jsonify({'error': 'List not found'}), 404
    del lists_db[list_id]
    return jsonify({'success': True})

@app.route('/api/lists/<list_id>/tasks/<task_id>', methods=['DELETE'])
def delete_task(list_id, task_id):
    if list_id not in lists_db:
        return jsonify({'error': 'List not found'}), 404
    
    t_list = lists_db[list_id]
    tasks = t_list['tasks']
    t_list['tasks'] = [t for t in tasks if t['id'] != task_id]
    return jsonify({'success': True})

@app.route('/api/lists/<list_id>/tasks/<task_id>/toggle', methods=['PATCH'])
def toggle_task(list_id, task_id):
    if list_id not in lists_db:
        return jsonify({'error': 'List not found'}), 404
    
    t_list = lists_db[list_id]
    for t in t_list['tasks']:
        if t['id'] == task_id:
            t['completed'] = not t['completed']
            return jsonify(t)
            
    return jsonify({'error': 'Task not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
