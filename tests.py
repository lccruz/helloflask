import unittest
import json
from app import app


class HelloTests(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app_context = app.app_context()
        self.app_context.push()
        self.app = app.test_client()

    def test_hello(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        response = response.get_json()
        self.assertEqual(response.get('message'), 'Flask and you')


if __name__ == "__main__":
    unittest.main()
