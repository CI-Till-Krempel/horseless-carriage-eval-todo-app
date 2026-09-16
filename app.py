from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data store for lists and tasks
# Lists: { list_id: { 'id': list_id, 'name': list_name } }
# Tasks: { task_id: { 'id': task_id, 'list_id': list_id, 'description': description, 'completed': bool } }
lists_db = {}
tasks_db = {}
list_id_counter = 1
task_id_counter = 1

@app.route('/')
def index():
    # Group tasks by list
    lists_with_tasks = []
    for l_id, lst in lists_db.items():
        lst_tasks = [t for t in tasks_db.values() if t['list_id'] == l_id]
        lists_with_tasks.append({
            'id': lst['id'],
            'name': lst['name'],
            'tasks': lst_tasks
        })
    return render_template('index.html', lists=lists_with_tasks)

@app.route('/lists', methods=['POST'])
def create_list():
    global list_id_counter
    name = request.form.get('name')
    if name:
        lists_db[list_id_counter] = {'id': list_id_counter, 'name': name}
        list_id_counter += 1
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/tasks', methods=['POST'])
def add_task(list_id):
    global task_id_counter
    description = request.form.get('description')
    if description and list_id in lists_db:
        tasks_db[task_id_counter] = {
            'id': task_id_counter,
            'list_id': list_id,
            'description': description,
            'completed': False
        }
        task_id_counter += 1
    return redirect(url_for('index'))

@app.route('/tasks/<int:task_id>/toggle', methods=['POST'])
def toggle_task(task_id):
    if task_id in tasks_db:
        tasks_db[task_id]['completed'] = not tasks_db[task_id]['completed']
    return redirect(url_for('index'))

@app.route('/tasks/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    if task_id in tasks_db:
        del tasks_db[task_id]
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/delete', methods=['POST'])
def delete_list(list_id):
    if list_id in lists_db:
        # Delete associated tasks
        to_delete = [t_id for t_id, t in tasks_db.items() if t['list_id'] == list_id]
        for t_id in to_delete:
            del tasks_db[t_id]
        del lists_db[list_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
