from flask_sqlalchemy import SQLAlchemy, event

from accuconf import app

db = SQLAlchemy(app)


@event.listens_for(db.get_engine(app), "connect")
def enable_fkey(dbcon, con_rec):
    cursor = dbcon.cursor()
    cursor.execute('PRAGMA foreign_keys=ON;')
    cursor.close()


def drop_db():
    db.drop_all()


def create_db():
    db.create_all()
