from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for lists
lists = []

@app.route('/')
def index():
    return render_template('index.html', lists=lists)

@app.route('/lists', methods=['POST'])
def create_list():
    name = request.form.get('name')
    if name:
        lists.append({'id': len(lists) + 1, 'name': name, 'tasks': []})
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>/tasks', methods=['POST'])
def add_task(list_id):
    content = request.form.get('content')
    if content:
        for lst in lists:
            if lst['id'] == list_id:
                lst['tasks'].append({'id': len(lst['tasks']) + 1, 'content': content, 'completed': False})
                break
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
