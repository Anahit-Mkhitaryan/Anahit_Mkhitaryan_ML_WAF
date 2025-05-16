# ML-WAF Project

## Overview
This is a Python-based machine learning Web Application Firewall. It detects malicious HTTP requests using character-level n-gram TF-IDF features and a Random Forest classifier.

## Folder Structure
- `app/`: Core logic
- `data/`: Dataset (CSV with 'request' and 'label' columns)
- `models/`: Trained model files
- `logs/`: Logs for each prediction

## API Endpoints
- `POST /predict` with JSON `{ "request": "<http-request>" }`
- `POST /retrain` retrains model from data

## How to Run
```bash
pip install -r requirements.txt
python -m app.api
```

Then use curl or Postman to test:
```bash
curl -X POST http://127.0.0.1:5000/predict \
     -H "Content-Type: application/json" \
     -d '{"request": "GET /index.php?id=1' OR '1'='1"}'
```

## Retrain API
Add new data to `data/waf_requests.csv`, then call `/retrain` endpoint.
