#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def remove_session(exception):
    if storage is not None:
        storage.close()


@app.route("/states_list", strict_slashes=False)
def display_states():
    data = storage.all(State)
    return render_template('7-states_list.html', states_list=data.values())


if __name__ == '__main__':
    app.run()
