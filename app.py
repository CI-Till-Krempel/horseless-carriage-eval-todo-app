from flask import Flask, render_template, request, redirect, url_for
from models import TaskManager

app = Flask(__name__)

@app.route('/')
def index():
    lists = TaskManager.get_all_lists()
    return render_template('index.html', lists=lists)

@app.route('/lists', methods=['POST'])
def create_list():
    name = request.form.get('name')
    if name:
        TaskManager.create_list(name)
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/delete', methods=['POST'])
def delete_list(list_id):
    TaskManager.delete_list(list_id)
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/tasks', methods=['POST'])
def add_task(list_id):
    description = request.form.get('description')
    if description:
        TaskManager.add_task(list_id, description)
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/tasks/<task_id>/toggle', methods=['POST'])
def toggle_task(list_id, task_id):
    TaskManager.toggle_task(list_id, task_id)
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/tasks/<task_id>/delete', methods=['POST'])
def delete_task(list_id, task_id):
    TaskManager.delete_task(list_id, task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
