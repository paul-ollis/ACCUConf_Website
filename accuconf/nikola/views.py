#!/usr/bin/env python

from flask import send_from_directory
from pathlib import Path, PurePosixPath
from . import nikola


@nikola.record
def init_blueprint(ctxt):
    app = ctxt.app
    nikola.config = app.config
    nikola.logger = app.logger


@nikola.route('/')
def index():
    nikola.logger.info("Index accessed")
    basedir = Path.cwd()
    return send_from_directory(PurePosixPath(basedir,
                                             'accuconf',
                                             'nikola',
                                             'static').as_posix(),
                               'index.html')


@nikola.route('/assets/<path:path>')
def asset(path):
    nikola.logger.info("assets accessed")
    basedir = Path.cwd()
    nikola.logger.info("Requested for %s" % (path))
    nikola.logger.info("Sending from: %s" % (PurePosixPath(basedir,
                                                           'accuconf',
                                                           'nikola',
                                                           'static',
                                                           'assets'
                                                           ).as_posix()))
    return send_from_directory(PurePosixPath(basedir,
                                             'accuconf',
                                             'nikola',
                                             'static',
                                             'assets').as_posix(),
                               path)
