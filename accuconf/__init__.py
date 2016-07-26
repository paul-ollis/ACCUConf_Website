#!/usr/bin/env python

from flask import Flask
import accuconf_config


app = Flask(__name__,
            instance_path="/etc/accuconf/",
            instance_relative_config=True)
app.config.from_object(accuconf_config.TestConfig)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/accuconf_test.db"
app.secret_key = app.config['SECRET_KEY']
from .views import *
