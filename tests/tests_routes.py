import unittest
from app import create_app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_classify_valid_input(self):
        response = self.client.post('/classify', json={"email_content": "You won a free prize!"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("classification", response.get_json())

    def test_classify_invalid_input(self):
        response = self.client.post('/classify', json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.get_json())