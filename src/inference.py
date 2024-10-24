# src/inference.py

import joblib
from src.preprocess import clean_text
from src.feature_extraction import extract_text_features

def predict_soft_skills(interview_text):
    """Predict soft skills from a given interview text."""
    # Load the trained model
    model = joblib.load('models/final_model.pkl')

    # Preprocess and extract features
    cleaned_text = clean_text(interview_text)
    features = extract_text_features([cleaned_text])

    # Make predictions
    prediction = model.predict(features)
    
    return prediction

if __name__ == "__main__":
    text = "I am very good at communicating and working in teams."
    print(predict_soft_skills(text))
