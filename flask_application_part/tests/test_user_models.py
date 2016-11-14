import pytest

from common import database

from accuconf.models import User, UserInfo

__author__ = 'Balachandran Sivakumar, Russel Winder'
__copyright__ = '© 2016  Balachandran Sivakumar, Russel Winder'
__licence__ = 'GPLv3'

email = 'a@b.c'
password = 'password'


def test_user_basic():
    user = User(email, password)
    assert user.user_id == email
    assert user.user_pass == password


def test_user_null_user():
    with pytest.raises(AttributeError) as ex:
        User(None, password)
    assert 'Email cannot be empty' in str(ex.value)


def test_user_empty_user():
    with pytest.raises(AttributeError) as ex:
        User('', password)
    assert 'Email cannot be empty' in str(ex.value)


def test_user_whitespace_user():
    with pytest.raises(AttributeError) as ex:
        User(' ', password)
    assert 'Email cannot be empty' in str(ex.value)


def test_user_null_password():
    with pytest.raises(AttributeError) as ex:
        User(email, None)
    assert 'Password should have at least 8 letters/numbers.' in str(ex.value)


def test_user_whitespace_password():
    with pytest.raises(AttributeError) as ex:
        User(email, '         ')
    assert 'Password should have at least 8 letters/numbers.' in str(ex.value)


def test_user_short_password():
    with pytest.raises(AttributeError) as ex:
        User(email, 'pass')
    assert 'Password should have at least 8 letters/numbers.' in str(ex.value)


user_data = (
    email,
    'User',
    'Name',
    '+01234567890',
    ' A human being who has done stuff',
    'admin',
)


def test_userinfo_basic():
    ui = UserInfo(*user_data)
    assert ui is not None
    assert (
        ui.user_id,
        ui.first_name,
        ui.last_name,
        ui.phone,
        ui.bio,
        ui.role
    ) == user_data


def test_basic(database):
    u = User(email, password)
    ui = UserInfo(*user_data)
    u.user_info = ui
    database.session.add(u)
    database.session.add(ui)
    database.session.commit()
    assert User.query.filter_by(user_id=email).first() == u


def test_userinfo_fkey(database):
    u = User(email, password)
    ui = UserInfo(*user_data)
    u.user_info = ui
    database.session.add(u)
    database.session.add(ui)
    database.session.commit()
    old_user = User.query.filter_by(user_id=email).first()
    old_user_info = old_user.user_info
    assert old_user_info.user_id == email
