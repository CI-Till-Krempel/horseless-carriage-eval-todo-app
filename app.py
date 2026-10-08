import os
from flask import Flask, render_template, request, redirect, url_for
from models import db, ToDoList, Task

def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
    if test_config:
        app.config.update(test_config)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route('/')
    def index():
        lists = ToDoList.query.all()
        return render_template('index.html', lists=lists)

    @app.route('/lists', methods=['POST'])
    def create_list():
        name = request.form.get('name')
        if name:
            new_list = ToDoList(name=name)
            db.session.add(new_list)
            db.session.commit()
        return redirect(url_for('index'))

    @app.route('/lists/<int:list_id>/delete', methods=['POST'])
    def delete_list(list_id):
        lst = ToDoList.query.get_or_404(list_id)
        db.session.delete(lst)
        db.session.commit()
        return redirect(url_for('index'))

    @app.route('/lists/<int:list_id>/tasks', methods=['POST'])
    def create_task(list_id):
        ToDoList.query.get_or_404(list_id)
        description = request.form.get('description')
        if description:
            task = Task(description=description, list_id=list_id)
            db.session.add(task)
            db.session.commit()
        return redirect(url_for('index'))

    @app.route('/tasks/<int:task_id>/toggle', methods=['POST'])
    def toggle_task(task_id):
        task = Task.query.get_or_404(task_id)
        task.complete = not task.complete
        db.session.commit()
        return redirect(url_for('index'))

    @app.route('/tasks/<int:task_id>/delete', methods=['POST'])
    def delete_task(task_id):
        task = Task.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()
        return redirect(url_for('index'))

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
