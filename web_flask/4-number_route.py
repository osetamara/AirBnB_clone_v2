#!/usr/bin/python3
"""Simple Flask app with multiple routes including dynamic '/number/<int:n>'."""
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
@app.route('/c/<text>')
def c_is_fun(text):
    """Return reformatted text with 'C ' prefix."""
    return 'C ' + text.replace('_', ' ')
@app.route('/python/')
@app.route('/python/<text>')
def python_with_text(text='is cool'):
    """Return reformatted text with 'Python ' prefix based on optional variable."""
    return 'Python ' + text.replace('_', ' ')
@app.route('/number/<int:n>')
def number(n=None):
    """Allow request if path variable is a valid integer and return it as a string."""
    return str(n) + ' is a number'
if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)

