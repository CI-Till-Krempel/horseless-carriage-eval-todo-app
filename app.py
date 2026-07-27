from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'todo-secret-key'

# In-memory data store
lists = []

@app.route('/')
def index():
    return render_template('index.html', lists=lists)

@app.route('/lists', methods=['POST'])
def create_list():
    name = request.form.get('name', '').strip()
    if not name:
        flash('List name cannot be empty or whitespace.', 'error')
    else:
        new_list = {'id': len(lists) + 1, 'name': name, 'tasks': []}
        lists.append(new_list)
        flash('To-do list created successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/tasks', methods=['POST'])
def add_task(list_id):
    description = request.form.get('description', '').strip()
    if not description:
        flash('Task description cannot be empty.', 'error')
    else:
        target_list = next((lst for lst in lists if lst['id'] == list_id), None)
        if target_list:
            new_task = {'id': len(target_list['tasks']) + 1, 'description': description, 'completed': False}
            target_list['tasks'].append(new_task)
            flash('Task added successfully!', 'success')
        else:
            flash('To-do list not found.', 'error')
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/tasks/<int:task_id>/toggle', methods=['POST'])
def toggle_task(list_id, task_id):
    target_list = next((lst for lst in lists if lst['id'] == list_id), None)
    if target_list:
        target_task = next((t for t in target_list['tasks'] if t['id'] == task_id), None)
        if target_task:
            target_task['completed'] = not target_task['completed']
            flash('Task status updated!', 'success')
        else:
            flash('Task not found.', 'error')
    else:
        flash('To-do list not found.', 'error')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
