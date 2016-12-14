from flask import Flask, render_template, request, session, flash, redirect, url_for, g
import sqlite3
from keys import secret_key_val

#Configuration
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = secret_key_val
DATABASE = 'blog.db'
app = Flask(__name__)

#Pulls in config info by looking for uppercase variables
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'].strip() != app.config['USERNAME'] or request.form['password'].strip() != app.config['PASSWORD']:
            error = 'Invalid credentials. Please try again'
        else:
            session['logged_in'] = True
            return redirect(url_for('main'))
    return render_template("login.html", error = error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash("You were logged out.")
    return redirect(url_for('login'))

@app.route('/main')
def main():
    return render_template("main.html")

if __name__ == "__main__":
    app.run(debug=True)
