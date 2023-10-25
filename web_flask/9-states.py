#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, render_template
from models import storage


app = Flask("__name__")


@app.teardown_appcontext
def remove_session(exception):
    storage.close()

@app.route("/states_list", strict_slashes=False)
def display_states():
    data = storage.all(State)
    return render_template('7-states_list.html', states_list=data.values())

@app.route("/cities_by_states", strict_slashes=False)
def display_cities():
    data = storage.all(State)
    return render_template('8-cities_by_states.html', states_list=data.values())


if __name__ == "__main__":
    app.run()
