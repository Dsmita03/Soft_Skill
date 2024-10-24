# src/feature_extraction.py

from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# Using TF-IDF for text feature extraction
def extract_text_features(corpus):
    vectorizer = TfidfVectorizer(max_features=5000)
    features = vectorizer.fit_transform(corpus)
    return features

# Example usage
if __name__ == "__main__":
    documents = ["Teamwork is crucial", "Leadership is a key soft skill"]
    features = extract_text_features(documents)
    print(features.toarray())
