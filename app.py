from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data store
# lists: dict mapping list_id -> {'id': list_id, 'name': name, 'tasks': []}
lists_store = {}
next_list_id = 1

@app.route('/')
def index():
    return render_template('index.html', lists=lists_store.values())

@app.route('/lists', methods=['POST'])
def create_list():
    global next_list_id
    name = request.form.get('name', '').strip()
    if name:
        list_id = str(next_list_id)
        next_list_id += 1
        lists_store[list_id] = {
            'id': list_id,
            'name': name,
            'tasks': []
        }
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
