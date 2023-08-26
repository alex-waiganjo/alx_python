#!/usr/bin/python3
""" Writing five routes  """
from flask import Flask,abort
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


@app.route('/c<text>', strict_slashes=False)
def task_2(text):
    return f'C  {text}'


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def task_3(text='cool'):
    return f'Python  {text}'


@app.route('/number/<int:n>', strict_slashes=False)
def task_4(n):      
      return f'{n} is a number'


if __name__ == "__main__":
    app.run(debug=True)