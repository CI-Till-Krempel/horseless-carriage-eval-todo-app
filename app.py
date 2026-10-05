import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
DB_NAME = "todo.db"

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS lists (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                list_id INTEGER NOT NULL,
                description TEXT NOT NULL,
                completed INTEGER NOT NULL DEFAULT 0,
                FOREIGN KEY (list_id) REFERENCES lists (id) ON DELETE CASCADE
            )
        """)
        conn.commit()

@app.route("/", methods=["GET"])
def index():
    conn = get_db()
    lists = conn.execute("SELECT * FROM lists").fetchall()
    selected_list_id = request.args.get("list_id", type=int)
    
    selected_list = None
    tasks = []
    if selected_list_id:
        selected_list = conn.execute("SELECT * FROM lists WHERE id = ?", (selected_list_id,)).fetchone()
        if selected_list:
            tasks = conn.execute("SELECT * FROM tasks WHERE list_id = ?", (selected_list_id,)).fetchall()
    elif lists:
        selected_list = lists[0]
        tasks = conn.execute("SELECT * FROM tasks WHERE list_id = ?", (selected_list["id"],)).fetchall()
        
    conn.close()
    return render_template("index.html", lists=lists, selected_list=selected_list, tasks=tasks)

@app.route("/lists", methods=["POST"])
def create_list():
    name = request.form.get("name", "").strip()
    if name:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO lists (name) VALUES (?)", (name,))
        list_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return redirect(url_for("index", list_id=list_id))
    return redirect(url_for("index"))

@app.route("/lists/<int:list_id>/delete", methods=["POST"])
def delete_list(list_id):
    conn = get_db()
    conn.execute("DELETE FROM tasks WHERE list_id = ?", (list_id,))
    conn.execute("DELETE FROM lists WHERE id = ?", (list_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))

@app.route("/lists/<int:list_id>/tasks", methods=["POST"])
def create_task(list_id):
    description = request.form.get("description", "").strip()
    if description:
        conn = get_db()
        conn.execute("INSERT INTO tasks (list_id, description, completed) VALUES (?, ?, 0)", (list_id, description))
        conn.commit()
        conn.close()
    return redirect(url_for("index", list_id=list_id))

@app.route("/tasks/<int:task_id>/toggle", methods=["POST"])
def toggle_task(task_id):
    conn = get_db()
    task = conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
    if task:
        new_status = 0 if task["completed"] else 1
        conn.execute("UPDATE tasks SET completed = ? WHERE id = ?", (new_status, task_id))
        conn.commit()
        list_id = task["list_id"]
        conn.close()
        return redirect(url_for("index", list_id=list_id))
    conn.close()
    return redirect(url_for("index"))

@app.route("/tasks/<int:task_id>/delete", methods=["POST"])
def delete_task(task_id):
    conn = get_db()
    task = conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
    list_id = task["list_id"] if task else None
    if task:
        conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
    conn.close()
    if list_id:
        return redirect(url_for("index", list_id=list_id))
    return redirect(url_for("index"))

if __name__ == "__main__":
    init_db()
    app.run(debug=True, host="0.0.0.0", port=5000)
