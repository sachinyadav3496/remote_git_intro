#!/usr/local/anaconda3/bin/python

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    # location of html files are always inside templates folder
@app.route('/data/')
def data():
    return render_template('data.html')


app.run('localhost', 80)
