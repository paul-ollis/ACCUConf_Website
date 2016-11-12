import pytest

from common import client, post_and_check_content


@pytest.fixture
def registrant():
    return {
        'email': 'a@b.c',
        'user_pass': 'Password1',
        'firstname': 'User',
        'lastname': 'Name',
        'phone': '+011234567890',
        'bio': 'A person of some identity.',
        'pincode': '123456',
        'country': 'India',
        'state': 'TamilNadu',
        'towncity' : 'Chennai',
        'streetaddress': 'Chepauk',
        'captcha': '1',
        'question': '12',
    }


def test_user_reg_basic(client, registrant):
    post_and_check_content(client, '/proposals/register', registrant, values=('You have successfully registered', 'Please login'))


def test_user_reg_dup(client, registrant):
    test_user_reg_basic(client, registrant)
    post_and_check_content(client, '/proposals/register', registrant, values=('Duplicate user id',))


def test_password_short(client):
    post_and_check_content(client, '/proposals/register', {
        'email': 'test@std.dom',
        'user_pass': 'Pass1',
        'firstname': 'User2',
        'lastname': 'Name2',
        'phone': '+011234567890',
        'pincode': '123456',
        'country': 'India',
        'state': 'TamilNadu',
        'towncity' : 'Chennai',
        'streetaddress': 'Chepauk',
        'bio': 'An indivual of the world.',
        'captcha': '1',
        'question': '12',
    }, values=('Password did not meet checks',))


def test_password_invalid(client):
    post_and_check_content(client, '/proposals/register', {
        'email': 'test@std.dom',
        'user_pass': 'password',
        'firstname': 'User2',
        'lastname': 'Name2',
        'phone': '+011234567890',
        'pincode': '123456',
        'country': 'India',
        'state': 'TamilNadu',
        'towncity' : 'Chennai',
        'streetaddress': 'Chepauk',
        'bio': 'An indivual of the world.',
        'captcha': '1',
        'question': '12'
    }, values=('Password did not meet checks',))


def test_username_invalid(client):
    post_and_check_content(client, '/proposals/register', {
        'email': 'testing.test.dom',
        'user_pass': 'passworD13',
        'firstname': 'User2',
        'lastname': 'Name2',
        'phone': '+011234567890',
        'pincode': '123456',
        'country': 'India',
        'state': 'TamilNadu',
        'towncity' : 'Chennai',
        'streetaddress': 'Chepauk',
        'bio': 'An indivual of the world.',
        'captcha': '1',
        'question': '12',
    }, values=('Invalid/Duplicate user id',))
