import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class TodoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    tasks = db.relationship('Task', backref='list', lazy=True, cascade='all, delete-orphan')

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False, nullable=False)
    list_id = db.Column(db.Integer, db.ForeignKey('todo_list.id'), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    lists = TodoList.query.all()
    return render_template('index.html', lists=lists)

@app.route('/list/create', methods=['POST'])
def create_list():
    name = request.form.get('name')
    if name:
        new_list = TodoList(name=name)
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
    todo_list = TodoList.query.get_or_404(list_id)
    db.session.delete(todo_list)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
