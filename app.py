from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data store
# List structure: {'id': int, 'name': str, 'tasks': [{'text': str, 'completed': bool}]}
lists = []
list_counter = 0

@app.route('/')
def index():
    return render_template('index.html', lists=lists)

@app.route('/create_list', methods=['POST'])
def create_list():
    global list_counter
    list_name = request.form.get('list_name')
    if list_name:
        list_counter += 1
        lists.append({'id': list_counter, 'name': list_name, 'tasks': []})
    return redirect(url_for('index'))

@app.route('/add_task/<int:list_id>', methods=['POST'])
def add_task(list_id):
    task_text = request.form.get('task_text')
    for todo_list in lists:
        if todo_list['id'] == list_id:
            todo_list['tasks'].append({'text': task_text, 'completed': False})
            break
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
