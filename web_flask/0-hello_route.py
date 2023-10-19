#!/usr/bin/python3

"""
simple flask app that displays Hello HBNB! in the root

Author: Bradley Dillion Gilden
Date: 19-10-2023
"""


from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """returns the string Hello HBNB!"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)