import requests

# Base URL for your Flask app
BASE_URL = 'http://127.0.0.1:5000'

# Test inputs: normal and malicious-looking URLs
test_paths = [
    '/home',
    '/login',
    '/search?query=hello',
    "/login?username=admin' OR '1'='1",  # SQLi
    "/search?query=<script>alert('XSS')</script>",  # XSS
    "/home?file=../../../../etc/passwd",  # Path traversal
]

for path in test_paths:
    url = BASE_URL + path
    print(f"GET {url}")

    try:
        response = requests.get(url)
        print("Status Code:", response.status_code)
        print("Response:", response.json())
    except Exception as e:
        print("Error:", str(e))

    print('-' * 50)
