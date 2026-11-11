from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for demonstration purposes
# Lists structure: { list_id: { 'name': str, 'tasks': [ { 'id': int, 'title': str, 'done': bool } ] } }
lists_db = {}
task_id_counter = 1

@app.route('/')
def index():
    return render_template('index.html', lists=lists_db)

@app.route('/lists', methods=['POST'])
def create_list():
    global lists_db
    list_name = request.form.get('list_name')
    if list_name:
        list_id = str(len(lists_db) + 1)
        lists_db[list_id] = {'name': list_name, 'tasks': []}
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/tasks', methods=['POST'])
def add_task(list_id):
    global task_id_counter
    if list_id in lists_db:
        task_title = request.form.get('task_title')
        if task_title:
            lists_db[list_id]['tasks'].append({
                'id': task_id_counter,
                'title': task_title,
                'done': False
            })
            task_id_counter += 1
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/tasks/<int:task_id>/toggle', methods=['POST'])
def toggle_task(list_id, task_id):
    if list_id in lists_db:
        for task in lists_db[list_id]['tasks']:
            if task['id'] == task_id:
                task['done'] = not task['done']
                break
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/tasks/<int:task_id>/delete', methods=['POST'])
def delete_task(list_id, task_id):
    if list_id in lists_db:
        lists_db[list_id]['tasks'] = [t for t in lists_db[list_id]['tasks'] if t['id'] != task_id]
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/delete', methods=['POST'])
def delete_list(list_id):
    if list_id in lists_db:
        del lists_db[list_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
