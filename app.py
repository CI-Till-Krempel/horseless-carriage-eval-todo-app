from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data store for To-Do Lists and Tasks (US-0004 explicit file touch)
todo_lists = {}
list_counter = 1
task_counter = 1

@app.route('/')
def index():
    return render_template('index.html', lists=todo_lists.values())

@app.route('/lists', methods=['POST'])
def create_list():
    global list_counter
    name = request.form.get('name', '').strip()
    if name:
        list_id = str(list_counter)
        list_counter += 1
        todo_lists[list_id] = {
            'id': list_id,
            'name': name,
            'tasks': []
        }
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/tasks', methods=['POST'])
def add_task(list_id):
    global task_counter
    if list_id in todo_lists:
        description = request.form.get('description', '').strip()
        if description:
            task_id = str(task_counter)
            task_counter += 1
            todo_lists[list_id]['tasks'].append({
                'id': task_id,
                'description': description,
                'completed': False
            })
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/tasks/<task_id>/toggle', methods=['POST'])
def toggle_task(list_id, task_id):
    if list_id in todo_lists:
        for task in todo_lists[list_id]['tasks']:
            if task['id'] == task_id:
                task['completed'] = not task['completed']
                break
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/tasks/<task_id>/delete', methods=['POST'])
def delete_task(list_id, task_id):
    if list_id in todo_lists:
        todo_lists[list_id]['tasks'] = [t for t in todo_lists[list_id]['tasks'] if t['id'] != task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
