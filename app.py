from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# In-memory storage for lists and tasks
# lists: dict mapping list_id (int) -> dict with 'id', 'title', 'tasks' (list of dicts)
todo_lists = {}
next_list_id = 1
next_task_id = 1

@app.route('/')
def index():
    return render_template('index.html', lists=todo_lists.values())

@app.route('/lists', methods=['POST'])
def create_list():
    global next_list_id
    title = request.form.get('title') or (request.json and request.json.get('title'))
    if not title:
        if request.is_json:
            return jsonify({'error': 'Title is required'}), 400
        return redirect(url_for('index'))
    
    list_id = next_list_id
    next_list_id += 1
    todo_lists[list_id] = {
        'id': list_id,
        'title': title,
        'tasks': []
    }
    
    if request.is_json or request.headers.get('Accept') == 'application/json':
        return jsonify(todo_lists[list_id]), 201
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/tasks', methods=['POST'])
def add_task(list_id):
    global next_task_id
    if list_id not in todo_lists:
        if request.is_json or request.headers.get('Accept') == 'application/json':
            return jsonify({'error': 'List not found'}), 404
        return redirect(url_for('index'))
    
    description = request.form.get('description') or (request.json and request.json.get('description'))
    if not description:
        if request.is_json or request.headers.get('Accept') == 'application/json':
            return jsonify({'error': 'Description is required'}), 400
        return redirect(url_for('index'))
    
    task_id = next_task_id
    next_task_id += 1
    task = {
        'id': task_id,
        'description': description,
        'completed': False
    }
    todo_lists[list_id]['tasks'].append(task)
    
    if request.is_json or request.headers.get('Accept') == 'application/json':
        return jsonify(task), 201
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
