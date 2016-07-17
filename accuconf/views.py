#!/usr/bin/env python

from accuconf import app
from flask import render_template, flash, redirect, url_for

@app.route("/")
def index():
    frontpage = {
        "title": "ACCU Conference 2017",
        "data": "Welcome to ACCU Conf 2017",
        "when_where": {
            "where": ["Marriott Hotel", "Lower Castle Street", "Bristol"],
            "when": "2016-04-19 to 2016-04-23"
        }
    }
    return render_template("index.html", frontpage=frontpage)
