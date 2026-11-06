import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
import bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)

# In-memory lists/tasks store for backward compatibility or future stories
lists_db = []

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html', lists=lists_db)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if not username or not password:
            flash('Username and password are required.')
            return redirect(url_for('register'))
        
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username is already taken.')
            return redirect(url_for('register'))
        
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        new_user = User(username=username, password_hash=hashed.decode('utf-8'))
        db.session.add(new_user)
        db.session.commit()
        
        session['user_id'] = new_user.id
        session['username'] = new_user.username
        flash('Registration successful!')
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/lists', methods=['POST'])
def create_list():
    name = request.form.get('name')
    if name:
        lists_db.append({'id': len(lists_db) + 1, 'name': name, 'tasks': []})
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/tasks', methods=['POST'])
def add_task(list_id):
    description = request.form.get('description')
    if description:
        for lst in lists_db:
            if lst['id'] == list_id:
                lst['tasks'].append({'id': len(lst['tasks']) + 1, 'description': description, 'completed': False})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
