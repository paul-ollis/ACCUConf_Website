#!/usr/bin/env python

from accuconf import app
from flask import render_template, flash, redirect, url_for

@app.route("/")
def index():
    frontpage = {
        "data": "Welcome to ACCU Conf 2017"
    }
    return render_template("index.html", frontpage=frontpage)
