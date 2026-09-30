from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

lists = []

@app.route('/')
def index():
    return render_template('index.html', lists=lists)

@app.route('/lists', methods=['POST'])
def create_list():
    name = request.form.get('name')
    if name:
        lists.append({'id': len(lists) + 1, 'name': name, 'tasks': []})
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/tasks', methods=['POST'])
def add_task(list_id):
    title = request.form.get('title')
    for lst in lists:
        if lst['id'] == list_id and title:
            lst['tasks'].append({'id': len(lst['tasks']) + 1, 'title': title, 'completed': False})
    return redirect(url_for('index'))

@app.route('/tasks/<int:task_id>/toggle', methods=['POST'])
def toggle_task(task_id):
    for lst in lists:
        for task in lst['tasks']:
            if task['id'] == task_id:
                task['completed'] = not task['completed']
    return redirect(url_for('index'))

@app.route('/tasks/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    for lst in lists:
        lst['tasks'] = [t for t in lst['tasks'] if t['id'] != task_id]
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/delete', methods=['POST'])
def delete_list(list_id):
    global lists
    lists = [lst for lst in lists if lst['id'] != list_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
