#!/usr/bin/python3
"""This module starts a flask web application"""
from flask import Flask, render_template


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


@app.route("/number/<int:n>")
def is_number(n):
    """returns a number in a URL, otherwise 404"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def num_int_template(n):
    """renders a template only if n is an integer instance, otherwise 404"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>")
def odd_even_template(n):
    """renders a template only if n is an integer instance, otherwise 404"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
