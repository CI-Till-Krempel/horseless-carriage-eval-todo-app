from flask import Flask
from models import db
from routes import main_bp
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'
db_path = os.path.join(app.instance_path, 'todo.db')
os.makedirs(app.instance_path, exist_ok=True)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.register_blueprint(main_bp)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
