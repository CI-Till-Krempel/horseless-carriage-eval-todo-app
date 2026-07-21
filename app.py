from flask import Flask, render_template, request, redirect, url_for
import uuid

app = Flask(__name__)

# In-memory storage: { list_id: {"name": str, "tasks": {task_id: {"text": str, "done": bool}}} }
lists = {}

@app.route('/')
def index():
    return render_template('index.html', lists=lists)

@app.route('/add_list', methods=['POST'])
def add_list():
    name = request.form.get('name')
    if name:
        lists[str(uuid.uuid4())] = {"name": name, "tasks": {}}
    return redirect(url_for('index'))

@app.route('/delete_list/<list_id>', methods=['POST'])
def delete_list(list_id):
    if list_id in lists:
        del lists[list_id]
    return redirect(url_for('index'))

@app.route('/add_task/<list_id>', methods=['POST'])
def add_task(list_id):
    text = request.form.get('text')
    if list_id in lists and text:
        lists[list_id]["tasks"][str(uuid.uuid4())] = {"text": text, "done": False}
    return redirect(url_for('index'))

@app.route('/toggle_task/<list_id>/<task_id>', methods=['POST'])
def toggle_task(list_id, task_id):
    if list_id in lists and task_id in lists[list_id]["tasks"]:
        task = lists[list_id]["tasks"][task_id]
        task["done"] = not task["done"]
    return redirect(url_for('index'))

@app.route('/delete_task/<list_id>/<task_id>', methods=['POST'])
def delete_task(list_id, task_id):
    if list_id in lists and task_id in lists[list_id]["tasks"]:
        del lists[list_id]["tasks"][task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
