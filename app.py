import json
from os import environ as env

from flask import Flask
from flask import render_template

import constants


app = Flask(__name__)
app.secret_key = constants.SECRET_KEY
app.debug = True

# Controllers API

@app.route('/')
def static_feed():
    return render_template('static.html')


if __name__ == "__main__":
    app.run()

