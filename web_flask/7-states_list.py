#!/usr/bin/python3

"""
This module lists states dynamically from a database

Author: Bradley Dillion Gilden
Date: 20-10-2023
"""


from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close_storage(err):
    """closes SQLAlchemy session if db storage or reloads file storage"""
    storage.close()

@app.route("/states_list", strict_slashes=False)
def states_list():
    """returns a template with a list of states"""
    states = list(storage.all(State).values())
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
