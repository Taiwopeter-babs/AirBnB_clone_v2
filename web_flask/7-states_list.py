#!/usr/bin/python3
"""
This module starts a web application that returns
all the State objects in a database
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states_list")
def all_states_obj():
    """This endpoint returns all State objects"""
    states_obj = storage.all("State")
    states = []
    for state in states_obj.keys():
        states.append(states_obj[state])
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def close_db_conn(error):
    """
    This function closes the database connection after
    every request
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
