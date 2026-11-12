from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# In-memory storage for lists and tasks
lists = {}
tasks = {}
task_counter = 1

@app.route('/')
def index():
    return render_template('index.html', lists=lists, tasks=tasks)

@app.route('/lists', methods=['POST'])
def create_list():
    global task_counter
    title = request.form.get('title')
    if title:
        list_id = str(len(lists) + 1)
        lists[list_id] = {'id': list_id, 'title': title}
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/tasks', methods=['POST'])
def add_task(list_id):
    global task_counter
    content = request.form.get('content')
    if content and list_id in lists:
        task_id = str(task_counter)
        task_counter += 1
        tasks[task_id] = {'id': task_id, 'list_id': list_id, 'content': content, 'completed': False}
    return redirect(url_for('index'))

@app.route('/tasks/<task_id>/toggle', methods=['POST'])
def toggle_task(task_id):
    if task_id in tasks:
        tasks[task_id]['completed'] = not tasks[task_id]['completed']
    return redirect(url_for('index'))

@app.route('/api/lists', methods=['GET', 'POST'])
def api_lists():
    global task_counter
    if request.method == 'POST':
        data = request.json or {}
        title = data.get('title')
        if not title:
            return jsonify({'error': 'Title is required'}), 400
        list_id = str(len(lists) + 1)
        lists[list_id] = {'id': list_id, 'title': title}
        return jsonify(lists[list_id]), 201
    return jsonify(list(lists.values()))

@app.route('/api/lists/<list_id>/tasks', methods=['GET', 'POST'])
def api_tasks(list_id):
    global task_counter
    if list_id not in lists:
        return jsonify({'error': 'List not found'}), 404
    if request.method == 'POST':
        data = request.json or {}
        content = data.get('content')
        if not content:
            return jsonify({'error': 'Content is required'}), 400
        task_id = str(task_counter)
        task_counter += 1
        tasks[task_id] = {'id': task_id, 'list_id': list_id, 'content': content, 'completed': False}
        return jsonify(tasks[task_id]), 201
    list_tasks = [t for t in tasks.values() if t['list_id'] == list_id]
    return jsonify(list_tasks)

@app.route('/api/tasks/<task_id>/toggle', methods=['POST'])
def api_toggle_task(task_id):
    if task_id not in tasks:
        return jsonify({'error': 'Task not found'}), 404
    tasks[task_id]['completed'] = not tasks[task_id]['completed']
    return jsonify(tasks[task_id])

if __name__ == '__main__':
    app.run(debug=True)
