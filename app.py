from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# In-memory storage for lists and tasks
# Structure:
# lists = {
#    1: {'id': 1, 'name': 'Groceries', 'tasks': [{ 'id': 1, 'text': 'Milk', 'completed': False }]}
# }
todos_db = {}
list_id_counter = 1
task_id_counter = 1

@app.route('/')
def index():
    return render_template('index.html', lists=todos_db)

@app.route('/lists', methods=['POST'])
def create_list():
    global list_id_counter
    name = request.form.get('name', '').strip()
    if name:
        todos_db[list_id_counter] = {'id': list_id_counter, 'name': name, 'tasks': []}
        list_id_counter += 1
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/delete', methods=['POST'])
def delete_list(list_id):
    if list_id in todos_db:
        del todos_db[list_id]
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/tasks', methods=['POST'])
def create_task(list_id):
    global task_id_counter
    if list_id in todos_db:
        text = request.form.get('text', '').strip()
        if text:
            todos_db[list_id]['tasks'].append({
                'id': task_id_counter,
                'text': text,
                'completed': False
            })
            task_id_counter += 1
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/tasks/<int:task_id>/toggle', methods=['POST'])
def toggle_task(list_id, task_id):
    if list_id in todos_db:
        for task in todos_db[list_id]['tasks']:
            if task['id'] == task_id:
                task['completed'] = not task['completed']
                break
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/tasks/<int:task_id>/delete', methods=['POST'])
def delete_task(list_id, task_id):
    if list_id in todos_db:
        todos_db[list_id]['tasks'] = [t for t in todos_db[list_id]['tasks'] if t['id'] != task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
