import pytest

from common import client

from accuconf.models import User, UserInfo
# TODO remove this sort of access to the db.
from accuconf import db

__author__ = 'Balachandran Sivakumar, Russel Winder'
__copyright__ = '© 2016  Balachandran Sivakumar, Russel Winder'
__licence__ = 'GPLv3'


def test_user_basic():
    user = User('a@b.c', 'password')
    assert user.user_id == 'a@b.c'


def test_user_null_user():
    with pytest.raises(AttributeError) as ex:
        user = User(None, 'password')
    assert 'Email cannot be empty' in str(ex.value)


def test_user_empty_user():
    with pytest.raises(AttributeError) as ex:
        user = User('', 'password')
    assert 'Email cannot be empty' in str(ex.value)


def test_user_whitespace_user():
    with pytest.raises(AttributeError) as ex:
        user = User(' ', 'password')
    assert 'Email cannot be empty' in str(ex.value)


def test_user_null_password():
    with pytest.raises(AttributeError) as ex:
        user = User('a@b.c', None)
    assert 'Password should have at least 8 letters/numbers.' in str(ex.value)


def test_user_whitespace_password():
    with pytest.raises(AttributeError) as ex:
        user = User('a@b.c', '         ')
    assert 'Password should have at least 8 letters/numbers.' in str(ex.value)


def test_user_short_password():
    with pytest.raises(AttributeError) as ex:
        user = User('a@b.c', 'pass')
    assert 'Password should have at least 8 letters/numbers.' in str(ex.value)


def test_userinfo_basic():
    ui = UserInfo('a@b.c',
                  'User',
                  'Name',
                  '+01234567890',
                  'admin')
    assert ui is not None


def test_basic(client):
    u = User('a@b.c', 'password')
    ui = UserInfo('a@b.c',
                  'User',
                  'Name',
                  '+01234567890',
                  'admin'
    )
    u.user_info = ui
    db.session.add(u)
    db.session.add(ui)
    db.session.commit()
    assert User.query.filter_by(user_id='a@b.c').first() == u


def test_userinfo_fkey(client):
    u = User('a@b.cc', 'password')
    ui = UserInfo('aa@b.c',
                  'User',
                  'Name',
                  '+01234567890',
                  'admin')
    u.user_info = ui
    db.session.add(u)
    db.session.add(ui)
    db.session.commit()
    oldU = User.query.filter_by(user_id='a@b.cc').first()
    oldUI = oldU.user_info
    assert  oldUI.userid == 'a@b.cc'
