from flask import Flask, render_template, request, redirect, url_for
import uuid
import os
import json

app = Flask(__name__)

DATA_FILE = "todos.json"

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

@app.route("/")
def index():
    status_filter = request.args.get("filter", "all")
    lists_db = load_data()
    
    rendered_lists = []
    for list_id, lst in lists_db.items():
        tasks = lst["tasks"]
        total_count = len(tasks)
        completed_count = sum(1 for t in tasks if t["completed"])
        active_count = total_count - completed_count
        
        if status_filter == "active":
            filtered_tasks = [t for t in tasks if not t["completed"]]
        elif status_filter == "completed":
            filtered_tasks = [t for t in tasks if t["completed"]]
        else:
            filtered_tasks = tasks
            
        rendered_lists.append({
            "id": lst["id"],
            "name": lst["name"],
            "tasks": filtered_tasks,
            "total_count": total_count,
            "active_count": active_count,
            "completed_count": completed_count
        })
        
    return render_template("index.html", lists=rendered_lists, current_filter=status_filter)

@app.route("/list/create", methods=["POST"])
def create_list():
    name = request.form.get("name", "").strip()
    if name:
        lists_db = load_data()
        list_id = str(uuid.uuid4())
        lists_db[list_id] = {
            "id": list_id,
            "name": name,
            "tasks": []
        }
        save_data(lists_db)
    return redirect(url_for("index", filter=request.args.get("filter", "all")))

@app.route("/list/<list_id>/task/add", methods=["POST"])
def add_task(list_id):
    lists_db = load_data()
    if list_id in lists_db:
        text = request.form.get("text", "").strip()
        if text:
            task_id = str(uuid.uuid4())
            lists_db[list_id]["tasks"].append({
                "id": task_id,
                "text": text,
                "completed": False
            })
            save_data(lists_db)
    return redirect(url_for("index", filter=request.args.get("filter", "all")))

@app.route("/list/<list_id>/task/<task_id>/toggle", methods=["POST"])
def toggle_task(list_id, task_id):
    lists_db = load_data()
    if list_id in lists_db:
        for task in lists_db[list_id]["tasks"]:
            if task["id"] == task_id:
                task["completed"] = not task["completed"]
                break
        save_data(lists_db)
    return redirect(url_for("index", filter=request.args.get("filter", "all")))

@app.route("/list/<list_id>/task/<task_id>/delete", methods=["POST"])
def delete_task(list_id, task_id):
    lists_db = load_data()
    if list_id in lists_db:
        lists_db[list_id]["tasks"] = [t for t in lists_db[list_id]["tasks"] if t["id"] != task_id]
        save_data(lists_db)
    return redirect(url_for("index", filter=request.args.get("filter", "all")))

@app.route("/list/<list_id>/delete", methods=["POST"])
def delete_list(list_id):
    lists_db = load_data()
    if list_id in lists_db:
        del lists_db[list_id]
        save_data(lists_db)
    return redirect(url_for("index", filter=request.args.get("filter", "all")))

if __name__ == "__main__":
    app.run(debug=True, port=5000)
