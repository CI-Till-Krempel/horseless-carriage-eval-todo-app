from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory database for lists and tasks
lists = []

@app.route('/')
def index():
    return render_template('index.html', lists=lists)

@app.route('/lists', methods=['POST'])
def create_list():
    title = request.form.get('title')
    if title:
        lists.append({'id': len(lists) + 1, 'title': title, 'tasks': []})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
