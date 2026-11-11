from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# In-memory storage for lists and tasks
lists = {}
next_list_id = 1

@app.route('/')
def index():
    return render_template('index.html', lists=lists)

@app.route('/lists', methods=['POST'])
def create_list():
    global next_list_id
    name = request.form.get('name') or (request.json and request.json.get('name'))
    if not name:
        if request.is_json:
            return jsonify({'error': 'List name is required'}), 400
        return redirect(url_for('index'))
    
    list_id = str(next_list_id)
    next_list_id += 1
    lists[list_id] = {'id': list_id, 'name': name, 'tasks': []}
    
    if request.is_json:
        return jsonify(lists[list_id]), 201
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
