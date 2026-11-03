from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# In-memory storage for lists and tasks
# lists: dict mapping list_id (int) -> dict(id, name, tasks)
# tasks: dict mapping task_id (int) -> dict(id, list_id, description, completed)
lists_store = {}
tasks_store = {}
list_id_counter = 1
task_id_counter = 1

@app.route('/')
def index():
    return render_template('index.html', lists=lists_store.values())

@app.route('/lists', methods=['POST'])
def create_list():
    global list_id_counter
    name = request.form.get('name') or (request.json and request.json.get('name'))
    if not name:
        if request.is_json:
            return jsonify({'error': 'List name is required'}), 400
        return redirect(url_for('index'))
    
    list_id = list_id_counter
    list_id_counter += 1
    new_list = {'id': list_id, 'name': name, 'tasks': []}
    lists_store[list_id] = new_list
    
    if request.is_json:
        return jsonify(new_list), 201
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
