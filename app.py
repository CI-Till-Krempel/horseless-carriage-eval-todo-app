from flask import Flask, render_template, request, redirect, url_for
import os
import json

app = Flask(__name__)

DATA_FILE = 'data.json'

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                data = json.load(f)
                return data.get('lists', []), data.get('list_id_counter', 1), data.get('task_id_counter', 1)
        except Exception:
            pass
    return [], 1, 1

def save_data(lists, list_id_counter, task_id_counter):
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump({
                'lists': lists,
                'list_id_counter': list_id_counter,
                'task_id_counter': task_id_counter
            }, f, indent=2)
    except Exception as e:
        print(f"Error saving data: {e}")

lists, list_id_counter, task_id_counter = load_data()

@app.route('/')
def index():
    return render_template('index.html', lists=lists)

@app.route('/lists/create', methods=['POST'])
def create_list():
    global list_id_counter, task_id_counter, lists
    name = request.form.get('name', '').strip()
    if name:
        lists.append({
            'id': list_id_counter,
            'name': name,
            'tasks': []
        })
        list_id_counter += 1
        save_data(lists, list_id_counter, task_id_counter)
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/delete', methods=['POST'])
def delete_list(list_id):
    global lists, list_id_counter, task_id_counter
    lists = [l for l in lists if l['id'] != list_id]
    save_data(lists, list_id_counter, task_id_counter)
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/tasks/add', methods=['POST'])
def add_task(list_id):
    global task_id_counter, lists, list_id_counter
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
        save_data(lists, list_id_counter, task_id_counter)
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/tasks/<int:task_id>/toggle', methods=['POST'])
def toggle_task(list_id, task_id):
    global lists, list_id_counter, task_id_counter
    for l in lists:
        if l['id'] == list_id:
            for t in l['tasks']:
                if t['id'] == task_id:
                    t['completed'] = not t['completed']
                    break
            break
    save_data(lists, list_id_counter, task_id_counter)
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/tasks/<int:task_id>/delete', methods=['POST'])
def delete_task(list_id, task_id):
    global lists, list_id_counter, task_id_counter
    for l in lists:
        if l['id'] == list_id:
            l['tasks'] = [t for t in l['tasks'] if t['id'] != task_id]
            break
    save_data(lists, list_id_counter, task_id_counter)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
