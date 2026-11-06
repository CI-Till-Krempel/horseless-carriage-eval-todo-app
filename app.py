import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret-key'

# In-memory data store for lists and tasks
lists_db = []

@app.route('/')
def index():
    return render_template('index.html', lists=lists_db)

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
