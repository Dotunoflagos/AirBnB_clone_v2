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
def hello():
    return "HBNB"

if __name__ == "__main__":
    """
    Flask App
    """
    app.run(host=host, port=port)
