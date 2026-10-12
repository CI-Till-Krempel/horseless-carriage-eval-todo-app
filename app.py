from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data store for lists: mapping list_name -> list of task dicts
todo_lists = {}

@app.route('/')
def index():
    return render_template('index.html', todo_lists=todo_lists)

@app.route('/lists', methods=['POST'])
def create_list():
    list_name = request.form.get('list_name')
    if list_name and list_name not in todo_lists:
        todo_lists[list_name] = []
    return redirect(url_for('index'))

@app.route('/lists/<list_name>/tasks', methods=['POST'])
def add_task(list_name):
    task_desc = request.form.get('task_description')
    if list_name in todo_lists and task_desc:
        todo_lists[list_name].append({'description': task_desc, 'completed': False})
    return redirect(url_for('index'))

@app.route('/lists/<list_name>/tasks/<int:task_index>/toggle', methods=['POST'])
def toggle_task(list_name, task_index):
    if list_name in todo_lists and 0 <= task_index < len(todo_lists[list_name]):
        task = todo_lists[list_name][task_index]
        task['completed'] = not task['completed']
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
