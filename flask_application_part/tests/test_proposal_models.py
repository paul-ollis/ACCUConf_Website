'''
Test the basic proposal model.
'''

import pytest

from common import client

from accuconf.models import User, UserInfo, UserLocation, Proposal, ProposalPresenter, ProposalStatus, NewProposal
from accuconf.proposals.utils.proposals import QuickProposalType
# TODO remove this sort of access to the db.
from accuconf import db

__author__ = 'Balachandran Sivakumar, Russel Winder'
__copyright__ = '© 2016  Balachandran Sivakumar, Russel Winder'
__licence__ = 'GPLv3'


def test_proposal_basic(client):
    u = User("abc@b.c", "password")
    ui = UserInfo("a@b.c",
                  'User',
                  'Name',
                  '+01234567890',
                  'admin')
    location = UserLocation(u.user_id, "IND", "KARNATAKA", "560093")
    p = Proposal("a@b.c",
                 "TDD with C++",
                 QuickProposalType(),
                 "AABBCC")
    presenter = ProposalPresenter(p.id, u.user_id, True, ui.first_name,
                                  ui.last_name, location.country,
                                  location.state)
    state = ProposalStatus(p.id, NewProposal())
    p.presenters = [presenter]
    p.status = state
    p.session_proposer = u
    p.lead_presenter = u
    u.user_info = ui
    u.location = location
    u.proposal = p
    db.session.add(u)
    db.session.add(ui)
    db.session.add(location)
    db.session.add(p)
    db.session.add(presenter)
    db.session.add(state)
    db.session.commit()

    p = User.query.filter_by(user_id="abc@b.c").first().proposal
    assert p.status.state == NewProposal().state()
