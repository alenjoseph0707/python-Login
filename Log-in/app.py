import os
import json
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = '#'  # Replace with your actual generated key

# Load users from JSON file
def load_users():
    if os.path.exists('users.json'):
        with open('users.json', 'r') as f:
            return json.load(f)
    return {}

# Save users to JSON file
def save_users(users):
    with open('users.json', 'w') as f:
        json.dump(users, f)

# Log function to print user login events to terminal
def log_user_login(username, password):
    now = datetime.now()
    formatted_date = now.strftime("%d/%b/%Y %H:%M:%S")
    print(f"User '{username}' with password '{password}' logged in at {formatted_date}")

# Route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = load_users()
        
        if username in users and users[username] == password:
            session['username'] = username
            log_user_login(username, password)  # Log user login event with password
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password. Please try again.', 'error')

    return render_template('login.html')

# Route for user signup
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == ['POST']:
        username = request.form['username']
        password = request.form['password']
        users = load_users()
        
        if username in users:
            flash('Username already exists. Please choose a different username.', 'error')
        else:
            users[username] = password
            save_users(users)
            flash('Account created successfully! Please log in.', 'success')
            return redirect(url_for('login'))

    return render_template('signup.html')

# Route for user logout
@app.route('/logout', methods=['POST'])
def logout():
    username = session.pop('username', None)
    if username:
        flash(f"User '{username}' logged out.", 'info')
    return redirect(url_for('login'))

# Route for index/home page
@app.route('/')
def index():
    username = session.get('username')
    if username:
        return render_template('index.html', username=username)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
