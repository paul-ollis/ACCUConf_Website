#!/usr/bin/env python

from accuconf.database import db


# Represents a user in the system, assumes userid = user.email
class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.String(100), primary_key=True)
    user_pass = db.Column(db.String(512), nullable=False)
    user_info = db.relationship('UserInfo',
                                uselist=False,
                                backref=db.backref('user'))
    location = db.relationship('UserLocation',
                               uselist=False,
                               backref=db.backref('user'))
    proposal = db.relationship('Proposal',
                               uselist=False,
                               backref=db.backref('proposed_by'),
                               foreign_keys="Proposal.proposer")

    def __init__(self, userid, userpass):
        if userid is None or len(userid.strip()) == 0:
            raise AttributeError("Email cannot be empty")
        if userpass is None or len(userpass.strip()) < 8:
            raise AttributeError("Password should have at least 8 "
                                 "letters/numbers.")
        self.user_id = userid
        self.user_pass = userpass


# Every user has a user info, backref'ed in the User class
class UserInfo(db.Model):
    __tablename__ = 'userinfo'
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(100), db.ForeignKey('users.user_id'))
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(12), nullable=False)

    def __init__(self, userid, fname, lname, role):
        self.userid = userid
        self.first_name = fname
        self.last_name = lname
        self.role = role


class UserLocation(db.Model):
    __tablename__ = 'user_location'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100), db.ForeignKey('users.user_id'))
    country = db.Column(db.String(5), nullable=False)
    state = db.Column(db.String(10), nullable=False)
    postal_code = db.Column(db.String(40), nullable=False)

    def __init__(self, user_id, country, state, postal_code):
        self.user_id = user_id
        self.country = country
        self.state = state
        self.postal_code = postal_code
