#!/usr/bin/env python
import pytest
from os.path import abspath, dirname, join
import sys
sys.path.insert(0, abspath(join(dirname(__file__), '..')))


from accuconf.models import *
from accuconf.proposals.utils.proposals import QuickProposalType
from accuconf import db, create_db, drop_db


class TestProposal:

    def setup_method(self, testmethod):
        create_db()

    def teardown_method(self, testmethod):
        drop_db()
        #pass

    def test_proposal_basic(self):
        u = User("abc@b.c", "password")
        ui = UserInfo("a@b.c",
                      'User',
                      'Name',
                      '',
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

