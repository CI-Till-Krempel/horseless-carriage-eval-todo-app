from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# In-memory store for demonstration
lists = []

@app.route('/')
def index():
    return render_template_string('''
        <h1>To-Do Lists</h1>
        <ul>
        {% for lst in lists %}
            <li>
                <strong>{{ lst.name }}</strong>
                <ul>
                {% for task in lst.tasks %}
                    <li>
                        {% if task.completed %}
                            <span style="text-decoration: line-through; color: gray;">[Completed] {{ task.title }}</span>
                        {% else %}
                            <span>[Pending] {{ task.title }}</span>
                        {% endif %}
                    </li>
                {% endfor %}
                </ul>
            </li>
        {% endfor %}
        </ul>
    ''', lists=lists)

if __name__ == '__main__':
    app.run(debug=True)
