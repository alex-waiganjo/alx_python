#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def task_0():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def task_1():
    return 'HBNB!'


@app.route('/c/<text>', strict_slashes=False)
def task_2(text):
    return f'C {text}'


if __name__ == "__main__":
    app.run(debug=True)
