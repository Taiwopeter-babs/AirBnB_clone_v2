#!/usr/bin/python3
"""This module starts a flask web application"""
from flask import Flask


app = Flask(__name__)
# set rule for all routes
app.url_map.strict_slashes = False


@app.route("/")
def index():
    """returns a text response"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """returns a text response"""
    return "HBNB"


@app.route("/c/<text>")
def c_text(text):
    """returns a text in a URL"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python")
@app.route("/python/<text>")
def python_text(text="is_cool"):
    """returns a text in a URL"""
    if "_" in text:
        text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<n>")
def is_number(n):
    """returns a number in a URL"""
    if n.isdigit():
        return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
