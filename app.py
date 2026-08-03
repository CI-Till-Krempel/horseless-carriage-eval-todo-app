from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data store for lists
todo_lists = []

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', todo_lists=todo_lists)

@app.route('/lists', methods=['POST'])
def create_list():
    name = request.form.get('name')
    if name:
        todo_lists.append({'id': len(todo_lists) + 1, 'name': name, 'tasks': []})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
