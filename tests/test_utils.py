import unittest
from app.utils import preprocess_email

class TestUtils(unittest.TestCase):
    def test_preprocess_email(self):
        content = "Hello, World! This is a test email."
        processed = preprocess_email(content)
        self.assertEqual(processed, "hello world this is a test email")