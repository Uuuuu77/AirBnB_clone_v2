#!/usr/bin/python3
"""
    Starts a Flask eb application.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """ Remove the current SQLAlchemy Session after each request. """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ display a HTML page [inside the tag BODY) """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    """Listening on 0.0.0.0, port 5000"""
    app.run(host='0.0.0.0', port=5000)
