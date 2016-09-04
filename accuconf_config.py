#!/usr/bin/env

from pathlib import Path


class Config(object):
    SQLALCHEMY_DATABASE_URI = "sqlite:///tmp/accuconf.db"
    DEBUG = False
    DATA_DIR = Path("/etc/accuconf/data")
    VENUE = DATA_DIR / "venue.json"
    COMMITTEE = DATA_DIR / "committee.json"
    MAINTENANCE = False
    SECRET_KEY = "TheObviouslyOpenSecret"
    MODULE_PATH = "/tmp/accuconfweb/accuconf"


class ProductionConfig(Config):
    pass


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///tmp/accuconf_test.db"
    DEBUG = True
    DATA_DIR = Path("/tmp/data")
    VENUE = DATA_DIR / "venue.json"
    COMMITTEE = DATA_DIR / "committee.json"
    FRONTPAGE = DATA_DIR / "frontpage.adoc"
    SECRET_KEY = "!@#!@#!#!@#!@$SDFQWETR!$#VWERT@#$%123412qwE%$"


class MaintenanceConfig(Config):
    MAINTENANCE = True


class MaintenanceTest(TestConfig):
    MAINTENANCE = True
