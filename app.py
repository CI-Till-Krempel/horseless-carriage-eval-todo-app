import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data store for lists and tasks
# Lists: { list_id: {'id': list_id, 'name': name, 'tasks': [ { 'id': task_id, 'text': text, 'done': False }, ... ] } }
lists_db = {}
next_list_id = 1
next_task_id = 1

@app.route('/')
def index():
    return render_template('index.html', lists=list(lists_db.values()))

@app.route('/lists', methods=['POST'])
def create_list():
    global next_list_id
    name = request.form.get('name', '').strip()
    if name:
        list_id = str(next_list_id)
        next_list_id += 1
        lists_db[list_id] = {'id': list_id, 'name': name, 'tasks': []}
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/tasks', methods=['POST'])
def add_task(list_id):
    global next_task_id
    text = request.form.get('text', '').strip()
    if text and list_id in lists_db:
        task_id = str(next_task_id)
        next_task_id += 1
        lists_db[list_id]['tasks'].append({'id': task_id, 'text': text, 'done': False})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
