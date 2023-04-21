#!/usr/bin/python3
"""
This module starts a web application that returns
all the State objects in a database
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states")
def all_states():
    """This endpoint returns all State objects"""
    states_obj = storage.all("State")
    states = []
    for state in states_obj.keys():
        states.append(states_obj[state])
    return render_template("7-states_list.html", states=states)


@app.route("/states/<id>")
def state_by_id(id):
    """This endpoint returns a State object that matches id"""
    found_state = None
    states_obj = storage.all("State")
    for key in states_obj.keys():
        if states_obj[key].__dict__.get("id") == id:
            found_state = states_obj[key]
            return render_template("9-states.html", found_state=found_state)

    return render_template("9-states.html", found_state=found_state)


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
