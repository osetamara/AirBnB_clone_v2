#!/usr/bin/python3
"""Simple Flask app with three routes:"""
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    """Return 'Hello HBNB!' for root route."""
    return 'Hello HBNB!'
@app.route('/hbnb')
def hbnb():
    """Return 'HBNB' for'/hbnb' route."""
    return 'HBNB'
@app.route('/c/<text>')
def c_is_fun(text):
    """Return reformatted text with 'C 'prefix."""
    return 'C ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
