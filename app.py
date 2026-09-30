import os
from flask import Flask, render_template, request, redirect, url_for
from models import db, ToDoList, Task

def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if test_config:
        app.config.update(test_config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route('/')
    def index():
        lists = ToDoList.query.all()
        return render_template('index.html', lists=lists)

    @app.route('/list/create', methods=['POST'])
    def create_list():
        name = request.form.get('name')
        if name:
            new_list = ToDoList(name=name)
            db.session.add(new_list)
            db.session.commit()
        return redirect(url_for('index'))

    @app.route('/list/<int:list_id>/task/add', methods=['POST'])
    def add_task(list_id):
        description = request.form.get('description')
        if description:
            task = Task(description=description, list_id=list_id)
            db.session.add(task)
            db.session.commit()
        return redirect(url_for('index'))

    @app.route('/task/<int:task_id>/toggle', methods=['POST'])
    def toggle_task(task_id):
        task = Task.query.get_or_404(task_id)
        task.completed = not task.completed
        db.session.commit()
        return redirect(url_for('index'))

    @app.route('/task/<int:task_id>/delete', methods=['POST'])
    def delete_task(task_id):
        task = Task.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()
        return redirect(url_for('index'))

    @app.route('/list/<int:list_id>/delete', methods=['POST'])
    def delete_list(list_id):
        todo_list = ToDoList.query.get_or_404(list_id)
        db.session.delete(todo_list)
        db.session.commit()
        return redirect(url_for('index'))

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
