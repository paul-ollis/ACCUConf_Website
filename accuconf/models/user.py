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

    def __init__(self, userid, userpass):
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
