#!/usr/bin/python3
"""
Flask App
"""
from flask import Flask, request

app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'


@app.route('/')
def hello():
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    return "HBNB"


@app.route('/c/<text>')
def c(text):
    return 'C {}'.format(text.replace("_", " "))

@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python(text):
    return 'C {}'.format(text.replace("_", " "))

if __name__ == "__main__":
    """
    Flask App
    """
    app.run(host=host, port=port)
