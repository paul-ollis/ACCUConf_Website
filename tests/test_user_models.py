import pytest
from os.path import abspath, dirname, join
import sys
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from accuconf.models import User, UserInfo
from accuconf import db, create_db, drop_db


class TestUser:

    def test_user_basic(self):
        user = User('a@b.c', 'password')
        assert user.user_id == 'a@b.c'

    def test_user_null_user(self):
        with pytest.raises(AttributeError) as ex:
            user = User(None, 'password')
        assert "Email cannot be empty" in str(ex.value)

    def test_user_empty_user(self):
        with pytest.raises(AttributeError) as ex:
            user = User("", 'password')
        assert "Email cannot be empty" in str(ex.value)

    def test_user_whitespace_user(self):
        with pytest.raises(AttributeError) as ex:
            user = User(" ", 'password')
        assert "Email cannot be empty" in str(ex.value)

    def test_user_null_password(self):
        with pytest.raises(AttributeError) as ex:
            user = User("a@b.c", None)
        assert "Password should have at least 8 letters/numbers." in str(ex.value)

    def test_user_whitespace_password(self):
        with pytest.raises(AttributeError) as ex:
            user = User("a@b.c", "         ")
        assert "Password should have at least 8 letters/numbers." in str(ex.value)

    def test_user_short_password(self):
        with pytest.raises(AttributeError) as ex:
            user = User("a@b.c", "pass")
        assert "Password should have at least 8 letters/numbers." in str(ex.value)


class TestUserInfo:

    def test_userinfo_basic(self):
        ui = UserInfo('a@b.c',
                      'Mr.',
                      'User',
                      'Name',
                      '',
                      '+01234567890',
                      'admin')

        assert ui is not None


class TestUserModel:

    def setup_class(cls):
        #db.session.execute('PRAGMA foreign_keys=ON;')
        pass

    def setup_method(self, testmethod):
        create_db()

    def teardown_method(self, testmethod):
        db.drop_all()
        #pass

    def test_basic(self):
        u = User('a@b.c', 'password')
        ui = UserInfo('a@b.c',
                      'Mr.',
                      'User',
                      'Name',
                      '',
                      '+01234567890',
                      'admin'
                      )
        u.user_info = ui
        db.session.add(u)
        db.session.add(ui)
        db.session.commit()

        assert User.query.filter_by(user_id='a@b.c').first() == u

    def test_userinfo_fkey(self):
        u = User('a@b.cc', 'password')
        ui = UserInfo('aa@b.c',
                      'Mr.',
                      'User',
                      'Name',
                      '',
                      '+01234567890',
                      'admin')
        u.user_info = ui
        db.session.add(u)
        db.session.add(ui)
        db.session.commit()
        oldU = User.query.filter_by(user_id="a@b.cc").first()
        oldUI = oldU.user_info
        assert  oldUI.userid == "a@b.cc"
