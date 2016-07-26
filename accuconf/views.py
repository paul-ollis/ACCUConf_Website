#!/usr/bin/env python

from accuconf import app
import json
from flask import render_template, flash, redirect, url_for, session, request
from accuconf.models import User, UserInfo
from accuconf.database import db
import hashlib


@app.route("/")
def index():
    if app.config.get("MAINTENANCE"):
        return redirect(url_for("maintenance"))
    when_where = {}
    committee = {}
    venuefile = app.config.get('VENUE')
    committeefile = app.config.get('COMMITTEE')
    session['username'] = "User"
    session['fullname'] = "User Name"
    session['active'] = True
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
    return render_template("index.html", frontpage=frontpage)


@app.route("/maintenance")
def maintenance():
    return render_template("maintenance.html")


@app.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        userid = request.form['usermail']
        passwd = request.form['password']
        user = User.query.filter_by(user_id=userid).first()
        password_hash = hashlib.sha256(passwd).hexdigest()
        if user.user_pass == password_hash:
            return redirect(url_for("index"))
        else:
            return redirect(url_for("login"))
    else:
        return redirect(url_for("index"))


@app.route("/register")
def register():
    if request.method == "POST":
        # Process registration data
        user_email = request.form["user_email"]
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        user_pass = request.form["password"]
        if type(user_pass) == str and len(user_pass):
            user_pass = hashlib.sha256(user_pass).hexdigest()
        newuser = User(user_email, user_pass)
        userinfo = UserInfo(user_email, first_name, last_name, Role.user)
        newuser.user_info = userinfo
        db.session.add(newuser)
        db.session.add(userinfo)
        db.session.commit()


@app.route("/proposal/submit")
def propose():
    pass



