from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data store for MVP
lists = {}
tasks = {}

@app.route('/')
def index():
    return render_template('index.html', lists=lists, tasks=tasks)

@app.route('/list/create', methods=['POST'])
def create_list():
    name = request.form.get('name')
    if name and name not in lists:
        lists[name] = []
    return redirect(url_for('index'))

@app.route('/list/<list_name>/task/add', methods=['POST'])
def add_task(list_name):
    description = request.form.get('description')
    if list_name in lists and description:
        task_id = len(tasks.get(list_name, [])) + 1
        if list_name not in tasks:
            tasks[list_name] = []
        tasks[list_name].append({'id': task_id, 'description': description, 'completed': False})
    return redirect(url_for('index'))

@app.route('/list/<list_name>/task/<int:task_id>/toggle', methods=['POST'])
def toggle_task(list_name, task_id):
    if list_name in tasks:
        for task in tasks[list_name]:
            if task['id'] == task_id:
                task['completed'] = not task['completed']
    return redirect(url_for('index'))

@app.route('/list/<list_name>/task/<int:task_id>/delete', methods=['POST'])
def delete_task(list_name, task_id):
    if list_name in tasks:
        tasks[list_name] = [t for t in tasks[list_name] if t['id'] != task_id]
    return redirect(url_for('index'))

@app.route('/list/<list_name>/delete', methods=['POST'])
def delete_list(list_name):
    if list_name in lists:
        del lists[list_name]
    if list_name in tasks:
        del tasks[list_name]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
