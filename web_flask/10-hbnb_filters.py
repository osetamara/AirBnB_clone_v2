#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
import os
app = Flask(__name__)
def handle_teardown(self):
    """
    Method to handle teardown, closing the storage connection
    """
    storage.close()
@app.route('/hbnb_filters', strict_slashes=False)
def filters_list():
    """
    Method to display HTML page 10-hbnb_filters.html and pass data to it
    """
    # Fetching all 'State' and 'Amenity' objects from the storage
    states = storage.all('State').values()
    amenities = storage.all('Amenity').values()

    # Rendering the HTML template and passing the retrieved data to it
    return render_template(
        "10-hbnb_filters.html",
        states=states, amenities=amenities)
if __name__ == '__main__':
    # Running the Flask application on host '0.0.0.0' and port 5000
    app.run(host='0.0.0.0', port=5000)
i
