#!/usr/bin/env python

from flask import Flask
import accuconf_config


app = Flask(__name__,
            instance_path="/etc/accuconf/",
            instance_relative_config=True)
app.config.from_object(accuconf_config.TestConfig)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/accuconf_test.db"
app.secret_key = app.config['SECRET_KEY']

from .database import db, create_db
from .models import MathPuzzle
from random import randint


def init_sec_ctxt():
    puzzle_init = [(randint(1,20), randint(1, 20)) for _ in range(1, 1001)]
    puzzles = [MathPuzzle("%d + %d" % (p[0], p[1]), p[0] + p[1]) for p in
                      puzzle_init]
    for p in puzzles:
        db.session.add(p)
    db.session.commit()

db.create_all()
init_sec_ctxt()

from .views import *
