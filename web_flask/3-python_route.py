#!/usr/bin/python3
"""
    Starts a flask web application.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ /: display "Hello HBNB!" """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ /hbnb: display "HBNB" """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text():
    """ displays c followed by <text> """
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """ display python followed by <text> """
    text = text.replace('_', ' ')
    return f"Python {text}"


if __name__ == "__main__":
    """Listening on 0.0.0.0, port 5000"""
    app.run(host='0.0.0.0', port=5000)