from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for MVP
lists = []

HOME_TEMPLATE = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>To-Do List Web App</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background: #f9f9f9; color: #333; }
        h1, h2 { color: #2c3e50; }
        .container { max-width: 600px; margin: auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        form { margin-bottom: 20px; }
        input[type="text"] { padding: 8px; width: 70%; border: 1px solid #ccc; border-radius: 4px; }
        button { padding: 8px 15px; background: #3498db; color: white; border: none; border-radius: 4px; cursor: pointer; }
        button:hover { background: #2980b9; }
        ul { list-style-type: none; padding: 0; }
        li { padding: 10px; background: #ecf0f1; margin-bottom: 8px; border-radius: 4px; display: flex; justify-content: space-between; align-items: center; }
        .list-link { text-decoration: none; color: #2980b9; font-weight: bold; }
        .list-link:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <div class="container">
        <h1>My To-Do Lists</h1>
        <form action="/lists" method="POST">
            <input type="text" name="name" placeholder="New list name..." required>
            <button type="submit">Create List</button>
        </form>
        <h2>Existing Lists</h2>
        <ul>
            {% if lists %}
                {% for lst in lists %}
                    <li>
                        <a class="list-link" href="{{ url_for('view_list', list_id=lst.id) }}">{{ lst.name }}</a>
                        <span>({{ lst.tasks|length }} tasks)</span>
                    </li>
                {% endfor %}
            {% else %}
                <p>No lists yet. Create one above!</p>
            {% endif %}
        </ul>
    </div>
</body>
</html>
'''

LIST_DETAIL_TEMPLATE = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>{{ lst.name }} - To-Do List</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background: #f9f9f9; color: #333; }
        h1, h2 { color: #2c3e50; }
        .container { max-width: 600px; margin: auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        form { margin-bottom: 20px; }
        input[type="text"] { padding: 8px; width: 70%; border: 1px solid #ccc; border-radius: 4px; }
        button { padding: 8px 15px; background: #3498db; color: white; border: none; border-radius: 4px; cursor: pointer; }
        button:hover { background: #2980b9; }
        ul { list-style-type: none; padding: 0; }
        li { padding: 10px; background: #ecf0f1; margin-bottom: 8px; border-radius: 4px; display: flex; justify-content: space-between; align-items: center; }
        .back { display: inline-block; margin-bottom: 20px; color: #7f8c8d; text-decoration: none; }
        .back:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <div class="container">
        <a class="back" href="{{ url_for('index') }}">&larr; Back to Lists</a>
        <h1>{{ lst.name }}</h1>
        <form action="{{ url_for('add_task', list_id=lst.id) }}" method="POST">
            <input type="text" name="description" placeholder="New task description..." required>
            <button type="submit">Add Task</button>
        </form>
        <h2>Tasks</h2>
        <ul>
            {% if lst.tasks %}
                {% for task in lst.tasks %}
                    <li>
                        <span>{{ task.description }}</span>
                    </li>
                {% endfor %}
            {% else %}
                <p>No tasks in this list yet.</p>
            {% endif %}
        </ul>
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HOME_TEMPLATE, lists=lists)

@app.route('/lists', methods=['POST'])
def create_list():
    name = request.form.get('name')
    if name:
        new_list = {'id': len(lists) + 1, 'name': name, 'tasks': []}
        lists.append(new_list)
    return redirect(url_for('index'))

@app.route('/lists/<int:list_id>')
def view_list(list_id):
    lst = next((l for l in lists if l['id'] == list_id), None)
    if not lst:
        return "List not found", 404
    return render_template_string(LIST_DETAIL_TEMPLATE, lst=lst)

@app.route('/lists/<int:list_id>/tasks', methods=['POST'])
def add_task(list_id):
    lst = next((l for l in lists if l['id'] == list_id), None)
    if not lst:
        return "List not found", 404
    description = request.form.get('description')
    if description:
        new_task = {'id': len(lst['tasks']) + 1, 'description': description, 'completed': False}
        lst['tasks'].append(new_task)
    return redirect(url_for('view_list', list_id=list_id))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
