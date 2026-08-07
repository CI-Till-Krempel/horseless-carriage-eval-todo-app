from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data store
# lists: dict mapping list_id -> {"id": str, "name": str, "tasks": [ {"id": str, "text": str, "completed": bool} ]}
lists_store = {}
list_id_counter = 1
task_id_counter = 1

@app.route('/')
def index():
    return render_template('index.html', lists=lists_store.values())

@app.route('/lists', methods=['POST'])
def create_list():
    global list_id_counter
    name = request.form.get('name', '').strip()
    if name:
        lid = str(list_id_counter)
        list_id_counter += 1
        lists_store[lid] = {
            "id": lid,
            "name": name,
            "tasks": []
        }
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/delete', methods=['POST'])
def delete_list(list_id):
    if list_id in lists_store:
        del lists_store[list_id]
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/tasks', methods=['POST'])
def add_task(list_id):
    global task_id_counter
    if list_id in lists_store:
        text = request.form.get('text', '').strip()
        if text:
            tid = str(task_id_counter)
            task_id_counter += 1
            lists_store[list_id]["tasks"].append({
                "id": tid,
                "text": text,
                "completed": False
            })
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/tasks/<task_id>/toggle', methods=['POST'])
def toggle_task(list_id, task_id):
    if list_id in lists_store:
        for task in lists_store[list_id]["tasks"]:
            if task["id"] == task_id:
                task["completed"] = not task["completed"]
                break
    return redirect(url_for('index'))

@app.route('/lists/<list_id>/tasks/<task_id>/delete', methods=['POST'])
def delete_task(list_id, task_id):
    if list_id in lists_store:
        lists_store[list_id]["tasks"] = [
            t for t in lists_store[list_id]["tasks"] if t["id"] != task_id
        ]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
