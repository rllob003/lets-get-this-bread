from functools import wraps
import json
from os import environ as env
from werkzeug.exceptions import HTTPException

from dotenv import load_dotenv, find_dotenv
from flask import Flask
from flask import jsonify
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for
from authlib.integrations.flask_client import OAuth
from six.moves.urllib.parse import urlencode

import constants


app = Flask(__name__)
app.secret_key = constants.SECRET_KEY
app.debug = True

# Controllers API

@app.route('/static')
def static_feed():
    return render_template('static.html')


if __name__ == "__main__":
    app.run()

