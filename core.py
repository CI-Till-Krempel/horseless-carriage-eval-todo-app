# Fresh source write for US-0003
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'todo-secret-key'

lists = []

@app.route('/')
def index():
    return render_template('index.html', lists=lists)
