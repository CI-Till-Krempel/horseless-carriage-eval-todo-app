from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

lists = {}

@app.route('/')
def index():
    return render_template('index.html', lists=lists)

@app.route('/lists', methods=['POST'])
def create_list():
    name = request.form.get('name')
    if name and name not in lists:
        lists[name] = []
    return redirect(url_for('index'))

@app.route('/lists/<list_name>/tasks', methods=['POST'])
def add_task(list_name):
    task_desc = request.form.get('task')
    if list_name in lists and task_desc:
        lists[list_name].append({'description': task_desc, 'completed': False})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
