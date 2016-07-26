#!/usr/bin/env python

from accuconf.database import db
from accuconf.models.user import User
from accuconf.proposals import *


class Proposal(db.Model):
    __tablename__ = "proposals"
    id = db.Column(db.Integer, primary_key=True)
    proposer = db.Column(db.String(100), db.ForeignKey('users.user_id'))
    title = db.Column(db.String(150), nullable=False)
    session_type = db.Column(db.String(20), nullable=False)
    text = db.Column(db.Text, nullable=False)
    lead = db.Column(db.String(100), db.ForeignKey('users.user_id'))
    presenters = db.relationship('ProposalPresenter',
                                 uselist=True)
    state = db.relationship('ProposalState',
                            uselist=False)
    reviews = db.relationship('ProposalReview',
                              uselist=True)
    categories = db.relationship('ProposalCategory',
                                 uselist=True)
    session_proposer = db.relationship('User',
                                       foreign_keys='Proposal.proposer')
    lead_presenter = db.relationship('User',
                                     foreign_keys='Proposal.lead')

    def __init__(self, proposer, title, session_type, text, lead):
        self.proposer = proposer
        self.title = title
        if type(session_type) == ProposalType:
            self.session_type = session_type
        else:
            raise TypeError("session_type should be of type "
                            "accuconf.proposals.ProposalType")


class ProposalPresenter(db.Model):
    __tablename__ = "proposal_presenters"
    id = db.Column(db.Integer, primary_key=True)
    proposal_id = db.Column(db.Integer, db.ForeignKey('proposals.id'))
    presenter = db.Column(db.String(100), db.ForeignKey('users.user_id'))

    def __init__(self, proposal_id, presenter):
        self.proposal_id = proposal_id
        self.presenter = presenter


class ProposalState(db.Model):
    __tablename__ = "proposal_states"
    id = db.Column(db.Integer, primary_key=True)
    proposal_id = db.Column(db.Integer, db.ForeignKey('proposals.id'))
    state = db.Column(db.String(20), nullable=False)

    def __init__(self, proposal_id, state):
        self.proposal_id = proposal_id
        if type(state) == ProposalState:
            self.state = state
        else:
            raise TypeError("state should be of type "
                            "accuconf.proposals.ProposalState")


class ProposalReview(db.Model):
    __tablename__ = "proposal_reviews"
    id = db.Column(db.Integer, primary_key=True)
    proposal_id = db.Column(db.Integer, db.ForeignKey('proposals.id'))
    reviewer = db.Column(db.String(100), db.ForeignKey('users.user_id'))
    score = db.Column(db.Integer)

    def __init__(self, proposal_id, reviewer, score):
        self.proposal_id = proposal_id
        self.reviewer = reviewer
        self.score = score


class ProposalCategory(db.Model):
    __tablename__ = "proposal_categories"
    id = db.Column(db.Integer, primary_key=True)
    proposal_id = db.Column(db.Integer, db.ForeignKey('proposals.id'))
    category = db.Column(db.String(100), nullable=False)

    def __init__(self, proposal_id, category):
        self.proposal_id = proposal_id
        if type(category) == ProposalCategory:
            self.category = category
        else:
            raise TypeError("category should be of type "
                            "accuconf.proposals.ProposalCategory")
