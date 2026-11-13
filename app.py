from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for MVP
lists = {}
next_list_id = 1
next_task_id = 1

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", lists=lists)

@app.route("/lists", methods=["POST"])
def create_list():
    global next_list_id
    name = request.form.get("name")
    if name:
        lists[str(next_list_id)] = {"name": name, "tasks": []}
        next_list_id += 1
    return redirect(url_for("index"))

@app.route("/lists/<list_id>/tasks", methods=["POST"])
def add_task(list_id):
    global next_task_id
    if list_id in lists:
        description = request.form.get("description")
        if description:
            lists[list_id]["tasks"].append({
                "id": next_task_id,
                "description": description,
                "completed": False
            })
            next_task_id += 1
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
