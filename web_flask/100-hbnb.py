#!/usr/bin/python3
"""
Flask App that integrates with AirBnB static HTML Template
"""
from flask import Flask, render_template, url_for
from models import storage
# Flask setup
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'
# Function to be called after each request to close the SQLAlchemy Session
@app.teardown_appcontext
def teardown_db(exception):
    """
    After each request, this method calls .close() (i.e. .remove()) on
    the current SQLAlchemy Session
    """
    storage.close()
# Route for handling requests to the '/hbnb' endpoint
@app.route('/hbnb')
def hbnb_filters(the_id=None):
    """
    Handles request to custom template with states, cities & amenities
    """
    # Fetching state, amenity, place, and user objects from the storage
    state_objs = storage.all('State').values()
    amens = storage.all('Amenity').values()
    places = storage.all('Place').values()
    users = dict([user.id, "{} {}".format(user.first_name, user.last_name)]
                 for user in storage.all('User').values())

    # Rendering the '100-hbnb.html' template and passing data to it
    return render_template('100-hbnb.html',
                           states=dict([state.name, state] for state in state_objs),
                           amens=amens,
                           places=places,
                           users=users)
if __name__ == "__main__":
    """
    MAIN Flask App
    """
    # Running the Flask application on host '0.0.0.0' and port 5000
    app.run(host=host, port=port)

