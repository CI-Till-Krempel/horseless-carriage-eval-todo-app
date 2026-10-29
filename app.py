from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory database for MVP
lists = []
tasks = {}

@app.route('/')
def index():
    return render_template('index.html', lists=lists, tasks=tasks)

@app.route('/lists', methods=['POST'])
def create_list():
    name = request.form.get('name')
    if name:
        list_id = len(lists) + 1
        lists.append({'id': list_id, 'name': name})
        tasks[list_id] = []
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
