#!/usr/bin/python3

"""
This module lists states dynamically from a database

Author: Bradley Dillion Gilden
Date: 20-10-2023
"""


from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.teardown_appcontext
def close_storage(err):
    """closes SQLAlchemy session if db storage or reloads file storage"""
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """returns a template with a list of states"""
    amenities = list(storage.all(Amenity).values())
    states = list(storage.all(State).values())
    return render_template('10-hbnb_filters.html',
                           amenities=amenities, states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
