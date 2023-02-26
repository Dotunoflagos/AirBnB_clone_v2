#!/usr/bin/python3
"""
Flask App
"""
from flask import Flask, request, render_template
from models import storage

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
    return 'Python {}'.format(text.replace("_", " "))


@app.route('/number/<int:n>')
def intys(n):
    if isinstance(n, int):
        return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def displ(n):
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def oddevn(n):
    if isinstance(n, int):
        return render_template('6-number_odd_or_even.html', n=n)

@app.route('/states_list')
def statelst():
    return render_template('7-states_list.html', states=storage.all('State').values())

@app.teardown_appcontext
def tear(exception):
    storage.close()

if __name__ == "__main__":
    """
    Flask App
    """
    app.run(host=host, port=port)
