from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# In-memory storage for lists and tasks
# Structure: lists = [{ 'id': 1, 'name': 'Work', 'tasks': [{ 'id': 1, 'text': 'Finish report', 'completed': False }] }]
lists = []
list_id_counter = 1
task_id_counter = 1

@app.route('/')
def index():
    return render_template('index.html', lists=lists)

@app.route('/lists/create', methods=['POST'])
def create_list():
    global list_id_counter
    name = request.form.get('name', '').strip()
    if name:
        lists.append({
            'id': list_id_counter,
            'name': name,
            'tasks': []
        })
        list_id_counter += 1
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/delete', methods=['POST'])
def delete_list(list_id):
    global lists
    lists = [l for l in lists if l['id'] != list_id]
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/tasks/add', methods=['POST'])
def add_task(list_id):
    global task_id_counter
    text = request.form.get('text', '').strip()
    if text:
        for l in lists:
            if l['id'] == list_id:
                l['tasks'].append({
                    'id': task_id_counter,
                    'text': text,
                    'completed': False
                })
                task_id_counter += 1
                break
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/tasks/<int:task_id>/toggle', methods=['POST'])
def toggle_task(list_id, task_id):
    for l in lists:
        if l['id'] == list_id:
            for t in l['tasks']:
                if t['id'] == task_id:
                    t['completed'] = not t['completed']
                    break
            break
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/tasks/<int:task_id>/delete', methods=['POST'])
def delete_task(list_id, task_id):
    for l in lists:
        if l['id'] == list_id:
            l['tasks'] = [t for t in l['tasks'] if t['id'] != task_id]
            break
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
