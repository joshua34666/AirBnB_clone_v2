#!/usr/bin/python3
'''
Script that starts a Flask web appliction and lists all the states and
cities objects alphabeticallly in A->Z. This also includes the HTML pages
'''
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_database(self):
    '''Closes all sqlalchemy session in the database'''
    storage.close()


@app.route('/states/', strict_slashes=False)
def states():
    '''Returns the list of all states'''
    states = storage.all(State)
    return render_template('9-states.html', states=states, mode='all')


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    '''Returns the list all the states by id'''
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', states=state, mode='id')
    return render_template('9-states.html', states=state, mode='none')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
