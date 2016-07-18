#!/usr/bin/env python

from sqlalchemy import create_engine
from sqlalchemy.org import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from accuconf import app

dburi = app.config['SQLALCHEMY_DATABASE_URI']
engine = create_engine(dburi, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Bind.query = db_session.query_property()

def drop_all():
    db.drop_all()


def create_all():
    from accuconf.models import *
    Base.metadata.create_all(bind=engine)


def remove_session():
    db.session.remove()

