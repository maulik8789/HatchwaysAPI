from app import app, posts
from unittest import TestCase
from unittest.mock import patch
import requests
import requests_mock


# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class MyTest(TestCase):

    def test_home(self):
        with app.test_client() as client:
            # can now make requests to flask via `client`
            resp = client.get('/')

            self.assertEqual(resp.status_code, 200)

    def test_posts(self):
        with app.test_client() as p:
            with requests_mock.Mocker() as rm:
                rm.post('/showposts', status_code = 400)

        