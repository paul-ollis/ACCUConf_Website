#!/usr/bin/env python

from accuconf import app
import json
from flask import render_template, flash, redirect, url_for


@app.route("/")
def index():
    if app.config.get("MAINTENANCE"):
        return redirect(url_for("maintenance"))
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
    return render_template("index.html", frontpage=frontpage)


@app.route("/maintenance")
def maintenance():
    return render_template("maintenance.html")
