from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory database for Sprint 1 MVP
# Structure: lists = [{'id': 1, 'name': 'Groceries', 'tasks': [{'id': 1, 'text': 'Milk', 'completed': False}]}]
todo_lists = []
next_list_id = 1
next_task_id = 1

@app.route('/')
def index():
    return render_template('index.html', lists=todo_lists)

@app.route('/lists', methods=['POST'])
def create_list():
    global next_list_id
    name = request.form.get('name')
    if name and name.strip():
        todo_lists.append({
            'id': next_list_id,
            'name': name.strip(),
            'tasks': []
        })
        next_list_id += 1
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/tasks', methods=['POST'])
def add_task(list_id):
    global next_task_id
    text = request.form.get('text')
    if text and text.strip():
        for lst in todo_lists:
            if lst['id'] == list_id:
                lst['tasks'].append({
                    'id': next_task_id,
                    'text': text.strip(),
                    'completed': False
                })
                next_task_id += 1
                break
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/tasks/<int:task_id>/toggle', methods=['POST'])
def toggle_task(list_id, task_id):
    for lst in todo_lists:
        if lst['id'] == list_id:
            for task in lst['tasks']:
                if task['id'] == task_id:
                    task['completed'] = not task['completed']
                    break
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/tasks/<int:task_id>/delete', methods=['POST'])
def delete_task(list_id, task_id):
    for lst in todo_lists:
        if lst['id'] == list_id:
            lst['tasks'] = [t for t in lst['tasks'] if t['id'] != task_id]
            break
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/delete', methods=['POST'])
def delete_list(list_id):
    global todo_lists
    todo_lists = [lst for lst in todo_lists if lst['id'] != list_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
