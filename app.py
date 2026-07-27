import os
import json
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'

DATA_FILE = 'todos.json'

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_data(data):
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=4)
    except Exception:
        pass

@app.route('/')
def index():
    data = load_data()
    lists = data.get('lists', {})
    return render_template('index.html', lists=lists.values())

@app.route('/help')
def help_page():
    return render_template('help.html')

@app.route('/lists', methods=['POST'])
def create_list():
    data = load_data()
    lists = data.get('lists', {})
    counter = data.get('list_id_counter', 1)
    
    name = request.form.get('name', '').strip()
    if not name:
        flash('List name cannot be empty or whitespace.', 'error')
    else:
        l_id = str(counter)
        counter += 1
        lists[l_id] = {
            'id': l_id,
            'name': name,
            'tasks': {}
        }
        data['lists'] = lists
        data['list_id_counter'] = counter
        save_data(data)
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/delete', methods=['POST'])
def delete_list(list_id):
    data = load_data()
    lists = data.get('lists', {})
    if list_id in lists:
        del lists[list_id]
        data['lists'] = lists
        save_data(data)
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/tasks', methods=['POST'])
def add_task(list_id):
    data = load_data()
    lists = data.get('lists', {})
    counter = data.get('task_id_counter', 1)

    if list_id in lists:
        title = request.form.get('title', '').strip()
        if not title:
            flash('Task description cannot be empty or whitespace.', 'error')
        else:
            t_id = str(counter)
            counter += 1
            lists[list_id]['tasks'][t_id] = {
                'id': t_id,
                'title': title,
                'completed': False
            }
            data['lists'] = lists
            data['task_id_counter'] = counter
            save_data(data)
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/tasks/<task_id>/toggle', methods=['POST'])
def toggle_task(list_id, task_id):
    data = load_data()
    lists = data.get('lists', {})
    if list_id in lists and task_id in lists[list_id]['tasks']:
        task = lists[list_id]['tasks'][task_id]
        task['completed'] = not task['completed']
        data['lists'] = lists
        save_data(data)
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/tasks/<task_id>/delete', methods=['POST'])
def delete_task(list_id, task_id):
    data = load_data()
    lists = data.get('lists', {})
    if list_id in lists and task_id in lists[list_id]['tasks']:
        del lists[list_id]['tasks'][task_id]
        data['lists'] = lists
        save_data(data)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
