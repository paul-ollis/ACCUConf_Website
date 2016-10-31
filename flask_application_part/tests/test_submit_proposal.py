import pytest

import sys
from pathlib import PurePath
sys.path.insert(0, str(PurePath(__file__).parent.parent))

from accuconf.models import User, Proposal
from accuconf import app, db, create_db, drop_db
import json


@pytest.fixture(scope='function')
def registration_data():
    return {
        'email': 'a@b.c',
        'user_pass': 'Password1',
        'firstname': 'User',
        'lastname': 'Name',
        'phone': '+011234567890',
        'pincode': '123456',
        'country': 'India',
        'state': 'TamilNadu',
        'captcha': '1',
        'question': '12',
    }


@pytest.fixture(scope='function')
def proposal_single_presenter():
    return {
        'proposer': 'a@b.c',
        'title': 'ACCU Proposal',
        'proposalType': 'quick',
        'abstract': '''This is a test proposal that will have
dummy data. Also this is not a very
lengthy proposal''',
        'presenters': [
            {
                'email': 'a@b.c',
                'lead': 1,
                'fname': 'User',
                'lname': 'Name',
                'country': 'India',
                'state': 'TamilNadu'
            },
        ]
    }


@pytest.fixture(scope='function')
def proposal_multiple_presenters_single_lead():
    return {
        'proposer': 'a@b.c',
        'title': 'ACCU Proposal',
        'proposalType': 'quick',
        'abstract': ''' This is a test proposal that will have
dummy data. Also this is not a very
lengthy proposal''',
        'presenters': [
            {
                'email': 'a@b.c',
                'lead': 1,
                'fname': 'User',
                'lname': 'Name',
                'country': 'India',
                'state': 'TamilNadu'
            },
            {
                'email': 'p2@b.c',
                'lead': 0,
                'fname': 'Presenter',
                'lname': 'Second',
                'country': 'India',
                'state': 'TamilNadu'
            },
        ]
    }


@pytest.fixture(scope='function')
def proposal_multiple_presenters_and_leads():
    return {
        'proposer': 'a@b.c',
        'title': 'ACCU Proposal',
        'proposalType': 'quick',
        'abstract': ''' This is a test proposal that will have
dummy data. Also this is not a very
lengthy proposal''',
        'presenters': [
            {
                'email': 'a@b.c',
                'lead': 1,
                'fname': 'User',
                'lname': 'Name',
                'country': 'India',
                'state': 'TamilNadu'
            },
            {
                'email': 'p2@b.c',
                'lead': 1,
                'fname': 'Presenter',
                'lname': 'Second',
                'country': 'India',
                'state': 'TamilNadu'
            },
        ]
    }


@pytest.fixture(scope='function')
def client():
    with app.app_context():
        drop_db()
        create_db()
    yield app.test_client()
    drop_db()


def test_user_can_register(client, registration_data):
    rv = client.post('/proposals/register', data=registration_data)
    assert rv is not None
    assert rv.data is not None
    assert "You have successfully registered" in rv.data.decode("utf-8")


def test_registered_user_can_login(client, registration_data):
    test_user_can_register(client, registration_data)
    rv = client.post('/proposals/login', data={'usermail': registration_data['email'], 'password': registration_data['user_pass']})
    assert rv is not None
    assert rv.data is not None
    assert "Redirecting" in rv.data.decode("utf-8")
    rv = client.get('/site/index.html')
    assert rv is not None
    assert rv.data is not None
    # TODO find out how to get this right.
    #assert "My Proposals" in rv.data.decode("utf-8")


def test_logged_in_user_can_get_submission_page(client, registration_data):
    test_registered_user_can_login(client, registration_data)
    rv = client.get("/proposals/proposal")
    assert rv is not None
    assert rv.data is not None
    assert "Submit a proposal" in rv.data.decode("utf-8")


def test_logged_in_user_can_submit_a_single_presenter_proposal(client, registration_data, proposal_single_presenter):
    test_registered_user_can_login(client, registration_data)
    rv = client.post("/proposals/proposal/submit", data=json.dumps(proposal_single_presenter), content_type="application/json")
    assert rv is not None
    assert "success" in rv.data.decode("utf-8")
    response = json.loads(rv.data.decode("utf-8"))
    assert response["success"]
    proposal = Proposal.query.filter_by(proposer="a@b.c").first()
    assert proposal is not None
    # TODO test stuff.
    user = User.query.filter_by(user_id="a@b.c").first()
    assert user is not None
    assert user.proposal is not None
    p = user.proposal
    assert p.proposer == user.user_id
    assert len(p.presenters) == 1


def test_logged_in_user_can_submit_multipresenter_single_lead_proposal(client, registration_data, proposal_multiple_presenters_single_lead):
    test_registered_user_can_login(client, registration_data)
    rv = client.post("/proposals/proposal/submit", data=json.dumps(proposal_multiple_presenters_single_lead), content_type="application/json")
    assert rv is not None
    assert "success" in rv.data.decode("utf-8")
    response = json.loads(rv.data.decode("utf-8"))
    assert response["success"]
    proposal = Proposal.query.filter_by(proposer="a@b.c").first()
    assert proposal is not None
    # TODO test stuff.
    user = User.query.filter_by(user_id="a@b.c").first()
    assert user is not None
    assert user.proposal is not None
    p = user.proposal
    assert p.proposer == user.user_id
    assert len(p.presenters) == 2


def test_logged_in_user_user_can_submit_multipresenter_multilead_proposal(client, registration_data, proposal_multiple_presenters_and_leads):
    test_registered_user_can_login(client, registration_data)
    rv = client.post("/proposals/proposal/submit", data=json.dumps(proposal_multiple_presenters_and_leads), content_type="application/json")
    assert rv is not None
    assert "success" in rv.data.decode("utf-8")
    response = json.loads(rv.data.decode("utf-8"))
    assert response["success"] is False
    assert "message" in response
    assert "both marked as lead presenters" in response["message"]
    #proposal = Proposal.query.filter_by(proposer="a@b.c").first()
    #assert proposal is not None
    # TODO test stuff.
    user = User.query.filter_by(user_id="a@b.c").first()
    assert user is not None
    assert user.proposal is None
    #p = user.proposal
    #assert p.proposer == user.user_id
    #assert len(p.presenters) == 2
