#!/usr/bin/python3
"""
    Starts a flask web application.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ /: display “Hello HBNB!” """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ /hbnb: display “HBNB” """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ display c followed by <text> """
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """ display python followed by <text> """
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ display n is number if integer """
    return f"{n} is a number"


if __name__ == "__main__":
    """listening on 0.0.0.0, port 5000"""
    app.run(host='0.0.0.0', port=5000, debug=True)
