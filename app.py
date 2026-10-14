from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

lists = {}

@app.route('/')
def index():
    return render_template('index.html', lists=lists)

@app.route('/lists', methods=['POST'])
def create_list():
    name = request.form.get('name')
    if name:
        lists[name] = []
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
