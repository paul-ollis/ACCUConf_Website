import pytest
from os.path import abspath, dirname, join
import sys
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from accuconf.models import *
from accuconf import app, db, create_db, drop_db
import json


@pytest.fixture
def testData(key="registration", subkey=None):
    data = {

        "registration": dict(email="a@b.c",
                             user_pass="Password1",
                             firstname="User",
                             lastname="Name",
                             phone="+011234567890",
                             pincode="123456",
                             suffix="",
                             country="India",
                             state="TamilNadu",
                             captcha="1",
                             question="12"
                             ),
        "proposals": {
            "valid": dict(proposer="a@b.c",
                          title="ACCU Proposal",
                          proposalType="quick",
                          abstract=""" This is a test proposal that will have
                                    dummy data. Also this is not a very
                                    lengthy proposal""",
                          presenters=[
                              {
                                  "email": "a@b.c",
                                  "lead": 1,
                                  "fname": "User",
                                  "lname": "Name",
                                  "country": "India",
                                  "state": "TamilNadu"
                              },
                          ]
                          ),
            "multipresenter_1": dict(proposer="a@b.c",
                                     title="ACCU Proposal",
                                     proposalType="quick",
                                     abstract=""" This is a test proposal that will have
                                     dummy data. Also this is not a very
                                     lengthy proposal""",
                                     presenters=[
                                         {
                                             "email": "a@b.c",
                                             "lead": 1,
                                             "fname": "User",
                                             "lname": "Name",
                                             "country": "India",
                                             "state": "TamilNadu"
                                         },
                                         {
                                             "email": "p2@b.c",
                                             "lead": 0,
                                             "fname": "Presenter",
                                             "lname": "Second",
                                             "country": "India",
                                             "state": "TamilNadu"
                                         },
                                     ]
                                     ),
            "multilead_1": dict(proposer="a@b.c",
                                title="ACCU Proposal",
                                proposalType="quick",
                                abstract=""" This is a test proposal that will have
                                dummy data. Also this is not a very
                                lengthy proposal""",
                                presenters=[
                                    {
                                        "email": "a@b.c",
                                        "lead": 1,
                                        "fname": "User",
                                        "lname": "Name",
                                        "country": "India",
                                        "state": "TamilNadu"
                                    },
                                    {
                                        "email": "p2@b.c",
                                        "lead": 1,
                                        "fname": "Presenter",
                                        "lname": "Second",
                                        "country": "India",
                                        "state": "TamilNadu"
                                    },
                                ]
                                )

        }
    }
    if subkey:
        if key in data and subkey in data[key]:
            return data[key][subkey]
    else:
        return data[key]


class TestProposalSubmission:

    def setup_method(self, method):
        self.app = app.test_client()
        with app.app_context():
            drop_db()
            create_db()

    def teardown_method(self, method):
        drop_db()

    def test_proposal_get(self):
        rv = self.app.post('/proposals/register', data=testData("registration"))
        # assert rv.data is not None
        # assert "You have successfully registered" in rv.data.decode("utf-8")
        rv = self.app.post('/proposals/login',
                           data=dict(usermail="a@b.c",
                                     password="Password1")
                           )
        # assert rv.data is not None
        # assert "Flask" in rv.data.decode("utf-8")
        rv = self.app.get("/proposals/proposal")
        assert rv is not None
        assert "Submit a proposal" in rv.data.decode("utf-8")


    def test_submit_proposal_basic(self):
        rv = self.app.post('/proposals/register', data=testData("registration"))
        rv = self.app.post('/proposals/login',
                           data=dict(usermail="a@b.c",
                                     password="Password1")
                           )
        rv = self.app.post("/proposals/proposal/submit",
                           data=json.dumps(testData("proposals", "valid")),
                           content_type="application/json")
        assert rv is not None
        assert "success" in rv.data.decode("utf-8")
        response = json.loads(rv.data.decode("utf-8"))
        assert response["success"]
        # p = Proposal.query.filter_by(proposer="a@b.c").first()
        user = User.query.filter_by(user_id="a@b.c").first()
        assert user is not None
        assert user.proposal is not None
        p = user.proposal
        assert p.proposer == user.user_id
        assert len(p.presenters) == 1


    def test_submit_proposal_multipresenter(self):
        rv = self.app.post('/proposals/register', data=testData("registration"))
        rv = self.app.post('/proposals/login',
                           data=dict(usermail="a@b.c",
                                     password="Password1")
                           )
        rv = self.app.post("/proposals/proposal/submit",
                           data=json.dumps(testData("proposals",
                                                    "multipresenter_1")),
                           content_type="application/json")
        assert rv is not None
        assert "success" in rv.data.decode("utf-8")
        response = json.loads(rv.data.decode("utf-8"))
        assert response["success"]
        # p = Proposal.query.filter_by(proposer="a@b.c").first()
        user = User.query.filter_by(user_id="a@b.c").first()
        assert user is not None
        assert user.proposal is not None
        p = user.proposal
        assert p.proposer == user.user_id
        assert len(p.presenters) == 2


    def test_submit_proposal_multilead(self):
        rv = self.app.post('/proposals/register', data=testData("registration"))
        rv = self.app.post('/proposals/login',
                           data=dict(usermail="a@b.c",
                                     password="Password1")
                           )
        rv = self.app.post("/proposals/proposal/submit",
                           data=json.dumps(testData("proposals",
                                                    "multilead_1")),
                           content_type="application/json")
        assert rv is not None
        assert "success" in rv.data.decode("utf-8")
        response = json.loads(rv.data.decode("utf-8"))
        assert response["success"] is False
        assert "message" in response
        assert "both marked as lead presenters" in response["message"]
        # p = Proposal.query.filter_by(proposer="a@b.c").first()
        user = User.query.filter_by(user_id="a@b.c").first()
        assert user is not None
        assert user.proposal is None
        # p = user.proposal
        # assert p.proposer == user.user_id
        # assert len(p.presenters) == 2
