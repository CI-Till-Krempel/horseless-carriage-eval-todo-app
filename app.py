from flask import Flask, render_template, request, redirect, url_for
import uuid

app = Flask(__name__)

# Simple in-memory store
lists = {}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        list_name = request.form.get('list_name')
        if list_name:
            list_id = str(uuid.uuid4())
            lists[list_id] = {'id': list_id, 'name': list_name, 'tasks': []}
        return redirect(url_for('index'))
    return render_template('index.html', lists=lists.values())

@app.route('/add_task/<list_id>', methods=['POST'])
def add_task(list_id):
    task_text = request.form.get('task_text')
    if list_id in lists and task_text:
        task_id = str(uuid.uuid4())
        lists[list_id]['tasks'].append({'id': task_id, 'text': task_text, 'completed': False})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
