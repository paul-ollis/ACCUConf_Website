
from pathlib import Path


class Config(object):
    ACCUCONF_DB_FILE = Path(__file__).resolve().parent / 'accuconf.db'
    SQLALCHEMY_DATABASE_URI = "sqlite:///%s" % (ACCUCONF_DB_FILE)
    DEBUG = False
    DATA_DIR = Path("/etc/accuconf/data")
    VENUE = DATA_DIR / "venue.json"
    COMMITTEE = DATA_DIR / "committee.json"
    MAINTENANCE = False
    SECRET_KEY = "TheObviouslyOpenSecret"
    NIKOLA_STATIC_PATH = Path(__file__).resolve().parent / 'accuconf' / 'nikola' / 'static'


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


class MaintenanceTestConfig(TestConfig):
    MAINTENANCE = True
