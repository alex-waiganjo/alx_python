#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def task_0():
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(debug=True)
