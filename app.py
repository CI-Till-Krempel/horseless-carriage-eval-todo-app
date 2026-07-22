from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data store for single-user todo app
# Lists structure: { list_id: { 'id': list_id, 'name': name } }
# Tasks structure: { task_id: { 'id': task_id, 'list_id': list_id, 'text': text, 'completed': bool } }
lists_db = {}
tasks_db = {}
list_counter = 1
task_counter = 1

@app.route('/')
def index():
    # Group tasks by list
    all_lists = list(lists_db.values())
    all_tasks = list(tasks_db.values())
    return render_template('index.html', lists=all_lists, tasks=all_tasks)

@app.route('/lists', methods=['POST'])
def create_list():
    global list_counter
    name = request.form.get('name', '').strip()
    if name:
        list_id = str(list_counter)
        list_counter += 1
        lists_db[list_id] = {'id': list_id, 'name': name}
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/delete', methods=['POST'])
def delete_list(list_id):
    if list_id in lists_db:
        del lists_db[list_id]
        # Delete associated tasks
        to_delete = [tid for tid, t in tasks_db.items() if t['list_id'] == list_id]
        for tid in to_delete:
            del tasks_db[tid]
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/tasks', methods=['POST'])
def add_task(list_id):
    global task_counter
    if list_id in lists_db:
        text = request.form.get('text', '').strip()
        if text:
            task_id = str(task_counter)
            task_counter += 1
            tasks_db[task_id] = {'id': task_id, 'list_id': list_id, 'text': text, 'completed': False}
    return redirect(url_for('index'))

@app.route('/tasks/<task_id>/toggle', methods=['POST'])
def toggle_task(task_id):
    if task_id in tasks_db:
        tasks_db[task_id]['completed'] = not tasks_db[task_id]['completed']
    return redirect(url_for('index'))

@app.route('/tasks/<task_id>/delete', methods=['POST'])
def delete_task(task_id):
    if task_id in tasks_db:
        del tasks_db[task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
