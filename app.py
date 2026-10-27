from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data store for MVP
# lists: dict of list_id -> {'id': list_id, 'name': str, 'tasks': dict of task_id -> {'id': task_id, 'text': str, 'completed': bool}}
lists_store = {}
list_counter = 1
task_counter = 1

@app.route('/')
def index():
    return render_template('index.html', lists=lists_store.values())

@app.route('/lists', methods=['POST'])
def create_list():
    global list_counter
    name = request.form.get('name', '').strip()
    if name:
        list_id = str(list_counter)
        list_counter += 1
        lists_store[list_id] = {
            'id': list_id,
            'name': name,
            'tasks': {}
        }
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/tasks', methods=['POST'])
def add_task(list_id):
    global task_counter
    if list_id in lists_store:
        text = request.form.get('text', '').strip()
        if text:
            task_id = str(task_counter)
            task_counter += 1
            lists_store[list_id]['tasks'][task_id] = {
                'id': task_id,
                'text': text,
                'completed': False
            }
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/tasks/<task_id>/toggle', methods=['POST'])
def toggle_task(list_id, task_id):
    if list_id in lists_store and task_id in lists_store[list_id]['tasks']:
        task = lists_store[list_id]['tasks'][task_id]
        task['completed'] = not task['completed']
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/tasks/<task_id>/delete', methods=['POST'])
def delete_task(list_id, task_id):
    if list_id in lists_store and task_id in lists_store[list_id]['tasks']:
        del lists_store[list_id]['tasks'][task_id]
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/delete', methods=['POST'])
def delete_list(list_id):
    if list_id in lists_store:
        del lists_store[list_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
