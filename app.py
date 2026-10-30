from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for lists and tasks
# lists: { list_id: { 'id': int, 'name': str, 'tasks': [ { 'id': int, 'text': str, 'completed': bool } ] } }
todos = {}
list_id_counter = 1
task_id_counter = 1

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/lists', methods=['POST'])
def create_list():
    global list_id_counter
    name = request.form.get('name')
    if name:
        todos[list_id_counter] = {
            'id': list_id_counter,
            'name': name,
            'tasks': []
        }
        list_id_counter += 1
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
