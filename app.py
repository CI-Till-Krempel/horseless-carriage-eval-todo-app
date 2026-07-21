from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simple in-memory store
lists = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        list_name = request.form.get('list_name')
        if list_name:
            lists.append({'id': len(lists) + 1, 'name': list_name, 'tasks': []})
        return redirect(url_for('index'))
    return render_template('index.html', lists=lists)

if __name__ == '__main__':
    app.run(debug=True)
