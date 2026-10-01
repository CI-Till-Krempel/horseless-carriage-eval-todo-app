import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///todo.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class TodoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    tasks = db.relationship('Task', backref='todolist', cascade='all, delete-orphan', lazy=True)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False, nullable=False)
    todolist_id = db.Column(db.Integer, db.ForeignKey('todo_list.id'), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            new_list = TodoList(name=name)
            db.session.add(new_list)
            db.session.commit()
        return redirect(url_for('index'))
    lists = TodoList.query.all()
    return render_template('index.html', lists=lists)

@app.route('/list/&lt;int:list_id&gt;', methods=['GET', 'POST'])
def view_list(list_id):
    todo_list = TodoList.query.get_or_404(list_id)
    if request.method == 'POST':
        title = request.form.get('title')
        if title:
            task = Task(title=title, todolist_id=todo_list.id)
            db.session.add(task)
            db.session.commit()
        return redirect(url_for('view_list', list_id=list_id))
    return render_template('list.html', todo_list=todo_list)

@app.route('/task/&lt;int:task_id&gt;/toggle', methods=['POST'])
def toggle_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for('view_list', list_id=task.todolist_id))

@app.route('/task/&lt;int:task_id&gt;/delete', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    list_id = task.todolist_id
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('view_list', list_id=list_id))

@app.route('/list/&lt;int:list_id&gt;/delete', methods=['POST'])
def delete_list(list_id):
    todo_list = TodoList.query.get_or_404(list_id)
    db.session.delete(todo_list)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
