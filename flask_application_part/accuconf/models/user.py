from accuconf import db


# Represents a user in the system, assumes user_id = user.email
class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.String(100), primary_key=True)
    user_pass = db.Column(db.String(512), nullable=False)
    user_info = db.relationship('UserInfo', uselist=False, backref=db.backref('user'))
    location = db.relationship('UserLocation', uselist=False)
    proposals = db.relationship('Proposal', uselist=True, backref=db.backref('proposed_by'), foreign_keys="Proposal.proposer")

    def __init__(self, user_id, user_pass):
        if user_id is None or len(user_id.strip()) == 0:
            raise AttributeError("Email cannot be empty")
        if user_pass is None or len(user_pass.strip()) < 8:
            raise AttributeError("Password should have at least 8 letters/numbers.")
        self.user_id = user_id
        self.user_pass = user_pass


# Every user has a user info, backref'ed in the User class
class UserInfo(db.Model):
    __tablename__ = 'user_infos'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100), db.ForeignKey('users.user_id'))
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(18), nullable=False)
    bio = db.Column(db.Text(), nullable=False)
    role = db.Column(db.String(12), nullable=False)

    def __init__(self, user_id, fname, lname, phone, bio, role):
        self.user_id = user_id
        self.first_name = fname
        self.last_name = lname
        self.phone = phone
        self.bio = bio
        self.role = role


class UserLocation(db.Model):
    __tablename__ = 'user_locations'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100), db.ForeignKey('users.user_id'))
    country = db.Column(db.String(5), nullable=False)
    state = db.Column(db.String(10), nullable=False)
    postal_code = db.Column(db.String(40), nullable=False)
    town_city = db.Column(db.String(30), nullable=False)
    street_address = db.Column(db.String(128), nullable=False)

    def __init__(self, user_id, country, state, postal_code, town_city, street_address):
        self.user_id = user_id
        self.country = country
        self.state = state
        self.postal_code = postal_code
        self.town_city = town_city
        self.street_address = street_address
