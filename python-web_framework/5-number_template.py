#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)


@app.errorhandler(404)
def error():

    return "error"


@app.route('/', strict_slashes=False)
def task_0():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def task_1():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def task_2(text):
    word = text.split('_')
    return f"C {' '.join(word)}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def task_3(text='is cool'):
    word = text.split('_')

    return f"Python {' '.join(word)}"


@app.route('/number/<n>', strict_slashes=False)
def task_4(n):
    if n is int():
        return f'{n} is a number'
    else:
        return error()


@app.route('/number_template/<n>', strict_slashes=False)
def task_5(n):
    if n is int():
        return render_template('5-number.html', num=n)
    else:
        return error()


if __name__ == "__main__":
    app.run(debug=True)
