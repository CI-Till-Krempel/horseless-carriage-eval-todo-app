from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for lists and tasks
lists = {}
next_list_id = 1
next_task_id = 1

@app.route('/')
def index():
    return render_template('index.html', lists=lists)

@app.route('/lists', methods=['POST'])
def create_list():
    global next_list_id
    name = request.form.get('name')
    if name:
        list_id = str(next_list_id)
        next_list_id += 1
        lists[list_id] = {'id': list_id, 'name': name, 'tasks': {}}
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/tasks', methods=['POST'])
def add_task(list_id):
    global next_task_id
    if list_id in lists:
        description = request.form.get('description')
        if description:
            task_id = str(next_task_id)
            next_task_id += 1
            lists[list_id]['tasks'][task_id] = {
                'id': task_id,
                'description': description,
                'completed': False
            }
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
