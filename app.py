from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for to-do lists and tasks
# Structure: lists = { list_id: { 'id': str, 'name': str, 'tasks': { task_id: { 'id': str, 'title': str, 'completed': bool } } } }
todo_lists = {}
list_id_counter = 1
task_id_counter = 1

@app.route('/')
def index():
    return render_template('index.html', lists=todo_lists.values())

@app.route('/lists', methods=['POST'])
def create_list():
    global list_id_counter
    name = request.form.get('name', '').strip()
    if name:
        l_id = str(list_id_counter)
        list_id_counter += 1
        todo_lists[l_id] = {
            'id': l_id,
            'name': name,
            'tasks': {}
        }
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/delete', methods=['POST'])
def delete_list(list_id):
    if list_id in todo_lists:
        del todo_lists[list_id]
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/tasks', methods=['POST'])
def add_task(list_id):
    global task_id_counter
    if list_id in todo_lists:
        title = request.form.get('title', '').strip()
        if title:
            t_id = str(task_id_counter)
            task_id_counter += 1
            todo_lists[list_id]['tasks'][t_id] = {
                'id': t_id,
                'title': title,
                'completed': False
            }
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/tasks/<task_id>/toggle', methods=['POST'])
def toggle_task(list_id, task_id):
    if list_id in todo_lists and task_id in todo_lists[list_id]['tasks']:
        task = todo_lists[list_id]['tasks'][task_id]
        task['completed'] = not task['completed']
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/tasks/<task_id>/delete', methods=['POST'])
def delete_task(list_id, task_id):
    if list_id in todo_lists and task_id in todo_lists[list_id]['tasks']:
        del todo_lists[list_id]['tasks'][task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
