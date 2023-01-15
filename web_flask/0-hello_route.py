#!/usr/bin/python3
'''
Script that starts a Flask web application:
    The web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
    The option strict_slashes=False must be used in the route definition
'''
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    '''Displays "Hello HBNB!"'''
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
