import os
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from app.preprocess import extract_features, vectorizer

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'waf_requests.csv')
MODEL_PATH = os.path.join(BASE_DIR, 'models', 'model.pkl')
model = None

def train_model():
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError("Dataset not found at: {}".format(DATA_PATH))

    df = pd.read_csv(DATA_PATH)
    if df.empty or 'request' not in df.columns or 'label' not in df.columns:
        raise ValueError("Dataset is empty or missing required columns ['request', 'label']")

    X = extract_features(df['request'], fit=True)
    y = df['label']

    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X, y)
    joblib.dump((clf, vectorizer), MODEL_PATH)
    print("✅ Model trained and saved at:", MODEL_PATH)


def load_model():
    global model
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError("Model file not found at: {}".format(MODEL_PATH))
    model = joblib.load(MODEL_PATH)
    print(model)
    print("✅ Model loaded.")

def predict_request(request_text):
    global model
    if model is None:
        raise Exception("Model not loaded.")
    clf, vec = model
    # print("model in predict : ", model)
    features = vec.transform([request_text])
    prediction = clf.predict(features)[0]
    print(f"🔎 Predicting: {request_text} → {prediction}")

    return prediction


if __name__ == "__main__":
    train_model()
