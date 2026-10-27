from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for lists and tasks
# Lists: {list_id: {'id': list_id, 'name': name}}
# Tasks: {task_id: {'id': task_id, 'list_id': list_id, 'description': description, 'completed': bool}}
lists_db = {}
tasks_db = {}
list_counter = 1
task_counter = 1

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', lists=lists_db.values(), tasks=tasks_db)

@app.route('/lists', methods=['POST'])
def create_list():
    global list_counter
    name = request.form.get('name', '').strip()
    if name:
        lists_db[list_counter] = {'id': list_counter, 'name': name}
        list_counter += 1
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
