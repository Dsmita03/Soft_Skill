# tests/test_api.py

import unittest
from src.api import app

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_predict_endpoint(self):
        response = self.app.post('/predict', json={'text': 'I am a good communicator'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('predicted_soft_skills', response.get_json())

if __name__ == '__main__':
    unittest.main()
