from functools import wraps
import json
from os import environ as env

# from werkzeug.exceptions import HTTPException

# from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template, url_for, flash, redirect
from flask import jsonify
from flask import session
from flask import send_from_directory
from authlib.integrations.flask_client import OAuth
from six.moves.urllib.parse import urlencode
from forms import LoginForm

MESSAGE = ""

# ENV_FILE = find_dotenv()
# if ENV_FILE:
#     load_dotenv(ENV_FILE)


app = Flask(__name__, static_url_path="/public", static_folder="./public")
app.debug = True
app.config["SECRET_KEY"] = "77abd6e0f451012576581201d898304d"


@app.errorhandler(Exception)
def handle_auth_error(ex):
    response = jsonify(message=str(ex))
    # response.status_code = ex.code if isinstance(ex, HTTPException) else 500
    return response


# Controllers API
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@xtremer.com" and form.password.data == "admin@123":
            return redirect(url_for("dashboard"))
        else:
            global MESSAGE
            MESSAGE = "Invalid credentials"
            return redirect(url_for("home"), MESSAGE)
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/video")
def video():
    return redirect("videotest.html")


@app.route("/stream")
def stream():
    return render_template("stream.html")


if __name__ == "__main__":
    app.run()
