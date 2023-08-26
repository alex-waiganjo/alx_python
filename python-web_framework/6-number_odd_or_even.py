#!/usr/bin/python3
""" Routes for all the tasks"""
from flask import Flask, render_template
app = Flask(__name__)


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


@app.route('/number_template/<int:n>', strict_slashes=False)
def task_5(n):
    return render_template('5-number.html', num=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def task_6(n):

    return render_template('6-number_odd_or_even.html', num=n)


if __name__ == "__main__":
    app.run(debug=True)
