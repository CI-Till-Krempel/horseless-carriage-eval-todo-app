from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///todo.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class TodoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    tasks = db.relationship('Task', backref='todo_list', lazy=True, cascade='all, delete-orphan')

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    complete = db.Column(db.Boolean, default=False, nullable=False)
    list_id = db.Column(db.Integer, db.ForeignKey('todo_list.id'), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    lists = TodoList.query.all()
    return render_template('index.html', lists=lists)

@app.route('/list', methods=['POST'])
def add_list():
    title = request.form.get('title')
    if title:
        new_list = TodoList(title=title)
        db.session.add(new_list)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/list/<int:list_id>/task', methods=['POST'])
def add_task(list_id):
    content = request.form.get('content')
    if content:
        new_task = Task(content=content, list_id=list_id, complete=False)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/task/<int:task_id>/toggle', methods=['POST'])
def toggle_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.complete = not task.complete
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
