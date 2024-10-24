# tests/test_preprocess.py

import unittest
from src.preprocess import clean_text

class TestPreprocess(unittest.TestCase):

    def test_clean_text(self):
        text = "Hello! I am a developer, and I love coding."
        expected_output = "hello developer love coding"
        self.assertEqual(clean_text(text), expected_output)

if __name__ == '__main__':
    unittest.main()
