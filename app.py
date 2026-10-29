from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# In-memory storage for MVP / test
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
    title = request.form.get('title')
    if title:
        task_id = len(tasks) + 1
        tasks.append({'id': task_id, 'list_id': list_id, 'title': title, 'completed': False})
    return redirect(url_for('index'))

@app.route('/tasks/<int:task_id>/toggle', methods=['POST'])
def toggle_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = not task['completed']
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

if __name__ == '__main__':
    app.run(debug=True)
