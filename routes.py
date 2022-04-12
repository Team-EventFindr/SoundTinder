from app import app, db
import random
import os

import flask
from flask_login import login_user, current_user, LoginManager, logout_user
from flask_login.utils import login_required
from models import User
from oauthlib.oauth2 import (WebApplicationClient,)  # will be used later on for Google sign-in, Possible Spotify Integration?
from werkzeug.security import generate_password_hash, check_password_hash

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_name):
    return User.query.get(user_name)


@app.route("/signup")
def signup():
    return flask.render_template("signup.html")


@app.route("/signup", methods=["POST"])
def signup_post():
    username = flask.request.form.get("Username")
    password = flask.request.form.get("Password")
    email = flask.request.form.get("Email")
    user = User.query.filter_by(username=username).first()
    if user:
        pass
    else:
        sign_user = User(
            Username=username,
            Email=email,
            Password=generate_password_hash(password, method="sha256"),
        )
        db.session.add(sign_user)
        db.session.commit()

    return flask.redirect(flask.url_for("login"))


@app.route("/login")
def login():
    return flask.render_template("login.html")


@app.route("/login", methods=["POST"])
def login_post():
    currusername = flask.request.form.get("Username")
    currpassword = flask.request.form.get("Password")
    user = User.query.filter_by(Username=currusername).first()
    currpassword = generate_password_hash(currpassword, method="sha256")
    currpass = User.query.filter_by(Password=currpassword).first()
    if user and currpass:
        login_user(user)
        return flask.redirect(flask.url_for("index"))

    else:
        return flask.jsonify({"status": 401, "reason": "Username or Password Error"})


@app.route("/")
def landing():
    if current_user.is_authenticated:
        return flask.redirect("index")
    return flask.redirect("login")


@app.route("/logout")
def logout():
    logout_user()
    return flask.redirect("login")


@app.route("/index")
@login_required
def index():
    
    # API calls
    


if __name__ == "__main__":
    app.run(
        host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", 8000)),
        debug=True,
    )
