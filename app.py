from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data store for lists and tasks
todo_lists = []

@app.route('/')
def index():
    return render_template('index.html', lists=todo_lists)

@app.route('/lists', methods=['POST'])
def create_list():
    name = request.form.get('name')
    if name and name.strip():
        todo_lists.append({'id': len(todo_lists) + 1, 'name': name.strip(), 'tasks': []})
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/tasks', methods=['POST'])
def add_task(list_id):
    content = request.form.get('content')
    if content and content.strip():
        for lst in todo_lists:
            if lst['id'] == list_id:
                lst['tasks'].append({
                    'id': len(lst['tasks']) + 1,
                    'content': content.strip(),
                    'completed': False
                })
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
            break
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
