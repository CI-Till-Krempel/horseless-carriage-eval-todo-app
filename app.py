from flask import Flask, render_template, request, redirect, url_for
import uuid

app = Flask(__name__)

# In-memory data store
# lists = { list_id: { "id": str, "name": str, "tasks": [ { "id": str, "text": str, "completed": bool } ] } }
lists_db = {}

@app.route("/")
def index():
    return render_template("index.html", lists=lists_db.values())

@app.route("/list/create", methods=["POST"])
def create_list():
    name = request.form.get("name", "").strip()
    if name:
        list_id = str(uuid.uuid4())
        lists_db[list_id] = {
            "id": list_id,
            "name": name,
            "tasks": []
        }
    return redirect(url_for("index"))

@app.route("/list/<list_id>/task/add", methods=["POST"])
def add_task(list_id):
    if list_id in lists_db:
        text = request.form.get("text", "").strip()
        if text:
            task_id = str(uuid.uuid4())
            lists_db[list_id]["tasks"].append({
                "id": task_id,
                "text": text,
                "completed": False
            })
    return redirect(url_for("index"))

@app.route("/list/<list_id>/task/<task_id>/toggle", methods=["POST"])
def toggle_task(list_id, task_id):
    if list_id in lists_db:
        for task in lists_db[list_id]["tasks"]:
            if task["id"] == task_id:
                task["completed"] = not task["completed"]
                break
    return redirect(url_for("index"))

@app.route("/list/<list_id>/task/<task_id>/delete", methods=["POST"])
def delete_task(list_id, task_id):
    if list_id in lists_db:
        lists_db[list_id]["tasks"] = [t for t in lists_db[list_id]["tasks"] if t["id"] != task_id]
    return redirect(url_for("index"))

@app.route("/list/<list_id>/delete", methods=["POST"])
def delete_list(list_id):
    if list_id in lists_db:
        del lists_db[list_id]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True, port=5000)
