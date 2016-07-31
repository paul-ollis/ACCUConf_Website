#!/usr/bin/env python
import pytest
from os.path import abspath, dirname, join
import sys
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from accuconf.models import *
from accuconf.database import db, create_db, drop_db
from accuconf import app, init_sec_ctxt


class TestUserRegistration:

    def setup_method(self, method):
        self.app = app.test_client()
        with app.app_context():
            drop_db()
            create_db()
            init_sec_ctxt()

    def teardown_method(self, method):
        drop_db()

    def test_user_reg_basic(self):
        rv = self.app.post('/register', data=dict(
                email="a@b.c",
                password="Password1",
                firstname="User",
                lastname="Name",
                phone="+011234567890",
                pincode="123456",
                salutation="Mr.",
                suffix="",
                country="India",
                state="TamilNadu",
                captcha="1",
                question="12"
                )
        )
        print (type(rv.data))
        assert rv.data is not None
        assert "You have successfully registered" in rv.data.decode("utf-8")

