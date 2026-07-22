from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app import db
from models import TodoList, Task

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    lists = TodoList.query.all()
    return render_template('index.html', lists=lists)

@bp.route('/lists', methods=['POST'])
def create_list():
    name = request.form.get('name', '').strip()
    if name:
        new_list = TodoList(name=name)
        db.session.add(new_list)
        db.session.commit()
    return redirect(url_for('main.index'))

@bp.route('/lists/<int:list_id>/delete', methods=['POST'])
def delete_list(list_id):
    todo_list = TodoList.query.get_or_404(list_id)
    db.session.delete(todo_list)
    db.session.commit()
    return redirect(url_for('main.index'))

@bp.route('/lists/<int:list_id>/tasks', methods=['POST'])
def create_task(list_id):
    TodoList.query.get_or_404(list_id)
    description = request.form.get('description', '').strip()
    if description:
        task = Task(description=description, list_id=list_id, completed=False)
        db.session.add(task)
        db.session.commit()
    return redirect(url_for('main.index'))

@bp.route('/tasks/<int:task_id>/toggle', methods=['POST'])
def toggle_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for('main.index'))

@bp.route('/tasks/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('main.index'))
