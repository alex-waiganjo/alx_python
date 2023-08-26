#!/usr/bin/python3
""" Contains five routes """
from flask import Flask, abort, render_template
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


# Display if n is integer
@app.route('/number/<int:n>', strict_slashes=False)
def task_4(n):
    return f'{n} is a number'


# Display if n is float
@app.route('/number/<float:n>', strict_slashes=False)
def task_4_1(n):
    abort(404)


# Display if n is string
@app.route('/number/<string:n>', strict_slashes=False)
def task_4_2(n):
    abort(404)


@app.route('/number_template/<int:n>', strict_slashes=False)
def task_5(n):
    return render_template('5-number.html',num=n)
    


if __name__ == "__main__":
    app.run(debug=True)
