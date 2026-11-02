from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

lists = {}
tasks = {}
task_id_counter = 0

@app.route('/')
def index():
    return render_template('index.html', lists=lists, tasks=tasks)

@app.route('/list', methods=['POST'])
def create_list():
    name = request.form.get('name')
    if name:
        list_id = f"list_{len(lists) + 1}"
        lists[list_id] = {'id': list_id, 'name': name}
    return redirect(url_for('index'))

@app.route('/task', methods=['POST'])
def create_task():
    global task_id_counter
    list_id = request.form.get('list_id')
    title = request.form.get('title')
    if list_id and title:
        task_id_counter += 1
        task_id = f"task_{task_id_counter}"
        tasks[task_id] = {'id': task_id, 'list_id': list_id, 'title': title, 'completed': False}
    return redirect(url_for('index'))

@app.route('/task/<task_id>/toggle', methods=['POST'])
def toggle_task(task_id):
    if task_id in tasks:
        tasks[task_id]['completed'] = not tasks[task_id]['completed']
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
