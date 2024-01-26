#!/usr/bin/python3
"""
    It starts a flask web application.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ /: displays "Hello HBNB!" """
    return "Hello HBNB!"


if __name__ == "__main__":
    """ Listening on 0.0.0.0, port 5000 """
    app.run(host='0.0.0.0', port=5000)
