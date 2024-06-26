from flask import Flask, render_template, redirect, url_for, request, flash, Response
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os
import time

app = Flask(__name__)
app.secret_key = 'secret123@@!'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

log_directory = os.path.expanduser('~/server3') 

users = {'admin': {'password': 'password'}} 

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id) if user_id in users else None

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            user = User(username)
            login_user(user)
            flash('Logged in successfully.')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.')
    return redirect(url_for('login'))

@app.route('/')
@login_required
def index():
    files = os.listdir(log_directory)
    return render_template('index.html', files=files)

@app.route('/logs/<filename>')
@login_required
def serve_log(filename):
    file_path = os.path.join(log_directory, filename)
    if not os.path.isfile(file_path):
        return "File not found", 404
    return render_template('log_viewer.html', filename=filename)

@app.route('/stream/<filename>')
@login_required
def stream_log(filename):
    file_path = os.path.join(log_directory, filename)
    if not os.path.isfile(file_path):
        return "File not found", 404

    return Response(
        stream_template(file_path),
        mimetype='text/event-stream'
    )

def stream_template(file_path):
    def generate():
        with open(file_path) as f:
            while True:
                where = f.tell()
                line = f.readline()
                if not line:
                    time.sleep(1)
                    f.seek(where)
                else:
                    yield 'data: {}\n\n'.format(line.strip())
    return generate()

if __name__ == '__main__':
    app.run(debug=True, port=3001)

