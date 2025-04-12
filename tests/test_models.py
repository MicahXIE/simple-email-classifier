import unittest
import logging
from app.model import classify_email

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TestModel(unittest.TestCase):
    def test_classify_email(self):
        test_email = "CONGRATULATIONS! You've won £1,000,000 in the UK lottery! To claim your prize, contact us at +44-XXX-XXXX or reply NOW!"
        result = classify_email(test_email)
        # Log the test input and result
        logging.info(f"Testing classify_email with input: '{test_email}'")
        logging.info(f"Classification result: {result}")

        self.assertIn(result, [0, 1])