#!/usr/bin/env python

from flask import Blueprint, render_template


nikola = Blueprint('nikola', __name__,
                   static_folder='static',
                   url_prefix='/site')
nikola.config = {}
nikola.logger = None
