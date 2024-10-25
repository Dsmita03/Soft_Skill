import unittest
from sklearn.linear_model import LogisticRegression
from src.model import train_model
from sklearn.datasets import make_classification

class TestModel(unittest.TestCase):

    def setUp(self):
        # Creating a sample dataset
        self.X, self.y = make_classification(n_samples=100, n_features=20, random_state=42)
        self.model = LogisticRegression()

    def test_train_model(self):
        model = train_model(self.X, self.y)
        self.assertIsNotNone(model)
        self.assertIsInstance(model, LogisticRegression)

if __name__ == '__main__':
    unittest.main()
