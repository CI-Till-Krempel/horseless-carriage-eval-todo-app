from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data store
# lists: { list_id: { 'id': list_id, 'name': str, 'tasks': [ { 'id': task_id, 'description': str, 'completed': bool } ] } }
lists_db = {}
list_id_counter = 1
task_id_counter = 1

@app.route('/')
def index():
    return render_template('index.html', lists=lists_db.values())

@app.route('/lists', methods=['POST'])
def create_list():
    global list_id_counter
    name = request.form.get('name', '').strip()
    if name:
        lists_db[list_id_counter] = {
            'id': list_id_counter,
            'name': name,
            'tasks': []
        }
        list_id_counter += 1
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/delete', methods=['POST'])
def delete_list(list_id):
    if list_id in lists_db:
        del lists_db[list_id]
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/tasks', methods=['POST'])
def create_task(list_id):
    global task_id_counter
    if list_id in lists_db:
        description = request.form.get('description', '').strip()
        if description:
            lists_db[list_id]['tasks'].append({
                'id': task_id_counter,
                'description': description,
                'completed': False
            })
            task_id_counter += 1
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/tasks/<int:task_id>/toggle', methods=['POST'])
def toggle_task(list_id, task_id):
    if list_id in lists_db:
        for task in lists_db[list_id]['tasks']:
            if task['id'] == task_id:
                task['completed'] = not task['completed']
                break
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/tasks/<int:task_id>/delete', methods=['POST'])
def delete_task(list_id, task_id):
    if list_id in lists_db:
        lists_db[list_id]['tasks'] = [t for t in lists_db[list_id]['tasks'] if t['id'] != task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
