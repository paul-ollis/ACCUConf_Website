#!/usr/bin/env python

from flask import Blueprint, render_template


proposals = Blueprint('proposals', __name__,
                      static_folder='../static',
                      template_folder='templates')
proposals.config = {}
proposals.logger = None

