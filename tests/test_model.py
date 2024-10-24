# tests/test_model.py

import unittest
import joblib
from sklearn.datasets import make_classification
from src.model import train_model

class TestModel(unittest.TestCase):

    def test_train_model(self):
        X, y = make_classification(n_samples=100, n_features=20, random_state=42)
        model = train_model(X, y)
        self.assertIsNotNone(model)
        
        # Save the model to test loading
        joblib.dump(model, 'models/test_model.pkl')
        loaded_model = joblib.load('models/test_model.pkl')
        self.assertIsNotNone(loaded_model)

if __name__ == '__main__':
    unittest.main()
