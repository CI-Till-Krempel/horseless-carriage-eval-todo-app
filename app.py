import uuid
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

# In-memory data store for MVP
# Structure: lists = { list_id: { "id": str, "name": str, "tasks": [ { "id": str, "text": str, "completed": bool } ] } }
lists_store = {}


@app.route("/")
def index():
    return render_template("index.html", lists=lists_store.values())


@app.route("/lists", methods=["POST"])
def create_list():
    name = request.form.get("name", "").strip()
    if name:
        list_id = str(uuid.uuid4())
        lists_store[list_id] = {"id": list_id, "name": name, "tasks": []}
    return redirect(url_for("index"))


@app.route("/lists/<list_id>/tasks", methods=["POST"])
def add_task(list_id):
    if list_id in lists_store:
        text = request.form.get("text", "").strip()
        if text:
            task_id = str(uuid.uuid4())
            lists_store[list_id]["tasks"].append(
                {"id": task_id, "text": text, "completed": False}
            )
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
