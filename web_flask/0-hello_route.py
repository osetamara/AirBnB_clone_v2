#!/usr/bin/python3
"""Start a Flask web app.
This script defines a simple Flask web application that responds with
'Hello HBNB!' when the root route ('/') is queried.
Usage:
    - Run the script to start the Flask app on '0.0.0.0' and port 5000.
Note:
    - The `app.url_map.strict_slashes` is set to False to allow both
      '/path' and '/path/' to be valid routes.
Dependencies:
    - Flask library is required.
Author:
    [Your Name]
"""
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_flask():
    """Return string when route is queried."""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
