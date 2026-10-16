from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data store for Sprint 1
lists = {}
# Structure: {list_id: {'id': str, 'name': str, 'tasks': [{'id': str, 'text': str, 'completed': bool}]}}

@app.route('/')
def index():
    return render_template('index.html', lists=lists)

@app.route('/lists', methods=['POST'])
def create_list():
    name = request.form.get('name', '').strip()
    if name:
        list_id = str(len(lists) + 1)
        lists[list_id] = {'id': list_id, 'name': name, 'tasks': []}
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/delete', methods=['POST'])
def delete_list(list_id):
    if list_id in lists:
        del lists[list_id]
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/tasks', methods=['POST'])
def add_task(list_id):
    if list_id in lists:
        text = request.form.get('text', '').strip()
        if text:
            task_id = str(len(lists[list_id]['tasks']) + 1)
            lists[list_id]['tasks'].append({'id': task_id, 'text': text, 'completed': False})
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/tasks/<task_id>/toggle', methods=['POST'])
def toggle_task(list_id, task_id):
    if list_id in lists:
        for task in lists[list_id]['tasks']:
            if task['id'] == task_id:
                task['completed'] = not task['completed']
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/tasks/<task_id>/delete', methods=['POST'])
def delete_task(list_id, task_id):
    if list_id in lists:
        lists[list_id]['tasks'] = [t for t in lists[list_id]['tasks'] if t['id'] != task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
