#!/usr/bin/python3
"""
starts a Flask web application
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """display text"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """display text"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """display text"""
    out = "C " + text.replace('_', ' ')
    return out


@app.route("/python", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pytho(text="is_cool"):
    """display text"""
    out = "Python " + text.replace('_', ' ')
    return out


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """display number n"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """display HTML page"""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
