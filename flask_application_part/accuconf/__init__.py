from flask import Flask, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy, event

app = Flask(__name__)
Bootstrap(app)
db = SQLAlchemy(app)

import accuconf_config
from .nikola import nikola, views
from .proposals import proposals, views


app.config.from_object(accuconf_config.Config)
app.secret_key = app.config['SECRET_KEY']
app.register_blueprint(nikola, url_prefix='/site')
app.register_blueprint(proposals, url_prefix='/proposals')
app.logger.info(app.url_map)


@event.listens_for(db.get_engine(app), "connect")
def enable_fkey(dbcon, con_rec):
    cursor = dbcon.cursor()
    cursor.execute('PRAGMA foreign_keys=ON;')
    cursor.close()


def drop_db():
    db.drop_all()


def create_db():
    db.create_all()


@app.route('/')
def index():
    return redirect(url_for('nikola.index'))
