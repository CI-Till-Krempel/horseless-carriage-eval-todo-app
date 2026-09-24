from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# In-memory storage for lists and tasks
# lists structure: { list_id: {'id': list_id, 'name': name} }
# tasks structure: { task_id: {'id': task_id, 'list_id': list_id, 'text': text, 'completed': bool} }
todo_lists = {}
tasks = {}
list_counter = 1
task_counter = 1

@app.route('/')
def index():
    global todo_lists, tasks
    lists_with_tasks = []
    for l_id, l_data in todo_lists.items():
        l_tasks = [t for t in tasks.values() if t['list_id'] == l_id]
        lists_with_tasks.append({
            'id': l_id,
            'name': l_data['name'],
            'tasks': l_tasks
        })
    return render_template('index.html', lists=lists_with_tasks)

@app.route('/lists', methods=['POST'])
def create_list():
    global list_counter
    name = request.form.get('name', '').strip()
    if name:
        todo_lists[list_counter] = {'id': list_counter, 'name': name}
        list_counter += 1
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/delete', methods=['POST'])
def delete_list(list_id):
    global todo_lists, tasks
    if list_id in todo_lists:
        del todo_lists[list_id]
        # Delete all tasks associated with this list
        to_delete = [t_id for t_id, t in tasks.items() if t['list_id'] == list_id]
        for t_id in to_delete:
            del tasks[t_id]
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/tasks', methods=['POST'])
def add_task(list_id):
    global task_counter
    text = request.form.get('text', '').strip()
    if text and list_id in todo_lists:
        tasks[task_counter] = {
            'id': task_counter,
            'list_id': list_id,
            'text': text,
            'completed': False
        }
        task_counter += 1
    return redirect(url_for('index'))

@app.route('/tasks/<int:task_id>/toggle', methods=['POST'])
def toggle_task(task_id):
    if task_id in tasks:
        tasks[task_id]['completed'] = not tasks[task_id]['completed']
    return redirect(url_for('index'))

@app.route('/tasks/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    if task_id in tasks:
        del tasks[task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
