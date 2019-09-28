import unittest
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
        self.assertEqual(response.get('message'), 'Flask 3000')

    def test_hello_message(self):
        response = self.app.get('/hello')
        response_str = response.data.decode('utf-8')
        self.assertIn('<h3>hello</h3>', response_str)


if __name__ == "__main__":
    unittest.main()
