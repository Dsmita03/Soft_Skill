# src/preprocess.py

import re
import nltk
from nltk.corpus import stopwords

# Download the NLTK stopwords if you haven't already
nltk.download('stopwords')
STOPWORDS = set(stopwords.words('english'))

def clean_text(text):
    """Remove special characters, stop words, and tokenize."""
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    tokens = text.split()
    tokens = [word for word in tokens if word not in STOPWORDS]
    return ' '.join(tokens)

def tokenize(text):
    """Simple tokenization function (can be replaced with something more advanced)."""
    return text.split()
