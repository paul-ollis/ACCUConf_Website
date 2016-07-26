import pytest
from os.path import abspath, dirname, join
import sys
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from accuconf.models import User, UserInfo


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
