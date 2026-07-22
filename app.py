import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(test_config=None):
    app = Flask(__name__)
    
    if test_config is None:
        db_path = os.path.join(app.instance_path, 'todo.db')
        os.makedirs(app.instance_path, exist_ok=True)
        app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    else:
        app.config.update(test_config)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        from models import TodoList, Task
        db.create_all()

    from routes import bp as main_bp
    app.register_blueprint(main_bp)

    return app
