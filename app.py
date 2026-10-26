from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for lists and tasks
# Lists: dictionary mapping list_id to {"id": list_id, "name": name, "tasks": []}
lists = {}
counter = 1

@app.route('/')
def index():
    return render_template('index.html', lists=lists)

@app.route('/lists', methods=['POST'])
def create_list():
    global counter
    name = request.form.get('name')
    if name:
        list_id = str(counter)
        counter += 1
        lists[list_id] = {"id": list_id, "name": name, "tasks": []}
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
