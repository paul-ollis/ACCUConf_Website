#!/usr/bin/env python
import pytest
from os.path import abspath, dirname, join
import sys
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from accuconf.models import *
from accuconf import app, create_db, drop_db


@pytest.fixture
def registrationData(key = "valid"):
    data = {

        "valid": dict(email="a@b.c",
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
        "valid2": dict(email="test@test.dom",
                       user_pass="passworD13",
                       firstname="User2",
                       lastname="Name2",
                       phone="+011234567890",
                       pincode="123456",
                       suffix="Jr.",
                       country="India",
                       state="TamilNadu",
                       captcha="1",
                       question="12"
                       ),
    }
    return data[key]


class TestUserAuthentication:

    def setup_method(self, method):
        self.app = app.test_client()
        with app.app_context():
            drop_db()
            create_db()

    def teardown_method(self, method):
        drop_db()

    def test_user_auth_basic(self):
        rv = self.app.post('/proposals/register', data=registrationData())
        assert rv is not None
        rv = self.app.post('/proposals/login',
                           data=dict(usermail="a@b.c",
                                     password="Password1"),
                           follow_redirects=True)
        assert rv is not None
        assert "ACCU Conference" in rv.data.decode("utf-8")

    def test_user_auth_fail(self):
        rv = self.app.post('/proposals/register', data=registrationData())
        assert rv is not None
        rv = self.app.post('/proposals/login',
                           data=dict(usermail="a@b.c",
                                     password="Password2"),
                           follow_redirects=True)
        assert rv is not None
        assert "Login" in rv.data.decode("utf-8")
