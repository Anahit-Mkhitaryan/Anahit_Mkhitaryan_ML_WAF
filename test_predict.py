from app.model import predict_request  # Import your function from model.py

# Test some sample inputs
test_samples = [
    "Hello",  # Normal request
    "<script>alert(1)</script>",  # Malicious request
    "GET /home",  # Another normal request
]

for text in test_samples:
    prediction = predict_request(text)
    print(f"Prediction for '{text}': {prediction}")
