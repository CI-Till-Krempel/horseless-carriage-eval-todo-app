from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory database for demo
lists = {}

@app.route('/')
def index():
    return render_template('index.html', lists=lists)

@app.route('/create_list', methods=['POST'])
def create_list():
    title = request.form.get('title')
    if title:
        lists[title] = []
    return redirect(url_for('index'))

@app.route('/delete_list/<list_name>', methods=['POST'])
def delete_list(list_name):
    if list_name in lists:
        del lists[list_name]
    return redirect(url_for('index'))

@app.route('/add_task/<list_name>', methods=['POST'])
def add_task(list_name):
    task_content = request.form.get('task')
    if list_name in lists and task_content:
        lists[list_name].append({'task': task_content, 'completed': False})
    return redirect(url_for('index'))

@app.route('/toggle_task/<list_name>/<int:task_index>', methods=['POST'])
def toggle_task(list_name, task_index):
    if list_name in lists and 0 <= task_index < len(lists[list_name]):
        current = lists[list_name][task_index]['completed']
        lists[list_name][task_index]['completed'] = not current
    return redirect(url_for('index'))

@app.route('/delete_task/<list_name>/<int:task_index>', methods=['POST'])
def delete_task(list_name, task_index):
    """Delete a task from a list."""
    if list_name in lists and 0 <= task_index < len(lists[list_name]):
        lists[list_name].pop(task_index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
