from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for lists and tasks
lists = []

@app.route('/')
def index():
    return render_template('index.html', lists=lists)

@app.route('/lists', methods=['POST'])
def create_list():
    name = request.form.get('name')
    if name:
        new_list = {
            'id': len(lists) + 1,
            'name': name,
            'tasks': []
        }
        lists.append(new_list)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
