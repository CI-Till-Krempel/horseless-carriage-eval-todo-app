from flask import Blueprint, render_template, request, redirect, url_for
from models import db, TodoList, Task

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    lists = TodoList.query.all()
    return render_template('index.html', lists=lists)

@main_bp.route('/list/create', methods=['POST'])
def create_list():
    name = request.form.get('name')
    if name:
        new_list = TodoList(name=name)
        db.session.add(new_list)
        db.session.commit()
    return redirect(url_for('main.index'))

@main_bp.route('/list/<int:list_id>/task/add', methods=['POST'])
def add_task(list_id):
    title = request.form.get('title')
    if title:
        task = Task(title=title, list_id=list_id)
        db.session.add(task)
        db.session.commit()
    return redirect(url_for('main.index'))

@main_bp.route('/task/<int:task_id>/toggle', methods=['POST'])
def toggle_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for('main.index'))

@main_bp.route('/task/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('main.index'))

@main_bp.route('/list/<int:list_id>/delete', methods=['POST'])
def delete_list(list_id):
    todo_list = TodoList.query.get_or_404(list_id)
    db.session.delete(todo_list)
    db.session.commit()
    return redirect(url_for('main.index'))
