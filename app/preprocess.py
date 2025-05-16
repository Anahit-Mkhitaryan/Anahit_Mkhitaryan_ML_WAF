import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(3, 5), max_features=5000)

def extract_features(data, fit=False):
    if fit:
        return vectorizer.fit_transform(data)
    return vectorizer.transform(data)
