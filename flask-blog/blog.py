from flask import Flask, render_template, request, session, flash, redirect, url_for, g
import sqlite3

#Configuration
DATABASE = 'blog.db'
app = Flask(__name__)

#Pulls in config info by looking for uppercase variables
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE']

if __name__ == "__main__":
    ap.run(debug=True)
