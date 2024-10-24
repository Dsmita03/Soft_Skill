# tests/test_feature_extraction.py

import unittest
from src.feature_extraction import extract_text_features

class TestFeatureExtraction(unittest.TestCase):

    def test_extract_text_features(self):
        corpus = ["I am a good communicator", "Teamwork is my strength"]
        features = extract_text_features(corpus)
        self.assertEqual(features.shape[0], 2)  # Ensure two samples
        self.assertGreater(features.shape[1], 0)  # Ensure features are extracted

if __name__ == '__main__':
    unittest.main()
