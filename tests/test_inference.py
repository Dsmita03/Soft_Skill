# tests/test_inference.py

import unittest
from src.inference import predict_soft_skills

class TestInference(unittest.TestCase):

    def test_predict_soft_skills(self):
        text = "I am a good team player with excellent communication skills."
        prediction = predict_soft_skills(text)
        self.assertIsNotNone(prediction)
        self.assertIsInstance(prediction, list)

if __name__ == '__main__':
    unittest.main()
