from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory database for lists and tasks
# lists: dict mapping list_id -> {"id": list_id, "title": title, "tasks": [ {"id": task_id, "description": desc, "completed": False} ] }
lists = {}
list_counter = 1
task_counter = 1

@app.route('/')
def index():
    return render_template('index.html', lists=lists.values())

@app.route('/lists', methods=['POST'])
def create_list():
    global list_counter
    title = request.form.get('title')
    if title:
        lists[str(list_counter)] = {"id": str(list_counter), "title": title, "tasks": []}
        list_counter += 1
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/tasks', methods=['POST'])
def add_task(list_id):
    global task_counter
    description = request.form.get('description')
    if list_id in lists and description:
        lists[list_id]["tasks"].append({"id": str(task_counter), "description": description, "completed": False})
        task_counter += 1
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
