#!/usr/bin/python3
"""Simple Flask app with two routes: '/' and '/hbnb'."""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    """Return 'Hello HBNB!' for the root route."""
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    """Return 'HBNB' for the '/hbnb' route."""
    return 'HBNB'

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
