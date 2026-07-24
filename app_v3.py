# Sprint 3 - US-0003 Implementation File
import os
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# In-memory storage for lists and tasks for MVP
lists_db = {}
next_list_id = 1
next_task_id = 1

@app.route('/')
def index():
    return render_template('index.html', lists=lists_db.values())

@app.route('/lists', methods=['POST'])
def create_list():
    global next_list_id
    name = (request.form.get('name') or (request.json and request.json.get('name')) or '').strip()
    if not name:
        if request.is_json:
            return jsonify({"error": "List name cannot be empty"}), 400
        return redirect(url_for('index'))
    
    new_id = next_list_id
    next_list_id += 1
    lists_db[new_id] = {"id": new_id, "name": name, "tasks": []}
    if request.is_json:
        return jsonify(lists_db[new_id]), 201
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>', methods=['GET'])
def get_list(list_id):
    todo_list = lists_db.get(list_id)
    if not todo_list:
        return jsonify({"error": "List not found"}), 404
    return jsonify(todo_list)

@app.route('/lists/<int:list_id>/tasks', methods=['POST'])
def create_task(list_id):
    global next_task_id
    todo_list = lists_db.get(list_id)
    if not todo_list:
        if request.is_json:
            return jsonify({"error": "List not found"}), 404
        return redirect(url_for('index'))
    
    text = (request.form.get('text') or (request.json and request.json.get('text')) or '').strip()
    if not text:
        if request.is_json:
            return jsonify({"error": "Task text cannot be empty"}), 400
        return redirect(url_for('index'))

    task_id = next_task_id
    next_task_id += 1
    task = {"id": task_id, "text": text, "completed": False}
    todo_list["tasks"].append(task)
    if request.is_json:
        return jsonify(task), 201
    return redirect(url_for('index'))

@app.route('/tasks/<int:task_id>/toggle', methods=['POST'])
def toggle_task(task_id):
    for todo_list in lists_db.values():
        for task in todo_list["tasks"]:
            if task["id"] == task_id:
                task["completed"] = not task["completed"]
                if request.is_json:
                    return jsonify(task)
                return redirect(url_for('index'))
    if request.is_json:
        return jsonify({"error": "Task not found"}), 404
    return redirect(url_for('index'))

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    for todo_list in lists_db.values():
        for task in todo_list["tasks"]:
            if task["id"] == task_id:
                todo_list["tasks"].remove(task)
                if request.is_json:
                    return jsonify({"success": True})
                return redirect(url_for('index'))
    if request.is_json:
        return jsonify({"error": "Task not found"}), 404
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>', methods=['DELETE'])
def delete_list(list_id):
    if list_id in lists_db:
        del lists_db[list_id]
        if request.is_json:
            return jsonify({"success": True})
        return redirect(url_for('index'))
    if request.is_json:
        return jsonify({"error": "List not found"}), 404
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
