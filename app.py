from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data store for lists
todo_lists = []

@app.route('/')
def index():
    return render_template('index.html', lists=todo_lists)

@app.route('/lists', methods=['POST'])
def create_list():
    name = request.form.get('name')
    if name and name.strip():
        todo_lists.append({'id': len(todo_lists) + 1, 'name': name.strip()})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
