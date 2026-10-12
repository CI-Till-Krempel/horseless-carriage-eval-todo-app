from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data store for lists and tasks
todo_lists = {}

@app.route('/')
def index():
    return render_template('index.html', todo_lists=todo_lists)

@app.route('/lists', methods=['POST'])
def create_list():
    list_name = request.form.get('list_name')
    if list_name and list_name not in todo_lists:
        todo_lists[list_name] = []
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
