'''
This tests that we are correctly accessing the Werkzeug test client of the application.
'''

import pytest

from os.path import abspath, dirname, join

import sys
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from accuconf import app


@pytest.fixture
def client(request):
    app.config['TESTING'] = True
    return app.test_client()


def test_getting_werkzeug_test_client(client):
    assert client is not None
