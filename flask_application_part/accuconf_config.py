
from pathlib import Path


class ConfigBase:
    _here = Path(__file__).resolve().parent
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + str(_here / 'accuconf.db')
    DEBUG = False
    DATA_DIR = _here / 'etc' / 'data'
    VENUE = DATA_DIR / "venue.json"
    COMMITTEE = DATA_DIR / "committee.json"
    MAINTENANCE = False
    SECRET_KEY = "TheObviouslyOpenSecret"
    NIKOLA_STATIC_PATH = _here / 'accuconf' / 'static'


class ProductionConfig(ConfigBase):
    pass


class TestConfig(ConfigBase):
    SQLALCHEMY_DATABASE_URI = "sqlite:///"+ str(ConfigBase._here / 'accuconf_test.db')
    DEBUG = True


class MaintenanceConfig(ConfigBase):
    MAINTENANCE = True


class MaintenanceTestConfig(TestConfig):
    MAINTENANCE = True


#Config = ConfigBase
Config = TestConfig
