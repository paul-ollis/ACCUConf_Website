#!/usr/bin/env


class Config(object):
    SQLALCHEMY_DATABASE_URI = "sqlite:///tmp/accuconf_test.db"
    DEBUG = False


class ProductionConfig(object):
    pass
