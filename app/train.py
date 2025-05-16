import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from app.preprocess import extract_features, vectorizer
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'waf_traffic_data.csv')
MODEL_PATH = os.path.join(BASE_DIR, 'models', 'model.pkl')


def train_model():
    df = pd.read_csv(DATA_PATH)

    # Combine method and URL to simulate how requests come in
    df['request_text'] = df['request_method'] + ' ' + df['request_url']

    X = extract_features(df['request_text'], fit=True)
    y = df['label']

    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X, y)

    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    print("📍 Saving model to:", MODEL_PATH)
    joblib.dump((clf, vectorizer), MODEL_PATH)
    print("✅ Model trained and saved.")


if __name__ == "__main__":
    train_model()

