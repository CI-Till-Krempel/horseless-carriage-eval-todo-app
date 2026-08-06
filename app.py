from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'super-secret-key'

# In-memory data store
# lists: {list_id: {'id': list_id, 'name': list_name}}
# tasks: {task_id: {'id': task_id, 'list_id': list_id, 'text': text, 'completed': bool}}
lists_store = {}
tasks_store = {}
list_counter = 1
task_counter = 1

@app.route('/')
def index():
    global list_counter, task_counter
    # Compute task counts for summary view
    lists_with_counts = []
    for lid, lst in lists_store.items():
        lst_tasks = [t for t in tasks_store.values() if t['list_id'] == lid]
        total_count = len(lst_tasks)
        completed_count = len([t for t in lst_tasks if t['completed']])
        lists_with_counts.append({
            'id': lid,
            'name': lst['name'],
            'total_count': total_count,
            'completed_count': completed_count
        })
    return render_template('index.html', lists=lists_with_counts)

@app.route('/lists', methods=['POST'])
def create_list():
    global list_counter
    name = request.form.get('name', '').strip()
    if not name:
        flash('List name cannot be empty.', 'error')
        return redirect(url_for('index'))
    
    list_id = str(list_counter)
    list_counter += 1
    lists_store[list_id] = {'id': list_id, 'name': name}
    flash('To-do list created successfully.', 'success')
    return redirect(url_for('index'))

@app.route('/lists/<list_id>')
def view_list(list_id):
    if list_id not in lists_store:
        flash('List not found.', 'error')
        return redirect(url_for('index'))
    lst = lists_store[list_id]
    lst_tasks = [t for t in tasks_store.values() if t['list_id'] == list_id]
    return render_template('list.html', list=lst, tasks=lst_tasks)

@app.route('/lists/<list_id>/tasks', methods=['POST'])
def add_task(list_id):
    global task_counter
    if list_id not in lists_store:
        flash('List not found.', 'error')
        return redirect(url_for('index'))
    
    text = request.form.get('text', '').strip()
    if not text:
        flash('Task description cannot be empty.', 'error')
        return redirect(url_for('view_list', list_id=list_id))
    
    task_id = str(task_counter)
    task_counter += 1
    tasks_store[task_id] = {'id': task_id, 'list_id': list_id, 'text': text, 'completed': False}
    flash('Task added successfully.', 'success')
    return redirect(url_for('view_list', list_id=list_id))

@app.route('/tasks/<task_id>/toggle', methods=['POST'])
def toggle_task(task_id):
    if task_id not in tasks_store:
        flash('Task not found.', 'error')
        return redirect(url_for('index'))
    task = tasks_store[task_id]
    task['completed'] = not task['completed']
    return redirect(url_for('view_list', list_id=task['list_id']))

@app.route('/tasks/<task_id>/delete', methods=['POST'])
def delete_task(task_id):
    if task_id not in tasks_store:
        flash('Task not found.', 'error')
        return redirect(url_for('index'))
    task = tasks_store[task_id]
    list_id = task['list_id']
    del tasks_store[task_id]
    flash('Task deleted.', 'success')
    return redirect(url_for('view_list', list_id=list_id))

@app.route('/lists/<list_id>/delete', methods=['POST'])
def delete_list(list_id):
    if list_id not in lists_store:
        flash('List not found.', 'error')
        return redirect(url_for('index'))
    # Delete all tasks associated with this list
    to_delete = [tid for tid, t in tasks_store.items() if t['list_id'] == list_id]
    for tid in to_delete:
        del tasks_store[tid]
    del lists_store[list_id]
    flash('List and its tasks deleted.', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
