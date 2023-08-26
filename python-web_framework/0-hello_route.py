#!/usr/bin/python3
""" Writing the first route in flask"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def task_0():
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(debug=True)
