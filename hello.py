"""
Simple "Hello, World" application using Flask
"""
from mbta_helper import *

from flask import Flask

app = Flask(__name__)

app.config['DEBUG'] = True


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/find')
def find_stop():
    place_name = 'Babson College'
    url = GMAPS_BASE_URL + '?address=' + place
    return get_json(url)


if __name__ == '__main__':
    app.run()
