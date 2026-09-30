import os
import json
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
DATA_FILE = os.path.join(os.path.dirname(__file__), 'todo_data.json')

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        except Exception:
            return {"lists": []}
    return {"lists": []}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/')
def index():
    data = load_data()
    return render_template('index.html', lists=data.get('lists', []))

@app.route('/lists', methods=['POST'])
def create_list():
    name = request.form.get('name', '').strip()
    if name:
        data = load_data()
        new_list = {
            "id": str(len(data['lists']) + 1),
            "name": name,
            "tasks": []
        }
        data['lists'].append(new_list)
        save_data(data)
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/tasks', methods=['POST'])
def add_task(list_id):
    content = request.form.get('content', '').strip()
    if content:
        data = load_data()
        for lst in data['lists']:
            if lst['id'] == list_id:
                new_task = {
                    "id": str(len(lst['tasks']) + 1),
                    "content": content,
                    "completed": False
                }
                lst['tasks'].append(new_task)
                break
        save_data(data)
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/tasks/<task_id>/toggle', methods=['POST'])
def toggle_task(list_id, task_id):
    data = load_data()
    for lst in data['lists']:
        if lst['id'] == list_id:
            for task in lst['tasks']:
                if task['id'] == task_id:
                    task['completed'] = not task['completed']
                    break
            break
    save_data(data)
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/tasks/<task_id>/delete', methods=['POST'])
def delete_task(list_id, task_id):
    data = load_data()
    for lst in data['lists']:
        if lst['id'] == list_id:
            lst['tasks'] = [t for t in lst['tasks'] if t['id'] != task_id]
            break
    save_data(data)
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/delete', methods=['POST'])
def delete_list(list_id):
    data = load_data()
    data['lists'] = [lst for lst in data['lists'] if lst['id'] != list_id]
    save_data(data)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
