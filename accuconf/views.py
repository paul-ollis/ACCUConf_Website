#!/usr/bin/env python

from accuconf import app
import json
from flask import render_template, flash, redirect, url_for, session, request
from accuconf.models import User, UserInfo, UserLocation, MathPuzzle
from accuconf.roles import Role
from accuconf.database import db
import hashlib
from random import randint


@app.route("/")
def index():
    if app.config.get("MAINTENANCE"):
        return redirect(url_for("maintenance"))
    session['active'] = False
    when_where = {}
    committee = {}
    venuefile = app.config.get('VENUE')
    committeefile = app.config.get('COMMITTEE')
    if venuefile.exists():
        when_where = json.loads(venuefile.open().read())

    if committeefile.exists():
        committee = json.loads(committeefile.open().read())

    frontpage = {
        "title": "ACCU Conference 2017",
        "data": "Welcome to ACCU Conf 2017",
        "when_where": when_where,
        "committee": committee.get("members", [])
    }
    return render_template("index.html", page=frontpage)


@app.route("/maintenance")
def maintenance():
    return render_template("maintenance.html")


@app.route("/login", methods = ['GET', 'POST'])
def login():
    if app.config.get("MAINTENANCE"):
        return redirect(url_for("maintenance"))
    if request.method == "POST":
        userid = request.form['usermail']
        passwd = request.form['password']
        user = User.query.filter_by(user_id=userid).first()
        password_hash = hashlib.sha256(passwd).hexdigest()
        if user.user_pass == password_hash:
            session['username'] = user.user_id
            session['fullname'] = "%s %s" % (user.user_info.first_name,
                                             user.user_info.last_name)
            session['active'] = True
            return redirect(url_for("index"))
        else:
            return redirect(url_for("login"))
    else:
        return redirect(url_for("index"))


@app.route("/logout")
def logout():
    session['active'] = False


@app.route("/register", methods=["GET", "POST"])
def register():
    if app.config.get("MAINTENANCE"):
        return redirect(url_for("maintenance"))
    if request.method == "POST":
        # Process registration data
        user_email = request.form["email"]
        user_pass = request.form["password"]
        salutation = request.form["salutation"]
        suffix = request.form["suffix"]
        first_name = request.form["firstname"]
        last_name = request.form["lastname"]
        country = request.form["country"]
        state = request.form["state"]
        #states = request.form["states"]
        phone = request.form["phone"]
        postal_code = request.form["pincode"]

        if type(user_pass) == str and len(user_pass):
            user_pass = hashlib.sha256(user_pass.encode('utf-8')).hexdigest()

        app.logger.debug("user_email: %s" % (user_email))
        newuser = User(user_email, user_pass)
        userinfo = UserInfo(newuser.user_id,
                            salutation,
                            first_name,
                            last_name,
                            suffix,
                            phone,
                            Role.user.get("name", "user")
                            )
        userlocation = UserLocation(newuser.user_id,
                                    country,
                                    state,
                                    postal_code)
        newuser.user_info = userinfo
        newuser.location = userlocation

        db.session.add(newuser)
        db.session.add(userinfo)
        db.session.add(userlocation)
        db.session.commit()
        page = {
            "title": "Registration successful",
            "data": "You have successfully registered for submitting "
                    "proposals for the ACCU Conf. Please login and start "
                    "preparing your proposal for the conference."
        }
        return render_template("registration_success.html", page=page)
    elif request.method == "GET":
        question_id = randint(1, 1000)
        question = MathPuzzle.query.filter_by(id=question_id).first()
        register = {
            "title": "Register",
            "data": "Register here for submitting proposals to ACCU Conference",
            "question": question.id,
            "puzzle": question.question
        }
        return render_template("register.html", page=register)


@app.route("/proposal/new")
def propose():
    if app.config.get("MAINTENANCE"):
        return redirect(url_for("maintenance"))
    if session.get("active", False):
        return render_template("submit_proposal.html")

@app.route("/proposal/submit")
def submit_proposal():
    if app.config.get("MAINTENANCE"):
        return redirect(url_for("maintenance"))



