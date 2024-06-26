#!/usr/bin/python3
"""Starts a Flask web app.
The application listens on 0.0.0.0, port 5000.

Routes:
    /: Displays 'Hello HBNB!'
    /hbnb: Displays 'HBNB'
"""
from flask import Flask

app = Flask(__name__)


# Define a route with variable
@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Returns 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns 'HBNB'"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
