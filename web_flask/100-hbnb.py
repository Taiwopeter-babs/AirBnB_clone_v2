#!/usr/bin/python3
"""
This module starts a web application that returns
all the State objects in a database
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/hbnb")
def hbnb_landing():
    """This endpoint renders in the template all the objects
    in their respective sections
    """
    all_objs = {}

    states = storage.all("State").values()
    cities = storage.all("City").values()
    amenities = storage.all("Amenity").values()
    places = storage.all("Place").values()

    obj_dict = {"states": states, "cities": cities, "amenities": amenities, "places": places}

    return render_template("100-hbnb.html", **obj_dict)


@app.teardown_appcontext
def close_db_conn(error):
    """
    This function closes the database connection after
    every request
    """
    storage.close()


if __name__ == "__main__":
    storage.reload()
    app.run(host="0.0.0.0", port=5000)
