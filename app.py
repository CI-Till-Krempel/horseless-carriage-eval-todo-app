from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data store
lists = []

@app.route('/')
def index():
    return render_template('index.html', lists=lists)

@app.route('/create_list', methods=['POST'])
def create_list():
    list_name = request.form.get('list_name')
    if list_name:
        lists.append({'name': list_name, 'tasks': []})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
