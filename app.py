from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data store for lists and tasks
lists_store = []
next_list_id = 1
next_task_id = 1

@app.route('/')
def index():
    return render_template('index.html', lists=lists_store)

@app.route('/lists', methods=['POST'])
def create_list():
    global next_list_id
    name = request.form.get('name', '').strip()
    if name:
        new_list = {
            'id': next_list_id,
            'name': name,
            'tasks': []
        }
        lists_store.append(new_list)
        next_list_id += 1
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/tasks', methods=['POST'])
def add_task(list_id):
    global next_task_id
    title = request.form.get('title', '').strip()
    if title:
        for lst in lists_store:
            if lst['id'] == list_id:
                new_task = {
                    'id': next_task_id,
                    'title': title,
                    'completed': False
                }
                lst['tasks'].append(new_task)
                next_task_id += 1
                break
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
