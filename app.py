from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simple in-memory store
lists = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add_list':
            list_name = request.form.get('list_name')
            if list_name:
                lists.append({'id': len(lists) + 1, 'name': list_name, 'tasks': []})
        elif action == 'add_task':
            list_id = int(request.form.get('list_id'))
            task_text = request.form.get('task_text')
            if task_text:
                for l in lists:
                    if l['id'] == list_id:
                        l['tasks'].append({'id': len(l['tasks']) + 1, 'text': task_text, 'completed': False})
        return redirect(url_for('index'))
    return render_template('index.html', lists=lists)

@app.route('/toggle_task/<int:list_id>/<int:task_id>')
def toggle_task(list_id, task_id):
    for l in lists:
        if l['id'] == list_id:
            for t in l['tasks']:
                if t['id'] == task_id:
                    t['completed'] = not t['completed']
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
