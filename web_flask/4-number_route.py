#!/usr/bin/python3

"""
simple flask app that displays Hello HBNB! in the root

Author: Bradley Dillion Gilden
Date: 19-10-2023
"""


from flask import Flask, abort


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """returns the string Hello HBNB! in /"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """returns the string HBNB in /hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """displays dynamic variable"""
    text = text.split('_')
    text = ' '.join(text)
    return f"C {text}"


@app.route("/python/<text>", strict_slashes=False)
@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
def python_route(text):
    """displays dynamic variable with default preset"""
    text = text.split('_')
    text = ' '.join(text)
    return f"Python {text}"


@app.route("/number/<n>", strict_slashes=False)
def number_route(n):
    """display 'n is a number' only if n is an integer"""
    try:
        n = int(n)
        return f"{n} is a number"
    except Exception:
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
