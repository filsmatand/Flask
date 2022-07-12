from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app=Flask(__name__)


@app.route('/')

def hello():
    return render_template('index.html')
app.run()