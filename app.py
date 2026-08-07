from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory database for MVP
# Structure: lists = [{'id': 1, 'name': 'Work', 'tasks': [{'id': 1, 'text': 'Finish report', 'completed': False}]}]
lists = []
list_id_counter = 1
task_id_counter = 1

@app.route('/')
def index():
    return render_template('index.html', lists=lists)

@app.route('/lists', methods=['POST'])
def create_list():
    global list_id_counter
    name = request.form.get('name')
    if name:
        lists.append({
            'id': list_id_counter,
            'name': name.strip(),
            'tasks': []
        })
        list_id_counter += 1
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/tasks', methods=['POST'])
def add_task(list_id):
    global task_id_counter
    text = request.form.get('text')
    if text:
        for lst in lists:
            if lst['id'] == list_id:
                lst['tasks'].append({
                    'id': task_id_counter,
                    'text': text.strip(),
                    'completed': False
                })
                task_id_counter += 1
                break
    return redirect(url_for('index'))

@app.route('/tasks/<int:task_id>/toggle', methods=['POST'])
def toggle_task(task_id):
    for lst in lists:
        for task in lst['tasks']:
            if task['id'] == task_id:
                task['completed'] = not task['completed']
                break
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
    app.run(debug=True, port=5000)
