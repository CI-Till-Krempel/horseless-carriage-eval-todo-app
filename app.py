from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for lists and tasks
# Lists: dictionary mapping list_id to {"id": list_id, "name": name, "tasks": []}
lists = {}
counter = 1
task_counter = 1

@app.route('/')
def index():
    return render_template('index.html', lists=lists)

@app.route('/lists', methods=['POST'])
def create_list():
    global counter
    name = request.form.get('name')
    if name:
        list_id = str(counter)
        counter += 1
        lists[list_id] = {"id": list_id, "name": name, "tasks": []}
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/tasks', methods=['POST'])
def add_task(list_id):
    global task_counter
    if list_id in lists:
        title = request.form.get('title')
        if title:
            task_id = str(task_counter)
            task_counter += 1
            lists[list_id]["tasks"].append({"id": task_id, "title": title, "completed": False})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
