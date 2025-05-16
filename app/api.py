from flask import Flask, request, jsonify
import datetime
import os
from app.model import load_model, predict_request
from app.train import train_model

app = Flask(__name__)
load_model()

LOG_FILE = 'logs/predictions.log'


@app.before_request
def waf_filter():
    # Combine path and query string (this simulates the URL in your dataset)
    query = request.query_string.decode()
    full_url = request.path + ('?' + query if query else '')

    # Optionally include method or user-agent to improve prediction
    request_text = f"{request.method} {full_url}"  # or include headers too

    pred = predict_request(request_text)
    log_prediction(request_text, pred)

    if pred == 1:
        return jsonify({"status": "blocked", "message": "Request blocked by WAF"}), 403


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    request_text = data.get('request', '')
    pred = predict_request(request_text)
    log_prediction(request_text, pred)

    if pred == "malicious":
        response = {"status": "blocked", "message": "Malicious request detected"}
    else:
        response = {"status": "allowed", "message": "Request is clean"}
    return jsonify(response)


@app.route('/retrain', methods=['POST'])
def retrain():
    train_model()
    load_model()
    return jsonify({"status": "success", "message": "Model retrained"})


def log_prediction(request_text, pred):
    os.makedirs('logs', exist_ok=True)
    with open(LOG_FILE, 'a') as f:
        time = datetime.datetime.now().isoformat()
        line = f"[{time}] Request: {request_text} => Prediction: {pred}\n"
        f.write(line)

@app.route('/home')
def home():
    return jsonify({"status": "success", "message": "Welcome to Home!"})


@app.route('/login')
def login():
    return jsonify({"status": "success", "message": "Login Page"})


@app.route('/search')
def search():
    return jsonify({"status": "success", "message": "Search Page"})


if __name__ == '__main__':
    app.run(debug=True)
