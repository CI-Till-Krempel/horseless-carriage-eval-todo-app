from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data structures
# lists = { list_id: {'id': list_id, 'name': str, 'tasks': [ {'id': task_id, 'text': str, 'completed': bool} ] } }
todo_lists = {}
list_id_counter = 1
task_id_counter = 1

@app.route('/')
def index():
    return render_template('index.html', lists=todo_lists.values())

@app.route('/lists', methods=['POST'])
def create_list():
    global list_id_counter
    name = request.form.get('name')
    if name:
        list_id = str(list_id_counter)
        list_id_counter += 1
        todo_lists[list_id] = {'id': list_id, 'name': name, 'tasks': []}
    return redirect(url_for('index'))

@app.route('/lists/<list_id>')
def view_list(list_id):
    todo_list = todo_lists.get(list_id)
    if not todo_list:
        return "List not found", 404
    return render_template('list.html', todo_list=todo_list)

@app.route('/lists/<list_id>/tasks', methods=['POST'])
def add_task(list_id):
    global task_id_counter
    todo_list = todo_lists.get(list_id)
    if not todo_list:
        return "List not found", 404
    text = request.form.get('text')
    if text:
        task_id = str(task_id_counter)
        task_id_counter += 1
        todo_list['tasks'].append({'id': task_id, 'text': text, 'completed': False})
    return redirect(url_for('view_list', list_id=list_id))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
