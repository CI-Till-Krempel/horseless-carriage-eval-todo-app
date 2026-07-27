from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'todo-secret-key'

# In-memory data store
lists = []

@app.route('/')
def index():
    return render_template('index.html', lists=lists)

@app.route('/lists', methods=['POST'])
def create_list():
    name = request.form.get('name', '').strip()
    if not name:
        flash('List name cannot be empty or whitespace.', 'error')
    else:
        new_list = {'id': len(lists) + 1, 'name': name, 'tasks': []}
        lists.append(new_list)
        flash('To-do list created successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
