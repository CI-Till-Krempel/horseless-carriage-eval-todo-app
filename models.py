from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ToDoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    tasks = db.relationship('Task', backref='todo_list', cascade='all, delete-orphan', lazy=True)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    complete = db.Column(db.Boolean, default=False, nullable=False)
    list_id = db.Column(db.Integer, db.ForeignKey('to_do_list.id'), nullable=False)
