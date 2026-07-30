import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data store for Sprint 1
# Lists format: { list_id: {'id': list_id, 'name': name, 'tasks': [ {'id': task_id, 'description': desc, 'completed': bool}, ... ] } }
lists_db = {}
next_list_id = 1
next_task_id = 1

@app.route('/')
def index():
    return render_template('index.html', lists=lists_db.values())

@app.route('/lists', methods=['POST'])
def create_list():
    global next_list_id
    name = request.form.get('name', '').strip()
    if name:
        lists_db[next_list_id] = {
            'id': next_list_id,
            'name': name,
            'tasks': []
        }
        next_list_id += 1
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/tasks', methods=['POST'])
def add_task(list_id):
    global next_task_id
    description = request.form.get('description', '').strip()
    if description and list_id in lists_db:
        lists_db[list_id]['tasks'].append({
            'id': next_task_id,
            'description': description,
            'completed': False
        })
        next_task_id += 1
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/tasks/<int:task_id>/toggle', methods=['POST'])
def toggle_task(list_id, task_id):
    if list_id in lists_db:
        for task in lists_db[list_id]['tasks']:
            if task['id'] == task_id:
                task['completed'] = not task['completed']
                break
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/delete', methods=['POST'])
def delete_list(list_id):
    if list_id in lists_db:
        del lists_db[list_id]
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/tasks/<int:task_id>/delete', methods=['POST'])
def delete_task(list_id, task_id):
    if list_id in lists_db:
        lists_db[list_id]['tasks'] = [t for t in lists_db[list_id]['tasks'] if t['id'] != task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
