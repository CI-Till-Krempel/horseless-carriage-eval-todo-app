from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class TodoList(db.Model):
    __tablename__ = 'todo_list'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    tasks = db.relationship('Task', backref='todo_list', cascade='all, delete-orphan', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'tasks': [task.to_dict() for task in self.tasks]
        }

class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    complete = db.Column(db.Boolean, default=False, nullable=False)
    list_id = db.Column(db.Integer, db.ForeignKey('todo_list.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'complete': self.complete,
            'list_id': self.list_id
        }
